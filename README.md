# Titan Python Client

Official low-level client for Intel 471's Titan API. It aims at providing common ground for all the endpoints in Python.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.19.0
- Package version: 1.19.0.2
- Build package: org.openapitools.codegen.languages.PythonLegacyClientCodegen

## Requirements.

Python >= 3.6 

## Installation & Usage
### pip install

```
pip install titan-client
```

You can install the python package directly from GitHub:

```sh
pip install git+ssh://git@github.com/intel471/titan-client-python.git
```
(you may need to run `pip` with root permission)

Then import the package:
```python
import titan_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import titan_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import titan_client
from titan_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.intel471.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = titan_client.Configuration(
    host = "https://api.intel471.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = titan_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with titan_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titan_client.ActorsApi(api_client)
    actor = 'synthx' # str | Search for handles only. At least one of `actor`, `forum` parameter is required. (optional)
    forum = '0day' # str | Search for actors active on given forum. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'relevance' # str | Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order. (optional) (default to 'relevance')
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Actors
        api_response = api_instance.actors_get(actor=actor, forum=forum, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ActorsApi->actors_get: %s\n" % e)
    
```

## Serialization

Each call to the API instance returns a structure of python objects. The response can be then serialized to one of the common formats if needed.

### Python dict

In order to convert the response into the python dict structure, call `to_dict()` method on the response object.
It accepts an optional boolean argument `serialize`, which defaults to `False`. When set to `True`, the names of the keys will not be normalised to snake_case, but will be kept intact, as received from the API endpoint.

```
serialized = api_response.to_dict(serialize=True)
```

### STIX format

