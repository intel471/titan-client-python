import base64
from collections.abc import Callable
import re
from typing import List, NamedTuple, Union

from titan_client.titan_stix.exceptions import TitanStixException
from .common import BaseMapper, StixMapper
from stix2 import Bundle, Report, Indicator, ExternalReference, TLP_AMBER
import datetime
from .. import STIXMapperSettings, author_identity, generate_id
from pytz import UTC
from enum import Enum


class ReportType(Enum):
    inforep = "inforep"
    fintel = "fintel"
    breach_alert = "breach_alert"
    spotrep = "spotrep"


class ReportSettings(NamedTuple):
    api_class: str
    method_name: str
    # either JSON path to the field or a function that extracts value from provided source
    title_source: Union[str, Callable[[dict], str]]
    description_source: Union[str, Callable[[dict], str]]
    attachments_fields: Union[List[str], None] = None


# @StixMapper.register("reports", lambda x: "reportTotalCount" in x)
@StixMapper.register("breach_alerts", lambda x: "breach_alerts_total_count" in x)
class ReportMapper(BaseMapper):
    """
    There are four types of reports and each can be represented in 2 or 3 formats.
    TYPE/FORMAT | in IOC endp. | short | full
       Fintel   |     x        |   x   |  x
       Inforep  |     x        |   x   |  x
       Breach   |     x        |       x
       Spot     |     x        |       x
    """
    remove_html_regex = re.compile(r"<.*?>")
    reports_settings = {
        ReportType.fintel: ReportSettings(
            "ReportsApi",
            "reports_uid_get",
            "subject",
            # There's no summary or anything similar. Try to extract contents of the first paragraph <h2>...</h2><p>get-this</p>...
            lambda x: re.split(r'</?p>', re.sub(r'^.*?<p>', '', x.get("rawText") or ""))[0],
            ["rawText"]
        ),        
        ReportType.inforep: ReportSettings(
            "ReportsApi",
            "reports_uid_get",
            "subject",
            "executive_summary",
            ["rawText", "rawTextTranslated", "researcherComments"]
        ),
        ReportType.breach_alert: ReportSettings(
            "ReportsApi",
            "breach_alerts_uid_get",
            "data.breach_alert.title",
            "data.breach_alert.summary",
        ),
        ReportType.spotrep: ReportSettings(
            "ReportsApi",
            "spot_reports_uid_get",
            "data.spot_report.spot_report_data.title",
            "data.spot_report.spot_report_data.text"
        )
    }

    def __init__(self, settings: STIXMapperSettings):
        super().__init__(settings)
        self.cache = {}

    def map(self, source: dict) -> Bundle:
        """
        Main entrypoint for mapping reponses from /report, /breachAlerts and /spotReports endpoint
        """
        container = {}
        container = self.__map_playground()
        # for each report in source:
        # determine type of the report
        # determine if full report is needed
        # based on above either call _map_report_short or _map_report_full
        # think if there should be a per-report config and one mapping method or separate method for each report type
        
        # if reports search response and full required and type in (fintel, inforep):
        #   self._fetch_and_map_report_full()
        # else
        #   self._map_report(report_src)
        if container:
            bundle = Bundle(*container.values(), allow_custom=True)
            return bundle

    def __map_playground(self):
        container = {}
        some_ind = Indicator(pattern="[ file:name = 'foo.dll' ]", pattern_type="stix")
        report = Report(name="qwe", object_refs={some_ind.id: some_ind}, published=datetime.datetime(2024,11,11,12,0,0))
        container[report.id] = report
        container[some_ind.id] = some_ind        
        return container

    def map_report_ioc(self, source: dict, object_refs: dict) -> Report:
        """
        Map report in the format as used when attached to IOCs (in the response of /iocs endpoint).
        This format differs from the one in actual reports endpoint (/reports, /breachAlerts, etc.)
        {"iocs": [{"links": {"reports": [{"uid": "123", "subject": "foo", ... }]}}]}
        """
        titan_id = source["uid"]
        titan_url = source["portalReportUrl"]
        report_type = ReportType[titan_url.split("/")[-2]]
        if self._full_report_required():
            return self._fetch_and_map_report_full(report_type, titan_id, object_refs)

        name = source["subject"]
        time_published = self._format_published(source["released"])
        id_ = generate_id(
                Report,
                name=self.shorten(name, 128).strip().lower(),
                published=time_published,
            )
        external_references = [ExternalReference(source_name="Titan URL", url=titan_url)]
        confidence = self.map_confidence(source.get("admiraltyCode"))
        
        return Report(
            id = id_,
            name=name,
            description=name,
            report_types = [report_type.value],
            confidence=confidence,
            published=time_published,
            object_refs=object_refs,
            external_references=external_references,
            created_by_ref=author_identity,
            object_marking_refs=TLP_AMBER,
            custom_properties={"x_intel471_com_uid": titan_id}
        )

    def _full_report_required(self) -> bool:
        return all([self.settings.titan_client, self.settings.api_client]) and \
           any([self.settings.report_description, self.settings.report_attachments_opencti])

    def _map_report(self, source: dict, object_refs: dict = None) -> Report:
        """
        Map report in the format that is used when getting a report by ID.
        In case of FINTEL and INFOREP (/reports endpoint) there will be extra (possible big) fields.
        Breach alert and Spot report look the same in their long and short representation
        """
        name = source.get("subject") or source.get("title")
        time_published = self._format_published(source.get("released_at") or source.get("created"))
        report_kwargs = {
            "id": generate_id(
                Report,
                name=self.shorten(name, 128).strip().lower(),
                published=time_published,
            ),
            "name": name,
            "description": self._get_description(source) or name,
            "report_types": [self._get_type(source).value],
            "confidence": self.map_confidence(source.get("admiraltyCode") or source.get("data", {}).get("breach_alert", {}).get("confidence", {}).get("level")),
            "published": time_published,
            "labels": self._get_malware_families(source),
            "external_references": [
                ExternalReference(source_name="Titan URL", url=self._get_url(source))
            ],
            "created_by_ref": author_identity,
            "object_marking_refs": [TLP_AMBER],
            "custom_properties": {
                "x_intel471_com_uid": source["uid"]
            }
        }
        if object_refs:
            report_kwargs["object_refs"] = object_refs.values()
        if opencti_files := self._get_opencti_files(source):
            report_kwargs["custom_properties"]["x_opencti_files"] = opencti_files
        return Report(**report_kwargs)

    def _fetch_and_map_report_full(self, report_type: ReportType, report_id: str, object_refs: dict = None) -> Report:
        report_settings = self.reports_settings.get(report_type)
        if report_id not in self.cache:
            api_instance = getattr(self.settings.titan_client, report_settings.api_class)(self.settings.api_client)
            api_response = getattr(api_instance, report_settings.method_name)(report_id)
            self.cache[report_id] = api_response.to_dict(serialize=True)
        return self._map_report(self.cache[report_id], object_refs)

    def _format_published(self, epoch_millis: int):
        """
        Formatting datetime object for use as ID contributing property in a same way as it's done by OpenCTI
        to have the same ID here and in OpenCTI.
        """
        parsed = datetime.datetime.fromtimestamp(epoch_millis / 1000, UTC)
        return parsed.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    def _get_type(self, source: dict) -> ReportType:
        if source.get("documentFamily") == "FINTEL":
            return ReportType.fintel
        if source.get("documentFamily") == "INFOREP":
            return ReportType.inforep
        if "breach_alert" in source.get("data", {}):
            return ReportType.breach_alert
        if "spot_report" in source.get("data", {}):
            return ReportType.breach_alert
        raise TitanStixException("Unkown report type")

    def _get_url(self, source: dict) -> str:
        report_type = self._get_type(source)
        report_id = source["uid"]
        return f"https://titan.intel471.com/report/{report_type.value}/{report_id}"

    def _get_description(self, source: dict) -> str:
        report_settings = self.reports_settings.get(self._get_type(source))
        description_source = report_settings.description_source

        if isinstance(description_source, Callable):
            source = description_source(source)
        else:
            for i in description_source.split("."):
                source = source.get(i, {})

        if source:
            return re.sub(self.remove_html_regex, "", source)
        
    def _get_malware_families(self, source: dict):
        return [i.get("value") for i in (source.get("entities") or []) if i.get("type") == "MalwareFamily"]
    
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
                    "name":  " ".join([i.capitalize() for i in re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))|[a-z]+', field_name)]) + ".html",
                    "mime_type": "text/html",
                    "data": base64.b64encode(bytes(value, "utf-8")).decode("utf-8")
                })
        return opencti_files