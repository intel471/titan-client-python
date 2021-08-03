# titan_client.PCAPApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**malware_pcaps_get**](PCAPApi.md#malware_pcaps_get) | **GET** /malware/pcaps | List of files


# **malware_pcaps_get**
> PCAPResponse malware_pcaps_get(malware_family=malware_family, malware_family_profile_uid=malware_family_profile_uid, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)

List of files

Returns a list of JSON documents. Document contains all relevant data like date, exit country, file download url. Endpoint allows to consume files on a daily basis (by specifying `lastUpdatedFrom=<the last request time>`) or full historical information (by specifying `from`/`until` range). 

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
    api_instance = titan_client.PCAPApi(api_client)
    malware_family = 'dridex' # str | Filter by malware family name. To get information about all malware families provide `*` as a value. At least one of `malwareFamily`, `malwareFamilyProfileUid` parameter is required. (optional)
malware_family_profile_uid = 'b38ef686caf0103866339452d3d1c4fb' # str | Filter by malware family profile uid.. (optional)
_from = '1day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
sort = 'relevance' # str | Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order. (optional) (default to 'relevance')
offset = 0 # float | Skip leading number of records. (optional) (default to 0)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # List of files
        api_response = api_instance.malware_pcaps_get(malware_family=malware_family, malware_family_profile_uid=malware_family_profile_uid, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PCAPApi->malware_pcaps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **malware_family** | **str**| Filter by malware family name. To get information about all malware families provide &#x60;*&#x60; as a value. At least one of &#x60;malwareFamily&#x60;, &#x60;malwareFamilyProfileUid&#x60; parameter is required. | [optional] 
 **malware_family_profile_uid** | **str**| Filter by malware family profile uid.. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by relevance or by the object&#39;s native time in descending (latest) or ascending (earliest) order. | [optional] [default to &#39;relevance&#39;]
 **offset** | **float**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**PCAPResponse**](PCAPResponse.md)

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

