import json
import os

import pytest
from stix2 import DomainName

from titan_client.titan_stix import STIXMapperSettings, StixObjects
from titan_client.titan_stix.mappers import ReportMapper
from titan_client.titan_stix.mappers.common import StixMapper
from titan_client.titan_stix.mappers.entities import EntitiesMapper
from titan_client.titan_stix.mappers.indicators import IndicatorsMapper
from titan_client.titan_stix.mappers.reports import ReportType

from .conftest import PREFIX, read_fixture
from mock import MagicMock

os.environ['I471_TITAN_CLIENT_CACHE_TTL'] = '0'

fixtures = {
    'test_indicators': ("indicators_input.json", "indicators_stix.json"),
    'test_iocs': ("iocs_input.json", "iocs_stix.json"),
    'test_yara': ("yara_input.json", "yara_stix.json"),
    'test_cves': ("cves_input.json", "cves_stix.json"),
    'test_cvesx': ("iocs_with_reports_input.json", "reports_from_iocs_stix.json"),
    'test_report_breach_alert': ("report_breach_alert_input.json", "report_breach_alert_stix.json"),
    'test_report_fintel': ("report_fintel_input.json", "report_fintel_stix.json"),
    'test_report_fintel_actor_profile': ("report_fintel_actor_profile_input.json", "report_fintel_actor_profile_stix.json"),
    'test_report_inforep': ("report_inforep_input.json", "report_inforep_stix.json"),
    'test_report_spot': ("report_spot_input.json", "report_spot_stix.json"),
    'test_report_malware': ("report_malware_input.json", "report_malware_stix.json"),
}


def strip_random_values(bundle: dict) -> dict:
    bundle["id"] = None
    remove_id_types = ('relationship', 'threat-actor', 'identity')
    for i1, o in enumerate(bundle["objects"]):
        bundle["objects"][i1]["created"] = None
        bundle["objects"][i1]["modified"] = None
        if o["type"] in remove_id_types:
            bundle["objects"][i1]["id"] = None
        for i2, object_ref_id in enumerate(o.get("object_refs", [])):
            if object_ref_id.split("--")[0] in remove_id_types:
                bundle["objects"][i1]["object_refs"][i2] = None

    return bundle


@pytest.mark.parametrize('fixtures', fixtures.values(), ids=fixtures.keys())
def test_stix_mappers(fixtures):
    in_fixture, out_fixture = fixtures
    api_response = read_fixture(f'{PREFIX}/fixtures/{in_fixture}')
    expected_result = read_fixture(f'{PREFIX}/fixtures/{out_fixture}')

    gir_mock = MagicMock(name="Gir mock")
    gir_mock.data.gir.path, gir_mock.data.gir.name = "1.1.1", "Lorem"
    api_response_mock = MagicMock(name="API response")
    api_response_mock.girs = [gir_mock]
    api_instance_mock = MagicMock(name="API instance")
    api_instance_mock.girs_get.return_value = api_response_mock
    mock_titan_client = MagicMock(name="titan_client")
    mock_titan_client.GIRsApi.return_value = api_instance_mock
    mock_api_client = MagicMock()

    mapper = StixMapper(STIXMapperSettings(
        titan_client=mock_titan_client, api_client=mock_api_client, report_full_content=False
    ))
    result = mapper.map(api_response)
    expected = strip_random_values(expected_result)
    assert expected == strip_random_values(json.loads(result.serialize()))


def test_report_from_ioc():
    mock_domain = DomainName(value="foo.bar")
    mapper = ReportMapper(STIXMapperSettings())
    result = mapper.map_report_ioc({
        "subject": "New malware released",
        "released": 1679321907000,
        "portalReportUrl": "https://foo.bar/fintel/123",
        "uid": "1fffffffffffffffffffffffffffffff",
        "admiraltyCode": "A1",
        "dateOfInformation": 1678060800000
    }, StixObjects([mock_domain]))
    report_serialized = json.loads(list(result.get())[-1].serialize())
    assert report_serialized["name"] == "New malware released"
    assert report_serialized["description"] == "New malware released"
    assert report_serialized["report_types"] == ["fintel"]
    assert report_serialized["confidence"] == 90
    assert getattr(report_serialized, "content", None) is None
    assert getattr(report_serialized, "labels", None) is None


