import datetime
import logging
import re
from typing import Union, NamedTuple

from pytz import UTC
from stix2 import Bundle, Report, ExternalReference, TLP_AMBER

from .common import BaseMapper
from .. import author_identity, generate_id

log = logging.getLogger(__name__)


class ReportSettings(NamedTuple):
    api_class: str
    method_name: str
    description_field: str


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
            "executive_summary",   # good for description; attach rawText, rawTextTranslated, researcherComments
        ),
        # inforep example
        # titan 'iocs?ioc=sldltcn2d6mgtp66vgmvjptdtwgqyyewsjgwkzjybq3x55plzw4tefid.onion'
        # titan reports/1d2d1de3603abf9503471b7f882c47e83e50fa42ad7588fc5d43a7cde1ff8bb4
        "spotrep": ReportSettings(
            "ReportsApi",
            "spot_reports_uid_get",
            "data.spot_report.spot_report_data.text",  # good for description
        ),
        # spotrep example
        # titan 'iocs?ioc=22d90ad1a0e5220ec0772918fa6efdb54604bddab1d5f15156ead1acd5d7aa37'
        # titan spotReports/5f486c27fb68281e23aa6d2c3b0d2b59
        "fintel": ReportSettings(
            "ReportsApi",
            "reports_uid_get",
            "raw_text"  # description should be shortened raw_text; raw text contains pictures; should be attached
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

    def __init__(self, titan_client, api_client):
        super().__init__(titan_client, api_client)
        self.cache = {}

    def map(self, source: dict) -> Bundle:
        return Bundle()

    def map_shortened_report(self, source: dict, object_refs: dict) -> dict:
        """
        Handles shortened representation of reports attached to IOCs in the response of /iocs endpoint
        {"iocs": [{"links": {"reports": [{"uid": "123", "subject": "foo", ... }]}}]}
        """
        container = {}
        if all([self.titan_client, self.api_client]):
            try:
                full_source = self._get_full_source(source)
                if full_source:
                    # Need to merge instead of using full_source only as subjects are consistently stored
                    # under `subject` field only in shortened version
                    source = {**source, **full_source}
            except Exception as e:
                log.warning("Unable to fetch or process full report source. Falling back to shortened version. Error: %s", e)
        # TODO: researcher comments/attachments
        # TODO: MD5, SHA256 and SHA1 entities
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
            "confidence": self.map_confidence(source.get("admiralty_code") or source.get("data", {}).get("breach_alert", {}).get("confidence", {}).get("level")),
            "published": time_published,
            "labels": self._get_malware_families(source),
            "object_refs": object_refs.values(),
            "external_references": [
                ExternalReference(source_name="Titan URL", url=self._get_url(source))
            ],
            "created_by_ref": author_identity,
            "object_marking_refs": [TLP_AMBER],
            "custom_properties": {"x_intel471_com_uid": self._get_uid(source)},
        }

    def _get_full_source(self, source: dict) -> Union[dict, None]:
        report_url = self._get_url(source)
        report_type = self._get_type(source)
        report_uid = self._get_uid(source)
        if report_url not in self.cache:
            api_cls, api_method, _ = self.reports_settings.get(report_type)
            api_instance = getattr(self.titan_client, api_cls)(self.api_client)
            api_response = getattr(api_instance, api_method)(report_uid)
            self.cache[report_url] = api_response.to_dict()
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
        description_field = report_settings.description_field
        for i in description_field.split("."):
            source = source.get(i, {})
        if source:
            return re.sub(self.remove_html_regex, "", source)
        return subject
