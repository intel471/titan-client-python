import datetime
import logging
import re
from typing import Union, NamedTuple, List, Callable
import base64

from pytz import UTC
from stix2 import Bundle, Report, ExternalReference, TLP_AMBER

from .common import BaseMapper
from .. import author_identity, generate_id, STIXMapperSettings

log = logging.getLogger(__name__)


class ReportSettings(NamedTuple):
    api_class: str
    method_name: str
    # either JSON path to the field or a function that extracts value from provided source
    description_source: Union[str, Callable[[dict], str]]
    attachments_fields: Union[List[str], None] = None


class ReportMapper(BaseMapper):
    remove_html_regex = re.compile(r"<.*?>")
    reports_settings = {
        "breach_alert": ReportSettings(
            "ReportsApi",
            "breach_alerts_uid_get",
            "data.breach_alert.summary",  # good for description
        ),
        # breach_alert example
        # titan 'iocs?ioc=akiral2iz6a7qgd3ayp3l6yub7xx2uep76idk3u2kollpj5z3z636bad.onion'
        # titan breachAlerts/fae604164acb6a34983d3684ecb83d7e
        "inforep": ReportSettings(
            "ReportsApi",
            "reports_uid_get",
            "executive_summary",
            ["rawText", "rawTextTranslated", "researcherComments"]
        ),
        # inforep example
        # titan 'iocs?ioc=sldltcn2d6mgtp66vgmvjptdtwgqyyewsjgwkzjybq3x55plzw4tefid.onion'
        # titan reports/1d2d1de3603abf9503471b7f882c47e83e50fa42ad7588fc5d43a7cde1ff8bb4
        "spotrep": ReportSettings(
            "ReportsApi",
            "spot_reports_uid_get",
            "data.spot_report.spot_report_data.text"
        ),
        # spotrep example
        # titan 'iocs?ioc=22d90ad1a0e5220ec0772918fa6efdb54604bddab1d5f15156ead1acd5d7aa37'
        # titan spotReports/5f486c27fb68281e23aa6d2c3b0d2b59
        "fintel": ReportSettings(
            "ReportsApi",
            "reports_uid_get",
            # There's no summary or anything similar. Try to extract contents of the first paragraph <h2>...</h2><p>get-this</p>...
            lambda x: re.split(r'</?p>', re.sub(r'^.*?<p>', '', x.get("rawText") or ""))[0],
            ["rawText"]
        ),
        # fintel example
        # titan 'iocs?ioc=http://162.55.187.234'
        "malrep": ReportSettings(
            "ReportsApi",
            "malware_reports_uid_get",
            "data.malware_report_data.text",
        ),
        "sitrep": ReportSettings(
            "ReportsApi",
            "situation_reports_report_uid_get",
            "data.situation_report.text",
        ),
        "cve": ReportSettings(
            "VulnerabilitiesApi",
            "cve_reports_uid_get",
            "data.cve_report.summary",
        )
    }

    def __init__(self, settings: STIXMapperSettings):
        super().__init__(settings)
        self.cache = {}

    def map(self, source: dict) -> Bundle:
        return Bundle()

    def map_shortened_report(self, source: dict, object_refs: dict) -> dict:
        """
        Handles shortened representation of reports attached to IOCs in the response of /iocs endpoint
        {"iocs": [{"links": {"reports": [{"uid": "123", "subject": "foo", ... }]}}]}
        """
        container = {}
        if all([self.settings.titan_client, self.settings.api_client]) and \
           any([self.settings.report_description, self.settings.report_attachments_opencti]):
            try:
                full_source = self._get_full_source(source)
                if full_source:
                    # Need to merge instead of using full_source only as subjects are consistently stored
                    # under `subject` field only in shortened version
                    source = {**source, **full_source}
            except Exception as e:
                log.warning("Unable to fetch or process full report source. Falling back to shortened version. Error: %s", e)
        # TODO: researcher comments/attachments
        # TODO: Proxy setup
        report_kwargs = self._map_report_kwargs(source, object_refs)
        report = Report(**report_kwargs)
        container[report.id] = report
        return container

    def _map_report_kwargs(self, source: dict, object_refs: dict):
        time_published = self._format_published(source.get("released") or source.get("created"))
        return {
            "id": generate_id(
                Report,
                name=self.shorten(source["subject"], 128).strip().lower(),
                published=time_published,
            ),
            "name": source["subject"],
            "description": self._get_description(source),
            "report_types": [self._get_type(source)],
            "confidence": self.map_confidence(source.get("admiraltyCode") or source.get("data", {}).get("breach_alert", {}).get("confidence", {}).get("level")),
            "published": time_published,
            "labels": self._get_malware_families(source),
            "object_refs": object_refs.values(),
            "external_references": [
                ExternalReference(source_name="Titan URL", url=self._get_url(source))
            ],
            "created_by_ref": author_identity,
            "object_marking_refs": [TLP_AMBER],
            "custom_properties": {
                "x_intel471_com_uid": self._get_uid(source),
                "x_opencti_files": self._get_opencti_files(source)
            }
        }

    def _get_full_source(self, source: dict) -> Union[dict, None]:
        report_url = self._get_url(source)
        report_type = self._get_type(source)
        report_uid = self._get_uid(source)
        if report_url not in self.cache:
            report_settings = self.reports_settings.get(report_type)
            api_instance = getattr(self.settings.titan_client, report_settings.api_class)(self.settings.api_client)
            api_response = getattr(api_instance, report_settings.method_name)(report_uid)
            self.cache[report_url] = api_response.to_dict(serialize=True)
        return self.cache[report_url]

    def _format_published(self, epoch_millis: int):
        """
        Formatting datetime object for use as ID contributing property in a same way as it's done by OpenCTI
        to have the same ID here and in OpenCTI.
        """
        parsed = datetime.datetime.fromtimestamp(epoch_millis / 1000, UTC)
        return parsed.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    @staticmethod
    def _get_url(source: dict):
        return source["portalReportUrl"]

    def _get_uid(self, source: dict):
        return self._get_url(source).split("/")[-1]

    def _get_type(self, source: dict):
        return self._get_url(source).split("/")[-2]

    def _get_malware_families(self, source: dict):
        return [i.get("value") for i in (source.get("entities") or []) if i.get("type") == "MalwareFamily"]

    def _get_description(self, source: dict):
        subject = source.get("subject")
        report_settings = self.reports_settings.get(self._get_type(source))
        description_source = report_settings.description_source

        if isinstance(description_source, Callable):
            source = description_source(source)
        else:
            for i in description_source.split("."):
                source = source.get(i, {})

        if source:
            return re.sub(self.remove_html_regex, "", source)
        return subject

    def _get_opencti_files(self, source: dict):
        if not self.settings.report_attachments_opencti:
            return []
        opencti_files = []
        report_settings = self.reports_settings.get(self._get_type(source))
        attachments_fields = report_settings.attachments_fields or []
        for field_name in attachments_fields:
            value = source.get(field_name)
            if isinstance(value, str):
                opencti_files.append({
                    "name":  " ".join([i.capitalize() for i in re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))|[a-z]+', field_name)]),
                    "mime_type": "text/html",
                    "data": base64.b64encode(bytes(value, "utf-8")).decode("utf-8")
                })
        return opencti_files
