# titan_client.VulnerabilitiesApi

All URIs are relative to *https://api.intel471.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cve_reports_get**](VulnerabilitiesApi.md#cve_reports_get) | **GET** /cve/reports | Search Vulnerability Reports (CVE)
[**cve_reports_uid_get**](VulnerabilitiesApi.md#cve_reports_uid_get) | **GET** /cve/reports/{uid} | Get Vulnerability Report (CVE)


# **cve_reports_get**
> SimpleCvesResponse cve_reports_get(cve_report=cve_report, cve_type=cve_type, cve_status=cve_status, cve_name=cve_name, risk_level=risk_level, patch_status=patch_status, vendor_name=vendor_name, product_name=product_name, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)

Search Vulnerability Reports (CVE)

Returns list of `Vulnerability Reports` matching filter criteria.

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
    api_instance = titan_client.VulnerabilitiesApi(api_client)
    cve_report = 'vulnerability' # str | Free text CVE reports search. (optional)
cve_type = 'Buffer overflow' # str | Search CVE reports by type. (optional)
cve_status = 'cve_status_example' # str | Search CVE reports by status. (optional)
cve_name = 'CVE-2015-6435' # str | Search CVE reports by name. (optional)
risk_level = 'risk_level_example' # str | Search CVE reports by risk level. (optional)
patch_status = 'patch_status_example' # str | Search CVE reports by patch status. (optional)
vendor_name = 'Mozilla' # str | Search CVE reports by vendor name. (optional)
product_name = 'Microsoft' # str | Search CVE reports by product name. (optional)
gir = '1.1.3' # str | Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program. (optional)
_from = '1day' # str | Long unix time or string time range. Search data starting from given creation time (including). (optional)
until = '1day' # str | Long unix time or string time range. Search data ending before given creation time (excluding). (optional)
last_updated_from = '1day' # str | Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. (optional)
last_updated_until = '1day' # str | Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. (optional)
sort = 'relevance' # str | Sort results by the object's native time in descending (latest) or ascending (earliest) order (optional) (default to 'relevance')
filter_by_gir_set = 'filter_by_gir_set_example' # str | Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required (optional)
offset = 0 # float | Skip leading number of records. (optional) (default to 0)
count = 10 # int | Returns given number of records starting from `offset` position. (optional) (default to 10)

    try:
        # Search Vulnerability Reports (CVE)
        api_response = api_instance.cve_reports_get(cve_report=cve_report, cve_type=cve_type, cve_status=cve_status, cve_name=cve_name, risk_level=risk_level, patch_status=patch_status, vendor_name=vendor_name, product_name=product_name, gir=gir, _from=_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, sort=sort, filter_by_gir_set=filter_by_gir_set, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VulnerabilitiesApi->cve_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_report** | **str**| Free text CVE reports search. | [optional] 
 **cve_type** | **str**| Search CVE reports by type. | [optional] 
 **cve_status** | **str**| Search CVE reports by status. | [optional] 
 **cve_name** | **str**| Search CVE reports by name. | [optional] 
 **risk_level** | **str**| Search CVE reports by risk level. | [optional] 
 **patch_status** | **str**| Search CVE reports by patch status. | [optional] 
 **vendor_name** | **str**| Search CVE reports by vendor name. | [optional] 
 **product_name** | **str**| Search CVE reports by product name. | [optional] 
 **gir** | **str**| Search by General Intel Requirements (GIR). &lt;br /&gt;Consult your collection manager for a General Intelligence Requirements program. | [optional] 
 **_from** | **str**| Long unix time or string time range. Search data starting from given creation time (including). | [optional] 
 **until** | **str**| Long unix time or string time range. Search data ending before given creation time (excluding). | [optional] 
 **last_updated_from** | **str**| Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded. | [optional] 
 **last_updated_until** | **str**| Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded. | [optional] 
 **sort** | **str**| Sort results by the object&#39;s native time in descending (latest) or ascending (earliest) order | [optional] [default to &#39;relevance&#39;]
 **filter_by_gir_set** | **str**| Filters results by user&#39;s GIRs (General intel requirements) or user&#39;s company PIRs (Prioritized intel requirements) if present. Dedicated user features are required | [optional] 
 **offset** | **float**| Skip leading number of records. | [optional] [default to 0]
 **count** | **int**| Returns given number of records starting from &#x60;offset&#x60; position. | [optional] [default to 10]

### Return type

[**SimpleCvesResponse**](SimpleCvesResponse.md)

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

# **cve_reports_uid_get**
> FullCveSchema cve_reports_uid_get(uid)

Get Vulnerability Report (CVE)

Returns single `Vulnerability Report` object

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
    api_instance = titan_client.VulnerabilitiesApi(api_client)
    uid = 'd6ec93bf8fdf355f7b35a3bc2c15566b' # str | Vulnerability report identifier.

    try:
        # Get Vulnerability Report (CVE)
        api_response = api_instance.cve_reports_uid_get(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VulnerabilitiesApi->cve_reports_uid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Vulnerability report identifier. | 

### Return type

[**FullCveSchema**](FullCveSchema.md)

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

