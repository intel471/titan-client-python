import datetime
import logging
import re
from enum import Enum
from typing import List, NamedTuple, Union, Callable

from pytz import UTC
from stix2 import TLP_AMBER, Bundle, ExternalReference, Report, ThreatActor

from titan_client.titan_stix.exceptions import TitanStixException
from .entities import EntitiesMapper

from .. import STIXMapperSettings, author_identity, generate_id, StixObjects
from .common import BaseMapper, StixMapper
from ..constants import INTEL_471, MARKING, REMOVE_HTML_REGEX
from ..sdo import map_organization


log = logging.getLogger(__name__)


class ReportType(Enum):
    INFOREP = "inforep"
    FINTEL = "fintel"
    BREACH_ALERT = "breach_alert"
    SPOTREP = "spotrep"
    MALWARE = "malware"


REPORT_SUBTYPE_ACTOR_PROFILE = "ACTOR_PROFILE"


class ReportSettings(NamedTuple):
    api_class: str
    method_name: str
    # either JSON path to the field or a function that extracts value from provided source
    title_path: str
    description_path_or_extractor: Union[str, Callable]
    released_at_path: str
    entities_path_or_extractor: Union[str, Callable]
    victims_path: str
    links_path: str
    girs_path: str
    is_sensitive_source_path: str
    contents_paths: Union[List[str], None] = None



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
            contents_paths=["rawText"],
            girs_path = "classification.intelRequirements",
            is_sensitive_source_path = "sensitiveSource"
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
            contents_paths=["executiveSummary", "researcherComments", "rawText", "rawTextTranslated", "sourceCharacterization"],
            girs_path = "classification.intelRequirements",
            is_sensitive_source_path = "sensitiveSource"
        ),
        ReportType.BREACH_ALERT: ReportSettings(
            api_class="ReportsApi",
            method_name="breach_alerts_uid_get",
            title_path="data.breach_alert.title",
            description_path_or_extractor="data.breach_alert.summary",
            released_at_path="data.breach_alert.released_at",
            entities_path_or_extractor="data.entities",
            victims_path="data.breach_alert.victim",
            links_path="data.breach_alert.sources",
            girs_path="data.breach_alert.intel_requirements",
            is_sensitive_source_path = "data.breach_alert.sensitive_source"
        ),
        ReportType.SPOTREP: ReportSettings(
            api_class="ReportsApi",
            method_name="spot_reports_uid_get",
            title_path="data.spot_report.spot_report_data.title",
            description_path_or_extractor="data.spot_report.spot_report_data.text",
            released_at_path="data.spot_report.spot_report_data.released_at",
            entities_path_or_extractor="data.entities",
            victims_path="data.spot_report.spot_report_data.victims",
            links_path="data.spot_report.spot_report_data.links",
            girs_path="data.spot_report.spot_report_data.intel_requirements",
            is_sensitive_source_path = "data.spot_report.spot_report_data.sensitive_source"
        ),
        ReportType.MALWARE: ReportSettings(
            api_class="ReportsApi",
            method_name="malware_reports_uid_get",
            title_path="data.malware_report_data.title",
            description_path_or_extractor=lambda src: re.split(r'</?p>', re.sub(r'^.*?<p>', '', src.get("data", {}).get("malware_report_data", {}).get("text") or ""))[1],
            released_at_path="data.malware_report_data.released_at",
            entities_path_or_extractor=lambda src: [{"type": "MalwareFamily", "value": src.get("data", {}).get("threat", {}).get("data", {}).get("family")}],
            victims_path="",
            links_path="",
            contents_paths=["data.malware_report_data.text"],
            girs_path = "classification.intelRequirements",
                is_sensitive_source_path = "data.malware_report_data.sensitive_source"
        )
    }

    def __init__(self, settings: STIXMapperSettings):
        super().__init__(settings)
        self.entities_mapper = EntitiesMapper()
        self.cache = {}

    def map(self, source: dict) -> Union[Bundle, None]:
        """
        Main entrypoint for mapping responses from /report, /breachAlerts and /spotReports endpoints
        """
        is_report_by_id = False
        if "reportTotalCount" in source:
            items = source.get("reports") or []
        elif "breach_alerts_total_count" in source:
            items = source.get("breach_alerts") or []
        elif "spotReportsTotalCount" in source:
            items = source.get("spotReports") or []
        elif "malwareReportTotalCount" in source:
            items = source.get("malwareReports") or []
        else:
            is_report_by_id = True
            items = [source]

        stix_objects = StixObjects()
        for item in items:
            report_type = self._get_type(item)
            if all([
                report_type in (ReportType.FINTEL, ReportType.INFOREP),
                not is_report_by_id,
                self._is_full_report_required()
            ]):
                # In this case search reports API returns shortened version, without content fields
                # Full version is available only when getting individual report by ID
                stix_objects.extend(self._fetch_and_map_report(report_type, item["uid"]).get())
            else:
                stix_objects.extend(self._map_report(item).get())
        if stix_objects:
            bundle = Bundle(*stix_objects.get(), allow_custom=True)
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
            object_refs=object_refs.get(),
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
            object_refs.extend(entities.get())
        if victims := self._get_victims(source):
            object_refs.extend(victims.get())

        report_type: ReportType = self._get_type(source)
        if not object_refs:
            log.info("No entities associated with the report. Skipping the report %s/%s",
                     report_type, source["uid"])
            return StixObjects()

        stix_objects = StixObjects([MARKING, author_identity])
        stix_objects.extend(object_refs.get())
        name = self._get_title(source)
        time_published = self._format_published(self._get_released_at(source))
        report_types = [report_type.value]
        labels = self._get_malware_families_names(stix_objects)
        if self._is_sensitive_source(source):
            labels.append(f"{INTEL_471} - sensitive source")
        labels.extend(self._get_girs_labels(source))
        description = self._get_description(source) or name
        if report_type == ReportType.FINTEL:
            document_type = source["documentType"]
            report_types.append(document_type.lower())
            if document_type == REPORT_SUBTYPE_ACTOR_PROFILE:
                threat_actor = self.entities_mapper.map(**{
                    "type": "Handle",
                    "value": name,
                    "description": description
                })
                stix_objects = StixObjects([i for i in stix_objects.get()
                                            if not (isinstance(i, ThreatActor) and i.name == name)])
                stix_objects.add(threat_actor)
                name = f"Actor Profile – {name}"

        report_kwargs = {
            "id": self._get_report_id(name, time_published),
            "name": name,
            "description": description,
            "report_types": report_types,
            "confidence": self.map_confidence(source.get("admiraltyCode") or
                                              source.get("data", {}).get("breach_alert", {})
                                              .get("confidence", {}).get("level")),
            "published": time_published,
            "labels": labels,
            "external_references": self._get_external_references(source),
            "object_refs": object_refs.get(),
            "created_by_ref": author_identity,
            "object_marking_refs": [MARKING],
            "custom_properties": {
                "x_intel471_com_uid": source["uid"],
                "content": self._get_opencti_content(source)
            }
        }
        report = Report(**report_kwargs)
        stix_objects.add(report)
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
        return all([self.settings.titan_client,
                    self.settings.api_client,
                    self.settings.report_full_content])

    @staticmethod
    def _get_report_id(name: str, time_published: str) -> str:
        return generate_id(
            Report,
            name=name.strip().lower(),
            published=time_published
        )

    def _extract_value(self, source: dict, path_or_extractor_name: str):
        report_type = self._get_type(source)
        report_settings = self.reports_settings.get(report_type)
        path_or_extractor = getattr(report_settings, path_or_extractor_name, "")
        if isinstance(path_or_extractor, Callable):
            try:
                return path_or_extractor(source)
            except Exception as e:
                log.warning("Can't extract value from report %s/%s using path/extractor `%s`. %s",
                            report_type, source["uid"], path_or_extractor_name, e)
                return None
        return self._extract_value_by_path(source, path_or_extractor) or None

    @staticmethod
    def _extract_value_by_path(source: dict, path: str):
        for i in path.split("."):
            if not source:
                break
            source = source.get(i, {})
        return source or None

    def _get_external_references(self, source: dict) -> List[ExternalReference]:
        references = [ExternalReference(source_name="Titan URL", url=self._get_url(source))]
        if value := self._extract_value(source, "links_path"):
            for link_source in value:
                if "intel471.com/report" in link_source["url"]:
                    continue
                source_name = f"{link_source.get('source_type', '')} {link_source['type']} - {link_source['title']}".strip()
                external_ref = ExternalReference(url=link_source["url"], source_name=source_name)
                references.append(external_ref)
        return references

    def _get_entities(self, source: dict) -> StixObjects:
        value = self._extract_value(source, "entities_path_or_extractor")
        stix_objects = StixObjects()
        for entities_source in value or []:
            if entity := self.entities_mapper.map(**entities_source):
                stix_objects.add(entity)
        return stix_objects

    def _get_victims(self, source: dict) -> StixObjects:
        stix_objects = StixObjects()
        if value := self._extract_value(source, "victims_path"):
            if isinstance(value, dict):
                value = [value]
            for victim_src in value:
                url = None
                if urls := victim_src.get("urls"):
                    url = urls[0]
                stix_objects.add(
                    map_organization(victim_src["name"], url))
            return stix_objects

    @staticmethod
    def _format_published(epoch_millis: int):
        """
        Formatting datetime object for use as ID contributing property in a same way as it's done
        by OpenCTI to have the same ID here and in OpenCTI.
        """
        parsed = datetime.datetime.fromtimestamp(epoch_millis / 1000, UTC)
        return parsed.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    @staticmethod
    def _get_type(source: dict) -> ReportType:
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
        return self._extract_value(source, "released_at_path") or None

    def _get_girs_labels(self, source: dict) -> List[str]:
        girs_paths = self._extract_value(source, "girs_path") or []
        return self.get_girs_labels(girs_paths)

    def _get_title(self, source: dict) -> Union[str, None]:
        return self._extract_value(source, "title_path") or None

    def _get_description(self, source: dict) -> Union[str, None]:
        value = self._extract_value(source, "description_path_or_extractor")
        if value and isinstance(value, str):
            return re.sub(REMOVE_HTML_REGEX, "", value)

    def _is_sensitive_source(self, source: dict) -> bool:
        return bool(self._extract_value(source, "is_sensitive_source_path"))

    @staticmethod
    def _get_malware_families_names(entities: StixObjects) -> List[str]:
        return [i.name for i in entities.get() if i.type == "malware"]

    def _get_opencti_content(self, source: dict):
        content_bits = []
        contents_paths = self.reports_settings.get(self._get_type(source)).contents_paths or []
        for path in contents_paths:
            value = self._extract_value_by_path(source, path)
            if value and isinstance(value, str):
                if len(contents_paths) > 1:
                    heading = " ".join([i.capitalize() for i in re.findall(
                        r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))|[a-z]+', path.split(".")[-1])])
                    content_bits.append(f"<h1>{heading}</h1>")
                content_bits.append(value)
        return "\n".join(content_bits)
