import json
import os

import pytest

from titan_client.titan_stix.mappers.common import StixMapper

from .conftest import PREFIX, read_fixture

os.environ['I471_TITAN_CLIENT_CACHE_TTL'] = '0'

fixtures = {
    'test_indicators': ("indicators_input.json", "indicators_stix.json"),
    'test_iocs': ("iocs_input.json", "iocs_stix.json"),
    'test_yara': ("yara_input.json", "yara_stix.json"),
    'test_cves': ("cves_input.json", "cves_stix.json")
}


def strip_random_values(bundle: dict) -> dict:
    bundle["id"] = None
    for i, o in enumerate(bundle["objects"]):
        bundle["objects"][i]["created"] = None
        bundle["objects"][i]["modified"] = None
        if o["id"].startswith("relationship--"):
            bundle["objects"][i]["id"] = None
    return bundle


@pytest.mark.parametrize('fixtures', fixtures.values(), ids=fixtures.keys())
def test_stix_mappers(fixtures):
    in_fixture, out_fixture = fixtures
    api_response = read_fixture(f'{PREFIX}/fixtures/{in_fixture}')
    expected_result = read_fixture(f'{PREFIX}/fixtures/{out_fixture}')
    mapper = StixMapper()
    result = mapper.map(api_response)
    expected = strip_random_values(expected_result)
    assert expected == strip_random_values(json.loads(result.serialize()))
