# titan_client.ReportsApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**breach_alerts_get**](ReportsApi.md#breach_alerts_get) | **GET** /breachAlerts | Search Breach Alerts
[**breach_alerts_uid_get**](ReportsApi.md#breach_alerts_uid_get) | **GET** /breachAlerts/{uid} | Get Breach Alert
[**malware_reports_get**](ReportsApi.md#malware_reports_get) | **GET** /malwareReports | Search Malware Intelligence Reports
[**malware_reports_uid_get**](ReportsApi.md#malware_reports_uid_get) | **GET** /malwareReports/{uid} | Get Malware Intelligence Report
[**reports_get**](ReportsApi.md#reports_get) | **GET** /reports | Search Reports
[**reports_uid_get**](ReportsApi.md#reports_uid_get) | **GET** /reports/{uid} | Get Report
[**situation_reports_get**](ReportsApi.md#situation_reports_get) | **GET** /situationReports | Search Situation Reports
[**situation_reports_report_uid_get**](ReportsApi.md#situation_reports_report_uid_get) | **GET** /situationReports/{reportUid} | Get Situation Report
[**spot_reports_get**](ReportsApi.md#spot_reports_get) | **GET** /spotReports | Search Spot Reports
[**spot_reports_uid_get**](ReportsApi.md#spot_reports_uid_get) | **GET** /spotReports/{uid} | Get Spot Report


# **breach_alerts_get**
> SimpleBreachAlertResponse breach_alerts_get(breach_alert=breach_alert, actor=actor, victim=victim, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search Breach Alerts

Returns list of `Breach alerts` matching filter criteria.

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
    api_instance = titan_client.ReportsApi(api_client)
    breach_alert = 'Communications' # str | Free text reports search - all fields included. At least one of `breachAlert`, `actor`, `victim` is required. (optional)
    actor = 'hakkr' # str | Search by actor or actor group names. At least one of `breachAlert`, `actor`, `victim` is required. (optional)
    victim = 'BCN Telecom' # str | Search by victim. At least one of `breachAlert`, `actor`, `victim` is required. (optional)
    gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'relevance' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'relevance')
    filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Breach Alerts
        api_response = api_instance.breach_alerts_get(breach_alert=breach_alert, actor=actor, victim=victim, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->breach_alerts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **breach_alert** | **str**| Free text reports search - all fields included. At least one of &#x60;breachAlert&#x60;, &#x60;actor&#x60;, &#x60;victim&#x60; is required. | [optional] 
 **actor** | **str**| Search by actor or actor group names. At least one of &#x60;breachAlert&#x60;, &#x60;actor&#x60;, &#x60;victim&#x60; is required. | [optional] 
 **victim** | **str**| Search by victim. At least one of &#x60;breachAlert&#x60;, &#x60;actor&#x60;, &#x60;victim&#x60; is required. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;relevance&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**SimpleBreachAlertResponse**](SimpleBreachAlertResponse.md)

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

# **breach_alerts_uid_get**
> FullBreachAlertSchema breach_alerts_uid_get(uid)

Get Breach Alert

Returns a `Breach alert` with specified id.

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
    api_instance = titan_client.ReportsApi(api_client)
    uid = '8c5e0e87e683c62bb0a50baeff732152' # str | Report identifier.

    try:
        # Get Breach Alert
        api_response = api_instance.breach_alerts_uid_get(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->breach_alerts_uid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Report identifier. | 

### Return type

[**FullBreachAlertSchema**](FullBreachAlertSchema.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **malware_reports_get**
> MalwareReportsSearchResponse malware_reports_get(malware_report=malware_report, threat_type=threat_type, report_title=report_title, malware_family=malware_family, malware_family_profile_uid=malware_family_profile_uid, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search Malware Intelligence Reports

Returns list of `Malware reports` matching filter criteria. Malware Intelligence is a different product from Intel 471 to adversary intelligence.

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
    api_instance = titan_client.ReportsApi(api_client)
    malware_report = 'malware_report_example' # str | Free text Malware reports search (all fields included). At least one of `malwareReport`, `threatType`, `reportTitle`, `malwareFamily`, 'malwareFamilyProfileUid` is required. (optional)
    threat_type = 'threat_type_example' # str | Search Malware reports by threat type (e.g. `malware`, `bulletproof_hosting`, `proxy_service`) (optional)
    report_title = 'report_title_example' # str | Search Malware reports by threat UID (optional)
    malware_family = 'malware_family_example' # str | Search Malware reports by malware family (e.g. `gozi_isfb`, `smokeloader`, `trickbot`). (optional)
    malware_family_profile_uid = 'malware_family_profile_uid_example' # str | Search Malware reports by malware family profile UID. Useful for getting context for everything we have around specific malware family, for instance https://api.intel471.com/v1/search?malwareFamilyProfileUid=20eb1f82621001883ea0c2085aff5729. (optional)
    gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'relevance' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'relevance')
    filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Malware Intelligence Reports
        api_response = api_instance.malware_reports_get(malware_report=malware_report, threat_type=threat_type, report_title=report_title, malware_family=malware_family, malware_family_profile_uid=malware_family_profile_uid, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->malware_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **malware_report** | **str**| Free text Malware reports search (all fields included). At least one of &#x60;malwareReport&#x60;, &#x60;threatType&#x60;, &#x60;reportTitle&#x60;, &#x60;malwareFamily&#x60;, &#39;malwareFamilyProfileUid&#x60; is required. | [optional] 
 **threat_type** | **str**| Search Malware reports by threat type (e.g. &#x60;malware&#x60;, &#x60;bulletproof_hosting&#x60;, &#x60;proxy_service&#x60;) | [optional] 
 **report_title** | **str**| Search Malware reports by threat UID | [optional] 
 **malware_family** | **str**| Search Malware reports by malware family (e.g. &#x60;gozi_isfb&#x60;, &#x60;smokeloader&#x60;, &#x60;trickbot&#x60;). | [optional] 
 **malware_family_profile_uid** | **str**| Search Malware reports by malware family profile UID. Useful for getting context for everything we have around specific malware family, for instance https://api.intel471.com/v1/search?malwareFamilyProfileUid&#x3D;20eb1f82621001883ea0c2085aff5729. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;relevance&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**MalwareReportsSearchResponse**](MalwareReportsSearchResponse.md)

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

# **malware_reports_uid_get**
> MalwareReportsSearchSchema malware_reports_uid_get(uid)

Get Malware Intelligence Report

Returns single Malware report with specified unique id.

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
    api_instance = titan_client.ReportsApi(api_client)
    uid = 'e7fafbb8f44a6ded005c154976627da4' # str | Report identifier.

    try:
        # Get Malware Intelligence Report
        api_response = api_instance.malware_reports_uid_get(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->malware_reports_uid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Report identifier. | 

### Return type

[**MalwareReportsSearchSchema**](MalwareReportsSearchSchema.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_get**
> SimpleReportsResponse reports_get(report=report, report_location=report_location, report_tag=report_tag, report_admiralty_code=report_admiralty_code, report_title=report_title, victim=victim, document_type=document_type, document_family=document_family, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search Reports

Returns list of [Information Reports or Fintel Reports](#tag/Reports/paths/~1reports~1{uid}/get) matching filter criteria ordered by creation date descending (the most recent are on the top). Filtering parameters combined with AND criteria and can be present multiple times in query string. In version 1.3.0 reports also include new field `actorSubjectOfReport` with actors, mentioned in report subject

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
    api_instance = titan_client.ReportsApi(api_client)
    report = ['[\"]ransomware-as-a-service\"]'] # list[str] | Search text in reports, subjects, and entities. (optional)
    report_location = 'Pakistan' # str | Country or region. (optional)
    report_tag = 'E-commerce' # str | Tag. (optional)
    report_admiralty_code = 'A6' # str | Search reports by admiralty code. (optional)
    report_title = 'ransomware' # str | Search reports by title. (optional)
    victim = 'Diagnostica' # str | Search by purported victim. (optional)
    document_type = 'document_type_example' # str | Search reports by document type. (optional)
    document_family = 'document_family_example' # str | Search reports by document family. (optional)
    gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'relevance' # str | Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order. (optional) (default to 'relevance')
    filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Reports
        api_response = api_instance.reports_get(report=report, report_location=report_location, report_tag=report_tag, report_admiralty_code=report_admiralty_code, report_title=report_title, victim=victim, document_type=document_type, document_family=document_family, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report** | [**list[str]**](str.md)| Search text in reports, subjects, and entities. | [optional] 
 **report_location** | **str**| Country or region. | [optional] 
 **report_tag** | **str**| Tag. | [optional] 
 **report_admiralty_code** | **str**| Search reports by admiralty code. | [optional] 
 **report_title** | **str**| Search reports by title. | [optional] 
 **victim** | **str**| Search by purported victim. | [optional] 
 **document_type** | **str**| Search reports by document type. | [optional] 
 **document_family** | **str**| Search reports by document family. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by relevance or by the object&#39;s native time in descending (latest) or ascending (earliest) order. | [optional] [default to &#39;relevance&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**SimpleReportsResponse**](SimpleReportsResponse.md)

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

# **reports_uid_get**
> FullReportSchema reports_uid_get(uid)

Get Report

Returns a single *Information Report* or *Fintel Report* object.

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
    api_instance = titan_client.ReportsApi(api_client)
    uid = '32537c9c6dce18ce6ea4d5106540f089' # str | Report identifier.

    try:
        # Get Report
        api_response = api_instance.reports_uid_get(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->reports_uid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Report identifier. | 

### Return type

[**FullReportSchema**](FullReportSchema.md)

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

# **situation_reports_get**
> SituationReportResponse situation_reports_get(situation_report, gir=gir, victim=victim, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search Situation Reports

Returns list of Situation reports matching filter criteria.

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
    api_instance = titan_client.ReportsApi(api_client)
    situation_report = 'situation_report_example' # str | Free text reports search (all fields included).
    gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
    victim = 'victim_example' # str | Search reports by purported victim. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'relevance' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'relevance')
    filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Situation Reports
        api_response = api_instance.situation_reports_get(situation_report, gir=gir, victim=victim, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->situation_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **situation_report** | **str**| Free text reports search (all fields included). | 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **victim** | **str**| Search reports by purported victim. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;relevance&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**SituationReportResponse**](SituationReportResponse.md)

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

# **situation_reports_report_uid_get**
> SituationReportSchema situation_reports_report_uid_get(report_uid)

Get Situation Report

Returns Situation report with specified id.

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
    api_instance = titan_client.ReportsApi(api_client)
    report_uid = '8c5e0e87e683c62bb0a50baeff732152' # str | Report identifier.

    try:
        # Get Situation Report
        api_response = api_instance.situation_reports_report_uid_get(report_uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->situation_reports_report_uid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_uid** | **str**| Report identifier. | 

### Return type

[**SituationReportSchema**](SituationReportSchema.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spot_reports_get**
> SimpleSpotReportsResponse spot_reports_get(spot_report, gir=gir, victim=victim, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search Spot Reports

Returns list of `Spot reports` matching filter criteria.

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
    api_instance = titan_client.ReportsApi(api_client)
    spot_report = 'spot_report_example' # str | Free text reports search (all fields included).
    gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
    victim = 'Diagnostica' # str | Search by purported victim. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'relevance' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'relevance')
    filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Spot Reports
        api_response = api_instance.spot_reports_get(spot_report, gir=gir, victim=victim, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->spot_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spot_report** | **str**| Free text reports search (all fields included). | 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **victim** | **str**| Search by purported victim. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;relevance&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**SimpleSpotReportsResponse**](SimpleSpotReportsResponse.md)

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

# **spot_reports_uid_get**
> FullSpotReportSchema spot_reports_uid_get(uid)

Get Spot Report

Returns list of `Spot reports` matching filter criteria.

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
    api_instance = titan_client.ReportsApi(api_client)
    uid = '8c5e0e87e683c62bb0a50baeff732152' # str | Report identifier.

    try:
        # Get Spot Report
        api_response = api_instance.spot_reports_uid_get(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->spot_reports_uid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Report identifier. | 

### Return type

[**FullSpotReportSchema**](FullSpotReportSchema.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

