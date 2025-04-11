from stix2 import Malware, ThreatActor, Identity, Vulnerability
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

def map_threat_actor(value: str, description: str = None, *args, **kwargs) -> ThreatActor:
    return ThreatActor(
        name = value,
        description = description,
        resource_level="individual",
        created_by_ref=author_identity,
        object_marking_refs=[MARKING],
)


def map_vulnerability(value: str, *args, **kwargs) -> Vulnerability:
    return Vulnerability(
        id=generate_id(Vulnerability, name=value.strip().lower()),
        name=value,
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
