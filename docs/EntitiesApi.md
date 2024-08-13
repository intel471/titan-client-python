# titan_client.EntitiesApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entities_get**](EntitiesApi.md#entities_get) | **GET** /entities | Search Entities.


# **entities_get**
> EntitiesResponse entities_get(entity, entity_type=entity_type, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)

Search Entities.

Returns list of `Entities` matching filter criteria.

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
    api_instance = titan_client.EntitiesApi(api_client)
    entity = 'syntax' # str | Search for all entities.
    entity_type = 'EmailAddress' # str | Search for all entities by entity type. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    var_from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'relevance' # str | Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order. (optional) (default to 'relevance')
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Entities.
        api_response = api_instance.entities_get(entity, entity_type=entity_type, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EntitiesApi->entities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| Search for all entities. | 
 **entity_type** | **str**| Search for all entities by entity type. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **var_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by relevance or by the object&#39;s native time in descending (latest) or ascending (earliest) order. | [optional] [default to &#39;relevance&#39;]
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**EntitiesResponse**](EntitiesResponse.md)

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

