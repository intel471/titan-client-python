import base64
import datetime
import re
from collections.abc import Callable
from enum import Enum
from typing import List, NamedTuple, Union

from pytz import UTC
from stix2 import TLP_AMBER, Bundle, ExternalReference, Report

from titan_client.titan_stix.exceptions import TitanStixException
from .entities import EntitiesMapper

from .. import STIXMapperSettings, author_identity, generate_id, StixObjects
from .common import BaseMapper, StixMapper
from ..constants import MARKING, REMOVE_HTML_REGEX
from ..sdo import map_organization


class ReportType(Enum):
    INFOREP = "inforep"
    FINTEL = "fintel"
    BREACH_ALERT = "breach_alert"
    SPOTREP = "spotrep"


class ReportSettings(NamedTuple):
    api_class: str
    method_name: str
    # either JSON path to the field or a function that extracts value from provided source
    title_path: str
    description_path_or_extractor: Union[str, Callable[[dict], str]]
    released_at_path: str
    victims_path: str
    links_path: str
    attachments_paths: Union[List[str], None] = None


@StixMapper.register("fintels_inforeps", lambda x: "reportTotalCount" in x)
@StixMapper.register("fintel_inforep", lambda x: x.get("documentFamily") in ("FINTEL", "INFOREP"))
@StixMapper.register("breach_alerts", lambda x: "breach_alerts_total_count" in x)
@StixMapper.register("breach_alert", lambda x: "breach_alert" in x.get("data", {}))
@StixMapper.register("spotreps", lambda x: "spotReportsTotalCount" in x)
@StixMapper.register("spotrep", lambda x: "spot_report" in x.get("data", {}))
class ReportMapper(BaseMapper):
    reports_settings = {
        ReportType.FINTEL: ReportSettings(
            "ReportsApi",
            "reports_uid_get",
            "subject",
            # There's no summary or anything similar. Try to extract contents of the first
            # paragraph <h2>...</h2><p>get-this</p>...
            lambda x: re.split(r'</?p>', re.sub(r'^.*?<p>', '', x.get("rawText") or ""))[0],
            "created",
            "victims",
            "sources",
            ["rawText"]
        ),
        ReportType.INFOREP: ReportSettings(
            "ReportsApi",
            "reports_uid_get",
            "subject",
            "executiveSummary",
            "created",
            "victims",
            "sources",
            ["rawText", "rawTextTranslated", "researcherComments"]
        ),
        ReportType.BREACH_ALERT: ReportSettings(
            "ReportsApi",
            "breach_alerts_uid_get",
            "data.breach_alert.title",
            "data.breach_alert.summary",
            "data.breach_alert.released_at",
            "data.breach_alert.victim",
            "data.breach_alert.sources"
        ),
        ReportType.SPOTREP: ReportSettings(
            "ReportsApi",
            "spot_reports_uid_get",
            "data.spot_report.spot_report_data.title",
            "data.spot_report.spot_report_data.text",
            "data.spot_report.spot_report_data.released_at",
            "data.spot_report.spot_report_data.victims",
            "data.spot_report.spot_report_data.links"
        )
    }

    def __init__(self, settings: STIXMapperSettings):
        super().__init__(settings)
        self.entities_mapper = EntitiesMapper()
        self.cache = {}

    def map(self, source: dict) -> Bundle:
        """
        Main entrypoint for mapping responses from /report, /breachAlerts and /spotReports endpoints
        """
        if "reportTotalCount" in source:
            items = source.get("reports") or []
        elif "breach_alerts_total_count" in source:
            items = source.get("breach_alerts") or []
        elif "spotReportsTotalCount" in source:
            items = source.get("spotReports") or []
        else:
            items = [source]

        stix_objects = StixObjects()
        for item in items:
            report_type = self._get_type(item)
            if report_type in (ReportType.FINTEL,
                               ReportType.INFOREP) and self._is_full_report_required():
                # In this case search reports API returns shortened version, without content fields
                # Full version is available only when getting individual report by ID
                stix_objects.extend(self._fetch_and_map_report(report_type, item["uid"]))
            else:
                stix_objects.extend(self._map_report(item))
        if stix_objects:
            bundle = Bundle(*stix_objects, allow_custom=True)
            return bundle

    def map_report_ioc(self, source: dict, object_refs: StixObjects) -> StixObjects:
        """
        Map report in the format as used when attached to IOCs (in the response of /iocs endpoint).
        This format differs from the one in actual reports endpoint (/reports, /breachAlerts, etc.)
        {"iocs": [{"links": {"reports": [{"uid": "123", "subject": "foo", ... }]}}]}
        """
        titan_id = source["uid"]
        titan_url = source["portalReportUrl"]
        report_type = ReportType[titan_url.split("/")[-2].upper()]
        if self._is_full_report_required():
            return self._fetch_and_map_report(report_type, titan_id, object_refs)

        name = source["subject"]
        time_published = self._format_published(source["released"])
        external_references = [ExternalReference(source_name="Titan URL", url=titan_url)]
        confidence = self.map_confidence(source.get("admiraltyCode"))

        return StixObjects([Report(
            id = self._get_report_id(name, time_published),
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
        )])

    def _map_report(self, source: dict, object_refs: StixObjects = None) -> StixObjects:
        """
        Map report in the format that is used when getting a report by ID.
        In case of FINTEL and INFOREP (/reports endpoint) there will be extra (possible big) fields.
        Breach alert and Spot report look the same in their long and short representation
        """
        stix_objects = StixObjects([MARKING, author_identity])
        name = self._get_title(source)
        time_published = self._format_published(self._get_released_at(source))
        report_kwargs = {
            "id": self._get_report_id(name, time_published),
            "name": name,
            "description": self._get_description(source) or name,
            "report_types": [self._get_type(source).value],
            "confidence": self.map_confidence(source.get("admiraltyCode") or 
                                              source.get("data", {}).get("breach_alert", {})
                                              .get("confidence", {}).get("level")),
            "published": time_published,
            "labels": self._get_malware_families(source),
            "external_references": self._get_external_references(source),
            "created_by_ref": author_identity,
            "object_marking_refs": [MARKING],
            "custom_properties": {
                "x_intel471_com_uid": source["uid"]
            }
        }

        if not object_refs:
            object_refs = StixObjects()
        if entities := self._get_entities(source):
            object_refs.extend(entities)
        if victims := self._get_victims(source):
            object_refs.extend(victims)

        report_kwargs["object_refs"] = object_refs
        stix_objects.extend(object_refs)
        if opencti_files := self._get_opencti_files(source):
            report_kwargs["custom_properties"]["x_opencti_files"] = opencti_files
        stix_objects.append(Report(**report_kwargs))
        return stix_objects

    def _fetch_and_map_report(self, report_type: ReportType, report_id: str,
                              object_refs: StixObjects = None) -> StixObjects:
        report_settings = self.reports_settings.get(report_type)
        if report_id not in self.cache:
            api_instance = getattr(self.settings.titan_client,
                                   report_settings.api_class)(self.settings.api_client)
            api_response = getattr(api_instance, report_settings.method_name)(report_id)
            self.cache[report_id] = api_response.to_dict(serialize=True)
        return self._map_report(self.cache[report_id], object_refs)

    def _is_full_report_required(self) -> bool:
        return all([self.settings.titan_client, self.settings.api_client]) and \
           any([self.settings.report_description, self.settings.report_attachments_opencti])

    def _get_report_id(self, name: str, time_published: str) -> str:
        return generate_id(
            Report,
            name=name.strip().lower(),
            published=time_published
        )

    def _get_external_references(self, source: dict) -> list[ExternalReference]:
        references = [ExternalReference(source_name="Titan URL", url=self._get_url(source))]
        report_settings = self.reports_settings.get(self._get_type(source))
        links_path = report_settings.links_path
        for i in links_path.split("."):
            source = source.get(i, {})
        if source:
            for link_source in source:
                if "intel471.com/report" in link_source["url"]:
                    continue
                source_name = f"{link_source.get('source_type', '')} {link_source['type']} - {link_source['title']}".strip()
                external_ref = ExternalReference(url=link_source["url"], source_name=source_name)
                references.append(external_ref)
        return references

    def _get_entities(self, source: dict) -> StixObjects:
        entities_sources = source.get("data", {}).get("entities") or source.get("entities") or []
        stix_objects = StixObjects()
        for entities_source in entities_sources:
            entity = self.entities_mapper.map(**entities_source)
            if not entity:
                # TODO: log.debug
                print(f"Not translating {entities_source}")
                continue
            stix_objects.append(entity)
        return stix_objects

    def _get_victims(self, source: dict) -> StixObjects:
        stix_objects = StixObjects()
        report_settings = self.reports_settings.get(self._get_type(source))
        for i in report_settings.victims_path.split("."):
            source = source.get(i, {})
        if source:
            if isinstance(source, dict):
                source = [source]
            for victim_src in source:
                stix_objects.append(
                    map_organization(victim_src["name"], victim_src["urls"][0]))
            return stix_objects

    def _format_published(self, epoch_millis: int):
        """
        Formatting datetime object for use as ID contributing property in a same way as it's done
        by OpenCTI to have the same ID here and in OpenCTI.
        """
        parsed = datetime.datetime.fromtimestamp(epoch_millis / 1000, UTC)
        return parsed.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    def _get_type(self, source: dict) -> ReportType:
        if source.get("documentFamily") == "FINTEL":
            return ReportType.FINTEL
        if source.get("documentFamily") == "INFOREP":
            return ReportType.INFOREP
        if "breach_alert" in source.get("data", {}):
            return ReportType.BREACH_ALERT
        if "spot_report" in source.get("data", {}):
            return ReportType.SPOTREP
        raise TitanStixException("Unkown report type")

    def _get_url(self, source: dict) -> str:
        report_type = self._get_type(source)
        report_id = source["uid"]
        return f"https://titan.intel471.com/report/{report_type.value}/{report_id}"

    def _get_released_at(self, source: dict) -> Union[int, None]:
        report_settings = self.reports_settings.get(self._get_type(source))
        released_at_path = report_settings.released_at_path
        for i in released_at_path.split("."):
            source = source.get(i, {})
        return source or None

    def _get_title(self, source: dict) -> Union[str, None]:
        report_settings = self.reports_settings.get(self._get_type(source))
        title_path = report_settings.title_path
        for i in title_path.split("."):
            source = source.get(i, {})
        return source or None

    def _get_description(self, source: dict) -> Union[str, None]:
        report_settings = self.reports_settings.get(self._get_type(source))
        description_path_or_extractor = report_settings.description_path_or_extractor
        if not self.settings.report_description:
            return None

        if isinstance(description_path_or_extractor, Callable):
            source = description_path_or_extractor(source)
        else:
            for i in description_path_or_extractor.split("."):
                source = source.get(i, {})

        if source and isinstance(source, str):
            return re.sub(REMOVE_HTML_REGEX, "", source)

    @staticmethod
    def _get_malware_families(source: dict):
        return [i.get("value") for i in (source.get("entities") or [])
                if i.get("type") == "MalwareFamily"]

    def _get_opencti_files(self, source: dict):
        if not self.settings.report_attachments_opencti:
            return []
        opencti_files = []
        report_settings = self.reports_settings.get(self._get_type(source))
        attachments_fields = report_settings.attachments_paths or []
        for field_name in attachments_fields:
            value = source.get(field_name)
            if isinstance(value, str):
                opencti_files.append({
                    "name":  " ".join([i.capitalize() for i in re.findall(
                        r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))|[a-z]+', field_name)]) + ".html",
                    "mime_type": "text/html",
                    "data": base64.b64encode(bytes(value, "utf-8")).decode("utf-8")
                })
        return opencti_files
