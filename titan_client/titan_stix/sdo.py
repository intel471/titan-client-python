from stix2 import Malware, ThreatActor, Identity, Vulnerability
import pycti
from . import author_identity
from .constants import MARKING



def map_malware(value: str, *args, **kwargs) -> Malware:
    return Malware(
        id=pycti.Malware.generate_id(value),
        name=value,
        is_family=True,
        created_by_ref=author_identity,
        object_marking_refs=[MARKING],
    )

def map_threat_actor(value: str, description: str = None, *args, **kwargs) -> ThreatActor:
    return ThreatActor(
        id=pycti.ThreatActorIndividual.generate_id(value),
        name = value,
        description = description,
        resource_level="individual",
        created_by_ref=author_identity,
        object_marking_refs=[MARKING],
)


def map_vulnerability(value: str, *args, **kwargs) -> Vulnerability:
    return Vulnerability(
        id=pycti.Vulnerability.generate_id(value),
        name=value,
        created_by_ref=author_identity,
        object_marking_refs=[MARKING],
    )


def map_organization(value: str, url=None, *args, **kwargs) -> Identity:
    return Identity(
        id=pycti.Identity.generate_id(value, identity_class="organization"),
        name = value,
        contact_information=url,
        identity_class="organization",
        created_by_ref=author_identity,
        object_marking_refs=[MARKING],
)