In order to convert the response into the STIX format, call `to_stix()` method on the response object.
It will convert the API response into respective STIX objects and return them inside the `Bundle` object (from [stix2](https://pypi.org/project/stix2/) package).
`Bundle` object can be serialized into JSON string using `serialize()` method.
If the objects returned by the endpoint for some reason can't be mapped into STIX format, `EmptyBundle` exception will be raised.

```
bundle = api_response.to_stix()
json_repr = bundle.serialize()
```

At the moment following API methods provide the response in STIX format:

API endpoint | Client methods/classes | Produced outcome | Additional info
-------------|------------------------|------------------|-----------------
`/indicators`|  `IndicatorsApi.indicators_get`,  `IndicatorsApi.indicators_stream_get` | `Indicator` and `Malware` SDOs related using `Relationship` object | |
`/iocs`      |  `IOCsApi.iocs_get`    | `Indicator` and `Report` SDOs related using `Report`'s internal property `object_refs` | Only indicators of type `MaliciousDomain` and `MaliciousURL` |
`/yara`      |  `YARAApi.yara_get`    | `Indicator` and `Malware` SDOs related using `Relationship` object | | 
`/cve/reports`      |  `VulnerabilitiesApi.cve_reports_get`    | `Vulnerability` SDOs | |
`/cve/reports/{uid}`      |  `VulnerabilitiesApi.cve_reports_uid_get`    | `Vulnerability` SDO | |

*Please note that STIX mapping is an experimental feature. Not all the endpoints are mapped yet and those that are mapped might have issues and might be a subject of further re-modelling.*
*If `to_stix()` method is called on a response from the endpoint that is not mapped yet, `StixMapperNotFound` exception will be raised.*

## Documentation for API Endpoints

All URIs are relative to *https://api.intel471.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActorsApi* | [**actors_get**](docs/ActorsApi.md#actors_get) | **GET** /actors | Search Actors
*ActorsApi* | [**actors_uid_get**](docs/ActorsApi.md#actors_uid_get) | **GET** /actors/{uid} | Get Actor
*AlertsApi* | [**alerts_get**](docs/AlertsApi.md#alerts_get) | **GET** /alerts | Get Alerts
*CredentialsApi* | [**credential_sets_accessed_urls_get**](docs/CredentialsApi.md#credential_sets_accessed_urls_get) | **GET** /credentialSets/accessedUrls | Search credential set accessed urls
*CredentialsApi* | [**credential_sets_accessed_urls_stream_get**](docs/CredentialsApi.md#credential_sets_accessed_urls_stream_get) | **GET** /credentialSets/accessedUrls/stream | Credential set accessed url stream
*CredentialsApi* | [**credential_sets_get**](docs/CredentialsApi.md#credential_sets_get) | **GET** /credentialSets | Search credential sets
*CredentialsApi* | [**credential_sets_stream_get**](docs/CredentialsApi.md#credential_sets_stream_get) | **GET** /credentialSets/stream | Credential set stream
*CredentialsApi* | [**credentials_accessed_urls_get**](docs/CredentialsApi.md#credentials_accessed_urls_get) | **GET** /credentials/accessedUrls | Search credential accessed urls
*CredentialsApi* | [**credentials_accessed_urls_stream_get**](docs/CredentialsApi.md#credentials_accessed_urls_stream_get) | **GET** /credentials/accessedUrls/stream | Credential accessed url stream
*CredentialsApi* | [**credentials_get**](docs/CredentialsApi.md#credentials_get) | **GET** /credentials | Search credentials
*CredentialsApi* | [**credentials_occurrences_get**](docs/CredentialsApi.md#credentials_occurrences_get) | **GET** /credentials/occurrences | Search credential occurrences
*CredentialsApi* | [**credentials_occurrences_stream_get**](docs/CredentialsApi.md#credentials_occurrences_stream_get) | **GET** /credentials/occurrences/stream | Credential occurrence stream
*CredentialsApi* | [**credentials_stream_get**](docs/CredentialsApi.md#credentials_stream_get) | **GET** /credentials/stream | Credential stream
*EntitiesApi* | [**entities_get**](docs/EntitiesApi.md#entities_get) | **GET** /entities | Search Entities.
*EventsApi* | [**events_get**](docs/EventsApi.md#events_get) | **GET** /events | Search Malware Intelligence Events
*EventsApi* | [**events_stream_get**](docs/EventsApi.md#events_stream_get) | **GET** /events/stream | Stream Malware Intelligence Events
*ForumsApi* | [**posts_get**](docs/ForumsApi.md#posts_get) | **GET** /posts | Search Forum Posts
*ForumsApi* | [**private_messages_get**](docs/ForumsApi.md#private_messages_get) | **GET** /privateMessages | Search Private Messages
*GIRsApi* | [**girs_get**](docs/GIRsApi.md#girs_get) | **GET** /girs | Search GIRs
*GlobalSearchApi* | [**search_get**](docs/GlobalSearchApi.md#search_get) | **GET** /search | Search - Global Search
*IOCsApi* | [**iocs_get**](docs/IOCsApi.md#iocs_get) | **GET** /iocs | Search Indicator of Compromise (IoC)
*IndicatorsApi* | [**indicators_get**](docs/IndicatorsApi.md#indicators_get) | **GET** /indicators | Search Malware Intelligence Indicators
*IndicatorsApi* | [**indicators_stream_get**](docs/IndicatorsApi.md#indicators_stream_get) | **GET** /indicators/stream | Stream Malware Intelligence Indicators
*MessagingServicesApi* | [**messaging_services_instant_messages_get**](docs/MessagingServicesApi.md#messaging_services_instant_messages_get) | **GET** /messagingServices/instantMessages | Search Instant Messages
*NewsApi* | [**news_get**](docs/NewsApi.md#news_get) | **GET** /news | Search News
*NewsApi* | [**news_uid_get**](docs/NewsApi.md#news_uid_get) | **GET** /news/{uid} | Get News
*PCAPApi* | [**malware_pcaps_get**](docs/PCAPApi.md#malware_pcaps_get) | **GET** /malware/pcaps | List of files
*ReportsApi* | [**breach_alerts_get**](docs/ReportsApi.md#breach_alerts_get) | **GET** /breachAlerts | Search Breach Alerts
*ReportsApi* | [**breach_alerts_uid_get**](docs/ReportsApi.md#breach_alerts_uid_get) | **GET** /breachAlerts/{uid} | Get Breach Alert
*ReportsApi* | [**malware_reports_get**](docs/ReportsApi.md#malware_reports_get) | **GET** /malwareReports | Search Malware Intelligence Reports
*ReportsApi* | [**malware_reports_uid_get**](docs/ReportsApi.md#malware_reports_uid_get) | **GET** /malwareReports/{uid} | Get Malware Intelligence Report
*ReportsApi* | [**reports_get**](docs/ReportsApi.md#reports_get) | **GET** /reports | Search Reports
*ReportsApi* | [**reports_uid_get**](docs/ReportsApi.md#reports_uid_get) | **GET** /reports/{uid} | Get Report
*ReportsApi* | [**situation_reports_get**](docs/ReportsApi.md#situation_reports_get) | **GET** /situationReports | Search Situation Reports
*ReportsApi* | [**situation_reports_report_uid_get**](docs/ReportsApi.md#situation_reports_report_uid_get) | **GET** /situationReports/{reportUid} | Get Situation Report
*ReportsApi* | [**spot_reports_get**](docs/ReportsApi.md#spot_reports_get) | **GET** /spotReports | Search Spot Reports
*ReportsApi* | [**spot_reports_uid_get**](docs/ReportsApi.md#spot_reports_uid_get) | **GET** /spotReports/{uid} | Get Spot Report
*TagsApi* | [**tags_get**](docs/TagsApi.md#tags_get) | **GET** /tags | Get Tag List
*VulnerabilitiesApi* | [**cve_reports_get**](docs/VulnerabilitiesApi.md#cve_reports_get) | **GET** /cve/reports | Search Vulnerability Reports (CVE)
*VulnerabilitiesApi* | [**cve_reports_uid_get**](docs/VulnerabilitiesApi.md#cve_reports_uid_get) | **GET** /cve/reports/{uid} | Get Vulnerability Report (CVE)
*WatchersApi* | [**watcher_groups_get**](docs/WatchersApi.md#watcher_groups_get) | **GET** /watcherGroups | Get Watcher Group List
*WatchersApi* | [**watcher_groups_group_uid_delete**](docs/WatchersApi.md#watcher_groups_group_uid_delete) | **DELETE** /watcherGroups/{group-uid} | Delete Watcher Group
*WatchersApi* | [**watcher_groups_group_uid_get**](docs/WatchersApi.md#watcher_groups_group_uid_get) | **GET** /watcherGroups/{group-uid} | Get Watcher Group
*WatchersApi* | [**watcher_groups_group_uid_put**](docs/WatchersApi.md#watcher_groups_group_uid_put) | **PUT** /watcherGroups/{group-uid} | Put Watcher Group
*WatchersApi* | [**watcher_groups_group_uid_watchers_get**](docs/WatchersApi.md#watcher_groups_group_uid_watchers_get) | **GET** /watcherGroups/{group-uid}/watchers | Get Watchers list
*WatchersApi* | [**watcher_groups_group_uid_watchers_post**](docs/WatchersApi.md#watcher_groups_group_uid_watchers_post) | **POST** /watcherGroups/{group-uid}/watchers | Create Watcher
*WatchersApi* | [**watcher_groups_group_uid_watchers_watcher_uid_delete**](docs/WatchersApi.md#watcher_groups_group_uid_watchers_watcher_uid_delete) | **DELETE** /watcherGroups/{group-uid}/watchers/{watcher-uid} | Delete Watcher
*WatchersApi* | [**watcher_groups_group_uid_watchers_watcher_uid_get**](docs/WatchersApi.md#watcher_groups_group_uid_watchers_watcher_uid_get) | **GET** /watcherGroups/{group-uid}/watchers/{watcher-uid} | Get Watcher
*WatchersApi* | [**watcher_groups_group_uid_watchers_watcher_uid_put**](docs/WatchersApi.md#watcher_groups_group_uid_watchers_watcher_uid_put) | **PUT** /watcherGroups/{group-uid}/watchers/{watcher-uid} | Put Watcher
*WatchersApi* | [**watcher_groups_post**](docs/WatchersApi.md#watcher_groups_post) | **POST** /watcherGroups | Create Watcher Group
*YARAApi* | [**yara_get**](docs/YARAApi.md#yara_get) | **GET** /yara | Search Malware Intelligence YARA


## Documentation For Models

 - [AlertListSchema](docs/AlertListSchema.md)
 - [AlertListSchemaChunks](docs/AlertListSchemaChunks.md)
 - [AlertListSchemaHighlights](docs/AlertListSchemaHighlights.md)
 - [AlertListSchemaReport](docs/AlertListSchemaReport.md)
 - [AlertListSchemaResponse](docs/AlertListSchemaResponse.md)
 - [CredentialAccessedUrlSchema](docs/CredentialAccessedUrlSchema.md)
 - [CredentialAccessedUrlSchemaActivity](docs/CredentialAccessedUrlSchemaActivity.md)
 - [CredentialAccessedUrlSchemaClassification](docs/CredentialAccessedUrlSchemaClassification.md)
 - [CredentialAccessedUrlSchemaData](docs/CredentialAccessedUrlSchemaData.md)
 - [CredentialAccessedUrlSchemaDataCredential](docs/CredentialAccessedUrlSchemaDataCredential.md)
 - [CredentialAccessedUrlStreamSchema](docs/CredentialAccessedUrlStreamSchema.md)
 - [CredentialAccessedUrlsResponse](docs/CredentialAccessedUrlsResponse.md)
 - [CredentialAccessedUrlsStreamResponse](docs/CredentialAccessedUrlsStreamResponse.md)
 - [CredentialOccurrenceSchema](docs/CredentialOccurrenceSchema.md)
 - [CredentialOccurrenceSchemaActivity](docs/CredentialOccurrenceSchemaActivity.md)
 - [CredentialOccurrenceSchemaClassification](docs/CredentialOccurrenceSchemaClassification.md)
 - [CredentialOccurrenceSchemaData](docs/CredentialOccurrenceSchemaData.md)
 - [CredentialOccurrenceSchemaDataCredential](docs/CredentialOccurrenceSchemaDataCredential.md)
 - [CredentialOccurrenceSchemaDataCredentialSet](docs/CredentialOccurrenceSchemaDataCredentialSet.md)
 - [CredentialOccurrencesResponse](docs/CredentialOccurrencesResponse.md)
 - [CredentialOccurrencesStreamResponse](docs/CredentialOccurrencesStreamResponse.md)
 - [CredentialSchema](docs/CredentialSchema.md)
 - [CredentialSchemaActivity](docs/CredentialSchemaActivity.md)
 - [CredentialSchemaClassification](docs/CredentialSchemaClassification.md)
 - [CredentialSchemaData](docs/CredentialSchemaData.md)
 - [CredentialSchemaDataCredentialSets](docs/CredentialSchemaDataCredentialSets.md)
 - [CredentialSchemaDataPassword](docs/CredentialSchemaDataPassword.md)
 - [CredentialSchemaDataPasswordComplexity](docs/CredentialSchemaDataPasswordComplexity.md)
 - [CredentialSchemaStatistics](docs/CredentialSchemaStatistics.md)
 - [CredentialSetAccessedUrlSchema](docs/CredentialSetAccessedUrlSchema.md)
 - [CredentialSetAccessedUrlSchemaActivity](docs/CredentialSetAccessedUrlSchemaActivity.md)
 - [CredentialSetAccessedUrlSchemaClassification](docs/CredentialSetAccessedUrlSchemaClassification.md)
 - [CredentialSetAccessedUrlSchemaData](docs/CredentialSetAccessedUrlSchemaData.md)
 - [CredentialSetAccessedUrlSchemaDataCredentialSet](docs/CredentialSetAccessedUrlSchemaDataCredentialSet.md)
 - [CredentialSetAccessedUrlStreamSchema](docs/CredentialSetAccessedUrlStreamSchema.md)
 - [CredentialSetAccessedUrlStreamSchemaData](docs/CredentialSetAccessedUrlStreamSchemaData.md)
 - [CredentialSetSchema](docs/CredentialSetSchema.md)
 - [CredentialSetSchemaActivity](docs/CredentialSetSchemaActivity.md)
 - [CredentialSetSchemaClassification](docs/CredentialSetSchemaClassification.md)
 - [CredentialSetSchemaData](docs/CredentialSetSchemaData.md)
 - [CredentialSetSchemaDataExternalSources](docs/CredentialSetSchemaDataExternalSources.md)
 - [CredentialSetSchemaDataInternalSources](docs/CredentialSetSchemaDataInternalSources.md)
 - [CredentialSetSchemaDataVictims](docs/CredentialSetSchemaDataVictims.md)
 - [CredentialSetSchemaStatistics](docs/CredentialSetSchemaStatistics.md)
 - [CredentialSetStreamSchema](docs/CredentialSetStreamSchema.md)
 - [CredentialSetStreamSchemaData](docs/CredentialSetStreamSchemaData.md)
 - [CredentialSetsAccessedUrlsResponse](docs/CredentialSetsAccessedUrlsResponse.md)
 - [CredentialSetsAccessedUrlsStreamResponse](docs/CredentialSetsAccessedUrlsStreamResponse.md)
 - [CredentialSetsResponse](docs/CredentialSetsResponse.md)
 - [CredentialSetsStreamResponse](docs/CredentialSetsStreamResponse.md)
 - [CredentialsResponse](docs/CredentialsResponse.md)
 - [CredentialsStreamResponse](docs/CredentialsStreamResponse.md)
 - [EntitiesResponse](docs/EntitiesResponse.md)
 - [EntitiesSchema](docs/EntitiesSchema.md)
 - [EntitiesSchemaLinks](docs/EntitiesSchemaLinks.md)
 - [EntitiesSchemaLinksActors](docs/EntitiesSchemaLinksActors.md)
 - [EntitiesSchemaLinksReports](docs/EntitiesSchemaLinksReports.md)
 - [EventSchema](docs/EventSchema.md)
 - [EventSchemaActivity](docs/EventSchemaActivity.md)
 - [EventSchemaData](docs/EventSchemaData.md)
 - [EventSchemaDataEventData](docs/EventSchemaDataEventData.md)
 - [EventSchemaDataEventDataController](docs/EventSchemaDataEventDataController.md)
 - [EventSchemaDataEventDataControllerGeoIp](docs/EventSchemaDataEventDataControllerGeoIp.md)
 - [EventSchemaDataEventDataControllerGeoIpIsp](docs/EventSchemaDataEventDataControllerGeoIpIsp.md)
 - [EventSchemaDataEventDataControllers](docs/EventSchemaDataEventDataControllers.md)
 - [EventSchemaDataEventDataEncryption](docs/EventSchemaDataEventDataEncryption.md)
 - [EventSchemaDataEventDataFile](docs/EventSchemaDataEventDataFile.md)
 - [EventSchemaDataEventDataLocation](docs/EventSchemaDataEventDataLocation.md)
 - [EventSchemaDataEventDataRecipientDomains](docs/EventSchemaDataEventDataRecipientDomains.md)
 - [EventSchemaDataEventDataTriggers](docs/EventSchemaDataEventDataTriggers.md)
 - [EventSchemaDataThreat](docs/EventSchemaDataThreat.md)
 - [EventSchemaDataThreatData](docs/EventSchemaDataThreatData.md)
 - [EventSchemaMeta](docs/EventSchemaMeta.md)
 - [EventStreamResponse](docs/EventStreamResponse.md)
 - [EventsResponse](docs/EventsResponse.md)
 - [FullBreachAlertSchema](docs/FullBreachAlertSchema.md)
 - [FullBreachAlertSchemaAllOf](docs/FullBreachAlertSchemaAllOf.md)
 - [FullCveSchema](docs/FullCveSchema.md)
 - [FullNewsSchema](docs/FullNewsSchema.md)
 - [FullReportSchema](docs/FullReportSchema.md)
 - [FullReportSchemaAllOf](docs/FullReportSchemaAllOf.md)
 - [FullSpotReportSchema](docs/FullSpotReportSchema.md)
 - [FullWatcherGroupSchema](docs/FullWatcherGroupSchema.md)
 - [FullWatcherGroupSchemaAllOf](docs/FullWatcherGroupSchemaAllOf.md)
 - [FullWatcherGroupSchemaAllOfLinks](docs/FullWatcherGroupSchemaAllOfLinks.md)
 - [FullWatcherGroupSchemaAllOfLinksForum](docs/FullWatcherGroupSchemaAllOfLinksForum.md)
 - [FullWatcherGroupSchemaAllOfLinksThread](docs/FullWatcherGroupSchemaAllOfLinksThread.md)
 - [FullWatcherGroupSchemaAllOfPatterns](docs/FullWatcherGroupSchemaAllOfPatterns.md)
 - [FullWatcherGroupSchemaAllOfWatchers](docs/FullWatcherGroupSchemaAllOfWatchers.md)
 - [GirSchema](docs/GirSchema.md)
 - [GirSchemaData](docs/GirSchemaData.md)
 - [GirSchemaDataGir](docs/GirSchemaDataGir.md)
 - [GirsResponse](docs/GirsResponse.md)
 - [IndicatorSearchResponse](docs/IndicatorSearchResponse.md)
 - [IndicatorSearchSchema](docs/IndicatorSearchSchema.md)
 - [IndicatorSearchSchemaActivity](docs/IndicatorSearchSchemaActivity.md)
 - [IndicatorSearchSchemaData](docs/IndicatorSearchSchemaData.md)
 - [IndicatorSearchSchemaDataContext](docs/IndicatorSearchSchemaDataContext.md)
 - [IndicatorSearchSchemaDataIndicatorData](docs/IndicatorSearchSchemaDataIndicatorData.md)
 - [IndicatorSearchSchemaDataIndicatorDataFile](docs/IndicatorSearchSchemaDataIndicatorDataFile.md)
 - [IndicatorSearchSchemaDataThreat](docs/IndicatorSearchSchemaDataThreat.md)
 - [IndicatorSearchSchemaDataThreatData](docs/IndicatorSearchSchemaDataThreatData.md)
 - [IndicatorSearchSchemaMeta](docs/IndicatorSearchSchemaMeta.md)
 - [IndicatorStreamResponse](docs/IndicatorStreamResponse.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InstantMessageSchema](docs/InstantMessageSchema.md)
 - [InstantMessageSchemaActivity](docs/InstantMessageSchemaActivity.md)
 - [InstantMessageSchemaData](docs/InstantMessageSchemaData.md)
 - [InstantMessageSchemaDataActor](docs/InstantMessageSchemaDataActor.md)
 - [InstantMessageSchemaDataChannel](docs/InstantMessageSchemaDataChannel.md)
 - [InstantMessageSchemaDataMessage](docs/InstantMessageSchemaDataMessage.md)
 - [InstantMessageSchemaDataMessageAttachments](docs/InstantMessageSchemaDataMessageAttachments.md)
 - [InstantMessageSchemaDataServer](docs/InstantMessageSchemaDataServer.md)
 - [IocSchema](docs/IocSchema.md)
 - [IocSchemaLinks](docs/IocSchemaLinks.md)
 - [IocSchemaLinksActors](docs/IocSchemaLinksActors.md)
 - [IocSchemaLinksReports](docs/IocSchemaLinksReports.md)
 - [IocsResponse](docs/IocsResponse.md)
 - [Malware](docs/Malware.md)
 - [MalwareReportsSearchResponse](docs/MalwareReportsSearchResponse.md)
 - [MalwareReportsSearchSchema](docs/MalwareReportsSearchSchema.md)
 - [MalwareReportsSearchSchemaActivity](docs/MalwareReportsSearchSchemaActivity.md)
 - [MalwareReportsSearchSchemaClassification](docs/MalwareReportsSearchSchemaClassification.md)
 - [MalwareReportsSearchSchemaData](docs/MalwareReportsSearchSchemaData.md)
 - [MalwareReportsSearchSchemaDataMalwareReportData](docs/MalwareReportsSearchSchemaDataMalwareReportData.md)
 - [MalwareReportsSearchSchemaDataMalwareReportDataAttachments](docs/MalwareReportsSearchSchemaDataMalwareReportDataAttachments.md)
 - [MalwareReportsSearchSchemaDataThreat](docs/MalwareReportsSearchSchemaDataThreat.md)
 - [MalwareReportsSearchSchemaDataThreatData](docs/MalwareReportsSearchSchemaDataThreatData.md)
 - [MessagingServicesResponse](docs/MessagingServicesResponse.md)
 - [NewsSchema](docs/NewsSchema.md)
 - [NewsSchemaActivity](docs/NewsSchemaActivity.md)
 - [NewsSchemaData](docs/NewsSchemaData.md)
 - [NewsSchemaDataAttachments](docs/NewsSchemaDataAttachments.md)
 - [PCAPResponse](docs/PCAPResponse.md)
 - [PCAPSchema](docs/PCAPSchema.md)
 - [PCAPSchemaData](docs/PCAPSchemaData.md)
 - [PCAPSchemaDataFile](docs/PCAPSchemaDataFile.md)
 - [PCAPSchemaDataMalwareFamily](docs/PCAPSchemaDataMalwareFamily.md)
 - [PCAPSchemaDataPcap](docs/PCAPSchemaDataPcap.md)
 - [PostSchema](docs/PostSchema.md)
 - [PostSchemaLinks](docs/PostSchemaLinks.md)
 - [PostSchemaLinksAuthorActor](docs/PostSchemaLinksAuthorActor.md)
 - [PostSchemaLinksForum](docs/PostSchemaLinksForum.md)
 - [PostSchemaLinksThread](docs/PostSchemaLinksThread.md)
 - [PostsResponse](docs/PostsResponse.md)
 - [PrivateMessageSchema](docs/PrivateMessageSchema.md)
 - [PrivateMessageSchemaLinks](docs/PrivateMessageSchemaLinks.md)
 - [PrivateMessageSchemaLinksAuthorActor](docs/PrivateMessageSchemaLinksAuthorActor.md)
 - [PrivateMessageSchemaLinksForum](docs/PrivateMessageSchemaLinksForum.md)
 - [PrivateMessageSchemaLinksRecipientActor](docs/PrivateMessageSchemaLinksRecipientActor.md)
 - [PrivateMessagesResponse](docs/PrivateMessagesResponse.md)
 - [SearchSchema](docs/SearchSchema.md)
 - [SimpleActorSchema](docs/SimpleActorSchema.md)
 - [SimpleActorSchemaLinks](docs/SimpleActorSchemaLinks.md)
 - [SimpleActorSchemaLinksContactInfo](docs/SimpleActorSchemaLinksContactInfo.md)
 - [SimpleActorSchemaLinksForums](docs/SimpleActorSchemaLinksForums.md)
 - [SimpleActorSchemaLinksInstantMessageServers](docs/SimpleActorSchemaLinksInstantMessageServers.md)
 - [SimpleActorsResponse](docs/SimpleActorsResponse.md)
 - [SimpleBreachAlertResponse](docs/SimpleBreachAlertResponse.md)
 - [SimpleBreachAlertSchema](docs/SimpleBreachAlertSchema.md)
 - [SimpleBreachAlertSchemaActivity](docs/SimpleBreachAlertSchemaActivity.md)
 - [SimpleBreachAlertSchemaData](docs/SimpleBreachAlertSchemaData.md)
 - [SimpleBreachAlertSchemaDataBreachAlert](docs/SimpleBreachAlertSchemaDataBreachAlert.md)
 - [SimpleBreachAlertSchemaDataBreachAlertConfidence](docs/SimpleBreachAlertSchemaDataBreachAlertConfidence.md)
 - [SimpleBreachAlertSchemaDataBreachAlertSources](docs/SimpleBreachAlertSchemaDataBreachAlertSources.md)
 - [SimpleBreachAlertSchemaDataBreachAlertVictim](docs/SimpleBreachAlertSchemaDataBreachAlertVictim.md)
 - [SimpleBreachAlertSchemaDataBreachAlertVictimIndustries](docs/SimpleBreachAlertSchemaDataBreachAlertVictimIndustries.md)
 - [SimpleBreachAlertSchemaDataEntities](docs/SimpleBreachAlertSchemaDataEntities.md)
 - [SimpleBreachAlertSchemaDataGeoInfo](docs/SimpleBreachAlertSchemaDataGeoInfo.md)
 - [SimpleCveSchema](docs/SimpleCveSchema.md)
 - [SimpleCveSchemaActivity](docs/SimpleCveSchemaActivity.md)
 - [SimpleCveSchemaClassification](docs/SimpleCveSchemaClassification.md)
 - [SimpleCveSchemaData](docs/SimpleCveSchemaData.md)
 - [SimpleCveSchemaDataCveReport](docs/SimpleCveSchemaDataCveReport.md)
 - [SimpleCveSchemaDataCveReportActivityLocation](docs/SimpleCveSchemaDataCveReportActivityLocation.md)
 - [SimpleCveSchemaDataCveReportCounterMeasureLinks](docs/SimpleCveSchemaDataCveReportCounterMeasureLinks.md)
 - [SimpleCveSchemaDataCveReportCvssScore](docs/SimpleCveSchemaDataCveReportCvssScore.md)
 - [SimpleCveSchemaDataCveReportExploitStatus](docs/SimpleCveSchemaDataCveReportExploitStatus.md)
 - [SimpleCveSchemaDataCveReportInterestLevel](docs/SimpleCveSchemaDataCveReportInterestLevel.md)
 - [SimpleCveSchemaDataCveReportPatchLinks](docs/SimpleCveSchemaDataCveReportPatchLinks.md)
 - [SimpleCveSchemaDataCveReportPocLinks](docs/SimpleCveSchemaDataCveReportPocLinks.md)
 - [SimpleCveSchemaDataCveReportTitanLinks](docs/SimpleCveSchemaDataCveReportTitanLinks.md)
 - [SimpleCvesResponse](docs/SimpleCvesResponse.md)
 - [SimpleNewsResponse](docs/SimpleNewsResponse.md)
 - [SimpleReportSchema](docs/SimpleReportSchema.md)
 - [SimpleReportSchemaActorSubjectOfReport](docs/SimpleReportSchemaActorSubjectOfReport.md)
 - [SimpleReportSchemaClassification](docs/SimpleReportSchemaClassification.md)
 - [SimpleReportSchemaEntities](docs/SimpleReportSchemaEntities.md)
 - [SimpleReportSchemaLocations](docs/SimpleReportSchemaLocations.md)
 - [SimpleReportSchemaRelatedReports](docs/SimpleReportSchemaRelatedReports.md)
 - [SimpleReportSchemaReportAttachments](docs/SimpleReportSchemaReportAttachments.md)
 - [SimpleReportSchemaSources](docs/SimpleReportSchemaSources.md)
 - [SimpleReportSchemaVictims](docs/SimpleReportSchemaVictims.md)
 - [SimpleReportsResponse](docs/SimpleReportsResponse.md)
 - [SimpleSpotReportSchema](docs/SimpleSpotReportSchema.md)
 - [SimpleSpotReportSchemaActivity](docs/SimpleSpotReportSchemaActivity.md)
 - [SimpleSpotReportSchemaData](docs/SimpleSpotReportSchemaData.md)
 - [SimpleSpotReportSchemaDataEntities](docs/SimpleSpotReportSchemaDataEntities.md)
 - [SimpleSpotReportSchemaDataSpotReport](docs/SimpleSpotReportSchemaDataSpotReport.md)
 - [SimpleSpotReportSchemaDataSpotReportSpotReportData](docs/SimpleSpotReportSchemaDataSpotReportSpotReportData.md)
 - [SimpleSpotReportSchemaDataSpotReportSpotReportDataLinks](docs/SimpleSpotReportSchemaDataSpotReportSpotReportDataLinks.md)
 - [SimpleSpotReportSchemaDataSpotReportSpotReportDataVictims](docs/SimpleSpotReportSchemaDataSpotReportSpotReportDataVictims.md)
 - [SimpleSpotReportsResponse](docs/SimpleSpotReportsResponse.md)
 - [SimpleWatcherGroupSchema](docs/SimpleWatcherGroupSchema.md)
 - [SituationReportResponse](docs/SituationReportResponse.md)
 - [SituationReportSchema](docs/SituationReportSchema.md)
 - [SituationReportSchemaActivity](docs/SituationReportSchemaActivity.md)
 - [SituationReportSchemaClassification](docs/SituationReportSchemaClassification.md)
 - [SituationReportSchemaData](docs/SituationReportSchemaData.md)
 - [SituationReportSchemaDataSituationReport](docs/SituationReportSchemaDataSituationReport.md)
 - [SituationReportSchemaDataSituationReportEntities](docs/SituationReportSchemaDataSituationReportEntities.md)
 - [SituationReportSchemaDataSituationReportLink](docs/SituationReportSchemaDataSituationReportLink.md)
 - [SituationReportSchemaDataSituationReportLinkMalwareFamily](docs/SituationReportSchemaDataSituationReportLinkMalwareFamily.md)
 - [SituationReportSchemaDataSituationReportLinkMalwareReport](docs/SituationReportSchemaDataSituationReportLinkMalwareReport.md)
 - [SituationReportSchemaDataSituationReportVictims](docs/SituationReportSchemaDataSituationReportVictims.md)
 - [TagResponse](docs/TagResponse.md)
 - [TagSchema](docs/TagSchema.md)
 - [WatcherGroupResponse](docs/WatcherGroupResponse.md)
 - [WatcherRequestBody](docs/WatcherRequestBody.md)
 - [WatcherRequestBodyFilters](docs/WatcherRequestBodyFilters.md)
 - [WatcherRequestBodyPatterns](docs/WatcherRequestBodyPatterns.md)
 - [WatcherRequestBodyPost](docs/WatcherRequestBodyPost.md)
 - [WatcherRequestBodyPostAllOf](docs/WatcherRequestBodyPostAllOf.md)
 - [WatcherRequestBodyPut](docs/WatcherRequestBodyPut.md)
 - [WatcherRequestBodyPutAllOf](docs/WatcherRequestBodyPutAllOf.md)
 - [WatcherSchema](docs/WatcherSchema.md)
 - [WatcherSchemaFilters](docs/WatcherSchemaFilters.md)
 - [WatcherSchemaForum](docs/WatcherSchemaForum.md)
 - [WatcherSchemaLinks](docs/WatcherSchemaLinks.md)
 - [WatcherSchemaPatterns](docs/WatcherSchemaPatterns.md)
 - [WatcherSchemaResponse](docs/WatcherSchemaResponse.md)
 - [WatcherSchemaThread](docs/WatcherSchemaThread.md)
 - [YARASearchResponse](docs/YARASearchResponse.md)
 - [YARASearchSchema](docs/YARASearchSchema.md)
 - [YARASearchSchemaActivity](docs/YARASearchSchemaActivity.md)
 - [YARASearchSchemaData](docs/YARASearchSchemaData.md)
 - [YARASearchSchemaDataThreat](docs/YARASearchSchemaDataThreat.md)
 - [YARASearchSchemaDataThreatData](docs/YARASearchSchemaDataThreatData.md)
 - [YARASearchSchemaDataYaraData](docs/YARASearchSchemaDataYaraData.md)
 - [YARASearchSchemaMeta](docs/YARASearchSchemaMeta.md)


## Documentation For Authorization


## BasicAuth

- **Type**: HTTP basic authentication


## Author




