import datetime
import uuid
from typing import Union, NamedTuple

from stix2 import Relationship, base, Identity
from stix2.base import _DomainObject, _Observable
from stix2.canonicalization.Canonicalize import canonicalize


class STIXMapperSettings(NamedTuple):
    titan_client: Union['titan_client', None] = None
    api_client: Union['ApiClient', None] = None
    # Resolve GIRs numbers into full names
    girs_names: bool = True
    # Get full reports' descriptions
    report_description: bool = True
    # Get HTML representation of reports contents and return them in a format
    # understandable for OpenCTI (base64 encoded, inside specific JSON structure)
    report_attachments_opencti: bool = False

def generate_id(
    stix_class: Union[_DomainObject, Relationship, _Observable],
    **id_contributing_properties: str,
):
    if id_contributing_properties:
        name = canonicalize(id_contributing_properties, utf8=False)
        return f"{stix_class._type}--{uuid.uuid5(base.SCO_DET_ID_NAMESPACE, name)}"
    return f"{stix_class._type}--{uuid.uuid4()}"


author_name = "Intel 471 Inc."
author_identity = Identity(
    id=generate_id(Identity, name=author_name.lower(), identity_class="organization"),
    name=author_name,
    identity_class="organization",
    created=datetime.datetime(2022, 1, 1),
    modified=datetime.datetime(2022, 1, 1),
)
