import json
import os

import pytest
from titan_client.titan_stix.mappers.common import StixMapper


here = os.path.abspath(os.path.dirname(__file__))
fixtures = {
    'test_indicators': ("indicators_input.json", "indicators_stix.json"),
    'test_iocs': ("iocs_input.json", "iocs_stix.json"),
    'test_yara': ("yara_input.json", "yara_stix.json"),
    'test_cves': ("cves_input.json", "cves_stix.json")
}


class TestStixMappers:
    @staticmethod
    def strip_random_values(bundle: dict) -> dict:
        bundle["id"] = None
        for i, o in enumerate(bundle["objects"]):
            bundle["objects"][i]["created"] = None
            bundle["objects"][i]["modified"] = None
            if o["id"].startswith("relationship--"):
                bundle["objects"][i]["id"] = None
        return bundle

    @pytest.mark.parametrize('fixtures', fixtures.values(), ids=fixtures.keys())
    def test_stix_mappers(self, fixtures):
        in_fixture, out_fixture  = fixtures
        with open(os.path.join(here, "fixtures", in_fixture)) as fh:
            api_response = json.load(fh)
        with open(os.path.join(here, "fixtures", out_fixture)) as fh:
            expected_result = json.load(fh)
        mapper = StixMapper()
        result = mapper.map(api_response)
        expected = self.strip_random_values(expected_result)
        assert expected == self.strip_random_values(json.loads(result.serialize()))
