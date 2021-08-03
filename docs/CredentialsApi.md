# titan_client.CredentialsApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credential_sets_accessed_urls_get**](CredentialsApi.md#credential_sets_accessed_urls_get) | **GET** /credentialSets/accessedUrls | Search credential set accessed urls
[**credential_sets_accessed_urls_stream_get**](CredentialsApi.md#credential_sets_accessed_urls_stream_get) | **GET** /credentialSets/accessedUrls/stream | Credential set accessed url stream
[**credential_sets_get**](CredentialsApi.md#credential_sets_get) | **GET** /credentialSets | Search credential sets
[**credential_sets_stream_get**](CredentialsApi.md#credential_sets_stream_get) | **GET** /credentialSets/stream | Credential set stream
[**credentials_accessed_urls_get**](CredentialsApi.md#credentials_accessed_urls_get) | **GET** /credentials/accessedUrls | Search credential accessed urls
[**credentials_accessed_urls_stream_get**](CredentialsApi.md#credentials_accessed_urls_stream_get) | **GET** /credentials/accessedUrls/stream | Credential accessed url stream
[**credentials_get**](CredentialsApi.md#credentials_get) | **GET** /credentials | Search credentials
[**credentials_occurrences_get**](CredentialsApi.md#credentials_occurrences_get) | **GET** /credentials/occurrences | Search credential occurrences
[**credentials_occurrences_stream_get**](CredentialsApi.md#credentials_occurrences_stream_get) | **GET** /credentials/occurrences/stream | Credential occurrence stream
[**credentials_stream_get**](CredentialsApi.md#credentials_stream_get) | **GET** /credentials/stream | Credential stream


# **credential_sets_accessed_urls_get**
> CredentialSetsAccessedUrlsResponse credential_sets_accessed_urls_get(text=text, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, accessed_url=accessed_url, gir=gir, victim=victim, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search credential set accessed urls

Returns list of `Credential set accessed urls` matching filter criteria.

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
    api_instance = titan_client.CredentialsApi(api_client)
    text = 'text_example' # str | Search text everywhere in credential sets accessed urls. (optional)
credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
credential_set_uid = 'credential_set_uid_example' # str | Search by credential set uid. (optional)
accessed_url = 'accessed_url_example' # str | Search by accessed url. (optional)
gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
victim = 'Diagnostica' # str | Search by purported victim. (optional)
_from = '1day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
sort = 'relevance' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'relevance')
filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
offset = 0 # int | Skip leading number of records. (optional) (default to 0)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search credential set accessed urls
        api_response = api_instance.credential_sets_accessed_urls_get(text=text, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, accessed_url=accessed_url, gir=gir, victim=victim, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CredentialsApi->credential_sets_accessed_urls_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Search text everywhere in credential sets accessed urls. | [optional] 
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **credential_set_uid** | **str**| Search by credential set uid. | [optional] 
 **accessed_url** | **str**| Search by accessed url. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **victim** | **str**| Search by purported victim. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;relevance&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**CredentialSetsAccessedUrlsResponse**](CredentialSetsAccessedUrlsResponse.md)

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

# **credential_sets_accessed_urls_stream_get**
> CredentialSetsAccessedUrlsStreamResponse credential_sets_accessed_urls_stream_get(text=text, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, accessed_url=accessed_url, gir=gir, victim=victim, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, cursor=cursor, filter_by_gir_set=filter_by_gir_set, count=count)

Credential set accessed url stream

Returns list of `Credential set accessed urls` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `credentialsets/accessedurls` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.

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
    api_instance = titan_client.CredentialsApi(api_client)
    text = 'text_example' # str | Search text everywhere in credential sets accessed urls. (optional)
credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
credential_set_uid = 'credential_set_uid_example' # str | Search by credential set uid. (optional)
accessed_url = 'accessed_url_example' # str | Search by accessed url. (optional)
gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
victim = 'Diagnostica' # str | Search by purported victim. (optional)
_from = '1569314472407' # str | Long unix time. Search data starting from given creation time (including). (optional)
until = '1569314472407' # str | Long unix time. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1569314472407' # str | Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1569314472407' # str | Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
cursor = 'cursor_example' # str | Continue scrolling from cursor. (optional)
filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Credential set accessed url stream
        api_response = api_instance.credential_sets_accessed_urls_stream_get(text=text, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, accessed_url=accessed_url, gir=gir, victim=victim, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, cursor=cursor, filter_by_gir_set=filter_by_gir_set, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CredentialsApi->credential_sets_accessed_urls_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Search text everywhere in credential sets accessed urls. | [optional] 
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **credential_set_uid** | **str**| Search by credential set uid. | [optional] 
 **accessed_url** | **str**| Search by accessed url. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **victim** | **str**| Search by purported victim. | [optional] 
 **_from** | **str**| Long unix time. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **cursor** | **str**| Continue scrolling from cursor. | [optional] 
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**CredentialSetsAccessedUrlsStreamResponse**](CredentialSetsAccessedUrlsStreamResponse.md)

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

# **credential_sets_get**
> CredentialSetsResponse credential_sets_get(text=text, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, gir=gir, victim=victim, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search credential sets

Returns list of `Credential sets` matching filter criteria.

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
    api_instance = titan_client.CredentialsApi(api_client)
    text = 'text_example' # str | Search text everywhere in credential sets. (optional)
credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
credential_set_uid = 'credential_set_uid_example' # str | Search by credential set uid. (optional)
gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
victim = 'Diagnostica' # str | Search by purported victim. (optional)
_from = '1day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
sort = 'relevance' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'relevance')
filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
offset = 0 # int | Skip leading number of records. (optional) (default to 0)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search credential sets
        api_response = api_instance.credential_sets_get(text=text, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, gir=gir, victim=victim, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CredentialsApi->credential_sets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Search text everywhere in credential sets. | [optional] 
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **credential_set_uid** | **str**| Search by credential set uid. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **victim** | **str**| Search by purported victim. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;relevance&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**CredentialSetsResponse**](CredentialSetsResponse.md)

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

# **credential_sets_stream_get**
> CredentialSetsStreamResponse credential_sets_stream_get(text=text, credential_set_name=credential_set_name, gir=gir, victim=victim, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, cursor=cursor, filter_by_gir_set=filter_by_gir_set, count=count)

Credential set stream

Returns list of `Credential sets` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/credentialsets` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.

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
    api_instance = titan_client.CredentialsApi(api_client)
    text = 'text_example' # str | Search text everywhere in credential sets. (optional)
credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
victim = 'Diagnostica' # str | Search by purported victim. (optional)
_from = '1569314472407' # str | Long unix time. Search data starting from given creation time (including). (optional)
until = '1569314472407' # str | Long unix time. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1569314472407' # str | Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1569314472407' # str | Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
cursor = 'cursor_example' # str | Continue scrolling from cursor. (optional)
filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Credential set stream
        api_response = api_instance.credential_sets_stream_get(text=text, credential_set_name=credential_set_name, gir=gir, victim=victim, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, cursor=cursor, filter_by_gir_set=filter_by_gir_set, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CredentialsApi->credential_sets_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Search text everywhere in credential sets. | [optional] 
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **victim** | **str**| Search by purported victim. | [optional] 
 **_from** | **str**| Long unix time. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **cursor** | **str**| Continue scrolling from cursor. | [optional] 
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**CredentialSetsStreamResponse**](CredentialSetsStreamResponse.md)

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

# **credentials_accessed_urls_get**
> CredentialAccessedUrlsResponse credentials_accessed_urls_get(text=text, credential_uid=credential_uid, accessed_url=accessed_url, domain=domain, affiliation_group=affiliation_group, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search credential accessed urls

Returns list of `Credential accessed urls` matching filter criteria.

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
    api_instance = titan_client.CredentialsApi(api_client)
    text = 'text_example' # str | Search text everywhere in credentials. (optional)
credential_uid = 'credential_uid_example' # str | Search by credential uid. (optional)
accessed_url = 'accessed_url_example' # str | Search by accessed url. (optional)
domain = 'domain_example' # str | Search by credential domain (detection domain). (optional)
affiliation_group = 'affiliation_group_example' # str | Search by credential affiliation group. (optional)
gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
_from = '1day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
sort = 'relevance' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'relevance')
filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
offset = 0 # int | Skip leading number of records. (optional) (default to 0)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search credential accessed urls
        api_response = api_instance.credentials_accessed_urls_get(text=text, credential_uid=credential_uid, accessed_url=accessed_url, domain=domain, affiliation_group=affiliation_group, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CredentialsApi->credentials_accessed_urls_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Search text everywhere in credentials. | [optional] 
 **credential_uid** | **str**| Search by credential uid. | [optional] 
 **accessed_url** | **str**| Search by accessed url. | [optional] 
 **domain** | **str**| Search by credential domain (detection domain). | [optional] 
 **affiliation_group** | **str**| Search by credential affiliation group. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;relevance&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**CredentialAccessedUrlsResponse**](CredentialAccessedUrlsResponse.md)

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

# **credentials_accessed_urls_stream_get**
> CredentialAccessedUrlsStreamResponse credentials_accessed_urls_stream_get(text=text, credential_uid=credential_uid, accessed_url=accessed_url, domain=domain, affiliation_group=affiliation_group, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, cursor=cursor, filter_by_gir_set=filter_by_gir_set, count=count)

Credential accessed url stream

Returns list of `Credential accessed urls` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/credentials/accessedurls` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.

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
    api_instance = titan_client.CredentialsApi(api_client)
    text = 'text_example' # str | Search text everywhere in credentials. (optional)
credential_uid = 'credential_uid_example' # str | Search by credential uid. (optional)
accessed_url = 'accessed_url_example' # str | Search by accessed url. (optional)
domain = 'domain_example' # str | Search by credential domain (detection domain). (optional)
affiliation_group = 'affiliation_group_example' # str | Search by credential affiliation group. (optional)
gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
_from = '1569314472407' # str | Long unix time. Search data starting from given creation time (including). (optional)
until = '1569314472407' # str | Long unix time. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1569314472407' # str | Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1569314472407' # str | Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
cursor = 'cursor_example' # str | Continue scrolling from cursor. (optional)
filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Credential accessed url stream
        api_response = api_instance.credentials_accessed_urls_stream_get(text=text, credential_uid=credential_uid, accessed_url=accessed_url, domain=domain, affiliation_group=affiliation_group, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, cursor=cursor, filter_by_gir_set=filter_by_gir_set, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CredentialsApi->credentials_accessed_urls_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Search text everywhere in credentials. | [optional] 
 **credential_uid** | **str**| Search by credential uid. | [optional] 
 **accessed_url** | **str**| Search by accessed url. | [optional] 
 **domain** | **str**| Search by credential domain (detection domain). | [optional] 
 **affiliation_group** | **str**| Search by credential affiliation group. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **_from** | **str**| Long unix time. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **cursor** | **str**| Continue scrolling from cursor. | [optional] 
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**CredentialAccessedUrlsStreamResponse**](CredentialAccessedUrlsStreamResponse.md)

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

# **credentials_get**
> CredentialsResponse credentials_get(text=text, credential_uid=credential_uid, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, credential_login=credential_login, detected_malware=detected_malware, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search credentials

Returns list of `Credentials` matching filter criteria.

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
    api_instance = titan_client.CredentialsApi(api_client)
    text = 'text_example' # str | Search text everywhere in credentials. (optional)
credential_uid = 'credential_uid_example' # str | Search by credential uid. (optional)
credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
credential_set_uid = 'credential_set_uid_example' # str | Search by credential set uid. (optional)
domain = 'domain_example' # str | Search by credential domain (detection domain). (optional)
affiliation_group = 'affiliation_group_example' # str | Search by credential affiliation group. (optional)
password_strength = 'password_strength_example' # str | Search by password strength. (optional)
password_length_gte = 0 # float | Search by password complexity length field as greater then or equal to input value. (optional) (default to 0)
password_lowercase_gte = 0 # float | Search by password complexity lowercase filed as greater then or equal to input value. (optional) (default to 0)
password_uppercase_gte = 0 # float | Search by password complexity uppercase filed as greater then or equal to input value. (optional) (default to 0)
password_numbers_gte = 0 # float | Search by password complexity numbers filed as greater then or equal to input value. (optional) (default to 0)
password_punctuation_gte = 0 # float | Search by password complexity punctuation filed as greater then or equal to input value. (optional) (default to 0)
password_symbols_gte = 0 # float | Search by password complexity symbols filed as greater then or equal to input value. (optional) (default to 0)
password_separators_gte = 0 # float | Search by password complexity separators filed as greater then or equal to input value. (optional) (default to 0)
password_other_gte = 0 # float | Search by password complexity other filed as greater then or equal to input value. (optional) (default to 0)
password_entropy_gte = 0 # float | Search by password complexity entropy filed as greater then or equal to input value. (optional) (default to 0)
password_plain = 'password_plain_example' # str | Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded. (optional)
credential_login = 'credential_login_example' # str | Search by credential login. (optional)
detected_malware = 'detected_malware_example' # str | Search by credential detected malware. (optional)
gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
_from = '1day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
sort = 'relevance' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'relevance')
filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
offset = 0 # int | Skip leading number of records. (optional) (default to 0)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search credentials
        api_response = api_instance.credentials_get(text=text, credential_uid=credential_uid, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, credential_login=credential_login, detected_malware=detected_malware, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CredentialsApi->credentials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Search text everywhere in credentials. | [optional] 
 **credential_uid** | **str**| Search by credential uid. | [optional] 
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **credential_set_uid** | **str**| Search by credential set uid. | [optional] 
 **domain** | **str**| Search by credential domain (detection domain). | [optional] 
 **affiliation_group** | **str**| Search by credential affiliation group. | [optional] 
 **password_strength** | **str**| Search by password strength. | [optional] 
 **password_length_gte** | **float**| Search by password complexity length field as greater then or equal to input value. | [optional] [default to 0]
 **password_lowercase_gte** | **float**| Search by password complexity lowercase filed as greater then or equal to input value. | [optional] [default to 0]
 **password_uppercase_gte** | **float**| Search by password complexity uppercase filed as greater then or equal to input value. | [optional] [default to 0]
 **password_numbers_gte** | **float**| Search by password complexity numbers filed as greater then or equal to input value. | [optional] [default to 0]
 **password_punctuation_gte** | **float**| Search by password complexity punctuation filed as greater then or equal to input value. | [optional] [default to 0]
 **password_symbols_gte** | **float**| Search by password complexity symbols filed as greater then or equal to input value. | [optional] [default to 0]
 **password_separators_gte** | **float**| Search by password complexity separators filed as greater then or equal to input value. | [optional] [default to 0]
 **password_other_gte** | **float**| Search by password complexity other filed as greater then or equal to input value. | [optional] [default to 0]
 **password_entropy_gte** | **float**| Search by password complexity entropy filed as greater then or equal to input value. | [optional] [default to 0]
 **password_plain** | **str**| Search by credential plain password. Note: the value of &#39;passwordPlain&#39; parameter must be URL-encoded. | [optional] 
 **credential_login** | **str**| Search by credential login. | [optional] 
 **detected_malware** | **str**| Search by credential detected malware. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;relevance&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**CredentialsResponse**](CredentialsResponse.md)

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

# **credentials_occurrences_get**
> CredentialOccurrencesResponse credentials_occurrences_get(text=text, credential_occurrence_uid=credential_occurrence_uid, credential_uid=credential_uid, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, credential_login=credential_login, detected_malware=detected_malware, accessed_url=accessed_url, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search credential occurrences

Returns list of `Credential occurrences` matching filter criteria.

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
    api_instance = titan_client.CredentialsApi(api_client)
    text = 'text_example' # str | Search text everywhere in credential occurrences. (optional)
credential_occurrence_uid = 'credential_occurrence_uid_example' # str | Search by credential occurrence uid. (optional)
credential_uid = 'credential_uid_example' # str | Search by credential uid. (optional)
credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
credential_set_uid = 'credential_set_uid_example' # str | Search by credential set uid. (optional)
domain = 'domain_example' # str | Search by credential domain (detection domain). (optional)
affiliation_group = 'affiliation_group_example' # str | Search by credential affiliation group. (optional)
password_strength = 'password_strength_example' # str | Search by password strength. (optional)
password_length_gte = 0 # float | Search by password complexity length field as greater then or equal to input value. (optional) (default to 0)
password_lowercase_gte = 0 # float | Search by password complexity lowercase filed as greater then or equal to input value. (optional) (default to 0)
password_uppercase_gte = 0 # float | Search by password complexity uppercase filed as greater then or equal to input value. (optional) (default to 0)
password_numbers_gte = 0 # float | Search by password complexity numbers filed as greater then or equal to input value. (optional) (default to 0)
password_punctuation_gte = 0 # float | Search by password complexity punctuation filed as greater then or equal to input value. (optional) (default to 0)
password_symbols_gte = 0 # float | Search by password complexity symbols filed as greater then or equal to input value. (optional) (default to 0)
password_separators_gte = 0 # float | Search by password complexity separators filed as greater then or equal to input value. (optional) (default to 0)
password_other_gte = 0 # float | Search by password complexity other filed as greater then or equal to input value. (optional) (default to 0)
password_entropy_gte = 0 # float | Search by password complexity entropy filed as greater then or equal to input value. (optional) (default to 0)
password_plain = 'password_plain_example' # str | Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded. (optional)
credential_login = 'credential_login_example' # str | Search by credential login. (optional)
detected_malware = 'detected_malware_example' # str | Search by credential detected malware. (optional)
accessed_url = 'accessed_url_example' # str | Search by accessed url. (optional)
gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
_from = '1day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
sort = 'relevance' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'relevance')
filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
offset = 0 # int | Skip leading number of records. (optional) (default to 0)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search credential occurrences
        api_response = api_instance.credentials_occurrences_get(text=text, credential_occurrence_uid=credential_occurrence_uid, credential_uid=credential_uid, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, credential_login=credential_login, detected_malware=detected_malware, accessed_url=accessed_url, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CredentialsApi->credentials_occurrences_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Search text everywhere in credential occurrences. | [optional] 
 **credential_occurrence_uid** | **str**| Search by credential occurrence uid. | [optional] 
 **credential_uid** | **str**| Search by credential uid. | [optional] 
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **credential_set_uid** | **str**| Search by credential set uid. | [optional] 
 **domain** | **str**| Search by credential domain (detection domain). | [optional] 
 **affiliation_group** | **str**| Search by credential affiliation group. | [optional] 
 **password_strength** | **str**| Search by password strength. | [optional] 
 **password_length_gte** | **float**| Search by password complexity length field as greater then or equal to input value. | [optional] [default to 0]
 **password_lowercase_gte** | **float**| Search by password complexity lowercase filed as greater then or equal to input value. | [optional] [default to 0]
 **password_uppercase_gte** | **float**| Search by password complexity uppercase filed as greater then or equal to input value. | [optional] [default to 0]
 **password_numbers_gte** | **float**| Search by password complexity numbers filed as greater then or equal to input value. | [optional] [default to 0]
 **password_punctuation_gte** | **float**| Search by password complexity punctuation filed as greater then or equal to input value. | [optional] [default to 0]
 **password_symbols_gte** | **float**| Search by password complexity symbols filed as greater then or equal to input value. | [optional] [default to 0]
 **password_separators_gte** | **float**| Search by password complexity separators filed as greater then or equal to input value. | [optional] [default to 0]
 **password_other_gte** | **float**| Search by password complexity other filed as greater then or equal to input value. | [optional] [default to 0]
 **password_entropy_gte** | **float**| Search by password complexity entropy filed as greater then or equal to input value. | [optional] [default to 0]
 **password_plain** | **str**| Search by credential plain password. Note: the value of &#39;passwordPlain&#39; parameter must be URL-encoded. | [optional] 
 **credential_login** | **str**| Search by credential login. | [optional] 
 **detected_malware** | **str**| Search by credential detected malware. | [optional] 
 **accessed_url** | **str**| Search by accessed url. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;relevance&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**CredentialOccurrencesResponse**](CredentialOccurrencesResponse.md)

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

# **credentials_occurrences_stream_get**
> CredentialOccurrencesStreamResponse credentials_occurrences_stream_get(text=text, credential_occurrence_uid=credential_occurrence_uid, credential_uid=credential_uid, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, credential_login=credential_login, detected_malware=detected_malware, accessed_url=accessed_url, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, cursor=cursor, filter_by_gir_set=filter_by_gir_set, count=count)

Credential occurrence stream

Returns list of `Credential occurrences` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/credentials/occurrences` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.

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
    api_instance = titan_client.CredentialsApi(api_client)
    text = 'text_example' # str | Search text everywhere in credential occurrences. (optional)
credential_occurrence_uid = 'credential_occurrence_uid_example' # str | Search by credential occurrence uid. (optional)
credential_uid = 'credential_uid_example' # str | Search by credential uid. (optional)
credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
credential_set_uid = 'credential_set_uid_example' # str | Search by credential set uid. (optional)
domain = 'domain_example' # str | Search by credential domain (detection domain). (optional)
affiliation_group = 'affiliation_group_example' # str | Search by credential affiliation group. (optional)
password_strength = 'password_strength_example' # str | Search by password strength. (optional)
password_length_gte = 0 # float | Search by password complexity length field as greater then or equal to input value. (optional) (default to 0)
password_lowercase_gte = 0 # float | Search by password complexity lowercase filed as greater then or equal to input value. (optional) (default to 0)
password_uppercase_gte = 0 # float | Search by password complexity uppercase filed as greater then or equal to input value. (optional) (default to 0)
password_numbers_gte = 0 # float | Search by password complexity numbers filed as greater then or equal to input value. (optional) (default to 0)
password_punctuation_gte = 0 # float | Search by password complexity punctuation filed as greater then or equal to input value. (optional) (default to 0)
password_symbols_gte = 0 # float | Search by password complexity symbols filed as greater then or equal to input value. (optional) (default to 0)
password_separators_gte = 0 # float | Search by password complexity separators filed as greater then or equal to input value. (optional) (default to 0)
password_other_gte = 0 # float | Search by password complexity other filed as greater then or equal to input value. (optional) (default to 0)
password_entropy_gte = 0 # float | Search by password complexity entropy filed as greater then or equal to input value. (optional) (default to 0)
password_plain = 'password_plain_example' # str | Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded. (optional)
credential_login = 'credential_login_example' # str | Search by credential login. (optional)
detected_malware = 'detected_malware_example' # str | Search by credential detected malware. (optional)
accessed_url = 'accessed_url_example' # str | Search by accessed url. (optional)
gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
_from = '1569314472407' # str | Long unix time. Search data starting from given creation time (including). (optional)
until = '1569314472407' # str | Long unix time. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1569314472407' # str | Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1569314472407' # str | Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
cursor = 'cursor_example' # str | Continue scrolling from cursor. (optional)
filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Credential occurrence stream
        api_response = api_instance.credentials_occurrences_stream_get(text=text, credential_occurrence_uid=credential_occurrence_uid, credential_uid=credential_uid, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, credential_login=credential_login, detected_malware=detected_malware, accessed_url=accessed_url, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, cursor=cursor, filter_by_gir_set=filter_by_gir_set, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CredentialsApi->credentials_occurrences_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Search text everywhere in credential occurrences. | [optional] 
 **credential_occurrence_uid** | **str**| Search by credential occurrence uid. | [optional] 
 **credential_uid** | **str**| Search by credential uid. | [optional] 
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **credential_set_uid** | **str**| Search by credential set uid. | [optional] 
 **domain** | **str**| Search by credential domain (detection domain). | [optional] 
 **affiliation_group** | **str**| Search by credential affiliation group. | [optional] 
 **password_strength** | **str**| Search by password strength. | [optional] 
 **password_length_gte** | **float**| Search by password complexity length field as greater then or equal to input value. | [optional] [default to 0]
 **password_lowercase_gte** | **float**| Search by password complexity lowercase filed as greater then or equal to input value. | [optional] [default to 0]
 **password_uppercase_gte** | **float**| Search by password complexity uppercase filed as greater then or equal to input value. | [optional] [default to 0]
 **password_numbers_gte** | **float**| Search by password complexity numbers filed as greater then or equal to input value. | [optional] [default to 0]
 **password_punctuation_gte** | **float**| Search by password complexity punctuation filed as greater then or equal to input value. | [optional] [default to 0]
 **password_symbols_gte** | **float**| Search by password complexity symbols filed as greater then or equal to input value. | [optional] [default to 0]
 **password_separators_gte** | **float**| Search by password complexity separators filed as greater then or equal to input value. | [optional] [default to 0]
 **password_other_gte** | **float**| Search by password complexity other filed as greater then or equal to input value. | [optional] [default to 0]
 **password_entropy_gte** | **float**| Search by password complexity entropy filed as greater then or equal to input value. | [optional] [default to 0]
 **password_plain** | **str**| Search by credential plain password. Note: the value of &#39;passwordPlain&#39; parameter must be URL-encoded. | [optional] 
 **credential_login** | **str**| Search by credential login. | [optional] 
 **detected_malware** | **str**| Search by credential detected malware. | [optional] 
 **accessed_url** | **str**| Search by accessed url. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **_from** | **str**| Long unix time. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **cursor** | **str**| Continue scrolling from cursor. | [optional] 
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**CredentialOccurrencesStreamResponse**](CredentialOccurrencesStreamResponse.md)

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

# **credentials_stream_get**
> CredentialsStreamResponse credentials_stream_get(text=text, credential_uid=credential_uid, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, credential_login=credential_login, detected_malware=detected_malware, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, cursor=cursor, filter_by_gir_set=filter_by_gir_set, count=count)

Credential stream

Returns list of `Credentials` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/credentials` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.

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
    api_instance = titan_client.CredentialsApi(api_client)
    text = 'text_example' # str | Search text everywhere in credentials. (optional)
credential_uid = 'credential_uid_example' # str | Search by credential uid. (optional)
credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
credential_set_uid = 'credential_set_uid_example' # str | Search by credential set uid. (optional)
domain = 'domain_example' # str | Search by credential domain (detection domain). (optional)
affiliation_group = 'affiliation_group_example' # str | Search by credential affiliation group. (optional)
password_strength = 'password_strength_example' # str | Search by password strength. (optional)
password_length_gte = 0 # float | Search by password complexity length field as greater then or equal to input value. (optional) (default to 0)
password_lowercase_gte = 0 # float | Search by password complexity lowercase filed as greater then or equal to input value. (optional) (default to 0)
password_uppercase_gte = 0 # float | Search by password complexity uppercase filed as greater then or equal to input value. (optional) (default to 0)
password_numbers_gte = 0 # float | Search by password complexity numbers filed as greater then or equal to input value. (optional) (default to 0)
password_punctuation_gte = 0 # float | Search by password complexity punctuation filed as greater then or equal to input value. (optional) (default to 0)
password_symbols_gte = 0 # float | Search by password complexity symbols filed as greater then or equal to input value. (optional) (default to 0)
password_separators_gte = 0 # float | Search by password complexity separators filed as greater then or equal to input value. (optional) (default to 0)
password_other_gte = 0 # float | Search by password complexity other filed as greater then or equal to input value. (optional) (default to 0)
password_entropy_gte = 0 # float | Search by password complexity entropy filed as greater then or equal to input value. (optional) (default to 0)
password_plain = 'password_plain_example' # str | Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded. (optional)
credential_login = 'credential_login_example' # str | Search by credential login. (optional)
detected_malware = 'detected_malware_example' # str | Search by credential detected malware. (optional)
gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
_from = '1day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
cursor = 'cursor_example' # str | Continue scrolling from cursor. (optional)
filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Credential stream
        api_response = api_instance.credentials_stream_get(text=text, credential_uid=credential_uid, credential_set_name=credential_set_name, credential_set_uid=credential_set_uid, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, credential_login=credential_login, detected_malware=detected_malware, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, cursor=cursor, filter_by_gir_set=filter_by_gir_set, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CredentialsApi->credentials_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Search text everywhere in credentials. | [optional] 
 **credential_uid** | **str**| Search by credential uid. | [optional] 
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **credential_set_uid** | **str**| Search by credential set uid. | [optional] 
 **domain** | **str**| Search by credential domain (detection domain). | [optional] 
 **affiliation_group** | **str**| Search by credential affiliation group. | [optional] 
 **password_strength** | **str**| Search by password strength. | [optional] 
 **password_length_gte** | **float**| Search by password complexity length field as greater then or equal to input value. | [optional] [default to 0]
 **password_lowercase_gte** | **float**| Search by password complexity lowercase filed as greater then or equal to input value. | [optional] [default to 0]
 **password_uppercase_gte** | **float**| Search by password complexity uppercase filed as greater then or equal to input value. | [optional] [default to 0]
 **password_numbers_gte** | **float**| Search by password complexity numbers filed as greater then or equal to input value. | [optional] [default to 0]
 **password_punctuation_gte** | **float**| Search by password complexity punctuation filed as greater then or equal to input value. | [optional] [default to 0]
 **password_symbols_gte** | **float**| Search by password complexity symbols filed as greater then or equal to input value. | [optional] [default to 0]
 **password_separators_gte** | **float**| Search by password complexity separators filed as greater then or equal to input value. | [optional] [default to 0]
 **password_other_gte** | **float**| Search by password complexity other filed as greater then or equal to input value. | [optional] [default to 0]
 **password_entropy_gte** | **float**| Search by password complexity entropy filed as greater then or equal to input value. | [optional] [default to 0]
 **password_plain** | **str**| Search by credential plain password. Note: the value of &#39;passwordPlain&#39; parameter must be URL-encoded. | [optional] 
 **credential_login** | **str**| Search by credential login. | [optional] 
 **detected_malware** | **str**| Search by credential detected malware. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **cursor** | **str**| Continue scrolling from cursor. | [optional] 
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**CredentialsStreamResponse**](CredentialsStreamResponse.md)

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

