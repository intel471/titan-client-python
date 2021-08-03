# titan_client.GlobalSearchApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_get**](GlobalSearchApi.md#search_get) | **GET** /search | Search - Global Search


# **search_get**
> SearchSchema search_get(text=text, ip_address=ip_address, url=url, contact_info_email=contact_info_email, post=post, private_message=private_message, private_message_subject=private_message_subject, actors=actors, entity=entity, victim=victim, ioc=ioc, report=report, report_tag=report_tag, report_location=report_location, report_admiralty_code=report_admiralty_code, document_type=document_type, document_family=document_family, event=event, indicator=indicator, yara=yara, nids=nids, malware_report=malware_report, spot_report=spot_report, breach_alert=breach_alert, situation_report=situation_report, event_type=event_type, indicator_type=indicator_type, nids_type=nids_type, threat_type=threat_type, threat_uid=threat_uid, malware_family=malware_family, malware_family_profile_uid=malware_family_profile_uid, confidence=confidence, cve_report=cve_report, cve_type=cve_type, cve_name=cve_name, risk_level=risk_level, patch_status=patch_status, vendor_name=vendor_name, product_name=product_name, instant_message=instant_message, instant_message_actor=instant_message_actor, instant_message_service=instant_message_service, instant_message_server=instant_message_server, instant_message_channel=instant_message_channel, gir=gir, credential_uid=credential_uid, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, detected_malware=detected_malware, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search - Global Search

Returns selection of results matching filter criteria. Can include the following entities:   - [Information Reports](#tag/Reports/paths/~1reports/get)   - [Fintel Reports](#tag/Reports/paths/~1reports/get)   - [Actors](#tag/Actors/paths/~1actors/get)   - [Entities](#tag/Entities/paths/~1entities/get)   - [Indicators of Compromise](#tag/Indicators/paths/~1indicators/get)   - [Posts](#tag/Forums/paths/~1posts/get)   - [PrivateMessages](#tag/Forums/paths/~1privateMessages/get)   - [Events](#tag/Events/paths/~1events/get)   - [Indicators](#tag/Indicators/paths/~1indicators/get)   - [YARA](#tag/YARA/paths/~1yara/get)   - [NIDS](#tag/NIDs/paths/~1nids/get)   - [Malware Reports](#tag/Malware/paths/~1malwareReports/get)   - [Breach Alerts](#tag/Reports/paths/~1breachAlerts/get)   - [Spot Reports](#tag/Reports/paths/~1spotReports/get)   - [Situation Reports](#tag/Global-Search/paths/~1search/get)   - [Cve Reports](#tag/Vulnerabilities/paths/~1cve~1reports/get)   - [Instant Messages](#tag/Messaging-Services/paths/~1messagingServices~1instantMessages/get)   - [Credential Sets](#tag/Credentials/paths/~1credentialSets/get)   - [Credentials](#tag/Credentials/paths/~1credentials/get)   - [Credential Occurrences](#tag/Credentials/paths/~1credentials~1occurrences/get) 

### Example

* Basic Authentication (BasicAuth):
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
    api_instance = titan_client.GlobalSearchApi(api_client)
    text = 'text_example' # str | Search text everywhere. (optional)
ip_address = 'ip_address_example' # str | IP address search. (optional)
url = 'url_example' # str | URL search. (optional)
contact_info_email = 'contact_info_email_example' # str | E-mail address search. (optional)
post = 'post_example' # str | Forum post search. (optional)
private_message = 'private_message_example' # str | Forum private message search. (optional)
private_message_subject = 'private_message_subject_example' # str | Search text in subjects of Private Messages. (optional)
actors = 'actors_example' # str | Actor search. (optional)
entity = 'entity_example' # str | Entity Search. (optional)
victim = 'victim_example' # str | Purported victim search. (optional)
ioc = 'ioc_example' # str | Indicators of compromise search. (optional)
report = 'report_example' # str | Report search. (optional)
report_tag = 'report_tag_example' # str | Search reports by tag. (optional)
report_location = 'report_location_example' # str | Search reports by location. (optional)
report_admiralty_code = 'report_admiralty_code_example' # str | Search reports by admiralty code. (optional)
document_type = 'document_type_example' # str | Search reports by document type. (optional)
document_family = 'document_family_example' # str | Search reports by document family. (optional)
event = 'event_example' # str | Free text event search. (optional)
indicator = 'indicator_example' # str | Free text indicator search. (optional)
yara = 'yara_example' # str | Free text YARAs search. (optional)
nids = 'nids_example' # str | Free text NIDS search. (optional)
malware_report = 'malware_report_example' # str | Free text malware reports search. (optional)
spot_report = 'spot_report_example' # str | Free text spot reports search. (optional)
breach_alert = 'breach_alert_example' # str | Free text breach alerts search. (optional)
situation_report = 'situation_report_example' # str | Free text situation reports search. (optional)
event_type = 'event_type_example' # str | Search events by type. (optional)
indicator_type = 'indicator_type_example' # str | Search indicators by type. (optional)
nids_type = 'nids_type_example' # str | Search NIDS by type. (optional)
threat_type = 'threat_type_example' # str | Search events, indicators, YARAs, NIDS and malware reports by threat type. (optional)
threat_uid = 'threat_uid_example' # str | Search events, indicators, YARAs, NIDS and malware reports by threat uid. (optional)
malware_family = 'malware_family_example' # str | Search events, indicators, YARAs, NIDS and malware reports by malware family (optional)
malware_family_profile_uid = 'malware_family_profile_uid_example' # str | Search events, indicators, YARAs, NIDS and malware reports by malware family profile UID (optional)
confidence = 'confidence_example' # str | Search indicators, YARAs and NIDS by confidence (optional)
cve_report = 'cve_report_example' # str | Free text CVE reports search. (optional)
cve_type = 'cve_type_example' # str | Search CVE reports by type. (optional)
cve_name = 'cve_name_example' # str | Search CVE reports by name. (optional)
risk_level = 'risk_level_example' # str | Search CVE reports by risk level. (optional)
patch_status = 'patch_status_example' # str | Search CVE reports by patch status. (optional)
vendor_name = 'vendor_name_example' # str | Search CVE reports by vendor name. (optional)
product_name = 'product_name_example' # str | Search CVE reports by product name. (optional)
instant_message = 'instant_message_example' # str | Free text instant messages search. (optional)
instant_message_actor = 'instant_message_actor_example' # str | Search instant messages by author handle (actual for the moment message was written). (optional)
instant_message_service = 'instant_message_service_example' # str | Search instant messages by service name (e.g. Telegram, Discord, WhatsApp etc.). (optional)
instant_message_server = 'instant_message_server_example' # str | Search instant messages by server name. (optional)
instant_message_channel = 'instant_message_channel_example' # str | Search instant messages by channel name. (optional)
gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
credential_uid = 'credential_uid_example' # str | Search by credential uid. (optional)
credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
credential_set_uid = 'credential_set_uid_example' # str | Search by credential set uid. (optional)
domain = 'domain_example' # str | Search by credential domain (detection domain). (optional)
affiliation_group = 'affiliation_group_example' # str | Search by credential affiliation group. (optional)
password_strength = 'password_strength_example' # str | Search by password strength. (optional)
password_length_gte = 0 # float | Search by password complexity length field as greater then or equal to input value. (optional) (default to 0)
password_lowercase_gte = 0 # float | Search by password complexity lowercase filed as greater then or equal to input value. (optional) (default to 0)
password_uppercase_gte = 0 # float | Search by password complexity uppercase filed as greater then or equal to input value. (optional) (default to 0)
password_numbers_gte = 0 # float | Search by password complexity numbers filed as greater then or equal to input value. (optional) (default to 0)
password_punctuation_gte = 0 # float | Search by password complexity punctuation filed as greater then or equal to input value. (optional) (default to 0)
password_symbols_gte = 0 # float | Search by password complexity symbols filed as greater then or equal to input value. (optional) (default to 0)
password_separators_gte = 0 # float | Search by password complexity separators filed as greater then or equal to input value. (optional) (default to 0)
password_other_gte = 0 # float | Search by password complexity other filed as greater then or equal to input value. (optional) (default to 0)
password_entropy_gte = 0 # float | Search by password complexity entropy filed as greater then or equal to input value. (optional) (default to 0)
password_plain = 'password_plain_example' # str | Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded. (optional)
detected_malware = 'detected_malware_example' # str | Search by credential detected malware. (optional)
_from = '1day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
sort = 'relevance' # str | Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order. (optional) (default to 'relevance')
filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
offset = 0 # float | Skip leading number of records. (optional) (default to 0)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search - Global Search
        api_response = api_instance.search_get(text=text, ip_address=ip_address, url=url, contact_info_email=contact_info_email, post=post, private_message=private_message, private_message_subject=private_message_subject, actors=actors, entity=entity, victim=victim, ioc=ioc, report=report, report_tag=report_tag, report_location=report_location, report_admiralty_code=report_admiralty_code, document_type=document_type, document_family=document_family, event=event, indicator=indicator, yara=yara, nids=nids, malware_report=malware_report, spot_report=spot_report, breach_alert=breach_alert, situation_report=situation_report, event_type=event_type, indicator_type=indicator_type, nids_type=nids_type, threat_type=threat_type, threat_uid=threat_uid, malware_family=malware_family, malware_family_profile_uid=malware_family_profile_uid, confidence=confidence, cve_report=cve_report, cve_type=cve_type, cve_name=cve_name, risk_level=risk_level, patch_status=patch_status, vendor_name=vendor_name, product_name=product_name, instant_message=instant_message, instant_message_actor=instant_message_actor, instant_message_service=instant_message_service, instant_message_server=instant_message_server, instant_message_channel=instant_message_channel, gir=gir, credential_uid=credential_uid, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, detected_malware=detected_malware, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GlobalSearchApi->search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Search text everywhere. | [optional] 
 **ip_address** | **str**| IP address search. | [optional] 
 **url** | **str**| URL search. | [optional] 
 **contact_info_email** | **str**| E-mail address search. | [optional] 
 **post** | **str**| Forum post search. | [optional] 
 **private_message** | **str**| Forum private message search. | [optional] 
 **private_message_subject** | **str**| Search text in subjects of Private Messages. | [optional] 
 **actors** | **str**| Actor search. | [optional] 
 **entity** | **str**| Entity Search. | [optional] 
 **victim** | **str**| Purported victim search. | [optional] 
 **ioc** | **str**| Indicators of compromise search. | [optional] 
 **report** | **str**| Report search. | [optional] 
 **report_tag** | **str**| Search reports by tag. | [optional] 
 **report_location** | **str**| Search reports by location. | [optional] 
 **report_admiralty_code** | **str**| Search reports by admiralty code. | [optional] 
 **document_type** | **str**| Search reports by document type. | [optional] 
 **document_family** | **str**| Search reports by document family. | [optional] 
 **event** | **str**| Free text event search. | [optional] 
 **indicator** | **str**| Free text indicator search. | [optional] 
 **yara** | **str**| Free text YARAs search. | [optional] 
 **nids** | **str**| Free text NIDS search. | [optional] 
 **malware_report** | **str**| Free text malware reports search. | [optional] 
 **spot_report** | **str**| Free text spot reports search. | [optional] 
 **breach_alert** | **str**| Free text breach alerts search. | [optional] 
 **situation_report** | **str**| Free text situation reports search. | [optional] 
 **event_type** | **str**| Search events by type. | [optional] 
 **indicator_type** | **str**| Search indicators by type. | [optional] 
 **nids_type** | **str**| Search NIDS by type. | [optional] 
 **threat_type** | **str**| Search events, indicators, YARAs, NIDS and malware reports by threat type. | [optional] 
 **threat_uid** | **str**| Search events, indicators, YARAs, NIDS and malware reports by threat uid. | [optional] 
 **malware_family** | **str**| Search events, indicators, YARAs, NIDS and malware reports by malware family | [optional] 
 **malware_family_profile_uid** | **str**| Search events, indicators, YARAs, NIDS and malware reports by malware family profile UID | [optional] 
 **confidence** | **str**| Search indicators, YARAs and NIDS by confidence | [optional] 
 **cve_report** | **str**| Free text CVE reports search. | [optional] 
 **cve_type** | **str**| Search CVE reports by type. | [optional] 
 **cve_name** | **str**| Search CVE reports by name. | [optional] 
 **risk_level** | **str**| Search CVE reports by risk level. | [optional] 
 **patch_status** | **str**| Search CVE reports by patch status. | [optional] 
 **vendor_name** | **str**| Search CVE reports by vendor name. | [optional] 
 **product_name** | **str**| Search CVE reports by product name. | [optional] 
 **instant_message** | **str**| Free text instant messages search. | [optional] 
 **instant_message_actor** | **str**| Search instant messages by author handle (actual for the moment message was written). | [optional] 
 **instant_message_service** | **str**| Search instant messages by service name (e.g. Telegram, Discord, WhatsApp etc.). | [optional] 
 **instant_message_server** | **str**| Search instant messages by server name. | [optional] 
 **instant_message_channel** | **str**| Search instant messages by channel name. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **credential_uid** | **str**| Search by credential uid. | [optional] 
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **credential_set_uid** | **str**| Search by credential set uid. | [optional] 
 **domain** | **str**| Search by credential domain (detection domain). | [optional] 
 **affiliation_group** | **str**| Search by credential affiliation group. | [optional] 
 **password_strength** | **str**| Search by password strength. | [optional] 
 **password_length_gte** | **float**| Search by password complexity length field as greater then or equal to input value. | [optional] [default to 0]
 **password_lowercase_gte** | **float**| Search by password complexity lowercase filed as greater then or equal to input value. | [optional] [default to 0]
 **password_uppercase_gte** | **float**| Search by password complexity uppercase filed as greater then or equal to input value. | [optional] [default to 0]
 **password_numbers_gte** | **float**| Search by password complexity numbers filed as greater then or equal to input value. | [optional] [default to 0]
 **password_punctuation_gte** | **float**| Search by password complexity punctuation filed as greater then or equal to input value. | [optional] [default to 0]
 **password_symbols_gte** | **float**| Search by password complexity symbols filed as greater then or equal to input value. | [optional] [default to 0]
 **password_separators_gte** | **float**| Search by password complexity separators filed as greater then or equal to input value. | [optional] [default to 0]
 **password_other_gte** | **float**| Search by password complexity other filed as greater then or equal to input value. | [optional] [default to 0]
 **password_entropy_gte** | **float**| Search by password complexity entropy filed as greater then or equal to input value. | [optional] [default to 0]
 **password_plain** | **str**| Search by credential plain password. Note: the value of &#39;passwordPlain&#39; parameter must be URL-encoded. | [optional] 
 **detected_malware** | **str**| Search by credential detected malware. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by relevance or by the object&#39;s native time in descending (latest) or ascending (earliest) order. | [optional] [default to &#39;relevance&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **float**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**SearchSchema**](SearchSchema.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

