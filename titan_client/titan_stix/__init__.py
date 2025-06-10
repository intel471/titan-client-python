import datetime
import uuid
from typing import Union, NamedTuple, Optional, List

from stix2 import Relationship, base, Identity
from stix2.base import _DomainObject, _Observable
from stix2.canonicalization.Canonicalize import canonicalize
import pycti

from titan_client.titan_stix.constants import INTEL_471


class STIXMapperSettings(NamedTuple):
    titan_client: Union['titan_client', None] = None
    api_client: Union['ApiClient', None] = None
    # Resolve GIRs numbers into full names
    girs_names: bool = True
    # Get full reports contents using additional API call. Applicable to FINTEL and INFOREP
    # as other reports have full content in respective search APIs already.
    report_full_content: bool = True
    ioc_opencti_score: Optional[int] = None


class StixObjects:
    """
    Helper class for collecting unique STIX instances (by STIX ID)
    """
    def __init__(self, objects: Union[List, None]=None):
        self._container = {}
        if objects:
            self.extend(objects)

    def add(self, item):
        item_id = item.id
        if item_id not in self._container:
            self._container[item_id] = item

    def extend(self, __iterable):
        for i in __iterable:
            self.add(i)

    def get(self):
        return self._container.values()

    def __bool__(self):
        return bool(self._container)


author_name = f"{INTEL_471} Inc."
author_identity = Identity(
    id=pycti.Identity.generate_id(author_name, identity_class="organization"),
    name=author_name,
    identity_class="organization",
    created=datetime.datetime(2022, 1, 1),
    modified=datetime.datetime(2022, 1, 1),
)
