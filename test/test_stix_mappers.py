import base64
import json
import os

import pytest
from stix2 import DomainName

from titan_client.titan_stix import STIXMapperSettings
from titan_client.titan_stix.mappers import ReportMapper
from titan_client.titan_stix.mappers.common import StixMapper

from .conftest import PREFIX, read_fixture
from mock import MagicMock

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


def test_report_enrichments():
    api_cls = "ReportsApi"
    method_name = "reports_uid_get"
    api_response = {"rawText": "<h2>Foo</h2><p>New malware <strong>Foobar</strong> released!</p><h2>Bar</h2>"}

    api_response_mock = MagicMock(name="API response")
    api_response_mock.to_dict.return_value = api_response
    api_instance_mock = MagicMock(name="API instance")
    getattr(api_instance_mock, method_name).return_value = api_response_mock
    mock_titan_client = MagicMock(name="titan_client")
    getattr(mock_titan_client, api_cls).return_value = api_instance_mock
    mock_api_client = MagicMock()
    mock_domain = DomainName(value="foo.bar")

    mapper = ReportMapper(STIXMapperSettings(mock_titan_client, mock_api_client, report_attachments_opencti=True))
    result = mapper.map_shortened_report({
        "subject": "New malware released",
        "released": 1679321907000,
        "portalReportUrl": "https://foo.bar/fintel/123",
        "uid": "1fffffffffffffffffffffffffffffff",
        "admiraltyCode": "A1",
        "dateOfInformation": 1678060800000
    }, {mock_domain.id: mock_domain})
    report_serialized = json.loads(list(result.values())[0].serialize())
    assert report_serialized["name"] == "New malware released"
    assert report_serialized["description"] == "New malware Foobar released!"
    assert report_serialized["report_types"] == ["fintel"]
    assert report_serialized["confidence"] == 90
    assert report_serialized["x_opencti_files"] == [
        {
            "name": "Raw Text",
            "mime_type": "text/html",
            "data": base64.b64encode(bytes(api_response["rawText"], "utf-8")).decode("utf-8")
        }
    ]
