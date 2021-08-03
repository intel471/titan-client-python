# titan_client.ForumsApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**posts_get**](ForumsApi.md#posts_get) | **GET** /posts | Search Forum Posts
[**private_messages_get**](ForumsApi.md#private_messages_get) | **GET** /privateMessages | Search Private Messages


# **posts_get**
> PostsResponse posts_get(post=post, posts_by_thread_uid=posts_by_thread_uid, actor=actor, forum=forum, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)

Search Forum Posts

Returns list of `Posts` matching filter criteria.

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
    api_instance = titan_client.ForumsApi(api_client)
    post = 'hacker' # str | Search text in posts and topics. (optional)
posts_by_thread_uid = '?' # str | Search posts by thread uid. At least one of `post`, `postsByThreadUid`, `forum` is required. (optional)
actor = 'armani' # str | Search posts authored by given actor handle. (optional)
forum = 'opensc.ws' # str | Search posts in a given forum. (optional)
_from = '1day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
sort = 'relevance' # str | Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order. (optional) (default to 'relevance')
offset = 0 # float | Skip leading number of records. (optional) (default to 0)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Forum Posts
        api_response = api_instance.posts_get(post=post, posts_by_thread_uid=posts_by_thread_uid, actor=actor, forum=forum, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ForumsApi->posts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post** | **str**| Search text in posts and topics. | [optional] 
 **posts_by_thread_uid** | **str**| Search posts by thread uid. At least one of &#x60;post&#x60;, &#x60;postsByThreadUid&#x60;, &#x60;forum&#x60; is required. | [optional] 
 **actor** | **str**| Search posts authored by given actor handle. | [optional] 
 **forum** | **str**| Search posts in a given forum. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by relevance or by the object&#39;s native time in descending (latest) or ascending (earliest) order. | [optional] [default to &#39;relevance&#39;]
 **offset** | **float**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**PostsResponse**](PostsResponse.md)

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

# **private_messages_get**
> PrivateMessagesResponse private_messages_get(private_message=private_message, private_message_subject=private_message_subject, actor=actor, forum=forum, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)

Search Private Messages

Returns list of `Private messages` matching filter criteria.

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
    api_instance = titan_client.ForumsApi(api_client)
    private_message = 'sell' # str | Search text in Private Messages. At least one of `privateMessage`, `privateMessageSubject`, `actor`, `forum` is required. (optional)
private_message_subject = 'sell' # str | Search text in subjects of Private Messages. (optional)
actor = 'schott' # str | Search messages authored or received by given actor handle. (optional)
forum = 'opensc.ws' # str | Search messages in a given forum. (optional)
_from = '1day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
sort = 'relevance' # str | Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order. (optional) (default to 'relevance')
offset = 0 # float | Skip leading number of records. (optional) (default to 0)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Private Messages
        api_response = api_instance.private_messages_get(private_message=private_message, private_message_subject=private_message_subject, actor=actor, forum=forum, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ForumsApi->private_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_message** | **str**| Search text in Private Messages. At least one of &#x60;privateMessage&#x60;, &#x60;privateMessageSubject&#x60;, &#x60;actor&#x60;, &#x60;forum&#x60; is required. | [optional] 
 **private_message_subject** | **str**| Search text in subjects of Private Messages. | [optional] 
 **actor** | **str**| Search messages authored or received by given actor handle. | [optional] 
 **forum** | **str**| Search messages in a given forum. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by relevance or by the object&#39;s native time in descending (latest) or ascending (earliest) order. | [optional] [default to &#39;relevance&#39;]
 **offset** | **float**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**PrivateMessagesResponse**](PrivateMessagesResponse.md)

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

