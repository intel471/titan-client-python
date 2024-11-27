import base64
import datetime
import logging
import re
from enum import Enum
from typing import List, NamedTuple, Union, Callable

from pytz import UTC
from stix2 import TLP_AMBER, Bundle, ExternalReference, Report

from titan_client.titan_stix.exceptions import TitanStixException
from .entities import EntitiesMapper

from .. import STIXMapperSettings, author_identity, generate_id, StixObjects
from .common import BaseMapper, StixMapper
from ..constants import MARKING, REMOVE_HTML_REGEX
from ..sdo import map_organization


log = logging.getLogger(__name__)


class ReportType(Enum):
    INFOREP = "inforep"
    FINTEL = "fintel"
    BREACH_ALERT = "breach_alert"
    SPOTREP = "spotrep"
    MALWARE = "malware"


class ReportSettings(NamedTuple):
    api_class: str
    method_name: str
    # either JSON path to the field or a function that extracts value from provided source
    title_path: str
    description_path_or_extractor: Union[str, Callable[[dict], str]]
    released_at_path: str
    entities_path_or_extractor: Union[str, Callable[[dict], str]]
    victims_path: str
    links_path: str
    attachments_paths: Union[List[str], None] = None


@StixMapper.register("fintels_inforeps", lambda x: "reportTotalCount" in x)
@StixMapper.register("fintel_inforep", lambda x: x.get("documentFamily") in ("FINTEL", "INFOREP"))
@StixMapper.register("breach_alerts", lambda x: "breach_alerts_total_count" in x)
@StixMapper.register("breach_alert", lambda x: "breach_alert" in x.get("data", {}))
@StixMapper.register("spotreps", lambda x: "spotReportsTotalCount" in x)
@StixMapper.register("spotrep", lambda x: "spot_report" in x.get("data", {}))
@StixMapper.register("malreps", lambda x: "malwareReportTotalCount" in x)
@StixMapper.register("malrep", lambda x: "malware_report_data" in x.get("data", {}))
class ReportMapper(BaseMapper):
    reports_settings = {
        ReportType.FINTEL: ReportSettings(
            api_class="ReportsApi",
            method_name="reports_uid_get",
            title_path="subject",
            # There's no summary or anything similar. Try to extract contents of the first
            # paragraph <h2>...</h2><p>get-this</p>...
            description_path_or_extractor=lambda src: re.split(r'</?p>', re.sub(r'^.*?<p>', '', src.get("rawText") or ""))[0],
            released_at_path="created",
            entities_path_or_extractor="entities",
            victims_path="victims",
            links_path="sources",
            attachments_paths=["rawText"]
        ),
        ReportType.INFOREP: ReportSettings(
            api_class="ReportsApi",
            method_name="reports_uid_get",
            title_path="subject",
            description_path_or_extractor="executiveSummary",
            released_at_path="created",
            entities_path_or_extractor="entities",
            victims_path="victims",
            links_path="sources",
            attachments_paths=["rawText", "rawTextTranslated", "researcherComments"]
        ),
        ReportType.BREACH_ALERT: ReportSettings(
            api_class="ReportsApi",
            method_name="breach_alerts_uid_get",
            title_path="data.breach_alert.title",
            description_path_or_extractor="data.breach_alert.summary",
            released_at_path="data.breach_alert.released_at",
            entities_path_or_extractor="data.entities",
            victims_path="data.breach_alert.victim",
            links_path="data.breach_alert.sources"
        ),
        ReportType.SPOTREP: ReportSettings(
            api_class="ReportsApi",
            method_name="spot_reports_uid_get",
            title_path="data.spot_report.spot_report_data.title",
            description_path_or_extractor="data.spot_report.spot_report_data.text",
            released_at_path="data.spot_report.spot_report_data.released_at",
            entities_path_or_extractor="data.entities",
            victims_path="data.spot_report.spot_report_data.victims",
            links_path="data.spot_report.spot_report_data.links"
        ),
        ReportType.MALWARE: ReportSettings(
            api_class="ReportsApi",
            method_name="malware_reports_uid_get",
            title_path="data.malware_report_data.title",
            description_path_or_extractor="data.malware_report_data.text",
            released_at_path="data.malware_report_data.released_at",
            entities_path_or_extractor=lambda src: [{"type": "MalwareFamily", "value": src.get("data", {}).get("threat", {}).get("data", {}).get("family")}],
            victims_path="",
            links_path=""
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
        elif "malwareReportTotalCount" in source:
            items = source.get("malwareReports") or []
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
        if not object_refs:
            object_refs = StixObjects()
        if entities := self._get_entities(source):
            object_refs.extend(entities)
        if victims := self._get_victims(source):
            object_refs.extend(victims)

        report_type: ReportType = self._get_type(source)
        if not object_refs:
            log.info("No entities associated with the report. Skipping the report %s/%s",
                     report_type, source["uid"])
            return StixObjects()

        stix_objects = StixObjects([MARKING, author_identity])
        stix_objects.extend(object_refs)
        name = self._get_title(source)
        time_published = self._format_published(self._get_released_at(source))
        report_types = [report_type.value]
        girs_paths = source.get("data", {}).get("classification", {}).get("intelRequirements")
        labels = self._get_malware_families(source)
        if girs_paths:
            girs_names = self.get_girs_names()
            girs = [{"path": i, "name": girs_names.get(i)} for i in girs_paths]
            labels = [labels] + self.format_girs_labels(girs)
        if report_type == ReportType.FINTEL:
            report_types.append(source["documentType"].lower())
        report_kwargs = {
            "id": self._get_report_id(name, time_published),
            "name": name,
            "description": self._get_description(source) or name,
            "report_types": report_types,
            "confidence": self.map_confidence(source.get("admiraltyCode") or 
                                              source.get("data", {}).get("breach_alert", {})
                                              .get("confidence", {}).get("level")),
            "published": time_published,
            "labels": labels,
            "external_references": self._get_external_references(source),
            "object_refs": object_refs,
            "created_by_ref": author_identity,
            "object_marking_refs": [MARKING],
            "custom_properties": {
                "x_intel471_com_uid": source["uid"],
            }
        }
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

    def _get_external_references(self, source: dict) -> List[ExternalReference]:
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
        report_settings = self.reports_settings.get(self._get_type(source))
        entities_path_or_extractor = report_settings.entities_path_or_extractor
        if isinstance(entities_path_or_extractor, Callable):
            source = entities_path_or_extractor(source)
        else:
            for i in entities_path_or_extractor.split("."):
                source = source.get(i, {})
        stix_objects = StixObjects()
        for entities_source in source or []:
            if entity := self.entities_mapper.map(**entities_source):
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
        if "malware_report_data" in source.get("data", {}):
            return ReportType.MALWARE
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
