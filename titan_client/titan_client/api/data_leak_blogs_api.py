# coding: utf-8

"""
    Titan API v1

    # Introduction The Intel 471 API is organized around the principles of REST. Our API lets you gather results from our platform using anything that can send a HTTP request, including cURL and modern internet browsers. Access to this API requires an API token which is managed from your account settings.  Intel 471 reserves the right to add fields to our API however we will provide backwards compatibility and older version support so that it will be possible to choose exact versions that provide a response with an older structure.  # Authentication Authentication to the API occurs by providing your email address as the login and API key as a password in the authorization header via HTTP Basic Auth. Your API key can be found in the [API](https://portal.intel471.com/api) section on the portal. It carries many privileges so please do not expose it on public web resources.  # Accessing the API  Following examples demonstrate different methods to get the reports from `/reports` endpoint.  ## Internet browser  Just open URL: https://api.intel471.com/v1/reports  Browser will ask you for credentials, provide your email as login and API key as password.  ## cURL command line utility  Execute following command in your terminal:  ``` curl -u <YOU EMAIL>:<YOUR API KEY> https://api.intel471.com/v1/reports ```  ## Python client  We provide a [Python client](https://github.com/intel471/titan-client-python) for Intel 471's Titan API, which aims at providing common ground for all the endpoints. Please note that all the call parameters and response body fields' names are normalized to camel_case, so for example when you search reports by document type using Python client use `document_type` instead of `documentType`.  Install the client using pip (python >= 3.6 required):  ``` pip install titan-client ```  Run following script  ```python import titan_client  configuration = titan_client.Configuration(     username=\"<YOU EMAIL>\",     password=\"<YOUR API KEY>\")  with titan_client.ApiClient(configuration) as api_client:     api_instance = titan_client.ReportsApi(api_client)     api_response = api_instance.reports_get() print(api_response) ```  # Use cases  Below we present several commonly used scenarios in both raw HTTP request format and as a script using Python client. Examples are simplified so that they do not contain the authentication part and for Python client they do not contain configuration and API client object creation portion. For full example please refer to **Accessing the API** section of this document.   ## Paging  One page of the results can carry up to 100 records and you can display up to 11 pages for one query (max offset is 1000) in non-stream API endpoints. Use `count` parameter to set the number of items per page. Use `offset` parameter to shift the window by given number of results.  **HTTP**  ``` # Get 20 reports, sorted by the default field GET https://api.intel471.com/v1/reports?count=20  # Get next 20 reports GET https://api.intel471.com/v1/reports?count=20&offset=20  # Get 40 reports in one go to save API calls GET https://api.intel471.com/v1/reports?count=40 ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(count=20, offset=20) ```  ## Paging beyond the max allowed offset  Paging described in the previous use case is generally sufficient for most needs. If there are more than 1100 objects to be obtained for a given time period and set of filter criteria, then it is possible to move the filter timestamps along and then restart the offset sequencing. There is a very small number of situations where this may cause issues, where there is multiple objects with the same timestamp adjacent to the last object in the response.  For the higher volume or fast changing data (such as malware indicators, malware events, creds) there are stream API endpoints available where cursors may be used in order to acquire data easily and to avoid the need to shift timestamp ranges.  ``` # Get first 11 pages, 100 objects each GET https://api.intel471.com/v1/reports?sort=latest&count=100 GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=1000 ... > {\"reports\": [{..., \"created\": 1661867086000}, {..., \"created\": 1661864268000}]} ```  Then the `created` time value from the last response will be used as an upper limit in the next series of calls:  ```  GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&count=100 GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=1000 ```  And so on, until the results are available or until the desired number of objects has been fetched.  ## Paging /alerts endpoint  Alerts endpoint differs from all the other non-stream API endpoints in that the `offset` parameter needs to be set to the uid of the most recent acquired alert instead of an integer indicating the shift.  **HTTP**  ``` GET https://api.intel471.com/v1/alerts?count=100 > {\"alerts\": [{..., \"uid\": \"abc123\"}, {..., \"uid\": \"abc234\"}]}  GET https://api.intel471.com/v1/alerts?count=100&offset=abc234 > {\"alerts\": [{..., \"uid\": \"abc345\"}, {..., \"uid\": \"abc456\"}]} ```  **Python**  ``` response = titan_client.AlertsApi(api_client).alerts_get(count=100, offset=\"abc456\") ```  ## Stream endpoints paging  Stream endpoints provide the same data as their regular counterparts but they differ in a way of paging. When working with a stream endpoint, the response always contains `cursorNext` field, which should be provided to the next subsequent call to fetch potential next page of the results. All the subsequent calls should have the same set of query parameters as the first one, except the cursor value. Keep calling the endpoint with a new cursor value until it stops yielding results. When new data appear after that, another call will fetch it.  **HTTP**  ``` GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT1\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT1 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT2\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT2 > {\"cursorNext\": \"MTY1NT3\"} ```  **Python**  ``` response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000) print(response.cursor_next, response.indicators) # MTY1NT1, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT1\")) print(response.cursor_next, response.indicators) # MTY1NT2, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT2\")) print(response.cursor_next, response.indicators) # MTY1NT3, None ```  ## Querying using logical operators  ### Array parameters  Any query parameter can be singular or array, if multiple parameters with the same name were provided. All parameters with the same name are internally combined into a query with `AND` operator.  So following query:  ``` GET https://api.intel471.com/v1/reports?report=sources&report=abba ```  Means \"find me reports with `source` AND `abba` in their body\".  This approach is not supported in the Python client. Instead use query string method discussed below.  ### Query string parameters  Query parameters accept Elastic's query string syntax, which allows for even better flexibility.  For example above query can be rephrased as:  **HTTP**  ``` GET https://api.intel471.com/v1/reports?report=sources OR abba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"sources OR abba\") ```  More advanced combination would include both `OR` and `AND` operators and a negation:  **HTTP**  ``` GET https://api.intel471.com/v1/reports?report=(sources OR abba) AND -creaba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"(sources OR abba) AND -creaba\") ```  Means \"find me reports with `source` or `abba` in their body which at the same time do not contain `creaba`\".  The query string \"mini-language\" reference and examples can be found on [Elastic's query string syntax](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/query-dsl-query-string-query.html#query-dsl-query-string-query) page.  ## Get CVEs using multiple filtering criteria  Get all CVE reports for Chrome product where the risk is high and the patch is not available yet.  **HTTP**  ``` GET https://api.intel471.com/v1/cve/reports?productName=Chrome&riskLevel=high&patchStatus=unavailable ```  **Python**  ``` response = titan_client.VulnerabilitiesApi(api_client).cve_reports_get(     product_name=\"Chrome\",     risk_level=\"high\",     patch_status=\"unavailable\" ) ```  ## List watcher groups  **HTTP**  ``` GET https://api.intel471.com/v1/watcherGroups ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_get() ```  ## Create watcher group  To create a watcher group you need to pass a body along with the request.  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups {   \"name\": \"my_group_name\",   \"description\": \"My description\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_post(   {\"name\": \"my_group_name\", \"description\": \"My description\"} ) ```  ## Create free text search watcher  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"freeTextPattern\": \"text to search\",   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"freeTextPattern\": \"text to search\",     \"notificationChannel\": \"website\"   } ) ```  ## Create specific search watcher  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"patterns\": [     {\"types\": \"Actor\" , \"pattern\": \"swisman\"}   ],   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"patterns\": [       {\"types\": \"Actor\" , \"pattern\": \"swisman\"}     ],     \"notificationChannel\": \"website\"   } ) ```  # API integration best practice with your application CORS requests to the API are not allowed due to security concerns, so please avoid AJAX calls directly from the browser. Instead consider setting up a server side proxy in your application to handle API requests.  Please consider not storing information provided by the API locally as we are constantly improving our data set and want you to have the most updated information.  # Versioning support We consistently improve our API and occasionally introduce the changes based on the customer feedback. The current API version is provided in this documentation's header. We provide API backwards compatibility whenever possible.  All requests are prefixed with the major version number, for example `/v1`:  ``` https://api.intel471.com/v1/reports ```  Different major versions are not compatible and imply significant response structure changes. Minor versions differences might include extra fields in response or provide new request parameter support. To stick to the specific version, just add `v` parameter to the request, for example: `?v=1.19.2`. If you specify a non existing version, it will be brought down to the nearest existing one.  Omitting the version parameter in the request will call the latest version of the API.  We consistently phase out the outdated versions of the API, keeping only several most recent versions. Specific version is getting disabled only when we do not record any requests using it, so it's guaranteed that calls to the outdated ones will work, though we recommend switching to the latest one as soon as possible.  We recommend to always add the version parameter to the request to be safe on API updates in your integrations.  Python client always adds the version parameter in the underlying request. API version matches the Python client's package version. 

    The version of the OpenAPI document: 1.20.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from titan_client.models.data_leak_posts_response import DataLeakPostsResponse

from titan_client.api_client import ApiClient, RequestSerialized
from titan_client.api_response import ApiResponse
from titan_client.rest import RESTResponseType


class DataLeakBlogsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def dataleak_posts_get(
        self,
        data_leak_post: Annotated[Optional[StrictStr], Field(description="Search text in data leak posts and topics (including images via OCR).")] = None,
        data_leak_posts_by_thread_uid: Annotated[Optional[StrictStr], Field(description="Search data leak posts by thread uid.")] = None,
        data_leak_blog: Annotated[Optional[StrictStr], Field(description="Search data leak posts in a given data leak blog.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=1000, strict=True, ge=0)]], Field(description="Skip leading number of records.")] = None,
        count: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=0)]], Field(description="Returns given number of records starting from `offset` position.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> DataLeakPostsResponse:
        """Search Data Leak Posts

        Returns list of `Data Leak Posts` matching filter criteria. At least one of `dataLeakPost`, `dataLeakPostsByThreadUid`, `dataLeakBlog` is required.

        :param data_leak_post: Search text in data leak posts and topics (including images via OCR).
        :type data_leak_post: str
        :param data_leak_posts_by_thread_uid: Search data leak posts by thread uid.
        :type data_leak_posts_by_thread_uid: str
        :param data_leak_blog: Search data leak posts in a given data leak blog.
        :type data_leak_blog: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order.
        :type sort: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._dataleak_posts_get_serialize(
            data_leak_post=data_leak_post,
            data_leak_posts_by_thread_uid=data_leak_posts_by_thread_uid,
            data_leak_blog=data_leak_blog,
            var_from=var_from,
            until=until,
            last_updated_from=last_updated_from,
            last_updated_until=last_updated_until,
            sort=sort,
            offset=offset,
            count=count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DataLeakPostsResponse",
            '412': "ActorsGet412Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def dataleak_posts_get_with_http_info(
        self,
        data_leak_post: Annotated[Optional[StrictStr], Field(description="Search text in data leak posts and topics (including images via OCR).")] = None,
        data_leak_posts_by_thread_uid: Annotated[Optional[StrictStr], Field(description="Search data leak posts by thread uid.")] = None,
        data_leak_blog: Annotated[Optional[StrictStr], Field(description="Search data leak posts in a given data leak blog.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=1000, strict=True, ge=0)]], Field(description="Skip leading number of records.")] = None,
        count: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=0)]], Field(description="Returns given number of records starting from `offset` position.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[DataLeakPostsResponse]:
        """Search Data Leak Posts

        Returns list of `Data Leak Posts` matching filter criteria. At least one of `dataLeakPost`, `dataLeakPostsByThreadUid`, `dataLeakBlog` is required.

        :param data_leak_post: Search text in data leak posts and topics (including images via OCR).
        :type data_leak_post: str
        :param data_leak_posts_by_thread_uid: Search data leak posts by thread uid.
        :type data_leak_posts_by_thread_uid: str
        :param data_leak_blog: Search data leak posts in a given data leak blog.
        :type data_leak_blog: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order.
        :type sort: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._dataleak_posts_get_serialize(
            data_leak_post=data_leak_post,
            data_leak_posts_by_thread_uid=data_leak_posts_by_thread_uid,
            data_leak_blog=data_leak_blog,
            var_from=var_from,
            until=until,
            last_updated_from=last_updated_from,
            last_updated_until=last_updated_until,
            sort=sort,
            offset=offset,
            count=count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DataLeakPostsResponse",
            '412': "ActorsGet412Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def dataleak_posts_get_without_preload_content(
        self,
        data_leak_post: Annotated[Optional[StrictStr], Field(description="Search text in data leak posts and topics (including images via OCR).")] = None,
        data_leak_posts_by_thread_uid: Annotated[Optional[StrictStr], Field(description="Search data leak posts by thread uid.")] = None,
        data_leak_blog: Annotated[Optional[StrictStr], Field(description="Search data leak posts in a given data leak blog.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=1000, strict=True, ge=0)]], Field(description="Skip leading number of records.")] = None,
        count: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=0)]], Field(description="Returns given number of records starting from `offset` position.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Search Data Leak Posts

        Returns list of `Data Leak Posts` matching filter criteria. At least one of `dataLeakPost`, `dataLeakPostsByThreadUid`, `dataLeakBlog` is required.

        :param data_leak_post: Search text in data leak posts and topics (including images via OCR).
        :type data_leak_post: str
        :param data_leak_posts_by_thread_uid: Search data leak posts by thread uid.
        :type data_leak_posts_by_thread_uid: str
        :param data_leak_blog: Search data leak posts in a given data leak blog.
        :type data_leak_blog: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order.
        :type sort: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._dataleak_posts_get_serialize(
            data_leak_post=data_leak_post,
            data_leak_posts_by_thread_uid=data_leak_posts_by_thread_uid,
            data_leak_blog=data_leak_blog,
            var_from=var_from,
            until=until,
            last_updated_from=last_updated_from,
            last_updated_until=last_updated_until,
            sort=sort,
            offset=offset,
            count=count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DataLeakPostsResponse",
            '412': "ActorsGet412Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _dataleak_posts_get_serialize(
        self,
        data_leak_post,
        data_leak_posts_by_thread_uid,
        data_leak_blog,
        var_from,
        until,
        last_updated_from,
        last_updated_until,
        sort,
        offset,
        count,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if data_leak_post is not None:
            
            _query_params.append(('dataLeakPost', data_leak_post))
            
        if data_leak_posts_by_thread_uid is not None:
            
            _query_params.append(('dataLeakPostsByThreadUid', data_leak_posts_by_thread_uid))
            
        if data_leak_blog is not None:
            
            _query_params.append(('dataLeakBlog', data_leak_blog))
            
        if var_from is not None:
            
            _query_params.append(('from', var_from))
            
        if until is not None:
            
            _query_params.append(('until', until))
            
        if last_updated_from is not None:
            
            _query_params.append(('lastUpdatedFrom', last_updated_from))
            
        if last_updated_until is not None:
            
            _query_params.append(('lastUpdatedUntil', last_updated_until))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if count is not None:
            
            _query_params.append(('count', count))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json', 
                'text/plain'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'BasicAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/dataleak/posts',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


