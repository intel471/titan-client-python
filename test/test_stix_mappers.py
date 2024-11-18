import base64
import json
import os

import pytest
from stix2 import DomainName

from titan_client.titan_stix import STIXMapperSettings, StixObjects
from titan_client.titan_stix.mappers import ReportMapper
from titan_client.titan_stix.mappers.common import StixMapper
from titan_client.titan_stix.mappers.observables import ObservableMapper

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
    }, StixObjects([mock_domain]))
    report_serialized = json.loads(result[1].serialize())
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

@pytest.mark.parametrize("source,expected_values", (
        # /iocs endpoint
        ({"type": "MaliciousURL", "value": "https://acme.com"}, {"type": "url", "value": "https://acme.com"}),
        ({"type": "URL", "value": "https://acme.com"}, {"type": "url", "value": "https://acme.com"}),
        ({"type": "MaliciousDomain", "value": "acme.com"}, {"type": "domain-name", "value": "acme.com"}),
        ({"type": "IPAddress", "value": "10.0.0.1"}, {"type": "ipv4-addr", "value": "10.0.0.1"}),
        ({"type": "IPv4Prefix", "value": "10.0.0.1/24"}, {"type": "ipv4-addr", "value": "10.0.0.1/24"}),
        ({"type": "IPv6Prefix", "value": "2a09:7c44::/32"}, {"type": "ipv6-addr", "value": "2a09:7c44::/32"}),
        ({"type": "AutonomousSystem", "value": "AS123456"}, {"type": "autonomous-system", "number": 123456}),
        ({"type": "MD5", "value": "acb9cf2560602aa023e9933b959974d1"}, {"type": "file", "hashes": {"MD5": "acb9cf2560602aa023e9933b959974d1"}}),
        ({"type": "SHA1", "value": "ae9de44e5f23758ffb6f4fa28065c6122c2e4467"}, {"type": "file", "hashes": {"SHA-1": "ae9de44e5f23758ffb6f4fa28065c6122c2e4467"}}),
        ({"type": "SHA256", "value": "890a0bfab48d0b93da8f7617b2e65621e8d7f8c93a854fa8596232d9bcb1b39e"}, {"type": "file", "hashes": {"SHA-256": "890a0bfab48d0b93da8f7617b2e65621e8d7f8c93a854fa8596232d9bcb1b39e"}}),
        ({"type": "FileName", "value": "acmecorp.exe"}, {"type": "file", "name": "acmecorp.exe"}),
        # /entities endpoint
        ({"type": "ActorDomain", "value": "acme.com"}, {"type": "domain-name", "value": "acme.com"}),
        ({"type": "ActorOtherWebsite", "value": "https://acme.com"}, {"type": "url", "value": "https://acme.com"}),
        ({"type": "BitcoinAddress", "value": "1HUu6K9sFvN1cGV"}, {"type": "cryptocurrency-wallet", "value": "1HUu6K9sFvN1cGV"}),
        ({"type": "OtherCryptoCurrencies", "value": "1HUu6K9sFvN1cGV"}, {"type": "cryptocurrency-wallet", "value": "1HUu6K9sFvN1cGV"}),
        ({"type": "EmailAddress", "value": "changeme@acme.com"}, {"type": "email-addr", "value": "changeme@acme.com"}),
        ({"type": "AIM", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "AIM"}),
        ({"type": "Discord", "value": "https://discord.gg/2xx2xx2"}, {"type": "user-account", "user_id": "2xx2xx2", "account_type": "Discord"}),
        ({"type": "Facebook", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "Facebook"}),
        ({"type": "GitHub", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "GitHub"}),
        ({"type": "ICQ", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "ICQ"}),
        ({"type": "Instagram", "value": "instagram.com/changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "Instagram"}),
        ({"type": "Jabber", "value": "changeme@jabber.de"}, {"type": "user-account", "user_id": "changeme@jabber.de", "account_type": "Jabber"}),
        ({"type": "LinkedIn", "value": "https://www.linkedin.com/in/iamweasel-58312b1a6/"}, {"type": "user-account", "user_id": "iamweasel-58312b1a6", "account_type": "LinkedIn"}),
        ({"type": "MSN", "value": "changeme@acme.com"}, {"type": "user-account", "user_id": "changeme@acme.com", "account_type": "MSN"}),
        ({"type": "MoiMir", "value": "my.mail.ru/mail/changeme/"}, {"type": "user-account", "user_id": "changeme", "account_type": "MoiMir"}),
        ({"type": "Odnoklassniki", "value": "ok.ru/profile/11111800259"}, {"type": "user-account", "user_id": "11111800259", "account_type": "Odnoklassniki"}),
        ({"type": "QQ", "value": "111159547"}, {"type": "user-account", "user_id": "111159547", "account_type": "QQ"}),
        ({"type": "Skype", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "Skype"}),
        ({"type": "Telegram", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "Telegram"}),
        ({"type": "TOX", "value": "2B41B398739E6BECE4E93EAFA0C665"}, {"type": "user-account", "user_id": "2B41B398739E6BECE4E93EAFA0C665", "account_type": "TOX"}),
        ({"type": "Twitter", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "Twitter"}),
        ({"type": "VK", "value": "vk.com/changeme_2"}, {"type": "user-account", "user_id": "changeme_2", "account_type": "VK"}),
        ({"type": "WeChat", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "WeChat"}),
        ({"type": "Wickr", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "Wickr"}),
        ({"type": "YahooIM", "value": "changeme@yahoo.com"}, {"type": "user-account", "user_id": "changeme@yahoo.com", "account_type": "YahooIM"}),
        ({"type": "PerfectMoneyID", "value": "U1111111"}, {"type": "user-account", "user_id": "U1111111", "account_type": "PerfectMoneyID"}),
        ({"type": "QiwiWallet", "value": "11110519386"}, {"type": "user-account", "user_id": "11110519386", "account_type": "QiwiWallet"}),
        ({"type": "WebMoneyID", "value": "111112935229"}, {"type": "user-account", "user_id": "111112935229", "account_type": "WebMoneyID"}),
        ({"type": "WebMoneyPurse", "value": "Z111144083730"}, {"type": "user-account", "user_id": "Z111144083730", "account_type": "WebMoneyPurse"}),
        ({"type": "YandexMoney", "value": "111113131482342"}, {"type": "user-account", "user_id": "111113131482342", "account_type": "YandexMoney"}),
        ({"type": "Phone", "value": "79874172111"}, {"type": "user-account", "user_id": "79874172111", "account_type": "Phone"}),

))
def test_observable_mapper(source, expected_values):
    mapper = ObservableMapper()
    sco = mapper.map(**source)
    for key, value in expected_values.items():
        assert getattr(sco, key) == value
