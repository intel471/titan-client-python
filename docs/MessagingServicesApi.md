# titan_client.MessagingServicesApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messaging_services_instant_messages_get**](MessagingServicesApi.md#messaging_services_instant_messages_get) | **GET** /messagingServices/instantMessages | Search Instant Messages


# **messaging_services_instant_messages_get**
> MessagingServicesResponse messaging_services_instant_messages_get(instant_message=instant_message, instant_message_actor=instant_message_actor, instant_message_service=instant_message_service, instant_message_server=instant_message_server, instant_message_channel=instant_message_channel, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)

Search Instant Messages

Returns list of `Instant messages` matching filter criteria.

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
    api_instance = titan_client.MessagingServicesApi(api_client)
    instant_message = 'credit card' # str | Free text instant messages search (including images via OCR). At least one of `instantMessage`, `instantMessageActor`, `instantMessageService`, `instantMessageServer`, `instantMessageChannel` is required. (optional)
    instant_message_actor = 'Synthx' # str | Search instant messages by actor name (actual for the moment message was written). (optional)
    instant_message_service = 'telegram' # str | Search instant messages by service. (optional)
    instant_message_server = '?' # str | Search instant messages by server. (optional)
    instant_message_channel = 'anon-ops' # str | Search instant messages by channel. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    var_from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'latest' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'latest')
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Instant Messages
        api_response = api_instance.messaging_services_instant_messages_get(instant_message=instant_message, instant_message_actor=instant_message_actor, instant_message_service=instant_message_service, instant_message_server=instant_message_server, instant_message_channel=instant_message_channel, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagingServicesApi->messaging_services_instant_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instant_message** | **str**| Free text instant messages search (including images via OCR). At least one of &#x60;instantMessage&#x60;, &#x60;instantMessageActor&#x60;, &#x60;instantMessageService&#x60;, &#x60;instantMessageServer&#x60;, &#x60;instantMessageChannel&#x60; is required. | [optional] 
 **instant_message_actor** | **str**| Search instant messages by actor name (actual for the moment message was written). | [optional] 
 **instant_message_service** | **str**| Search instant messages by service. | [optional] 
 **instant_message_server** | **str**| Search instant messages by server. | [optional] 
 **instant_message_channel** | **str**| Search instant messages by channel. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **var_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;latest&#39;]
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**MessagingServicesResponse**](MessagingServicesResponse.md)

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