def test_full_report_from_ioc():
    api_cls = "ReportsApi"
    method_name = "reports_uid_get"
    api_response = {
        "uid": "1fffffffffffffffffffffffffffffff",
        "documentFamily": "FINTEL",
        "documentType": "MALWARE_CAMPAIGN",
        "subject": "New malware released (fromAPI)",
        "admiraltyCode": "A1",
        "created": 1679321907000,
        "dateOfInformation": 1678060800000,
        "rawText": "<h2>Foo</h2><p>New malware <strong>Foobar</strong> released!</p><h2>Bar</h2>",
        "classification": {"intelRequirements": ["1.1"]}
        }

    api_response_mock = MagicMock(name="API response")
    api_response_mock.to_dict.return_value = api_response
    api_instance_mock = MagicMock(name="API instance")
    getattr(api_instance_mock, method_name).return_value = api_response_mock
    mock_titan_client = MagicMock(name="titan_client")
    getattr(mock_titan_client, api_cls).return_value = api_instance_mock
    mock_api_client = MagicMock()
    mock_domain = DomainName(value="foo.bar")

    mapper = ReportMapper(STIXMapperSettings(mock_titan_client, mock_api_client, report_full_content=True))
    result = mapper.map_report_ioc({
        "subject": "New malware released",
        "released": 1679321907000,
        "portalReportUrl": "https://foo.bar/fintel/123",
        "uid": "1fffffffffffffffffffffffffffffff",
        "admiraltyCode": "A1",
        "dateOfInformation": 1678060800000
    }, StixObjects([mock_domain]))
    report_serialized = json.loads(list(result.get())[-1].serialize())
    assert report_serialized["name"] == "New malware released (fromAPI)"
    assert report_serialized["description"] == "New malware Foobar released!"
    assert report_serialized["report_types"] == ["fintel", "malware_campaign"]
    assert report_serialized["confidence"] == 90
    assert report_serialized["content"] == api_response['rawText']
    assert report_serialized["labels"] == ["Intel 471 - GIR 1.1"]


def test_full_report_from_reports_api():
    api_cls = "ReportsApi"
    method_name = "reports_uid_get"
    api_response = {
        "uid": "1fffffffffffffffffffffffffffffff",
        "documentFamily": "INFOREP",
        "documentType": "INFOREP",
        "subject": "New malware released (fromAPI)",
        "admiraltyCode": "A1",
        "created": 1679321907000,
        "dateOfInformation": 1678060800000,
        "classification": {"intelRequirements": ["1.1"]},
        "entities": [{"type": "ActorDomain", "value": "foo.bar"}],
        "executiveSummary": "This report examines the cybercriminal underground",
        "rawText": "<h2>Foo</h2><p>New malware <strong>Foobar</strong> released!</p><h2>Bar</h2>",
        "researcherComments": "<h3>Actor and information assessment</h3><p>The actor joined the XYZ forum"
                              "<figure class=\"image image_resized width52\"><img src=\"data:image/png;base64,iVBORw0KGgoAAAANSU</figure></p>",
        }

    api_response_mock = MagicMock(name="API response")
    api_response_mock.to_dict.return_value = api_response
    api_instance_mock = MagicMock(name="API instance")
    getattr(api_instance_mock, method_name).return_value = api_response_mock
    mock_titan_client = MagicMock(name="titan_client")
    getattr(mock_titan_client, api_cls).return_value = api_instance_mock
    mock_api_client = MagicMock()

    mapper = ReportMapper(STIXMapperSettings(mock_titan_client, mock_api_client, report_full_content=True))
    bundle = mapper.map({"reportTotalCount": "1", "reports": [{
        "documentFamily": "FINTEL",
        "subject": "New malware released",
        "released": 1679321907000,
        "uid": "1fffffffffffffffffffffffffffffff",
        "admiraltyCode": "A1",
        "dateOfInformation": 1678060800000
    }]})
    report = bundle.objects[-1]
    assert report.name == "New malware released (fromAPI)"
    assert report.description == "This report examines the cybercriminal underground"
    assert report.report_types == ["inforep"]
    assert report.confidence == 90
    assert report.labels == ["Intel 471 - GIR 1.1"]
    assert report.content == ('<h1>Executive Summary</h1>\n'
                              'This report examines the cybercriminal underground\n'
                              '<h1>Researcher Comments</h1>\n'
                              '<h3>Actor and information assessment</h3>'
                              '<p>The actor joined the XYZ forum<figure class="image image_resized width52">'
                              '<img src="data:image/png;base64,iVBORw0KGgoAAAANSU</figure></p>\n'
                              '<h1>Raw Text</h1>\n'
                              '<h2>Foo</h2>'
                              '<p>New malware <strong>Foobar</strong> released!</p><h2>Bar</h2>')


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
        ({"type": "Handle", "value": "acme"}, {"type": "threat-actor", "name": "acme"}),
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
        ({"type": "CveID", "value": "CVE-2024-23113"}, {"type": "vulnerability", "name": "CVE-2024-23113"}),
        # Invalid stuff
        ({"type": "Handle", "value": "a"}, None),
        ({"type": "MD5", "value": "invalidMd5"}, None)
))
def test_observable_mapper(source, expected_values):
    mapper = EntitiesMapper()
    sco = mapper.map(**source)
    if expected_values is None:
        assert sco is expected_values
    else:
        for key, value in expected_values.items():
            assert getattr(sco, key) == value


