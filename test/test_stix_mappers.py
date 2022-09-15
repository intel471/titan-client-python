import json
import os
import unittest

from titan_client.titan_stix.mappers.common import StixMapper


here = os.path.abspath(os.path.dirname(__file__))
fixtures = (("indicators_input.json", "indicators_stix.json"),
            ("iocs_input.json", "iocs_stix.json"),
            ("yara_input.json", "yara_stix.json"),
            ("cves_input.json", "cves_stix.json")
            )


class TestStixMappers(unittest.TestCase):

    @staticmethod
    def strip_random_values(bundle: dict) -> dict:
        bundle["id"] = None
        for i, o in enumerate(bundle["objects"]):
            bundle["objects"][i]["created"] = None
            bundle["objects"][i]["modified"] = None
            if o["id"].startswith("relationship--"):
                bundle["objects"][i]["id"] = None
        return bundle

    def testMappers(self):
        for in_fixture, out_fixture in fixtures:
            with self.subTest():
                with open(os.path.join(here, "fixtures", in_fixture)) as fh:
                    api_response = json.load(fh)
                with open(os.path.join(here, "fixtures", out_fixture)) as fh:
                    expected_result = json.load(fh)
                mapper = StixMapper()
                result = mapper.map(api_response)
                expected = self.strip_random_values(expected_result)
                self.assertEqual(expected, self.strip_random_values(json.loads(result.serialize())))


if __name__ == '__main__':
    unittest.main()
