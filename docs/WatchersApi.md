# titan_client.WatchersApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**watcher_groups_get**](WatchersApi.md#watcher_groups_get) | **GET** /watcherGroups | Get Watcher Group List
[**watcher_groups_group_uid_delete**](WatchersApi.md#watcher_groups_group_uid_delete) | **DELETE** /watcherGroups/{group-uid} | Delete Watcher Group
[**watcher_groups_group_uid_get**](WatchersApi.md#watcher_groups_group_uid_get) | **GET** /watcherGroups/{group-uid} | Get Watcher Group
[**watcher_groups_group_uid_put**](WatchersApi.md#watcher_groups_group_uid_put) | **PUT** /watcherGroups/{group-uid} | Put Watcher Group
[**watcher_groups_group_uid_watchers_get**](WatchersApi.md#watcher_groups_group_uid_watchers_get) | **GET** /watcherGroups/{group-uid}/watchers | Get Watchers list
[**watcher_groups_group_uid_watchers_post**](WatchersApi.md#watcher_groups_group_uid_watchers_post) | **POST** /watcherGroups/{group-uid}/watchers | Create Watcher
[**watcher_groups_group_uid_watchers_watcher_uid_delete**](WatchersApi.md#watcher_groups_group_uid_watchers_watcher_uid_delete) | **DELETE** /watcherGroups/{group-uid}/watchers/{watcher-uid} | Delete Watcher
[**watcher_groups_group_uid_watchers_watcher_uid_get**](WatchersApi.md#watcher_groups_group_uid_watchers_watcher_uid_get) | **GET** /watcherGroups/{group-uid}/watchers/{watcher-uid} | Get Watcher
[**watcher_groups_group_uid_watchers_watcher_uid_put**](WatchersApi.md#watcher_groups_group_uid_watchers_watcher_uid_put) | **PUT** /watcherGroups/{group-uid}/watchers/{watcher-uid} | Put Watcher
[**watcher_groups_post**](WatchersApi.md#watcher_groups_post) | **POST** /watcherGroups | Create Watcher Group


# **watcher_groups_get**
> WatcherGroupResponse watcher_groups_get(section=section)

Get Watcher Group List

Returns list of Watcher groups matching filter criteria.

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
    api_instance = titan_client.WatchersApi(api_client)
    section = 'section_example' # str | Shows watcher groups from defined section. (optional)

    try:
        # Get Watcher Group List
        api_response = api_instance.watcher_groups_get(section=section)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WatchersApi->watcher_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section** | **str**| Shows watcher groups from defined section. | [optional] 

### Return type

[**WatcherGroupResponse**](WatcherGroupResponse.md)

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

# **watcher_groups_group_uid_delete**
> watcher_groups_group_uid_delete(group_uid)

Delete Watcher Group

Delete defined watcher group. Only groups of type owned_by_me are allowed to be deleted.

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
    api_instance = titan_client.WatchersApi(api_client)
    group_uid = '5e375ff0-7f0d-4703-83de-d2fea5620335' # str | Watcher group identifier.

    try:
        # Delete Watcher Group
        api_instance.watcher_groups_group_uid_delete(group_uid)
    except ApiException as e:
        print("Exception when calling WatchersApi->watcher_groups_group_uid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uid** | **str**| Watcher group identifier. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watcher_groups_group_uid_get**
> SimpleWatcherGroupSchema watcher_groups_group_uid_get(group_uid)

Get Watcher Group

Get a watcher group by UID.

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
    api_instance = titan_client.WatchersApi(api_client)
    group_uid = '5e375ff0-7f0d-4703-83de-d2fea5620335' # str | Watcher group identifier.

    try:
        # Get Watcher Group
        api_response = api_instance.watcher_groups_group_uid_get(group_uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WatchersApi->watcher_groups_group_uid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uid** | **str**| Watcher group identifier. | 

### Return type

[**SimpleWatcherGroupSchema**](SimpleWatcherGroupSchema.md)

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

# **watcher_groups_group_uid_put**
> SimpleWatcherGroupSchema watcher_groups_group_uid_put(group_uid, inline_object1)

Put Watcher Group

Update watcher group's name or description. Only groups of type `owned_by_me` are allowed to be updated.

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
    api_instance = titan_client.WatchersApi(api_client)
    group_uid = '5e375ff0-7f0d-4703-83de-d2fea5620335' # str | Watcher group identifier.
    inline_object1 = titan_client.InlineObject1() # InlineObject1 | 

    try:
        # Put Watcher Group
        api_response = api_instance.watcher_groups_group_uid_put(group_uid, inline_object1)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WatchersApi->watcher_groups_group_uid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uid** | **str**| Watcher group identifier. | 
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | 

### Return type

[**SimpleWatcherGroupSchema**](SimpleWatcherGroupSchema.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watcher_groups_group_uid_watchers_get**
> WatcherSchemaResponse watcher_groups_group_uid_watchers_get(group_uid)

Get Watchers list

Returns list of `Watchers` of a given Watcher group.

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
    api_instance = titan_client.WatchersApi(api_client)
    group_uid = '5e375ff0-7f0d-4703-83de-d2fea5620335' # str | Watcher group identifier.

    try:
        # Get Watchers list
        api_response = api_instance.watcher_groups_group_uid_watchers_get(group_uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WatchersApi->watcher_groups_group_uid_watchers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uid** | **str**| Watcher group identifier. | 

### Return type

[**WatcherSchemaResponse**](WatcherSchemaResponse.md)

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

# **watcher_groups_group_uid_watchers_post**
> WatcherSchema watcher_groups_group_uid_watchers_post(group_uid, watcher_request_body_post)

Create Watcher

Create new watcher in a given Watcher group from a json object supplied in request body

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
    api_instance = titan_client.WatchersApi(api_client)
    group_uid = '5e375ff0-7f0d-4703-83de-d2fea5620335' # str | Watcher group identifier.
    watcher_request_body_post = titan_client.WatcherRequestBodyPost() # WatcherRequestBodyPost | JSON request body

    try:
        # Create Watcher
        api_response = api_instance.watcher_groups_group_uid_watchers_post(group_uid, watcher_request_body_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WatchersApi->watcher_groups_group_uid_watchers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uid** | **str**| Watcher group identifier. | 
 **watcher_request_body_post** | [**WatcherRequestBodyPost**](WatcherRequestBodyPost.md)| JSON request body | 

### Return type

[**WatcherSchema**](WatcherSchema.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watcher_groups_group_uid_watchers_watcher_uid_delete**
> watcher_groups_group_uid_watchers_watcher_uid_delete(watcher_uid, group_uid)

Delete Watcher

Delete a given watcher in a given watcher group specified by watcher-uid and group-uid parameters. Confirmed with \"No Content\" response.

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
    api_instance = titan_client.WatchersApi(api_client)
    watcher_uid = '8f16dc64d43ae2492f0ecd052c05599e' # str | Unique identifier of watcher.
    group_uid = '5e375ff0-7f0d-4703-83de-d2fea5620335' # str | Watcher group identifier.

    try:
        # Delete Watcher
        api_instance.watcher_groups_group_uid_watchers_watcher_uid_delete(watcher_uid, group_uid)
    except ApiException as e:
        print("Exception when calling WatchersApi->watcher_groups_group_uid_watchers_watcher_uid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watcher_uid** | **str**| Unique identifier of watcher. | 
 **group_uid** | **str**| Watcher group identifier. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watcher_groups_group_uid_watchers_watcher_uid_get**
> WatcherSchema watcher_groups_group_uid_watchers_watcher_uid_get(watcher_uid, group_uid)

Get Watcher

Get single Watcher from given Watcher group.

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
    api_instance = titan_client.WatchersApi(api_client)
    watcher_uid = '8f16dc64d43ae2492f0ecd052c05599e' # str | Unique identifier of watcher.
    group_uid = '5e375ff0-7f0d-4703-83de-d2fea5620335' # str | Watcher group identifier.

    try:
        # Get Watcher
        api_response = api_instance.watcher_groups_group_uid_watchers_watcher_uid_get(watcher_uid, group_uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WatchersApi->watcher_groups_group_uid_watchers_watcher_uid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watcher_uid** | **str**| Unique identifier of watcher. | 
 **group_uid** | **str**| Watcher group identifier. | 

### Return type

[**WatcherSchema**](WatcherSchema.md)

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

# **watcher_groups_group_uid_watchers_watcher_uid_put**
> WatcherSchema watcher_groups_group_uid_watchers_watcher_uid_put(watcher_uid, group_uid, watcher_request_body_put)

Put Watcher

Editing of existing watcher in a given Watcher group from a json object supplied in request body. Whole watcher body should be supplied

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
    api_instance = titan_client.WatchersApi(api_client)
    watcher_uid = '8f16dc64d43ae2492f0ecd052c05599e' # str | Unique identifier of watcher.
    group_uid = '5e375ff0-7f0d-4703-83de-d2fea5620335' # str | Watcher group identifier.
    watcher_request_body_put = titan_client.WatcherRequestBodyPut() # WatcherRequestBodyPut | JSON request body

    try:
        # Put Watcher
        api_response = api_instance.watcher_groups_group_uid_watchers_watcher_uid_put(watcher_uid, group_uid, watcher_request_body_put)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WatchersApi->watcher_groups_group_uid_watchers_watcher_uid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watcher_uid** | **str**| Unique identifier of watcher. | 
 **group_uid** | **str**| Watcher group identifier. | 
 **watcher_request_body_put** | [**WatcherRequestBodyPut**](WatcherRequestBodyPut.md)| JSON request body | 

### Return type

[**WatcherSchema**](WatcherSchema.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watcher_groups_post**
> SimpleWatcherGroupSchema watcher_groups_post(inline_object)

Create Watcher Group

Create watcher group from json object supplied in a request body which contains name and description

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
    api_instance = titan_client.WatchersApi(api_client)
    inline_object = titan_client.InlineObject() # InlineObject | 

    try:
        # Create Watcher Group
        api_response = api_instance.watcher_groups_post(inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WatchersApi->watcher_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | 

### Return type

[**SimpleWatcherGroupSchema**](SimpleWatcherGroupSchema.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

