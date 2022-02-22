# titan_client.AlertsApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts_get**](AlertsApi.md#alerts_get) | **GET** /alerts | Get Alerts


# **alerts_get**
> AlertListSchemaResponse alerts_get(_from=_from, until=until, offset=offset, watcher_group=watcher_group, count=count, show_read=show_read, display_watchers=display_watchers, mark_as_read=mark_as_read, sort=sort)

Get Alerts

Returns list of `Alerts` matching filter criteria excluding the following types: Malware reports, YARA

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
    api_instance = titan_client.AlertsApi(api_client)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    watcher_group = 'watcher_group_example' # str | Show `Alerts` from specified watcher group only. Object field: watcherGroupUid. Multiple values allowed. (optional)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)
    show_read = True # bool | Show read alerts. (optional) (default to True)
    display_watchers = False # bool | Show watcher groups info. (optional) (default to False)
    mark_as_read = False # bool | Mark displayed alerts as read. (optional) (default to False)
    sort = 'latest' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'latest')

    try:
        # Get Alerts
        api_response = api_instance.alerts_get(_from=_from, until=until, offset=offset, watcher_group=watcher_group, count=count, show_read=show_read, display_watchers=display_watchers, mark_as_read=mark_as_read, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertsApi->alerts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **watcher_group** | **str**| Show &#x60;Alerts&#x60; from specified watcher group only. Object field: watcherGroupUid. Multiple values allowed. | [optional] 
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]
 **show_read** | **bool**| Show read alerts. | [optional] [default to True]
 **display_watchers** | **bool**| Show watcher groups info. | [optional] [default to False]
 **mark_as_read** | **bool**| Mark displayed alerts as read. | [optional] [default to False]
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;latest&#39;]

### Return type

[**AlertListSchemaResponse**](AlertListSchemaResponse.md)

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

