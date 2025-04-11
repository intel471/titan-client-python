import datetime
import logging
from typing import Union

from pytz import UTC
from stix2 import Bundle, Indicator, Report, DomainName, URL, Relationship

from .. import author_identity, generate_id, StixObjects
from ..constants import MARKING
from ..patterning import create_domain_pattern, create_url_pattern, create_ipv4_pattern, create_file_pattern
from ..sco import map_domain, map_url, map_ipv4, map_file
from .reports import ReportMapper
from .common import StixMapper, BaseMapper, MappingConfig

log = logging.getLogger(__name__)


@StixMapper.register("iocs", lambda x: "iocTotalCount" in x)
class IOCMapper(BaseMapper):

    mapping_configs = {
        "MaliciousURL": MappingConfig(
            patterning_mapper=create_url_pattern,
            entities_mapper=map_url,
            kwargs_extractor=lambda i: {"value": i["value"]},
            name_extractor=lambda i: i["value"],
            opencti_type="Url"
        ),
        "MaliciousDomain": MappingConfig(
            patterning_mapper=create_domain_pattern,
            entities_mapper=map_domain,
            kwargs_extractor=lambda i: {"value": i["value"].split("://")[-1]},
            name_extractor=lambda i: i["value"].split("://")[-1],
            opencti_type="Domain-Name"
        ),
        "IPAddress": MappingConfig(
            patterning_mapper=create_ipv4_pattern,
            entities_mapper=map_ipv4,
            kwargs_extractor=lambda i: {"value": i["value"]},
            name_extractor=lambda i: i["value"],
            opencti_type="IPv4-Addr"
        ),
        "MD5": MappingConfig(
            patterning_mapper=create_file_pattern,
            entities_mapper=map_file,
            kwargs_extractor=lambda i: {"md5": i["value"]},
            name_extractor=lambda i: i["value"],
            opencti_type="StixFile"
        ),
        "SHA1": MappingConfig(
            patterning_mapper=create_file_pattern,
            entities_mapper=map_file,
            kwargs_extractor=lambda i: {"sha1": i["value"]},
            name_extractor=lambda i: i["value"],
            opencti_type="StixFile"
        ),
        "SHA256": MappingConfig(
            patterning_mapper=create_file_pattern,
            entities_mapper=map_file,
            kwargs_extractor=lambda i: {"sha256": i["value"]},
            name_extractor=lambda i: i["value"],
            opencti_type="StixFile"
        )
    }

    def map(self, source: dict) -> Bundle:
        container = StixObjects()
        report_mapper = ReportMapper(self.settings)
        items = source.get("iocs") or [] if "iocTotalCount" in source else [source]
        for item in items:
            ioc_type = item["type"]
            mapping_config = self.mapping_configs.get(ioc_type)
            if not mapping_config:
                continue
            report_sources = item["links"].get("reports") or []
            valid_from = datetime.datetime.fromtimestamp(item["activeFrom"] / 1000, UTC)
            valid_until = datetime.datetime.fromtimestamp(
                item["activeTill"] / 1000, UTC
            )
            if valid_from == valid_until:
                valid_until = None

            name = mapping_config.name_extractor(item)
            kwargs = mapping_config.kwargs_extractor(item)
            stix_pattern = mapping_config.patterning_mapper(**kwargs)
            observable = self.map_entity(item)
            indicator = Indicator(
                id=generate_id(Indicator, pattern=stix_pattern),
                name=name,
                pattern_type="stix",
                pattern=stix_pattern,
                indicator_types=["malicious-activity"],
                valid_from=valid_from,
                valid_until=valid_until,
                created_by_ref=author_identity,
                object_marking_refs=[MARKING],
                custom_properties={"x_opencti_main_observable_type": mapping_config.opencti_type}
            )
            r1 = Relationship(
                indicator, "based-on", observable, created_by_ref=author_identity
            )
            container.extend([indicator, observable, r1, author_identity, MARKING])
            for stix_object in self._map_reports(
                report_mapper, report_sources, indicator, observable, r1).get():
                if isinstance(stix_object, Report):
                    if already_mapped_reports := [i for i in container.get() if i.id == stix_object.id]:
                        already_mapped_report = already_mapped_reports[0]
                        already_mapped_report.object_refs.extend(stix_object.object_refs)
                container.add(stix_object)
        if container:
            bundle = Bundle(*container.get(), allow_custom=True)
            return bundle

    def map_entity(self, source: dict):
        mapping_config = self.mapping_configs.get(source["type"])
        kwargs = mapping_config.kwargs_extractor(source)
        return mapping_config.entities_mapper(**kwargs)

    @staticmethod
    def _map_reports(
        report_mapper,
        report_sources: list,
        indicator: Indicator,
        observable: Union[URL, DomainName],
        relationship: Relationship
    ) -> StixObjects:
        stix_objects = StixObjects()
        for report_source in report_sources:
            report_etc: StixObjects = report_mapper.map_report_ioc(
                report_source,
                object_refs=StixObjects([indicator, observable, relationship]))
            stix_objects.extend(report_etc.get())
        return stix_objects
