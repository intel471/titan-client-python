# titan_client.AlertsApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts_get**](AlertsApi.md#alerts_get) | **GET** /alerts | Get Alerts
[**alerts_subscriptions_delete**](AlertsApi.md#alerts_subscriptions_delete) | **DELETE** /alerts/subscriptions | Alerts - Alert Subscriptions - Delete
[**alerts_subscriptions_get**](AlertsApi.md#alerts_subscriptions_get) | **GET** /alerts/subscriptions | Alerts - Alert Subscriptions - Get
[**alerts_subscriptions_post**](AlertsApi.md#alerts_subscriptions_post) | **POST** /alerts/subscriptions | Alerts - Alert Subscriptions - Subscribe | Ping
[**alerts_subscriptions_put**](AlertsApi.md#alerts_subscriptions_put) | **PUT** /alerts/subscriptions | Alerts - Alert Subscriptions - Put


# **alerts_get**
> AlertListSchemaResponse alerts_get(_from=_from, until=until, offset=offset, watcher_group=watcher_group, count=count, show_read=show_read, display_watchers=display_watchers, mark_as_read=mark_as_read, sort=sort)

Get Alerts

Returns list of `Alerts` matching filter criteria excluding the following types: Malware reports, YARA, NIDS

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
    _from = '1day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
offset = 0 # float | Skip leading number of records. (optional) (default to 0)
watcher_group = 'watcher_group_example' # str | Show `Alerts` from specified watcher group only. Object field: watcherGroupUid. Multiple values allowed. (optional)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)
show_read = True # bool | Show read alerts. (optional) (default to True)
display_watchers = False # bool | Show watcher groups info. (optional) (default to False)
mark_as_read = False # bool | Mark displayed alerts as read. (optional) (default to False)
sort = 'relevance' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'relevance')

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
 **offset** | **float**| Skip leading number of records. | [optional] [default to 0]
 **watcher_group** | **str**| Show &#x60;Alerts&#x60; from specified watcher group only. Object field: watcherGroupUid. Multiple values allowed. | [optional] 
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]
 **show_read** | **bool**| Show read alerts. | [optional] [default to True]
 **display_watchers** | **bool**| Show watcher groups info. | [optional] [default to False]
 **mark_as_read** | **bool**| Mark displayed alerts as read. | [optional] [default to False]
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;relevance&#39;]

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

# **alerts_subscriptions_delete**
> alerts_subscriptions_delete(endpoint)

Alerts - Alert Subscriptions - Delete

Deletes registered endpoint. Data should be sent in request body in JSON format.

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
    endpoint = 'endpoint_example' # str | The endpoint url to delete

    try:
        # Alerts - Alert Subscriptions - Delete
        api_instance.alerts_subscriptions_delete(endpoint)
    except ApiException as e:
        print("Exception when calling AlertsApi->alerts_subscriptions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| The endpoint url to delete | 

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
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_subscriptions_get**
> AlertSubscriptionSubscribeResponse alerts_subscriptions_get(endpoint=endpoint, status=status)

Alerts - Alert Subscriptions - Get

Returns list of registered user's endpoints and their statuses.

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
    endpoint = 'endpoint_example' # str | The endpoint url to receive ping notifications on new alerts. (optional)
status = 'active' # str | Optionally specify status of the new endpoint (optional) (default to 'active')

    try:
        # Alerts - Alert Subscriptions - Get
        api_response = api_instance.alerts_subscriptions_get(endpoint=endpoint, status=status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertsApi->alerts_subscriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| The endpoint url to receive ping notifications on new alerts. | [optional] 
 **status** | **str**| Optionally specify status of the new endpoint | [optional] [default to &#39;active&#39;]

### Return type

[**AlertSubscriptionSubscribeResponse**](AlertSubscriptionSubscribeResponse.md)

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

# **alerts_subscriptions_post**
> AlertSubscriptionSubscribeResponse alerts_subscriptions_post(alert_subscription_schema)

Alerts - Alert Subscriptions - Subscribe | Ping

We strongly suggest to register your endpoint url to receive [ping notifications] from Intel 471 on new alerts available. Once registered, our server will send POST request to your endpoint when new alerts are fired for you. During registration our server will send a POST handshake request in JSON format with param `handshakeString` — a randomly generated string. Your endpoint should echo this response back with the same string and status 200. After this verification procedure endpoint will be registered. You can register up to 10 endpoints. <br />Handshake request example:  ```{ \"handshakeString\": \"/9fa1969e-6324-11e7-814c-0401beb96201/\" }``` <br />Example python client with ping subscription you can download here: [intel471_alert_api_client_example.py](https://titan.intel471.com/api/docs/intel471_alert_api_client_example.py) <br /><h3>Alert Subscriptions - Ping</h3> When new alerts are fired, Intel 471 API will send a POST request to all of a user's `active` endpoints. Endpoints should reply with HTTP status 200 OK. If there is no answer received from endpoint or connection with endpoint could not be established, Intel 471 API will try to ping endpoint with increasing frequency up to 24 hours. If endpoint still does not reply after that period, its status will be changed to suspended and no more requests will be sent. To enable this endpoint again, user should fix issues and change status back to active as described in section Alert subscriptions — put. <br />Ping request example: <br />```{ \"newAlertsAvailable\": true }``` <br />Example python client with ping subscription you can download here: [intel471_alert_api_client_example.py](https://titan.intel471.com/api/docs/intel471_alert_api_client_example.py) <br /> 

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
    alert_subscription_schema = titan_client.AlertSubscriptionSchema() # AlertSubscriptionSchema | 

    try:
        # Alerts - Alert Subscriptions - Subscribe | Ping
        api_response = api_instance.alerts_subscriptions_post(alert_subscription_schema)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertsApi->alerts_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_subscription_schema** | [**AlertSubscriptionSchema**](AlertSubscriptionSchema.md)|  | 

### Return type

[**AlertSubscriptionSubscribeResponse**](AlertSubscriptionSubscribeResponse.md)

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

# **alerts_subscriptions_put**
> AlertSubscriptionSubscribeResponse alerts_subscriptions_put(alert_subscription_schema)

Alerts - Alert Subscriptions - Put

Updates status of `endpoint` url. Status should be `active` or `inactive`. Data should be sent in request body in JSON format.

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
    alert_subscription_schema = titan_client.AlertSubscriptionSchema() # AlertSubscriptionSchema | 

    try:
        # Alerts - Alert Subscriptions - Put
        api_response = api_instance.alerts_subscriptions_put(alert_subscription_schema)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertsApi->alerts_subscriptions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_subscription_schema** | [**AlertSubscriptionSchema**](AlertSubscriptionSchema.md)|  | 

### Return type

[**AlertSubscriptionSubscribeResponse**](AlertSubscriptionSubscribeResponse.md)

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

