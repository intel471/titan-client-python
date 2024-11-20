from stix2 import Malware, TLP_AMBER, ThreatActor
from . import generate_id, author_identity


def map_malware(value: str, *args, **kwargs) -> Malware:
    return Malware(
        id=generate_id(Malware, name=value.strip().lower()),
        name=value,
        is_family=True,
        created_by_ref=author_identity,
        object_marking_refs=[TLP_AMBER],
    )

def map_threat_actor(value: str, *args, **kwargs) -> ThreatActor:
    return ThreatActor(
        name = value,
        created_by_ref=author_identity,
        object_marking_refs=[TLP_AMBER],
)