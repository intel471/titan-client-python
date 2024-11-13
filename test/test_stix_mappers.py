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
    for i1, o in enumerate(bundle["objects"]):
        bundle["objects"][i1]["created"] = None
        bundle["objects"][i1]["modified"] = None
        if o["id"].startswith("relationship--"):
            bundle["objects"][i1]["id"] = None
        for i2, object_ref_id in enumerate(o.get("object_refs", [])):
            if object_ref_id.startswith("relationship--"):
                bundle["objects"][i1]["object_refs"][i2] = None

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
    api_response = {
        "uid": "1fffffffffffffffffffffffffffffff",
        "documentFamily": "FINTEL",
        "subject": "New malware released (fromAPI)",
        "admiraltyCode": "A1",
        "created": 1679321907000,
        "dateOfInformation": 1678060800000,
        "rawText": "<h2>Foo</h2><p>New malware <strong>Foobar</strong> released!</p><h2>Bar</h2>"
        }

    api_response_mock = MagicMock(name="API response")
    api_response_mock.to_dict.return_value = api_response
    api_instance_mock = MagicMock(name="API instance")
    getattr(api_instance_mock, method_name).return_value = api_response_mock
    mock_titan_client = MagicMock(name="titan_client")
    getattr(mock_titan_client, api_cls).return_value = api_instance_mock
    mock_api_client = MagicMock()
    mock_domain = DomainName(value="foo.bar")

    mapper = ReportMapper(STIXMapperSettings(mock_titan_client, mock_api_client, report_attachments_opencti=True))
    result = mapper.map_report_ioc({
        "subject": "New malware released",
        "released": 1679321907000,
        "portalReportUrl": "https://foo.bar/fintel/123",
        "uid": "1fffffffffffffffffffffffffffffff",
        "admiraltyCode": "A1",
        "dateOfInformation": 1678060800000
    }, {mock_domain.id: mock_domain})
    report_serialized = json.loads(result.serialize())
    assert report_serialized["name"] == "New malware released (fromAPI)"
    assert report_serialized["description"] == "New malware Foobar released!"
    assert report_serialized["report_types"] == ["fintel"]
    assert report_serialized["confidence"] == 90
    assert report_serialized["x_opencti_files"] == [
        {
            "name": "Raw Text.html",
            "mime_type": "text/html",
            "data": base64.b64encode(bytes(api_response["rawText"], "utf-8")).decode("utf-8")
        }
    ]

def test_ioc_mapper_attached_reports(capsys):
    ioc_fixture = read_fixture(f'{PREFIX}/fixtures/iocs_with_reports_input.json')
    expected_result = read_fixture(f'{PREFIX}/fixtures/reports_from_iocs_stix.json')
    mapper = StixMapper()
    result = mapper.map(ioc_fixture)
    with capsys.disabled():
        result_serialized = json.loads(result.serialize())
        result_serialized["objects"] = [i for i in result_serialized["objects"] if i["type"] == "report"]
        expected = strip_random_values(expected_result)
        assert expected == strip_random_values(result_serialized)


@pytest.mark.skip(reason="work in progress")
def test_breach_alert_mapper(capsys):
    breach_alert_fixture = read_fixture(f'{PREFIX}/fixtures/breach_alert_af3e62.json')
    mapper = StixMapper()
    result = mapper.map(breach_alert_fixture)
    x = result.serialize()
    with capsys.disabled():
        result_serialized = json.loads(result.serialize())
        result_serialized = [i for i in result_serialized["objects"] if i["type"] == "report"]
        print(json.dumps(result_serialized, indent=2, sort_keys=True))

