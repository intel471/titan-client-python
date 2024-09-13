import datetime
import logging
from typing import Union

from pytz import UTC
from stix2 import Bundle, Indicator, Report, TLP_AMBER, DomainName, URL, Relationship

from .. import author_identity, generate_id
from ..patterning import create_domain_pattern, create_url_pattern, create_ipv4_pattern, create_file_pattern
from ..observables import create_domain, create_url, create_ipv4, create_file
from .reports import ReportMapper
from .common import StixMapper, BaseMapper, MappingConfig

log = logging.getLogger(__name__)


@StixMapper.register("iocs", lambda x: "iocTotalCount" in x)
class IOCMapper(BaseMapper):

    mapping_configs = {
        "MaliciousURL": MappingConfig(
            patterning_mapper=create_url_pattern,
            observable_mapper=create_url,
            kwargs_extractor=lambda i: {"value": i["value"]},
            name_extractor=lambda i: i["value"],
            opencti_type="Url"
        ),
        "MaliciousDomain": MappingConfig(
            patterning_mapper=create_domain_pattern,
            observable_mapper=create_domain,
            kwargs_extractor=lambda i: {"value": i["value"].split("://")[-1]},
            name_extractor=lambda i: i["value"].split("://")[-1],
            opencti_type="Domain-Name"
        ),
        "IPAddress": MappingConfig(
            patterning_mapper=create_ipv4_pattern,
            observable_mapper=create_ipv4,
            kwargs_extractor=lambda i: {"value": i["value"]},
            name_extractor=lambda i: i["value"],
            opencti_type="IPv4-Addr"
        ),
        "MD5": MappingConfig(
            patterning_mapper=create_file_pattern,
            observable_mapper=create_file,
            kwargs_extractor=lambda i: {"md5": i["value"]},
            name_extractor=lambda i: i["value"],
            opencti_type="StixFile"
        ),
        "SHA1": MappingConfig(
            patterning_mapper=create_file_pattern,
            observable_mapper=create_file,
            kwargs_extractor=lambda i: {"sha1": i["value"]},
            name_extractor=lambda i: i["value"],
            opencti_type="StixFile"
        ),
        "SHA256": MappingConfig(
            patterning_mapper=create_file_pattern,
            observable_mapper=create_file,
            kwargs_extractor=lambda i: {"sha256": i["value"]},
            name_extractor=lambda i: i["value"],
            opencti_type="StixFile"
        )
    }

    def map(self, source: dict) -> Bundle:
        container = {}
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
            observable = mapping_config.observable_mapper(author=author_identity.id, **kwargs)
            indicator = Indicator(
                id=generate_id(Indicator, pattern=stix_pattern),
                name=name,
                pattern_type="stix",
                pattern=stix_pattern,
                indicator_types=["malicious-activity"],
                valid_from=valid_from,
                valid_until=valid_until,
                created_by_ref=author_identity,
                object_marking_refs=[TLP_AMBER],
                custom_properties={"x_opencti_main_observable_type": mapping_config.opencti_type}
            )
            r1 = Relationship(
                indicator, "based-on", observable, created_by_ref=author_identity
            )
            for stix_object in [indicator, observable, r1, author_identity, TLP_AMBER]:
                container[stix_object.id] = stix_object
            for uid, stix_object in self.map_reports(
                report_mapper, report_sources, indicator, observable, r1
            ).items():
                if isinstance(stix_object, Report) and uid in container:
                    stix_object.object_refs.extend(container[uid].object_refs)
                container[uid] = stix_object
        if container:
            bundle = Bundle(*container.values(), allow_custom=True)
            return bundle

    def map_reports(
        self,
        report_mapper,
        report_sources: list,
        indicator: Indicator,
        observable: Union[URL, DomainName],
        relationship: Relationship
    ) -> dict:
        container = {}
        for report_source in report_sources:
            container.update(
                report_mapper.map_shortened_report(
                    report_source,
                    object_refs={
                        indicator.id: indicator,
                        observable.id: observable,
                        relationship.id: relationship
                    },
                )
            )
        return container
