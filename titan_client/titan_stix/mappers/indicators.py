import datetime

import yaml
from pytz import UTC
from stix2 import Indicator, Bundle, Relationship, KillChainPhase, TLP_AMBER

from .. import author_identity, generate_id, StixObjects
from .common import StixMapper, BaseMapper, MappingConfig
from ..patterning import create_url_pattern, create_ipv4_pattern, create_file_pattern
from ..sco import map_url, map_ipv4, map_file
from ..sdo import map_malware


@StixMapper.register("indicators", lambda x: "indicatorTotalCount" in x)
class IndicatorsMapper(BaseMapper):

    mapping_configs = {
        "url": MappingConfig(
            patterning_mapper=create_url_pattern,
            entities_mapper=map_url,
            kwargs_extractor=lambda i: {"value": i["data"]["indicator_data"]["url"]},
            name_extractor=lambda i: i["data"]["indicator_data"]["url"],
            opencti_type="Url"
        ),
        "ipv4": MappingConfig(
            patterning_mapper=create_ipv4_pattern,
            entities_mapper=map_ipv4,
            kwargs_extractor=lambda i: {
                "value": i["data"]["indicator_data"]["address"]
            },
            name_extractor=lambda i: i["data"]["indicator_data"]["address"],
            opencti_type="IPv4-Addr"
        ),
        "file": MappingConfig(
            patterning_mapper=create_file_pattern,
            entities_mapper=map_file,
            kwargs_extractor=lambda i: {
                "md5": i["data"]["indicator_data"]["file"]["md5"],
                "sha1": i["data"]["indicator_data"]["file"]["sha1"],
                "sha256": i["data"]["indicator_data"]["file"]["sha256"],
            },
            name_extractor=lambda i: i["data"]["indicator_data"]["file"]["sha256"],
            opencti_type="StixFile"
        ),
    }

    def map(self, source: dict) -> Bundle:
        container = StixObjects()
        items = (
            source.get("indicators") or []
            if "indicatorTotalCount" in source
            else [source]
        )
        for item in items:
            indicator_type = item["data"]["indicator_type"]
            mapping_config = self.mapping_configs.get(indicator_type)
            if not mapping_config:
                continue
            malware_family_name = item["data"]["threat"]["data"]["family"]
            valid_from = datetime.datetime.fromtimestamp(
                item["activity"]["first"] / 1000, UTC
            )
            valid_until = datetime.datetime.fromtimestamp(
                item["data"]["expiration"] / 1000, UTC
            )
            tactics = self.map_tactic(item["data"]["mitre_tactics"])
            confidence = self.map_confidence(item["data"]["confidence"])
            name = mapping_config.name_extractor(item)
            description = item["data"]["context"]["description"]
            kwargs = mapping_config.kwargs_extractor(item)
            stix_pattern = mapping_config.patterning_mapper(**kwargs)
            observable = mapping_config.entities_mapper(**kwargs)
            malware = map_malware(malware_family_name)
            custom_properties = {"x_opencti_main_observable_type": mapping_config.opencti_type}
            if self.settings.ioc_opencti_score:
                custom_properties.update({"x_opencti_score": self.settings.ioc_opencti_score})
            labels = [malware_family_name]
            labels.extend(self.get_girs_labels(item["data"]["intel_requirements"]))
            indicator = Indicator(
                id=generate_id(Indicator, pattern=stix_pattern),
                pattern_type="stix",
                pattern=stix_pattern,
                indicator_types=["malicious-activity"],
                valid_from=valid_from,
                valid_until=valid_until,
                created_by_ref=author_identity,
                object_marking_refs=[TLP_AMBER],
                name=name,
                description=description,
                labels=labels,
                confidence=confidence,
                kill_chain_phases=[
                    KillChainPhase(kill_chain_name="mitre-attack", phase_name=tactics)
                ],
                custom_properties=custom_properties
            )
            r1 = Relationship(
                indicator, "indicates", malware, created_by_ref=author_identity
            )
            r2 = Relationship(
                indicator, "based-on", observable, created_by_ref=author_identity
            )
            for stix_object in [
                malware,
                indicator,
                observable,
                r1,
                r2,
                author_identity,
                TLP_AMBER,
            ]:
                container.add(stix_object)
        if container:
            bundle = Bundle(*container.get(), allow_custom=True)
            return bundle