@pytest.mark.parametrize("report_type,source,expected_values", (
    (ReportType.FINTEL.value, {"uid": "ab1", "documentFamily": "FINTEL", "sources": [
        {"type": "External Link", "title": "ACME corp news", "url": "https://acme.corp/123", "index": "1"}]},
     {"source_name": "External Link - ACME corp news", "url": "https://acme.corp/123"}),
    (ReportType.FINTEL.value, {"uid": "ab1", "documentFamily": "FINTEL", "sources": [
        {"type": "External Link", "title": "Titan Information Report", "url": "https://titan.intel471.com/report/inforep/487a8", "index": "1"}]},
     {}),
    (ReportType.INFOREP.value, {"uid": "ab1", "documentFamily": "INFOREP", "sources": [
        {"type": "Forum Post", "title": "[SOURCE CODE] HexSec | Android RAT",
         "url": "https://titan.intel471.com/post_thread/9cacd56", "index": "1"}]},
     {"source_name": "Forum Post - [SOURCE CODE] HexSec | Android RAT", "url": "https://titan.intel471.com/post_thread/9cacd56"}),
    (ReportType.INFOREP.value, {"uid": "ab1", "documentFamily": "INFOREP", "sources": [
        {"type": "Forum Post", "title": "[SOURCE CODE] HexSec | Android RAT",
         "url": "https://titan.intel471.com/post_thread/9cacd56", "index": "1"}]},
     {"source_name": "Forum Post - [SOURCE CODE] HexSec | Android RAT",
      "url": "https://titan.intel471.com/post_thread/9cacd56"}),
    (ReportType.BREACH_ALERT.value, {"uid": "ab1", "data": {"breach_alert": {"sources": [
        {"type": "internal", "source_type": "Forum Thread", "title": "acmesystems",
         "url": "https://titan.intel471.com/post_thread/2984", "index": "1"}]}}},
     {"source_name": "Forum Thread internal - acmesystems",
      "url": "https://titan.intel471.com/post_thread/2984"}),
    (ReportType.SPOTREP.value, {"uid": "ab1", "data": {"spot_report": {"spot_report_data": {"links": [
        {"type": "internal", "title": "Forum thread",
         "url": "https://titan.intel471.com/post_thread/2984"}]}}}},
     {"source_name": "internal - Forum thread",
      "url": "https://titan.intel471.com/post_thread/2984"}),
))
def test_map_reports_external_references(report_type, source, expected_values):
    mapper = ReportMapper(STIXMapperSettings())
    external_refs = mapper._get_external_references(source)
    external_ref_0 = json.loads(external_refs[0].serialize())
    assert external_ref_0 == {"source_name": "Titan URL", "url": f"https://titan.intel471.com/report/{report_type}/ab1"}
    if expected_values:
        external_ref_1 = json.loads(external_refs[1].serialize())
        assert external_ref_1 == expected_values


