import abc
import datetime
import json
import logging
import os
import re
import tempfile
from abc import ABC
from collections import namedtuple
from collections.abc import Callable
from functools import wraps
from typing import Union, List

from stix2 import Bundle

from .. import INTEL_471, STIXMapperSettings
from ..exceptions import EmptyBundle, StixMapperNotFound

log = logging.getLogger(__name__)


MappingConfig = namedtuple(
    "MappingConfig",
    ["patterning_mapper", "entities_mapper", "kwargs_extractor", "name_extractor", "opencti_type"]
)


class StixMapper:
    def __init__(self, settings: STIXMapperSettings = None):
        self.settings = settings if settings else STIXMapperSettings()

    mappers = {}

    @classmethod
    def register(cls, name: str, condition) -> Callable:
        """
        Decorator used for registering mapper classes. Decorate any class derived from BaseMapper like this:

        @StixMapper.register("actors", lambda x: "actorTotalCount" in x)
        class ActorsMapper(BaseMapper):
            def map(self, source: dict) -> Bundle:
                ... my implementation ...

        @param name: unique name under which the mapper will be registered
        @param condition: callable that will be called against the source dict
                          to determine if given mapper should be used or not

        """

        def inner_wrapper(wrapped_class: Callable) -> Callable:
            if name in cls.mappers:
                log.info(f"Mapper for {name} already exists. Will replace it")
            cls.mappers[name] = (condition, wrapped_class)
            return wrapped_class

        return inner_wrapper

    def map(self, source: dict, stix_version: str = "2.1") -> Bundle:
        log.info(f"Initializing converter. STIX version {stix_version}.")
        for name, (condition, mapper_class) in self.mappers.items():
            if condition(source):
                log.info(f"Mapping Titan payload for {name}.")
                mapper = mapper_class(self.settings)
                bundle = mapper.map(source)
                if bundle:
                    return bundle
                else:
                    raise EmptyBundle("STIX Mapper produced an empty bundle.")
        raise StixMapperNotFound(
            f"STIX Mapper for this payload is not available (keys: {', '.join(source.keys())})."
        )


def cached(key):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ttl_seconds = 10 * 60 * 60  # 10 hours by default
            try:
                ttl_seconds = int(os.getenv("I471_TITAN_CLIENT_CACHE_TTL"))
            except (TypeError, ValueError):
                pass
            if ttl_seconds == 0:
                return func(*args, **kwargs)
            tempdir = tempfile.gettempdir()
            cache_postfix = int(datetime.datetime.utcnow().timestamp() / ttl_seconds)
            cache_path = os.path.join(tempdir, f"{key}{cache_postfix}")
            result = {}
            try:
                with open(cache_path) as fh:
                    result = json.load(fh)
            except Exception as e:
                try:
                    result = func(*args, **kwargs)
                    try:
                        for tmpfile in list(os.walk(tempdir))[0][2]:
                            if tmpfile.startswith(key):
                                os.remove(os.path.join(tempdir, tmpfile))
                    except Exception:
                        pass
                    with open(cache_path, 'w') as fh:
                        json.dump(result, fh)
                except Exception as e:
                    pass
            return result
        return wrapper
    return decorate


class BaseMapper(ABC):
    def __init__(self, settings: STIXMapperSettings):
        self.now = datetime.datetime.utcnow()
        self.settings = settings

    @abc.abstractmethod
    def map(self, source: dict) -> Bundle:
        raise NotImplementedError

    def map_confidence(self, confidence: Union[str, None]):
        # There are two confidence scales used in Titan: https://en.wikipedia.org/wiki/Admiralty_code and low/medium/high
        # This function handles both according to
        # [STIX confidence scales](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_1v6elyto0uqg)

        # If it's Admiralty_code we're interested in the second part only (Credibility), which is a number between 1 and 6.
        value = re.sub(r"^[A-F]([1-6])$", "\\1", confidence or "", re.IGNORECASE)

        # If there's no match, we expect a word from low/medium/high scale.
        # If for any reason it's not the case either, we set confidence as not specified (`None`)
        return {
            "6": 0, "5": 10, "4": 30, "3": 50, "2": 70, "1": 90,
            "low": 15, "medium": 50, "high": 85
        }.get(value, 0)

    def map_tactic(self, tactic: str):
        if tactic and len(tactic) > 0:
            return tactic.replace("_", "-").replace(" ", "-").lower()

    @staticmethod
    def shorten(text: str, limit: int) -> str:
        if len(text) > limit:
            text = text[:limit]
            while text[-1] != " ":
                text = text[:-1]
        return text.strip()

    @cached("i471titanclientgirs")
    def _get_girs_names(self) -> dict:
        girs_names = {}
        if not all([self.settings.titan_client, self.settings.api_client, self.settings.girs_names]):
            return girs_names
        api_instance = self.settings.titan_client.GIRsApi(self.settings.api_client)
        for offset in range(0, 1000, 100):
            api_response = api_instance.girs_get(count=100, offset=offset)
            if not api_response.girs:
                break
            for gir in api_response.girs:
                girs_names[gir.data.gir.path] = gir.data.gir.name
        return girs_names

    def get_girs_labels(self, gir_paths: List[str]):
        girs_names = self._get_girs_names()
        paths_and_names = {i: girs_names.get(i) for i in gir_paths}
        return [
            f'{INTEL_471} - GIR {path}{" - " + name if name else ""}'
            for path, name in paths_and_names.items()
        ]
