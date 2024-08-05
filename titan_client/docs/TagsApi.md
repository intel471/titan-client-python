# titan_client.TagsApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_get**](TagsApi.md#tags_get) | **GET** /tags | Get Tag List


# **tags_get**
> TagResponse tags_get(used=used)

Get Tag List

Returns list of tags ordered by alphabet. Filtering parameter either displays full list of tags or filters out used tags with `use_count` > 0

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import os
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
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with titan_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = titan_client.TagsApi(api_client)
    used = True # bool | If present displays only used tags with `use_count` > 0. (optional)

    try:
        # Get Tag List
        api_response = api_instance.tags_get(used=used)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->tags_get: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **used** | **bool**| If present displays only used tags with &#x60;use_count&#x60; &gt; 0. | [optional] 

### Return type

[**TagResponse**](TagResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

