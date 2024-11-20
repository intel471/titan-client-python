from stix2 import Malware, ThreatActor, Identity
from . import generate_id, author_identity
from .constants import MARKING


def map_malware(value: str, *args, **kwargs) -> Malware:
    return Malware(
        id=generate_id(Malware, name=value.strip().lower()),
        name=value,
        is_family=True,
        created_by_ref=author_identity,
        object_marking_refs=[MARKING],
    )

def map_threat_actor(value: str, *args, **kwargs) -> ThreatActor:
    return ThreatActor(
        name = value,
        created_by_ref=author_identity,
        object_marking_refs=[MARKING],
)


def map_organization(value: str, url=None, *args, **kwargs) -> Identity:
    return Identity(
        name = value,
        contact_information=url,
        identity_class="organization",
        created_by_ref=author_identity,
        object_marking_refs=[MARKING],
)
