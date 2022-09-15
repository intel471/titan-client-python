import datetime
import uuid
from typing import Union

from stix2 import Relationship, base, Identity
from stix2.base import _DomainObject, _Observable
from stix2.canonicalization.Canonicalize import canonicalize


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