@pytest.mark.parametrize("report_type,source", (
    (ReportType.FINTEL.value, {"uid": "ab1", "documentFamily": "FINTEL", "entities": [{"type": "MalwareFamily", "value": "acme"}, {"type": "IPAddress", "value": "0.0.0.1"}]}),
    (ReportType.FINTEL.value, {"uid": "ab1", "documentFamily": "INFOREP", "entities": [{"type": "MalwareFamily", "value": "acme"}]}),
    (ReportType.BREACH_ALERT.value, {"uid": "ab1", "data": {"breach_alert": {}, "entities": [{"type": "MalwareFamily", "value": "acme"}]}}),
    (ReportType.SPOTREP.value, {"uid": "ab1", "data": {"spot_report": {}, "entities": [{"type": "MalwareFamily", "value": "acme"}]}}),
    (ReportType.MALWARE.value, {"uid": "ab1", "data": {"malware_report_data": {}, "threat": {"data": {"family": "acme"}}}}),
))
def test_map_reports_entities(report_type, source):
    mapper = ReportMapper(STIXMapperSettings())
    entities = mapper._get_entities(source)
    entity = json.loads(list(entities.get())[0].serialize())
    assert entity["type"] == "malware"
    assert entity["name"] == "acme"
    malware_families_names = mapper._get_malware_families_names(entities)
    assert malware_families_names == ["acme"]


@pytest.mark.parametrize("report_type,source", (
    (ReportType.FINTEL.value, {"uid": "ab1", "documentFamily": "FINTEL", "victims": [
        {"name": "ACME corp", "urls": ["https://acme.corp"]}]}),
    (ReportType.INFOREP.value, {"uid": "ab1", "documentFamily": "INFOREP", "victims": [
        {"name": "ACME corp", "urls": ["https://acme.corp"]}]}),
    (ReportType.BREACH_ALERT.value, {"uid": "ab1", "data": {"breach_alert": {"victim": {
            "country": "United States",
            "industries": [
                {
                    "industry": "Financial and investment consulting industry",
                    "sector": "Professional services and consulting sector"
                }
            ],
            "name": "ACME corp",
            "region": "North America",
            "revenue": "US $100 million",
            "urls": [
                "https://acme.corp"
            ]
        }}}}),
    (ReportType.SPOTREP.value, {"uid": "ab1", "data": {"spot_report": {"spot_report_data": {"victims": [
        {"name": "ACME corp", "urls": ["https://acme.corp"]}]}}}}),
))
def test_map_reports_victims(report_type, source):
    mapper = ReportMapper(STIXMapperSettings())
    victims = list(mapper._get_victims(source).get())
    assert victims[0].type == "identity"
    assert victims[0].identity_class == "organization"
    assert victims[0].name == "ACME corp"
    assert victims[0].contact_information == "https://acme.corp"


@pytest.mark.parametrize("report_type,source", (
        (ReportType.FINTEL, {"uid": "123", "documentFamily": "FINTEL", "classification": {"intelRequirements": ["1.1.1", "1.2.2"]}}),
        (ReportType.INFOREP, {"uid": "123", "documentFamily": "INFOREP", "classification": {"intelRequirements": ["1.1.1", "1.2.2"]}}),
        (ReportType.SPOTREP, {"uid": "123", "data": {"spot_report": {"spot_report_data":{"intel_requirements": ["1.1.1", "1.2.2"]}}}}),
        (ReportType.MALWARE, {"uid": "123", "data": {"malware_report_data": {}}, "classification": {"intelRequirements": ["1.1.1", "1.2.2"]}}),
        (ReportType.BREACH_ALERT, {"uid": "123", "data": {"breach_alert":{"intel_requirements": ["1.1.1", "1.2.2"]}}}),
))
def test_reports_gir_labels(report_type, source):
    mapper = ReportMapper(STIXMapperSettings())
    girs_labels = mapper._get_girs_labels(source)
    assert girs_labels == ["Intel 471 - GIR 1.1.1", "Intel 471 - GIR 1.2.2"]


def test_indicator_pattern_url_quote():
    mapper = IndicatorsMapper(STIXMapperSettings())
    result = mapper.map({"indicatorTotalCount": "1", "indicators": [{
        "activity": {"first": 1747231416000, "last": 1747317804000},
        "data": {
            "indicator_data": {
                "url": "https://foo.bar.com/pixel.png'ogi,TO"
            },
            "indicator_type": "url",
            "threat": {"data": {"family": "foo"}},
            "expiration": 1747317804000,
            "mitre_tactics": "command_and_control",
            "confidence": "high",
            "context": {"description": "foo"},
            "intel_requirements": ["1.3.11.1"]
        }
    }]})
    assert result.objects[1].pattern == \
        "[url:value = 'https://foo.bar.com/pixel.png%27ogi,TO']"
