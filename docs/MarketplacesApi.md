# titan_client.MarketplacesApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketplaces_get**](MarketplacesApi.md#marketplaces_get) | **GET** /marketplaces | Search Marketplaces
[**marketplaces_products_get**](MarketplacesApi.md#marketplaces_products_get) | **GET** /marketplaces/products | Search Products
[**marketplaces_products_stream_get**](MarketplacesApi.md#marketplaces_products_stream_get) | **GET** /marketplaces/products/stream | Products stream
[**marketplaces_resources_get**](MarketplacesApi.md#marketplaces_resources_get) | **GET** /marketplaces/resources | Search Resources
[**marketplaces_resources_stream_get**](MarketplacesApi.md#marketplaces_resources_stream_get) | **GET** /marketplaces/resources/stream | Resources stream
[**marketplaces_vendors_get**](MarketplacesApi.md#marketplaces_vendors_get) | **GET** /marketplaces/vendors | Search Vendors
[**marketplaces_vendors_stream_get**](MarketplacesApi.md#marketplaces_vendors_stream_get) | **GET** /marketplaces/vendors/stream | Vendors stream


# **marketplaces_get**
> MarketplaceSearchResponse marketplaces_get(text=text, status=status, tier=tier, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)

Search Marketplaces

Returns list of `Marketplaces` matching filter criteria.

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
    api_instance = titan_client.MarketplacesApi(api_client)
    text = 'asyncrat' # str | Free text marketplace search. (optional)
    status = 'status_example' # str | Search by marketplace status. (optional)
    tier = 'tier_example' # str | Search by marketplace tier. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    var_from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'latest' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'latest')
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Marketplaces
        api_response = api_instance.marketplaces_get(text=text, status=status, tier=tier, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketplacesApi->marketplaces_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Free text marketplace search. | [optional] 
 **status** | **str**| Search by marketplace status. | [optional] 
 **tier** | **str**| Search by marketplace tier. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **var_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;latest&#39;]
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**MarketplaceSearchResponse**](MarketplaceSearchResponse.md)

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

# **marketplaces_products_get**
> MarketplaceProductSearchResponse marketplaces_products_get(text=text, availability=availability, product_type=product_type, vendor_uid=vendor_uid, bin=bin, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)

Search Products

Returns list of `Products` matching filter criteria.

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
    api_instance = titan_client.MarketplacesApi(api_client)
    text = 'asyncrat' # str | Free text product search. (optional)
    availability = 'availability_example' # str | Availability status of product. (optional)
    product_type = 'product_type_example' # str | Type of product (optional)
    vendor_uid = '147540e129e096fa91700e9db6588354' # str | Vendor unique identifier. (optional)
    bin = '4543' # str | Search by product BIN. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    var_from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'latest' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'latest')
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Products
        api_response = api_instance.marketplaces_products_get(text=text, availability=availability, product_type=product_type, vendor_uid=vendor_uid, bin=bin, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketplacesApi->marketplaces_products_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Free text product search. | [optional] 
 **availability** | **str**| Availability status of product. | [optional] 
 **product_type** | **str**| Type of product | [optional] 
 **vendor_uid** | **str**| Vendor unique identifier. | [optional] 
 **bin** | **str**| Search by product BIN. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **var_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;latest&#39;]
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**MarketplaceProductSearchResponse**](MarketplaceProductSearchResponse.md)

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

# **marketplaces_products_stream_get**
> MarketplaceProductStreamResponse marketplaces_products_stream_get(text=text, availability=availability, product_type=product_type, vendor_uid=vendor_uid, cursor=cursor, bin=bin, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, count=count)

Products stream

Returns list of `Products` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/marketplaces/products` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br/> Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.

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
    api_instance = titan_client.MarketplacesApi(api_client)
    text = 'asyncrat' # str | Free text product search. (optional)
    availability = 'availability_example' # str | Availability status of product. (optional)
    product_type = 'product_type_example' # str | Type of product (optional)
    vendor_uid = '147540e129e096fa91700e9db6588354' # str | Vendor unique identifier. (optional)
    cursor = 'cursor_example' # str | Continue scrolling from cursor. (optional)
    bin = '4543' # str | Search by product BIN. (optional)
    _from = '1627776000000' # str | Long unix time. Search data starting from given creation time (including). (optional)
    var_from = '1627776000000' # str | Long unix time. Search data starting from given creation time (including). (optional)
    until = '1627948800000' # str | Long unix time. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '1627948800000' # str | Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1627948800000' # str | Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Products stream
        api_response = api_instance.marketplaces_products_stream_get(text=text, availability=availability, product_type=product_type, vendor_uid=vendor_uid, cursor=cursor, bin=bin, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketplacesApi->marketplaces_products_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Free text product search. | [optional] 
 **availability** | **str**| Availability status of product. | [optional] 
 **product_type** | **str**| Type of product | [optional] 
 **vendor_uid** | **str**| Vendor unique identifier. | [optional] 
 **cursor** | **str**| Continue scrolling from cursor. | [optional] 
 **bin** | **str**| Search by product BIN. | [optional] 
 **_from** | **str**| Long unix time. Search data starting from given creation time (including). | [optional] 
 **var_from** | **str**| Long unix time. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**MarketplaceProductStreamResponse**](MarketplaceProductStreamResponse.md)

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

# **marketplaces_resources_get**
> MarketplaceResourceSearchResponse marketplaces_resources_get(text=text, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)

Search Resources

Returns list of `Resources` matching filter criteria.

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
    api_instance = titan_client.MarketplacesApi(api_client)
    text = 'asyncrat' # str | Free text resources search. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    var_from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'latest' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'latest')
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Resources
        api_response = api_instance.marketplaces_resources_get(text=text, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketplacesApi->marketplaces_resources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Free text resources search. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **var_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;latest&#39;]
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**MarketplaceResourceSearchResponse**](MarketplaceResourceSearchResponse.md)

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

# **marketplaces_resources_stream_get**
> MarketplaceResourceStreamResponse marketplaces_resources_stream_get(text=text, cursor=cursor, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, count=count)

Resources stream

Returns list of `Resources` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/marketplaces/resources` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br/> Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.

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
    api_instance = titan_client.MarketplacesApi(api_client)
    text = 'asyncrat' # str | Free text resources search. (optional)
    cursor = 'cursor_example' # str | Continue scrolling from cursor. (optional)
    _from = '1627776000000' # str | Long unix time. Search data starting from given creation time (including). (optional)
    var_from = '1627776000000' # str | Long unix time. Search data starting from given creation time (including). (optional)
    until = '1627948800000' # str | Long unix time. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '1627948800000' # str | Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1627948800000' # str | Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Resources stream
        api_response = api_instance.marketplaces_resources_stream_get(text=text, cursor=cursor, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketplacesApi->marketplaces_resources_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Free text resources search. | [optional] 
 **cursor** | **str**| Continue scrolling from cursor. | [optional] 
 **_from** | **str**| Long unix time. Search data starting from given creation time (including). | [optional] 
 **var_from** | **str**| Long unix time. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**MarketplaceResourceStreamResponse**](MarketplaceResourceStreamResponse.md)

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

# **marketplaces_vendors_get**
> MarketplaceVendorSearchResponse marketplaces_vendors_get(text=text, marketplace_uid=marketplace_uid, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)

Search Vendors

Returns list of `Vendors` matching filter criteria.

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
    api_instance = titan_client.MarketplacesApi(api_client)
    text = 'asyncrat' # str | Free text vendor search. (optional)
    marketplace_uid = 'c81e728d9d4c2f636f067f89cc14862c' # str | Unique identifier of marketplace. (optional)
    _from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    var_from = '2day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
    until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '2day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    sort = 'latest' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'latest')
    offset = 0 # int | Skip leading number of records. (optional) (default to 0)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Vendors
        api_response = api_instance.marketplaces_vendors_get(text=text, marketplace_uid=marketplace_uid, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketplacesApi->marketplaces_vendors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Free text vendor search. | [optional] 
 **marketplace_uid** | **str**| Unique identifier of marketplace. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **var_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;latest&#39;]
 **offset** | **int**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**MarketplaceVendorSearchResponse**](MarketplaceVendorSearchResponse.md)

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

# **marketplaces_vendors_stream_get**
> MarketplaceVendorStreamResponse marketplaces_vendors_stream_get(text=text, marketplace_uid=marketplace_uid, cursor=cursor, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, count=count)

Vendors stream

Returns list of `Vendors` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/marketplaces/vendors` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br/> Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.

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
    api_instance = titan_client.MarketplacesApi(api_client)
    text = 'asyncrat' # str | Free text vendor search. (optional)
    marketplace_uid = 'c81e728d9d4c2f636f067f89cc14862c' # str | Unique identifier of marketplace. (optional)
    cursor = 'cursor_example' # str | Continue scrolling from cursor. (optional)
    _from = '1627776000000' # str | Long unix time. Search data starting from given creation time (including). (optional)
    var_from = '1627776000000' # str | Long unix time. Search data starting from given creation time (including). (optional)
    until = '1627948800000' # str | Long unix time. Search data ending before given creation time (excluding). (optional)
    last_updated_from = '1627948800000' # str | Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
    last_updated_until = '1627948800000' # str | Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
    count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Vendors stream
        api_response = api_instance.marketplaces_vendors_stream_get(text=text, marketplace_uid=marketplace_uid, cursor=cursor, _from=_from, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketplacesApi->marketplaces_vendors_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Free text vendor search. | [optional] 
 **marketplace_uid** | **str**| Unique identifier of marketplace. | [optional] 
 **cursor** | **str**| Continue scrolling from cursor. | [optional] 
 **_from** | **str**| Long unix time. Search data starting from given creation time (including). | [optional] 
 **var_from** | **str**| Long unix time. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**MarketplaceVendorStreamResponse**](MarketplaceVendorStreamResponse.md)

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

