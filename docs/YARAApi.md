# titan_client.YARAApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**yara_get**](YARAApi.md#yara_get) | **GET** /yara | Search Malware Intelligence YARA


# **yara_get**
> YARASearchResponse yara_get(yara=yara, threat_type=threat_type, threat_uid=threat_uid, malware_family=malware_family, malware_family_profile_uid=malware_family_profile_uid, confidence=confidence, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search Malware Intelligence YARA

Returns list of `YARA` matching filter criteria. Malware Intelligence is a different product from Intel 471 to adversary intelligence.

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
    api_instance = titan_client.YARAApi(api_client)
    yara = 'yara_example' # str | Free text YARA search (all fields included). At least one of `yara`, `threatType`, `threatUid`, `malwareFamily`, `malwareFamilyProfileUid` or `confidence` is required. (optional)
    threat_type = 'malware' # str | Search `YARA` by threat type (optional)
    threat_uid = 'threat_uid_example' # str | Search YARA by threat UID (optional)
    malware_family = 'malware_family_example' # str | Search YARA by malware family (e.g. `gozi_isfb`, `smokeloader`, `trickbot`) (optional)
    malware_family_profile_uid = 'malware_family_profile_uid_example' # str | Search YARA by malware family profile UID. Useful for getting context for everything we have around specific malware family, for instance https://api.intel471.com/v1/search?malwareFamilyProfileUid=d073f7352b82c1b8eedda381590adced (optional)
    confidence = 'confidence_example' # str | Search YARA by confidence. See detailed description of confidence levels below. (optional)
    gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'latest' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'latest')
    filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Malware Intelligence YARA
        api_response = api_instance.yara_get(yara=yara, threat_type=threat_type, threat_uid=threat_uid, malware_family=malware_family, malware_family_profile_uid=malware_family_profile_uid, confidence=confidence, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling YARAApi->yara_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **yara** | **str**| Free text YARA search (all fields included). At least one of &#x60;yara&#x60;, &#x60;threatType&#x60;, &#x60;threatUid&#x60;, &#x60;malwareFamily&#x60;, &#x60;malwareFamilyProfileUid&#x60; or &#x60;confidence&#x60; is required. | [optional] 
 **threat_type** | **str**| Search &#x60;YARA&#x60; by threat type | [optional] 
 **threat_uid** | **str**| Search YARA by threat UID | [optional] 
 **malware_family** | **str**| Search YARA by malware family (e.g. &#x60;gozi_isfb&#x60;, &#x60;smokeloader&#x60;, &#x60;trickbot&#x60;) | [optional] 
 **malware_family_profile_uid** | **str**| Search YARA by malware family profile UID. Useful for getting context for everything we have around specific malware family, for instance https://api.intel471.com/v1/search?malwareFamilyProfileUid&#x3D;d073f7352b82c1b8eedda381590adced | [optional] 
 **confidence** | **str**| Search YARA by confidence. See detailed description of confidence levels below. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;latest&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**YARASearchResponse**](YARASearchResponse.md)

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

