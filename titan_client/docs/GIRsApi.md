# titan_client.GIRsApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**girs_get**](GIRsApi.md#girs_get) | **GET** /girs | Search GIRs


# **girs_get**
> GirsResponse girs_get(gir_path=gir_path, gir_name=gir_name, gir_description=gir_description, offset=offset, count=count)

Search GIRs

Returns list of General Intelligence Requirements matching filter criteria.

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
    api_instance = titan_client.GIRsApi(api_client)
    gir_path = '1.1.1' # str | Search GIRs by path. (optional)
    gir_name = 'Ransomware malware' # str | Search GIRs by name (optional)
    gir_description = 'unauthorized' # str | Search GIRs description (optional)
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search GIRs
        api_response = api_instance.girs_get(gir_path=gir_path, gir_name=gir_name, gir_description=gir_description, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GIRsApi->girs_get: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gir_path** | **str**| Search GIRs by path. | [optional] 
 **gir_name** | **str**| Search GIRs by name | [optional] 
 **gir_description** | **str**| Search GIRs description | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**GirsResponse**](GirsResponse.md)

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

