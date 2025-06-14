import datetime

from pytz import UTC
import pycti
from stix2 import Indicator, Bundle, Relationship, TLP_AMBER
from .common import StixMapper, BaseMapper
from .. import author_identity, StixObjects
from ..sdo import map_malware


@StixMapper.register("yara", lambda x: "yaraTotalCount" in x)
class YaraMapper(BaseMapper):
    def map(self, source: dict) -> Bundle:
        container = StixObjects()
        items = source.get("yaras") or [] if "yaraTotalCount" in source else [source]
        for item in items:
            yara_signature = item["data"]["yara_data"]["signature"]
            malware_family_name = item["data"]["threat"]["data"]["family"]
            valid_from = datetime.datetime.fromtimestamp(
                item["activity"]["first"] / 1000, UTC
            )
            confidence = self.map_confidence(item["data"]["confidence"])
            labels = [malware_family_name]
            labels.extend(self.get_girs_labels(item["data"]["intel_requirements"]))
            malware = map_malware(malware_family_name)
            indicator = Indicator(
                id=pycti.Indicator.generate_id(yara_signature),
                pattern_type="yara",
                pattern=yara_signature,
                indicator_types=["malicious-activity"],
                valid_from=valid_from,
                created_by_ref=author_identity,
                object_marking_refs=[TLP_AMBER],
                labels=labels,
                confidence=confidence,
            )
            relationship = Relationship(
                id=pycti.StixCoreRelationship.generate_id(
                    relationship_type="indicates",
                    source_ref=indicator.id,
                    target_ref=malware.id),
                source_ref=indicator,
                relationship_type="indicates",
                target_ref=malware,
                created_by_ref=author_identity
            )
            for stix_object in [
                malware,
                indicator,
                relationship,
                author_identity,
                TLP_AMBER,
            ]:
                container.add(stix_object)
        if container:
            bundle = Bundle(*container.get(), allow_custom=True)
            return bundle
