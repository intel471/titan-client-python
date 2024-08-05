import json
import re
from unittest.mock import MagicMock, patch

import pytest
import titan_client

from .conftest import PREFIX, read_fixture


configuration = titan_client.Configuration()

test_params = {
    'ActorsApi:actors_get': ('ActorsApi', 'actors_get', {'actor': 'synthx', 'count': 1}, 'SimpleActorsResponse', 'https://api.intel471.com/v1/actors?actor=synthx&count=1'),
    'ActorsApi:actors_uid_get': ('ActorsApi', 'actors_uid_get', {'uid': '636452233dec0f291302cbafc630c130'}, 'SimpleActorSchema', 'https://api.intel471.com/v1/actors/636452233dec0f291302cbafc630c130'),
    'AlertsApi:alerts_get': ('AlertsApi', 'alerts_get', {'count': 1}, 'AlertListSchemaResponse', 'https://api.intel471.com/v1/alerts?count=1'),
    'CredentialsApi:credential_sets_accessed_urls_get': ('CredentialsApi', 'credential_sets_accessed_urls_get', {'text': 'hubspot', 'count': 1}, 'CredentialSetsAccessedUrlsResponse', 'https://api.intel471.com/v1/credentialSets/accessedUrls?text=hubspot&count=1'),
    'CredentialsApi:credential_sets_accessed_urls_stream_get': ('CredentialsApi', 'credential_sets_accessed_urls_stream_get', {'text': 'hubspot', 'count': 1}, 'CredentialSetsAccessedUrlsStreamResponse', 'https://api.intel471.com/v1/credentialSets/accessedUrls/stream?text=hubspot&count=1'),
    'CredentialsApi:credential_sets_get': ('CredentialsApi', 'credential_sets_get', {'text': 'leak', 'count': 1}, 'CredentialSetsResponse', 'https://api.intel471.com/v1/credentialSets?text=leak&count=1'),
    'CredentialsApi:credential_sets_stream_get': ('CredentialsApi', 'credential_sets_stream_get', {'text': 'leak', 'count': 1}, 'CredentialSetsStreamResponse', 'https://api.intel471.com/v1/credentialSets/stream?text=leak&count=1'),
    'CredentialsApi:credentials_accessed_urls_get': ('CredentialsApi', 'credentials_accessed_urls_get', {'text': 'hubspot', 'count': 1}, 'CredentialAccessedUrlsResponse', 'https://api.intel471.com/v1/credentials/accessedUrls?text=hubspot&count=1'),
    'CredentialsApi:credentials_accessed_urls_stream_get': ('CredentialsApi', 'credentials_accessed_urls_stream_get', {'text': 'hubspot', 'count': 1}, 'CredentialAccessedUrlsStreamResponse', 'https://api.intel471.com/v1/credentials/accessedUrls/stream?text=hubspot&count=1'),
    'CredentialsApi:credentials_get': ('CredentialsApi', 'credentials_get', {'text': 'leak', 'count': 1}, 'CredentialsResponse', 'https://api.intel471.com/v1/credentials?text=leak&count=1'),
    'CredentialsApi:credentials_occurrences_get': ('CredentialsApi', 'credentials_occurrences_get', {'text': 'leak', 'count': 1}, 'CredentialOccurrencesResponse', 'https://api.intel471.com/v1/credentials/occurrences?text=leak&count=1'),
    'CredentialsApi:credentials_occurrences_stream_get': ('CredentialsApi', 'credentials_occurrences_stream_get', {'text': 'leak', 'count': 1}, 'CredentialOccurrencesStreamResponse', 'https://api.intel471.com/v1/credentials/occurrences/stream?text=leak&count=1'),
    'CredentialsApi:credentials_stream_get': ('CredentialsApi', 'credentials_stream_get', {'text': 'leak', 'count': 1}, 'CredentialsStreamResponse', 'https://api.intel471.com/v1/credentials/stream?text=leak&count=1'),
    'EntitiesApi:entities_get': ('EntitiesApi', 'entities_get', {'entity': 'syntax', 'count': 1}, 'EntitiesResponse', 'https://api.intel471.com/v1/entities?entity=syntax&count=1'),
    'EventsApi:events_get': ('EventsApi', 'events_get', {'count': 1}, 'EventsResponse', 'https://api.intel471.com/v1/events?count=1'),
    'EventsApi:events_stream_get': ('EventsApi', 'events_stream_get', {'count': 1}, 'EventStreamResponse', 'https://api.intel471.com/v1/events/stream?count=1'),
    'ForumsApi:posts_get': ('ForumsApi', 'posts_get', {'forum': 'opensc.ws', 'count': 1}, 'PostsResponse', 'https://api.intel471.com/v1/posts?forum=opensc.ws&count=1'),
    'ForumsApi:private_messages_get': ('ForumsApi', 'private_messages_get', {'forum': 'opensc.ws', 'count': 1}, 'PrivateMessagesResponse', 'https://api.intel471.com/v1/privateMessages?forum=opensc.ws&count=1'),
    'GIRsApi:girs_get': ('GIRsApi', 'girs_get', {'count': 1}, 'GirsResponse', 'https://api.intel471.com/v1/girs?count=1'),
    'GlobalSearchApi:search_get': ('GlobalSearchApi', 'search_get', {'text': 'joker', 'count': 1}, 'SearchSchema', 'https://api.intel471.com/v1/search?text=joker&count=1'),
    'IOCsApi:iocs_get': ('IOCsApi', 'iocs_get', {'ioc': '.com', 'count': 1}, 'IocsResponse', 'https://api.intel471.com/v1/iocs?ioc=.com&count=1'),
    'IndicatorsApi:indicators_get': ('IndicatorsApi', 'indicators_get', {'count': 1}, 'IndicatorSearchResponse', 'https://api.intel471.com/v1/indicators?count=1'),
    'IndicatorsApi:indicators_stream_get': ('IndicatorsApi', 'indicators_stream_get', {'count': 1}, 'IndicatorStreamResponse', 'https://api.intel471.com/v1/indicators/stream?count=1'),
    'MalwareFamiliesApi:malware_families_get': ('MalwareFamiliesApi', 'malware_families_get', {'count': 1}, 'MalwareFamilySearchResponse', 'https://api.intel471.com/v1/malwareFamilies?count=1'),
    'MarketplacesApi:marketplaces_get': ('MarketplacesApi', 'marketplaces_get', {'text': 'market', 'count': 1}, 'MarketplaceSearchResponse', 'https://api.intel471.com/v1/marketplaces?text=market&count=1'),
    'MarketplacesApi:marketplaces_products_get': ('MarketplacesApi', 'marketplaces_products_get', {'text': 'visa', 'count': 1}, 'MarketplaceProductSearchResponse', 'https://api.intel471.com/v1/marketplaces/products?text=visa&count=1'),
    'MarketplacesApi:marketplaces_products_stream_get': ('MarketplacesApi', 'marketplaces_products_stream_get', {'text': 'visa', 'count': 1}, 'MarketplaceProductStreamResponse', 'https://api.intel471.com/v1/marketplaces/products/stream?text=visa&count=1'),
    'MarketplacesApi:marketplaces_resources_get': ('MarketplacesApi', 'marketplaces_resources_get', {'text': 'visa', 'count': 1}, 'MarketplaceResourceSearchResponse', 'https://api.intel471.com/v1/marketplaces/resources?text=visa&count=1'),
    'MarketplacesApi:marketplaces_resources_stream_get': ('MarketplacesApi', 'marketplaces_resources_stream_get', {'text': 'visa', 'count': 1}, 'MarketplaceResourceStreamResponse', 'https://api.intel471.com/v1/marketplaces/resources/stream?text=visa&count=1'),
    'MarketplacesApi:marketplaces_vendors_get': ('MarketplacesApi', 'marketplaces_vendors_get', {'text': 'hydra', 'count': 1}, 'MarketplaceVendorSearchResponse', 'https://api.intel471.com/v1/marketplaces/vendors?text=hydra&count=1'),
    'MarketplacesApi:marketplaces_vendors_stream_get': ('MarketplacesApi', 'marketplaces_vendors_stream_get', {'text': 'hydra', 'count': 1}, 'MarketplaceVendorStreamResponse', 'https://api.intel471.com/v1/marketplaces/vendors/stream?text=hydra&count=1'),
    'MessagingServicesApi:messaging_services_instant_messages_get': ('MessagingServicesApi', 'messaging_services_instant_messages_get', {'instant_message_service': 'telegram', 'count': 1}, 'MessagingServicesResponse', 'https://api.intel471.com/v1/messagingServices/instantMessages?instantMessageService=telegram&count=1'),
    'NewsApi:news_get': ('NewsApi', 'news_get', {'count': 1}, 'SimpleNewsResponse', 'https://api.intel471.com/v1/news?count=1'),
    'NewsApi:news_uid_get': ('NewsApi', 'news_uid_get', {'uid': '1c6c177fb29b4e896b4753a4d7c010b2'}, 'FullNewsSchema', 'https://api.intel471.com/v1/news/1c6c177fb29b4e896b4753a4d7c010b2'),
    'ReportsApi:breach_alerts_get': ('ReportsApi', 'breach_alerts_get', {'breach_alert': 'lock', 'count': 1}, 'SimpleBreachAlertResponse', 'https://api.intel471.com/v1/breachAlerts?breachAlert=lock&count=1'),
    'ReportsApi:breach_alerts_uid_get': ('ReportsApi', 'breach_alerts_uid_get', {'uid': 'b43a4f4171a94aee7822dc4bd34b60b3'}, 'SimpleBreachAlertSchema', 'https://api.intel471.com/v1/breachAlerts/b43a4f4171a94aee7822dc4bd34b60b3'),
    'ReportsApi:malware_reports_get': ('ReportsApi', 'malware_reports_get', {'threat_type': 'malware', 'count': 1}, 'MalwareReportsSearchResponse', 'https://api.intel471.com/v1/malwareReports?threatType=malware&count=1'),
    'ReportsApi:malware_reports_uid_get': ('ReportsApi', 'malware_reports_uid_get', {'uid': '05b23856b7d609aee914b870ea579cd8'}, 'MalwareReportsSearchSchema', 'https://api.intel471.com/v1/malwareReports/05b23856b7d609aee914b870ea579cd8'),
    'ReportsApi:reports_get': ('ReportsApi', 'reports_get', {'count': 1}, 'SimpleReportsResponse', 'https://api.intel471.com/v1/reports?count=1'),
    'ReportsApi:reports_uid_get': ('ReportsApi', 'reports_uid_get', {'uid': '36d9c4bec9420d643be1ebff3a6942bf0a6fce9ac1b0cd1376fbf76b00f0ba09'}, 'FullReportSchema', 'https://api.intel471.com/v1/reports/36d9c4bec9420d643be1ebff3a6942bf0a6fce9ac1b0cd1376fbf76b00f0ba09'),
    'ReportsApi:spot_reports_get': ('ReportsApi', 'spot_reports_get', {'spot_report': 'card', 'count': 1}, 'SimpleSpotReportsResponse', 'https://api.intel471.com/v1/spotReports?spotReport=card&count=1'),
    'ReportsApi:spot_reports_uid_get': ('ReportsApi', 'spot_reports_uid_get', {'uid': '71209453544e87917ffe2e2967f1c385'}, 'FullSpotReportSchema', 'https://api.intel471.com/v1/spotReports/71209453544e87917ffe2e2967f1c385'),
    'ReportsApi:situation_reports_get': ('ReportsApi', 'situation_reports_get', {'situation_report': 'malware', 'count': 1}, 'SituationReportResponse', 'https://api.intel471.com/v1/situationReports?situationReport=malware&count=1'),
    'ReportsApi:situation_reports_report_uid_get': ('ReportsApi', 'situation_reports_report_uid_get', {'report_uid': '517fc6de76929e70eeb3843b63d5ce41'}, 'SituationReportSchema', 'https://api.intel471.com/v1/situationReports/517fc6de76929e70eeb3843b63d5ce41'),
    'TagsApi:tags_get': ('TagsApi', 'tags_get', {}, 'TagResponse', 'https://api.intel471.com/v1/tags'),
    'VulnerabilitiesApi:cve_reports_get': ('VulnerabilitiesApi', 'cve_reports_get', {'count': 1}, 'SimpleCvesResponse', 'https://api.intel471.com/v1/cve/reports?count=1'),
    'VulnerabilitiesApi:cve_reports_uid_get': ('VulnerabilitiesApi', 'cve_reports_uid_get', {'uid': '6b95e65d42a546629cb0a23bc022ecde'}, 'FullCveSchema', 'https://api.intel471.com/v1/cve/reports/6b95e65d42a546629cb0a23bc022ecde'),
    'WatchersApi:watcher_groups_get': ('WatchersApi', 'watcher_groups_get', {}, 'WatcherGroupResponse', 'https://api.intel471.com/v1/watcherGroups'),
    'WatchersApi:watcher_groups_group_uid_get': ('WatchersApi', 'watcher_groups_group_uid_get', {'group_uid': '3d0b4432-7390-4ae5-92be-52c3e39dc775'}, 'SimpleWatcherGroupSchema', 'https://api.intel471.com/v1/watcherGroups/3d0b4432-7390-4ae5-92be-52c3e39dc775'),
    'WatchersApi:watcher_groups_group_uid_watchers_get': ('WatchersApi', 'watcher_groups_group_uid_watchers_get', {'group_uid': '3d0b4432-7390-4ae5-92be-52c3e39dc775'}, 'WatcherSchemaResponse', 'https://api.intel471.com/v1/watcherGroups/3d0b4432-7390-4ae5-92be-52c3e39dc775/watchers'),
    'WatchersApi:watcher_groups_group_uid_watchers_watcher_uid_get': ('WatchersApi', 'watcher_groups_group_uid_watchers_watcher_uid_get', {'group_uid': '3d0b4432-7390-4ae5-92be-52c3e39dc775', 'watcher_uid': '81808755feef2000acb593a3a5239cdc'}, 'WatcherSchema', 'https://api.intel471.com/v1/watcherGroups/3d0b4432-7390-4ae5-92be-52c3e39dc775/watchers/81808755feef2000acb593a3a5239cdc'),
    'YARAApi:yara_get': ('YARAApi', 'yara_get', {'threat_type': 'malware', 'count': 1}, 'YARASearchResponse', 'https://api.intel471.com/v1/yara?threatType=malware&count=1'),
}

@patch('titan_client.rest.RESTClientObject')
@pytest.mark.parametrize('api_cls_name, method_name, kwargs, filename, query_url', test_params.values(), ids=test_params.keys())
def test_api_responses(rest_client_class_mock, api_cls_name, method_name, kwargs, filename, query_url):
    rest_client_response = MagicMock()
    rest_client_response.status = 200
    rest_client_response.reason = 'OK'
    rest_client_response.getheader.return_value = 'application/json; charset=utf-8'
    rest_client_response.getheaders.return_value = None
    response = read_fixture(f'{PREFIX}/fixtures/api_responses/{filename}.json')
    rest_client_response.data = json.dumps(response).encode('utf-8')

    rest_client_instance_mock = MagicMock()
    rest_client_instance_mock.request.return_value = rest_client_response

    rest_client_class_mock.side_effect = [rest_client_instance_mock]

    with titan_client.ApiClient(configuration) as api_client:
        api_instance = getattr(titan_client, api_cls_name)(api_client)
        api_response = getattr(api_instance, method_name)(**kwargs)

        assert rest_client_instance_mock.request.call_args_list[0][0][1] == query_url
        assert api_response.to_dict() == response
