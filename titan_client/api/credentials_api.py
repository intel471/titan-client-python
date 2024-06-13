# coding: utf-8

"""
    Titan API v1

    # Introduction The Intel 471 API is organized around the principles of REST. Our API lets you gather results from our platform using anything that can send a HTTP request, including cURL and modern internet browsers. Access to this API requires an API token which is managed from your account settings.  Intel 471 reserves the right to add fields to our API however we will provide backwards compatibility and older version support so that it will be possible to choose exact versions that provide a response with an older structure.  # Authentication Authentication to the API occurs by providing your email address as the login and API key as a password in the authorization header via HTTP Basic Auth. Your API key can be found in the [API](https://portal.intel471.com/api) section on the portal. It carries many privileges so please do not expose it on public web resources.  # Accessing the API  Following examples demonstrate different methods to get the reports from `/reports` endpoint.  ## Internet browser  Just open URL: https://api.intel471.com/v1/reports  Browser will ask you for credentials, provide your email as login and API key as password.  ## cURL command line utility  Execute following command in your terminal:  ``` curl -u <YOU EMAIL>:<YOUR API KEY> https://api.intel471.com/v1/reports ```  ## Python client  We provide a [Python client](https://github.com/intel471/titan-client-python) for Intel 471's Titan API, which aims at providing common ground for all the endpoints. Please note that all the call parameters and response body fields' names are normalized to camel_case, so for example when you search reports by document type using Python client use `document_type` instead of `documentType`.  Install the client using pip (python >= 3.6 required):  ``` pip install titan-client ```  Run following script  ```python import titan_client  configuration = titan_client.Configuration(     username=\"<YOU EMAIL>\",     password=\"<YOUR API KEY>\")  with titan_client.ApiClient(configuration) as api_client:     api_instance = titan_client.ReportsApi(api_client)     api_response = api_instance.reports_get() print(api_response) ```  # Use cases  Below we present several commonly used scenarios in both raw HTTP request format and as a script using Python client. Examples are simplified so that they do not contain the authentication part and for Python client they do not contain configuration and API client object creation portion. For full example please refer to **Accessing the API** section of this document.   ## Paging  One page of the results can carry up to 100 records and you can display up to 11 pages for one query (max offset is 1000) in non-stream API endpoints. Use `count` parameter to set the number of items per page. Use `offset` parameter to shift the window by given number of results.  **HTTP**  ``` # Get 20 reports, sorted by the default field GET https://api.intel471.com/v1/reports?count=20  # Get next 20 reports GET https://api.intel471.com/v1/reports?count=20&offset=20  # Get 40 reports in one go to save API calls GET https://api.intel471.com/v1/reports?count=40 ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(count=20, offset=20) ```  ## Paging beyond the max allowed offset  Paging described in the previous use case is generally sufficient for most needs. If there are more than 1100 objects to be obtained for a given time period and set of filter criteria, then it is possible to move the filter timestamps along and then restart the offset sequencing. There is a very small number of situations where this may cause issues, where there is multiple objects with the same timestamp adjacent to the last object in the response.  For the higher volume or fast changing data (such as malware indicators, malware events, creds) there are stream API endpoints available where cursors may be used in order to acquire data easily and to avoid the need to shift timestamp ranges.  ``` # Get first 11 pages, 100 objects each GET https://api.intel471.com/v1/reports?sort=latest&count=100 GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=1000 ... > {\"reports\": [{..., \"created\": 1661867086000}, {..., \"created\": 1661864268000}]} ```  Then the `created` time value from the last response will be used as an upper limit in the next series of calls:  ```  GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&count=100 GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=1000 ```  And so on, until the results are available or until the desired number of objects has been fetched.  ## Paging /alerts endpoint  Alerts endpoint differs from all the other non-stream API endpoints in that the `offset` parameter needs to be set to the uid of the most recent acquired alert instead of an integer indicating the shift.  **HTTP**  ``` GET https://api.intel471.com/v1/alerts?count=100 > {\"alerts\": [{..., \"uid\": \"abc123\"}, {..., \"uid\": \"abc234\"}]}  GET https://api.intel471.com/v1/alerts?count=100&offset=abc234 > {\"alerts\": [{..., \"uid\": \"abc345\"}, {..., \"uid\": \"abc456\"}]} ```  **Python**  ``` response = titan_client.AlertsApi(api_client).alerts_get(count=100, offset=\"abc456\") ```  ## Stream endpoints paging  Stream endpoints provide the same data as their regular counterparts but they differ in a way of paging. When working with a stream endpoint, the response always contains `cursorNext` field, which should be provided to the next subsequent call to fetch potential next page of the results. All the subsequent calls should have the same set of query parameters as the first one, except the cursor value. Keep calling the endpoint with a new cursor value until it stops yielding results. When new data appear after that, another call will fetch it.  **HTTP**  ``` GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT1\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT1 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT2\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT2 > {\"cursorNext\": \"MTY1NT3\"} ```  **Python**  ``` response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000) print(response.cursor_next, response.indicators) # MTY1NT1, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT1\")) print(response.cursor_next, response.indicators) # MTY1NT2, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT2\")) print(response.cursor_next, response.indicators) # MTY1NT3, None ```  ## Querying using logical operators  ### Array parameters  Any query parameter can be singular or array, if multiple parameters with the same name were provided. All parameters with the same name are internally combined into a query with `AND` operator.  So following query:  ``` GET https://api.intel471.com/v1/reports?report=sources&report=abba ```  Means \"find me reports with `source` AND `abba` in their body\".  This approach is not supported in the Python client. Instead use query string method discussed below.  ### Query string parameters  Query parameters accept Elastic's query string syntax, which allows for even better flexibility.  For example above query can be rephrased as:  **HTTP**  ``` GET https://api.intel471.com/v1/reports?report=sources OR abba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"sources OR abba\") ```  More advanced combination would include both `OR` and `AND` operators and a negation:  **HTTP**  ``` GET https://api.intel471.com/v1/reports?report=(sources OR abba) AND -creaba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"(sources OR abba) AND -creaba\") ```  Means \"find me reports with `source` or `abba` in their body which at the same time do not contain `creaba`\".  The query string \"mini-language\" reference and examples can be found on [Elastic's query string syntax](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/query-dsl-query-string-query.html#query-dsl-query-string-query) page.  ## Get CVEs using multiple filtering criteria  Get all CVE reports for Chrome product where the risk is high and the patch is not available yet.  **HTTP**  ``` GET https://api.intel471.com/v1/cve/reports?productName=Chrome&riskLevel=high&patchStatus=unavailable ```  **Python**  ``` response = titan_client.VulnerabilitiesApi(api_client).cve_reports_get(     product_name=\"Chrome\",     risk_level=\"high\",     patch_status=\"unavailable\" ) ```  ## List watcher groups  **HTTP**  ``` GET https://api.intel471.com/v1/watcherGroups ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_get() ```  ## Create watcher group  To create a watcher group you need to pass a body along with the request.  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups {   \"name\": \"my_group_name\",   \"description\": \"My description\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_post(   {\"name\": \"my_group_name\", \"description\": \"My description\"} ) ```  ## Create free text search watcher  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"freeTextPattern\": \"text to search\",   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"freeTextPattern\": \"text to search\",     \"notificationChannel\": \"website\"   } ) ```  ## Create specific search watcher  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"patterns\": [     {\"types\": \"Actor\" , \"pattern\": \"swisman\"}   ],   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"patterns\": [       {\"types\": \"Actor\" , \"pattern\": \"swisman\"}     ],     \"notificationChannel\": \"website\"   } ) ```  # API integration best practice with your application CORS requests to the API are not allowed due to security concerns, so please avoid AJAX calls directly from the browser. Instead consider setting up a server side proxy in your application to handle API requests.  Please consider not storing information provided by the API locally as we are constantly improving our data set and want you to have the most updated information.  # Versioning support We consistently improve our API and occasionally introduce the changes based on the customer feedback. The current API version is provided in this documentation's header. We provide API backwards compatibility whenever possible.  All requests are prefixed with the major version number, for example `/v1`:  ``` https://api.intel471.com/v1/reports ```  Different major versions are not compatible and imply significant response structure changes. Minor versions differences might include extra fields in response or provide new request parameter support. To stick to the specific version, just add `v` parameter to the request, for example: `?v=1.19.2`. If you specify a non existing version, it will be brought down to the nearest existing one.  Omitting the version parameter in the request will call the latest version of the API.  We consistently phase out the outdated versions of the API, keeping only several most recent versions. Specific version is getting disabled only when we do not record any requests using it, so it's guaranteed that calls to the outdated ones will work, though we recommend switching to the latest one as soon as possible.  We recommend to always add the version parameter to the request to be safe on API updates in your integrations.  Python client always adds the version parameter in the underlying request. API version matches the Python client's package version.   # noqa: E501

    The version of the OpenAPI document: 1.20.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from titan_client.api_client import ApiClient
from titan_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CredentialsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def credential_sets_accessed_urls_get(self, **kwargs):  # noqa: E501
        """Search credential set accessed urls  # noqa: E501

        Returns list of `Credential set accessed urls` matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credential_sets_accessed_urls_get(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credential sets accessed urls.
        :type text: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search by purported victim.
        :type victim: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by the object's native time in descending (latest) or ascending (earliest) order
        :type sort: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CredentialSetsAccessedUrlsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.credential_sets_accessed_urls_get_with_http_info(**kwargs)  # noqa: E501

    def credential_sets_accessed_urls_get_with_http_info(self, **kwargs):  # noqa: E501
        """Search credential set accessed urls  # noqa: E501

        Returns list of `Credential set accessed urls` matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credential_sets_accessed_urls_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credential sets accessed urls.
        :type text: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search by purported victim.
        :type victim: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by the object's native time in descending (latest) or ascending (earliest) order
        :type sort: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CredentialSetsAccessedUrlsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'text',
            'credential_set_name',
            'credential_set_uid',
            'accessed_url',
            'gir',
            'victim',
            '_from',
            'until',
            'last_updated_from',
            'last_updated_until',
            'sort',
            'filter_by_gir_set',
            'offset',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credential_sets_accessed_urls_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `credential_sets_accessed_urls_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `credential_sets_accessed_urls_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credential_sets_accessed_urls_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credential_sets_accessed_urls_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('text') is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if local_var_params.get('credential_set_name') is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if local_var_params.get('credential_set_uid') is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if local_var_params.get('accessed_url') is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if local_var_params.get('gir') is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if local_var_params.get('victim') is not None:  # noqa: E501
            query_params.append(('victim', local_var_params['victim']))  # noqa: E501
        if local_var_params.get('_from') is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if local_var_params.get('until') is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if local_var_params.get('last_updated_from') is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if local_var_params.get('last_updated_until') is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if local_var_params.get('sort') is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if local_var_params.get('filter_by_gir_set') is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if local_var_params.get('count') is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        response_types_map = {
            200: "CredentialSetsAccessedUrlsResponse",
            412: "CredentialSetsGet412Response",
        }

        return self.api_client.call_api(
            '/credentialSets/accessedUrls', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def credential_sets_accessed_urls_stream_get(self, **kwargs):  # noqa: E501
        """Credential set accessed url stream  # noqa: E501

        Returns list of `Credential set accessed urls` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `credentialsets/accessedurls` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credential_sets_accessed_urls_stream_get(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credential sets accessed urls.
        :type text: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search by purported victim.
        :type victim: str
        :param _from: Long unix time. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param cursor: Continue scrolling from cursor.
        :type cursor: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CredentialSetsAccessedUrlsStreamResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.credential_sets_accessed_urls_stream_get_with_http_info(**kwargs)  # noqa: E501

    def credential_sets_accessed_urls_stream_get_with_http_info(self, **kwargs):  # noqa: E501
        """Credential set accessed url stream  # noqa: E501

        Returns list of `Credential set accessed urls` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `credentialsets/accessedurls` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credential_sets_accessed_urls_stream_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credential sets accessed urls.
        :type text: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search by purported victim.
        :type victim: str
        :param _from: Long unix time. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param cursor: Continue scrolling from cursor.
        :type cursor: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CredentialSetsAccessedUrlsStreamResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'text',
            'credential_set_name',
            'credential_set_uid',
            'accessed_url',
            'gir',
            'victim',
            '_from',
            'until',
            'last_updated_from',
            'last_updated_until',
            'cursor',
            'filter_by_gir_set',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credential_sets_accessed_urls_stream_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credential_sets_accessed_urls_stream_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credential_sets_accessed_urls_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('text') is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if local_var_params.get('credential_set_name') is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if local_var_params.get('credential_set_uid') is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if local_var_params.get('accessed_url') is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if local_var_params.get('gir') is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if local_var_params.get('victim') is not None:  # noqa: E501
            query_params.append(('victim', local_var_params['victim']))  # noqa: E501
        if local_var_params.get('_from') is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if local_var_params.get('until') is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if local_var_params.get('last_updated_from') is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if local_var_params.get('last_updated_until') is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if local_var_params.get('cursor') is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if local_var_params.get('filter_by_gir_set') is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if local_var_params.get('count') is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        response_types_map = {
            200: "CredentialSetsAccessedUrlsStreamResponse",
            412: "CredentialSetsStreamGet412Response",
        }

        return self.api_client.call_api(
            '/credentialSets/accessedUrls/stream', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def credential_sets_get(self, **kwargs):  # noqa: E501
        """Search credential sets  # noqa: E501

        Returns list of `Credential sets` matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credential_sets_get(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credential sets.
        :type text: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search by purported victim.
        :type victim: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by the object's native time in descending (latest) or ascending (earliest) order
        :type sort: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CredentialSetsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.credential_sets_get_with_http_info(**kwargs)  # noqa: E501

    def credential_sets_get_with_http_info(self, **kwargs):  # noqa: E501
        """Search credential sets  # noqa: E501

        Returns list of `Credential sets` matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credential_sets_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credential sets.
        :type text: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search by purported victim.
        :type victim: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by the object's native time in descending (latest) or ascending (earliest) order
        :type sort: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CredentialSetsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'text',
            'credential_set_name',
            'credential_set_uid',
            'gir',
            'victim',
            '_from',
            'until',
            'last_updated_from',
            'last_updated_until',
            'sort',
            'filter_by_gir_set',
            'offset',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credential_sets_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `credential_sets_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `credential_sets_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credential_sets_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credential_sets_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('text') is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if local_var_params.get('credential_set_name') is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if local_var_params.get('credential_set_uid') is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if local_var_params.get('gir') is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if local_var_params.get('victim') is not None:  # noqa: E501
            query_params.append(('victim', local_var_params['victim']))  # noqa: E501
        if local_var_params.get('_from') is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if local_var_params.get('until') is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if local_var_params.get('last_updated_from') is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if local_var_params.get('last_updated_until') is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if local_var_params.get('sort') is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if local_var_params.get('filter_by_gir_set') is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if local_var_params.get('count') is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        response_types_map = {
            200: "CredentialSetsResponse",
            412: "CredentialSetsGet412Response",
        }

        return self.api_client.call_api(
            '/credentialSets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def credential_sets_stream_get(self, **kwargs):  # noqa: E501
        """Credential set stream  # noqa: E501

        Returns list of `Credential sets` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/credentialsets` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credential_sets_stream_get(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credential sets.
        :type text: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search by purported victim.
        :type victim: str
        :param _from: Long unix time. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param cursor: Continue scrolling from cursor.
        :type cursor: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CredentialSetsStreamResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.credential_sets_stream_get_with_http_info(**kwargs)  # noqa: E501

    def credential_sets_stream_get_with_http_info(self, **kwargs):  # noqa: E501
        """Credential set stream  # noqa: E501

        Returns list of `Credential sets` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/credentialsets` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credential_sets_stream_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credential sets.
        :type text: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search by purported victim.
        :type victim: str
        :param _from: Long unix time. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param cursor: Continue scrolling from cursor.
        :type cursor: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CredentialSetsStreamResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'text',
            'credential_set_name',
            'gir',
            'victim',
            '_from',
            'until',
            'last_updated_from',
            'last_updated_until',
            'cursor',
            'filter_by_gir_set',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credential_sets_stream_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credential_sets_stream_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credential_sets_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('text') is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if local_var_params.get('credential_set_name') is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if local_var_params.get('gir') is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if local_var_params.get('victim') is not None:  # noqa: E501
            query_params.append(('victim', local_var_params['victim']))  # noqa: E501
        if local_var_params.get('_from') is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if local_var_params.get('until') is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if local_var_params.get('last_updated_from') is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if local_var_params.get('last_updated_until') is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if local_var_params.get('cursor') is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if local_var_params.get('filter_by_gir_set') is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if local_var_params.get('count') is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        response_types_map = {
            200: "CredentialSetsStreamResponse",
            412: "CredentialSetsStreamGet412Response",
        }

        return self.api_client.call_api(
            '/credentialSets/stream', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def credentials_accessed_urls_get(self, **kwargs):  # noqa: E501
        """Search credential accessed urls  # noqa: E501

        Returns list of `Credential accessed urls` matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credentials_accessed_urls_get(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credentials.
        :type text: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param affiliation_group: Search by credential affiliation group.
        :type affiliation_group: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by the object's native time in descending (latest) or ascending (earliest) order
        :type sort: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CredentialAccessedUrlsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.credentials_accessed_urls_get_with_http_info(**kwargs)  # noqa: E501

    def credentials_accessed_urls_get_with_http_info(self, **kwargs):  # noqa: E501
        """Search credential accessed urls  # noqa: E501

        Returns list of `Credential accessed urls` matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credentials_accessed_urls_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credentials.
        :type text: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param affiliation_group: Search by credential affiliation group.
        :type affiliation_group: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by the object's native time in descending (latest) or ascending (earliest) order
        :type sort: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CredentialAccessedUrlsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'text',
            'credential_uid',
            'accessed_url',
            'domain',
            'affiliation_group',
            'gir',
            '_from',
            'until',
            'last_updated_from',
            'last_updated_until',
            'sort',
            'filter_by_gir_set',
            'offset',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credentials_accessed_urls_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `credentials_accessed_urls_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `credentials_accessed_urls_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credentials_accessed_urls_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credentials_accessed_urls_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('text') is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if local_var_params.get('credential_uid') is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if local_var_params.get('accessed_url') is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if local_var_params.get('domain') is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if local_var_params.get('affiliation_group') is not None:  # noqa: E501
            query_params.append(('affiliationGroup', local_var_params['affiliation_group']))  # noqa: E501
        if local_var_params.get('gir') is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if local_var_params.get('_from') is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if local_var_params.get('until') is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if local_var_params.get('last_updated_from') is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if local_var_params.get('last_updated_until') is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if local_var_params.get('sort') is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if local_var_params.get('filter_by_gir_set') is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if local_var_params.get('count') is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        response_types_map = {
            200: "CredentialAccessedUrlsResponse",
            412: "CredentialsGet412Response",
        }

        return self.api_client.call_api(
            '/credentials/accessedUrls', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def credentials_accessed_urls_stream_get(self, **kwargs):  # noqa: E501
        """Credential accessed url stream  # noqa: E501

        Returns list of `Credential accessed urls` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/credentials/accessedurls` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credentials_accessed_urls_stream_get(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credentials.
        :type text: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param affiliation_group: Search by credential affiliation group.
        :type affiliation_group: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param _from: Long unix time. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param cursor: Continue scrolling from cursor.
        :type cursor: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CredentialAccessedUrlsStreamResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.credentials_accessed_urls_stream_get_with_http_info(**kwargs)  # noqa: E501

    def credentials_accessed_urls_stream_get_with_http_info(self, **kwargs):  # noqa: E501
        """Credential accessed url stream  # noqa: E501

        Returns list of `Credential accessed urls` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/credentials/accessedurls` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credentials_accessed_urls_stream_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credentials.
        :type text: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param affiliation_group: Search by credential affiliation group.
        :type affiliation_group: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param _from: Long unix time. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param cursor: Continue scrolling from cursor.
        :type cursor: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CredentialAccessedUrlsStreamResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'text',
            'credential_uid',
            'accessed_url',
            'domain',
            'affiliation_group',
            'gir',
            '_from',
            'until',
            'last_updated_from',
            'last_updated_until',
            'cursor',
            'filter_by_gir_set',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credentials_accessed_urls_stream_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credentials_accessed_urls_stream_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credentials_accessed_urls_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('text') is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if local_var_params.get('credential_uid') is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if local_var_params.get('accessed_url') is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if local_var_params.get('domain') is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if local_var_params.get('affiliation_group') is not None:  # noqa: E501
            query_params.append(('affiliationGroup', local_var_params['affiliation_group']))  # noqa: E501
        if local_var_params.get('gir') is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if local_var_params.get('_from') is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if local_var_params.get('until') is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if local_var_params.get('last_updated_from') is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if local_var_params.get('last_updated_until') is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if local_var_params.get('cursor') is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if local_var_params.get('filter_by_gir_set') is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if local_var_params.get('count') is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        response_types_map = {
            200: "CredentialAccessedUrlsStreamResponse",
            412: "CredentialsStreamGet412Response",
        }

        return self.api_client.call_api(
            '/credentials/accessedUrls/stream', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def credentials_get(self, **kwargs):  # noqa: E501
        """Search credentials  # noqa: E501

        Returns list of `Credentials` matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credentials_get(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credentials.
        :type text: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param affiliation_group: Search by credential affiliation group.
        :type affiliation_group: str
        :param password_strength: Search by password strength.
        :type password_strength: str
        :param password_length_gte: Search by password complexity length field as greater then or equal to input value.
        :type password_length_gte: int
        :param password_lowercase_gte: Search by password complexity lowercase filed as greater then or equal to input value.
        :type password_lowercase_gte: int
        :param password_uppercase_gte: Search by password complexity uppercase filed as greater then or equal to input value.
        :type password_uppercase_gte: int
        :param password_numbers_gte: Search by password complexity numbers filed as greater then or equal to input value.
        :type password_numbers_gte: int
        :param password_punctuation_gte: Search by password complexity punctuation filed as greater then or equal to input value.
        :type password_punctuation_gte: int
        :param password_symbols_gte: Search by password complexity symbols filed as greater then or equal to input value.
        :type password_symbols_gte: int
        :param password_separators_gte: Search by password complexity separators filed as greater then or equal to input value.
        :type password_separators_gte: int
        :param password_other_gte: Search by password complexity other filed as greater then or equal to input value.
        :type password_other_gte: int
        :param password_entropy_gte: Search by password complexity entropy filed as greater then or equal to input value.
        :type password_entropy_gte: int
        :param password_plain: Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded.
        :type password_plain: str
        :param credential_login: Search by credential login.
        :type credential_login: str
        :param detected_malware: Search by credential detected malware.
        :type detected_malware: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by the object's native time in descending (latest) or ascending (earliest) order
        :type sort: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CredentialsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.credentials_get_with_http_info(**kwargs)  # noqa: E501

    def credentials_get_with_http_info(self, **kwargs):  # noqa: E501
        """Search credentials  # noqa: E501

        Returns list of `Credentials` matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credentials_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credentials.
        :type text: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param affiliation_group: Search by credential affiliation group.
        :type affiliation_group: str
        :param password_strength: Search by password strength.
        :type password_strength: str
        :param password_length_gte: Search by password complexity length field as greater then or equal to input value.
        :type password_length_gte: int
        :param password_lowercase_gte: Search by password complexity lowercase filed as greater then or equal to input value.
        :type password_lowercase_gte: int
        :param password_uppercase_gte: Search by password complexity uppercase filed as greater then or equal to input value.
        :type password_uppercase_gte: int
        :param password_numbers_gte: Search by password complexity numbers filed as greater then or equal to input value.
        :type password_numbers_gte: int
        :param password_punctuation_gte: Search by password complexity punctuation filed as greater then or equal to input value.
        :type password_punctuation_gte: int
        :param password_symbols_gte: Search by password complexity symbols filed as greater then or equal to input value.
        :type password_symbols_gte: int
        :param password_separators_gte: Search by password complexity separators filed as greater then or equal to input value.
        :type password_separators_gte: int
        :param password_other_gte: Search by password complexity other filed as greater then or equal to input value.
        :type password_other_gte: int
        :param password_entropy_gte: Search by password complexity entropy filed as greater then or equal to input value.
        :type password_entropy_gte: int
        :param password_plain: Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded.
        :type password_plain: str
        :param credential_login: Search by credential login.
        :type credential_login: str
        :param detected_malware: Search by credential detected malware.
        :type detected_malware: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by the object's native time in descending (latest) or ascending (earliest) order
        :type sort: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CredentialsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'text',
            'credential_uid',
            'credential_set_name',
            'credential_set_uid',
            'domain',
            'affiliation_group',
            'password_strength',
            'password_length_gte',
            'password_lowercase_gte',
            'password_uppercase_gte',
            'password_numbers_gte',
            'password_punctuation_gte',
            'password_symbols_gte',
            'password_separators_gte',
            'password_other_gte',
            'password_entropy_gte',
            'password_plain',
            'credential_login',
            'detected_malware',
            'gir',
            '_from',
            'until',
            'last_updated_from',
            'last_updated_until',
            'sort',
            'filter_by_gir_set',
            'offset',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credentials_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'password_length_gte' in local_var_params and local_var_params['password_length_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_length_gte` when calling `credentials_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_lowercase_gte' in local_var_params and local_var_params['password_lowercase_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_lowercase_gte` when calling `credentials_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_uppercase_gte' in local_var_params and local_var_params['password_uppercase_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_uppercase_gte` when calling `credentials_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_numbers_gte' in local_var_params and local_var_params['password_numbers_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_numbers_gte` when calling `credentials_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_punctuation_gte' in local_var_params and local_var_params['password_punctuation_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_punctuation_gte` when calling `credentials_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_symbols_gte' in local_var_params and local_var_params['password_symbols_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_symbols_gte` when calling `credentials_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_separators_gte' in local_var_params and local_var_params['password_separators_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_separators_gte` when calling `credentials_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_other_gte' in local_var_params and local_var_params['password_other_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_other_gte` when calling `credentials_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_entropy_gte' in local_var_params and local_var_params['password_entropy_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_entropy_gte` when calling `credentials_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `credentials_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `credentials_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credentials_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credentials_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('text') is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if local_var_params.get('credential_uid') is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if local_var_params.get('credential_set_name') is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if local_var_params.get('credential_set_uid') is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if local_var_params.get('domain') is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if local_var_params.get('affiliation_group') is not None:  # noqa: E501
            query_params.append(('affiliationGroup', local_var_params['affiliation_group']))  # noqa: E501
        if local_var_params.get('password_strength') is not None:  # noqa: E501
            query_params.append(('passwordStrength', local_var_params['password_strength']))  # noqa: E501
        if local_var_params.get('password_length_gte') is not None:  # noqa: E501
            query_params.append(('passwordLengthGte', local_var_params['password_length_gte']))  # noqa: E501
        if local_var_params.get('password_lowercase_gte') is not None:  # noqa: E501
            query_params.append(('passwordLowercaseGte', local_var_params['password_lowercase_gte']))  # noqa: E501
        if local_var_params.get('password_uppercase_gte') is not None:  # noqa: E501
            query_params.append(('passwordUppercaseGte', local_var_params['password_uppercase_gte']))  # noqa: E501
        if local_var_params.get('password_numbers_gte') is not None:  # noqa: E501
            query_params.append(('passwordNumbersGte', local_var_params['password_numbers_gte']))  # noqa: E501
        if local_var_params.get('password_punctuation_gte') is not None:  # noqa: E501
            query_params.append(('passwordPunctuationGte', local_var_params['password_punctuation_gte']))  # noqa: E501
        if local_var_params.get('password_symbols_gte') is not None:  # noqa: E501
            query_params.append(('passwordSymbolsGte', local_var_params['password_symbols_gte']))  # noqa: E501
        if local_var_params.get('password_separators_gte') is not None:  # noqa: E501
            query_params.append(('passwordSeparatorsGte', local_var_params['password_separators_gte']))  # noqa: E501
        if local_var_params.get('password_other_gte') is not None:  # noqa: E501
            query_params.append(('passwordOtherGte', local_var_params['password_other_gte']))  # noqa: E501
        if local_var_params.get('password_entropy_gte') is not None:  # noqa: E501
            query_params.append(('passwordEntropyGte', local_var_params['password_entropy_gte']))  # noqa: E501
        if local_var_params.get('password_plain') is not None:  # noqa: E501
            query_params.append(('passwordPlain', local_var_params['password_plain']))  # noqa: E501
        if local_var_params.get('credential_login') is not None:  # noqa: E501
            query_params.append(('credentialLogin', local_var_params['credential_login']))  # noqa: E501
        if local_var_params.get('detected_malware') is not None:  # noqa: E501
            query_params.append(('detectedMalware', local_var_params['detected_malware']))  # noqa: E501
        if local_var_params.get('gir') is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if local_var_params.get('_from') is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if local_var_params.get('until') is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if local_var_params.get('last_updated_from') is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if local_var_params.get('last_updated_until') is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if local_var_params.get('sort') is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if local_var_params.get('filter_by_gir_set') is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if local_var_params.get('count') is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        response_types_map = {
            200: "CredentialsResponse",
            412: "CredentialsGet412Response",
        }

        return self.api_client.call_api(
            '/credentials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def credentials_occurrences_get(self, **kwargs):  # noqa: E501
        """Search credential occurrences  # noqa: E501

        Returns list of `Credential occurrences` matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credentials_occurrences_get(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credential occurrences.
        :type text: str
        :param credential_occurrence_uid: Search by credential occurrence uid.
        :type credential_occurrence_uid: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param affiliation_group: Search by credential affiliation group.
        :type affiliation_group: str
        :param password_strength: Search by password strength.
        :type password_strength: str
        :param password_length_gte: Search by password complexity length field as greater then or equal to input value.
        :type password_length_gte: int
        :param password_lowercase_gte: Search by password complexity lowercase filed as greater then or equal to input value.
        :type password_lowercase_gte: int
        :param password_uppercase_gte: Search by password complexity uppercase filed as greater then or equal to input value.
        :type password_uppercase_gte: int
        :param password_numbers_gte: Search by password complexity numbers filed as greater then or equal to input value.
        :type password_numbers_gte: int
        :param password_punctuation_gte: Search by password complexity punctuation filed as greater then or equal to input value.
        :type password_punctuation_gte: int
        :param password_symbols_gte: Search by password complexity symbols filed as greater then or equal to input value.
        :type password_symbols_gte: int
        :param password_separators_gte: Search by password complexity separators filed as greater then or equal to input value.
        :type password_separators_gte: int
        :param password_other_gte: Search by password complexity other filed as greater then or equal to input value.
        :type password_other_gte: int
        :param password_entropy_gte: Search by password complexity entropy filed as greater then or equal to input value.
        :type password_entropy_gte: int
        :param password_plain: Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded.
        :type password_plain: str
        :param credential_login: Search by credential login.
        :type credential_login: str
        :param detected_malware: Search by credential detected malware.
        :type detected_malware: str
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by the object's native time in descending (latest) or ascending (earliest) order
        :type sort: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CredentialOccurrencesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.credentials_occurrences_get_with_http_info(**kwargs)  # noqa: E501

    def credentials_occurrences_get_with_http_info(self, **kwargs):  # noqa: E501
        """Search credential occurrences  # noqa: E501

        Returns list of `Credential occurrences` matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credentials_occurrences_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credential occurrences.
        :type text: str
        :param credential_occurrence_uid: Search by credential occurrence uid.
        :type credential_occurrence_uid: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param affiliation_group: Search by credential affiliation group.
        :type affiliation_group: str
        :param password_strength: Search by password strength.
        :type password_strength: str
        :param password_length_gte: Search by password complexity length field as greater then or equal to input value.
        :type password_length_gte: int
        :param password_lowercase_gte: Search by password complexity lowercase filed as greater then or equal to input value.
        :type password_lowercase_gte: int
        :param password_uppercase_gte: Search by password complexity uppercase filed as greater then or equal to input value.
        :type password_uppercase_gte: int
        :param password_numbers_gte: Search by password complexity numbers filed as greater then or equal to input value.
        :type password_numbers_gte: int
        :param password_punctuation_gte: Search by password complexity punctuation filed as greater then or equal to input value.
        :type password_punctuation_gte: int
        :param password_symbols_gte: Search by password complexity symbols filed as greater then or equal to input value.
        :type password_symbols_gte: int
        :param password_separators_gte: Search by password complexity separators filed as greater then or equal to input value.
        :type password_separators_gte: int
        :param password_other_gte: Search by password complexity other filed as greater then or equal to input value.
        :type password_other_gte: int
        :param password_entropy_gte: Search by password complexity entropy filed as greater then or equal to input value.
        :type password_entropy_gte: int
        :param password_plain: Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded.
        :type password_plain: str
        :param credential_login: Search by credential login.
        :type credential_login: str
        :param detected_malware: Search by credential detected malware.
        :type detected_malware: str
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by the object's native time in descending (latest) or ascending (earliest) order
        :type sort: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CredentialOccurrencesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'text',
            'credential_occurrence_uid',
            'credential_uid',
            'credential_set_name',
            'credential_set_uid',
            'domain',
            'affiliation_group',
            'password_strength',
            'password_length_gte',
            'password_lowercase_gte',
            'password_uppercase_gte',
            'password_numbers_gte',
            'password_punctuation_gte',
            'password_symbols_gte',
            'password_separators_gte',
            'password_other_gte',
            'password_entropy_gte',
            'password_plain',
            'credential_login',
            'detected_malware',
            'accessed_url',
            'gir',
            '_from',
            'until',
            'last_updated_from',
            'last_updated_until',
            'sort',
            'filter_by_gir_set',
            'offset',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credentials_occurrences_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'password_length_gte' in local_var_params and local_var_params['password_length_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_length_gte` when calling `credentials_occurrences_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_lowercase_gte' in local_var_params and local_var_params['password_lowercase_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_lowercase_gte` when calling `credentials_occurrences_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_uppercase_gte' in local_var_params and local_var_params['password_uppercase_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_uppercase_gte` when calling `credentials_occurrences_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_numbers_gte' in local_var_params and local_var_params['password_numbers_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_numbers_gte` when calling `credentials_occurrences_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_punctuation_gte' in local_var_params and local_var_params['password_punctuation_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_punctuation_gte` when calling `credentials_occurrences_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_symbols_gte' in local_var_params and local_var_params['password_symbols_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_symbols_gte` when calling `credentials_occurrences_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_separators_gte' in local_var_params and local_var_params['password_separators_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_separators_gte` when calling `credentials_occurrences_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_other_gte' in local_var_params and local_var_params['password_other_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_other_gte` when calling `credentials_occurrences_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_entropy_gte' in local_var_params and local_var_params['password_entropy_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_entropy_gte` when calling `credentials_occurrences_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `credentials_occurrences_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `credentials_occurrences_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credentials_occurrences_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credentials_occurrences_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('text') is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if local_var_params.get('credential_occurrence_uid') is not None:  # noqa: E501
            query_params.append(('credentialOccurrenceUid', local_var_params['credential_occurrence_uid']))  # noqa: E501
        if local_var_params.get('credential_uid') is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if local_var_params.get('credential_set_name') is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if local_var_params.get('credential_set_uid') is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if local_var_params.get('domain') is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if local_var_params.get('affiliation_group') is not None:  # noqa: E501
            query_params.append(('affiliationGroup', local_var_params['affiliation_group']))  # noqa: E501
        if local_var_params.get('password_strength') is not None:  # noqa: E501
            query_params.append(('passwordStrength', local_var_params['password_strength']))  # noqa: E501
        if local_var_params.get('password_length_gte') is not None:  # noqa: E501
            query_params.append(('passwordLengthGte', local_var_params['password_length_gte']))  # noqa: E501
        if local_var_params.get('password_lowercase_gte') is not None:  # noqa: E501
            query_params.append(('passwordLowercaseGte', local_var_params['password_lowercase_gte']))  # noqa: E501
        if local_var_params.get('password_uppercase_gte') is not None:  # noqa: E501
            query_params.append(('passwordUppercaseGte', local_var_params['password_uppercase_gte']))  # noqa: E501
        if local_var_params.get('password_numbers_gte') is not None:  # noqa: E501
            query_params.append(('passwordNumbersGte', local_var_params['password_numbers_gte']))  # noqa: E501
        if local_var_params.get('password_punctuation_gte') is not None:  # noqa: E501
            query_params.append(('passwordPunctuationGte', local_var_params['password_punctuation_gte']))  # noqa: E501
        if local_var_params.get('password_symbols_gte') is not None:  # noqa: E501
            query_params.append(('passwordSymbolsGte', local_var_params['password_symbols_gte']))  # noqa: E501
        if local_var_params.get('password_separators_gte') is not None:  # noqa: E501
            query_params.append(('passwordSeparatorsGte', local_var_params['password_separators_gte']))  # noqa: E501
        if local_var_params.get('password_other_gte') is not None:  # noqa: E501
            query_params.append(('passwordOtherGte', local_var_params['password_other_gte']))  # noqa: E501
        if local_var_params.get('password_entropy_gte') is not None:  # noqa: E501
            query_params.append(('passwordEntropyGte', local_var_params['password_entropy_gte']))  # noqa: E501
        if local_var_params.get('password_plain') is not None:  # noqa: E501
            query_params.append(('passwordPlain', local_var_params['password_plain']))  # noqa: E501
        if local_var_params.get('credential_login') is not None:  # noqa: E501
            query_params.append(('credentialLogin', local_var_params['credential_login']))  # noqa: E501
        if local_var_params.get('detected_malware') is not None:  # noqa: E501
            query_params.append(('detectedMalware', local_var_params['detected_malware']))  # noqa: E501
        if local_var_params.get('accessed_url') is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if local_var_params.get('gir') is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if local_var_params.get('_from') is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if local_var_params.get('until') is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if local_var_params.get('last_updated_from') is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if local_var_params.get('last_updated_until') is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if local_var_params.get('sort') is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if local_var_params.get('filter_by_gir_set') is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if local_var_params.get('count') is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        response_types_map = {
            200: "CredentialOccurrencesResponse",
            412: "CredentialsGet412Response",
        }

        return self.api_client.call_api(
            '/credentials/occurrences', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def credentials_occurrences_stream_get(self, **kwargs):  # noqa: E501
        """Credential occurrence stream  # noqa: E501

        Returns list of `Credential occurrences` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/credentials/occurrences` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credentials_occurrences_stream_get(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credential occurrences.
        :type text: str
        :param credential_occurrence_uid: Search by credential occurrence uid.
        :type credential_occurrence_uid: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param affiliation_group: Search by credential affiliation group.
        :type affiliation_group: str
        :param password_strength: Search by password strength.
        :type password_strength: str
        :param password_length_gte: Search by password complexity length field as greater then or equal to input value.
        :type password_length_gte: int
        :param password_lowercase_gte: Search by password complexity lowercase filed as greater then or equal to input value.
        :type password_lowercase_gte: int
        :param password_uppercase_gte: Search by password complexity uppercase filed as greater then or equal to input value.
        :type password_uppercase_gte: int
        :param password_numbers_gte: Search by password complexity numbers filed as greater then or equal to input value.
        :type password_numbers_gte: int
        :param password_punctuation_gte: Search by password complexity punctuation filed as greater then or equal to input value.
        :type password_punctuation_gte: int
        :param password_symbols_gte: Search by password complexity symbols filed as greater then or equal to input value.
        :type password_symbols_gte: int
        :param password_separators_gte: Search by password complexity separators filed as greater then or equal to input value.
        :type password_separators_gte: int
        :param password_other_gte: Search by password complexity other filed as greater then or equal to input value.
        :type password_other_gte: int
        :param password_entropy_gte: Search by password complexity entropy filed as greater then or equal to input value.
        :type password_entropy_gte: int
        :param password_plain: Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded.
        :type password_plain: str
        :param credential_login: Search by credential login.
        :type credential_login: str
        :param detected_malware: Search by credential detected malware.
        :type detected_malware: str
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param _from: Long unix time. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param cursor: Continue scrolling from cursor.
        :type cursor: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CredentialOccurrencesStreamResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.credentials_occurrences_stream_get_with_http_info(**kwargs)  # noqa: E501

    def credentials_occurrences_stream_get_with_http_info(self, **kwargs):  # noqa: E501
        """Credential occurrence stream  # noqa: E501

        Returns list of `Credential occurrences` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/credentials/occurrences` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credentials_occurrences_stream_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credential occurrences.
        :type text: str
        :param credential_occurrence_uid: Search by credential occurrence uid.
        :type credential_occurrence_uid: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param affiliation_group: Search by credential affiliation group.
        :type affiliation_group: str
        :param password_strength: Search by password strength.
        :type password_strength: str
        :param password_length_gte: Search by password complexity length field as greater then or equal to input value.
        :type password_length_gte: int
        :param password_lowercase_gte: Search by password complexity lowercase filed as greater then or equal to input value.
        :type password_lowercase_gte: int
        :param password_uppercase_gte: Search by password complexity uppercase filed as greater then or equal to input value.
        :type password_uppercase_gte: int
        :param password_numbers_gte: Search by password complexity numbers filed as greater then or equal to input value.
        :type password_numbers_gte: int
        :param password_punctuation_gte: Search by password complexity punctuation filed as greater then or equal to input value.
        :type password_punctuation_gte: int
        :param password_symbols_gte: Search by password complexity symbols filed as greater then or equal to input value.
        :type password_symbols_gte: int
        :param password_separators_gte: Search by password complexity separators filed as greater then or equal to input value.
        :type password_separators_gte: int
        :param password_other_gte: Search by password complexity other filed as greater then or equal to input value.
        :type password_other_gte: int
        :param password_entropy_gte: Search by password complexity entropy filed as greater then or equal to input value.
        :type password_entropy_gte: int
        :param password_plain: Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded.
        :type password_plain: str
        :param credential_login: Search by credential login.
        :type credential_login: str
        :param detected_malware: Search by credential detected malware.
        :type detected_malware: str
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param _from: Long unix time. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param cursor: Continue scrolling from cursor.
        :type cursor: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CredentialOccurrencesStreamResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'text',
            'credential_occurrence_uid',
            'credential_uid',
            'credential_set_name',
            'credential_set_uid',
            'domain',
            'affiliation_group',
            'password_strength',
            'password_length_gte',
            'password_lowercase_gte',
            'password_uppercase_gte',
            'password_numbers_gte',
            'password_punctuation_gte',
            'password_symbols_gte',
            'password_separators_gte',
            'password_other_gte',
            'password_entropy_gte',
            'password_plain',
            'credential_login',
            'detected_malware',
            'accessed_url',
            'gir',
            '_from',
            'until',
            'last_updated_from',
            'last_updated_until',
            'cursor',
            'filter_by_gir_set',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credentials_occurrences_stream_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'password_length_gte' in local_var_params and local_var_params['password_length_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_length_gte` when calling `credentials_occurrences_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_lowercase_gte' in local_var_params and local_var_params['password_lowercase_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_lowercase_gte` when calling `credentials_occurrences_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_uppercase_gte' in local_var_params and local_var_params['password_uppercase_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_uppercase_gte` when calling `credentials_occurrences_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_numbers_gte' in local_var_params and local_var_params['password_numbers_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_numbers_gte` when calling `credentials_occurrences_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_punctuation_gte' in local_var_params and local_var_params['password_punctuation_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_punctuation_gte` when calling `credentials_occurrences_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_symbols_gte' in local_var_params and local_var_params['password_symbols_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_symbols_gte` when calling `credentials_occurrences_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_separators_gte' in local_var_params and local_var_params['password_separators_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_separators_gte` when calling `credentials_occurrences_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_other_gte' in local_var_params and local_var_params['password_other_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_other_gte` when calling `credentials_occurrences_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_entropy_gte' in local_var_params and local_var_params['password_entropy_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_entropy_gte` when calling `credentials_occurrences_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credentials_occurrences_stream_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credentials_occurrences_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('text') is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if local_var_params.get('credential_occurrence_uid') is not None:  # noqa: E501
            query_params.append(('credentialOccurrenceUid', local_var_params['credential_occurrence_uid']))  # noqa: E501
        if local_var_params.get('credential_uid') is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if local_var_params.get('credential_set_name') is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if local_var_params.get('credential_set_uid') is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if local_var_params.get('domain') is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if local_var_params.get('affiliation_group') is not None:  # noqa: E501
            query_params.append(('affiliationGroup', local_var_params['affiliation_group']))  # noqa: E501
        if local_var_params.get('password_strength') is not None:  # noqa: E501
            query_params.append(('passwordStrength', local_var_params['password_strength']))  # noqa: E501
        if local_var_params.get('password_length_gte') is not None:  # noqa: E501
            query_params.append(('passwordLengthGte', local_var_params['password_length_gte']))  # noqa: E501
        if local_var_params.get('password_lowercase_gte') is not None:  # noqa: E501
            query_params.append(('passwordLowercaseGte', local_var_params['password_lowercase_gte']))  # noqa: E501
        if local_var_params.get('password_uppercase_gte') is not None:  # noqa: E501
            query_params.append(('passwordUppercaseGte', local_var_params['password_uppercase_gte']))  # noqa: E501
        if local_var_params.get('password_numbers_gte') is not None:  # noqa: E501
            query_params.append(('passwordNumbersGte', local_var_params['password_numbers_gte']))  # noqa: E501
        if local_var_params.get('password_punctuation_gte') is not None:  # noqa: E501
            query_params.append(('passwordPunctuationGte', local_var_params['password_punctuation_gte']))  # noqa: E501
        if local_var_params.get('password_symbols_gte') is not None:  # noqa: E501
            query_params.append(('passwordSymbolsGte', local_var_params['password_symbols_gte']))  # noqa: E501
        if local_var_params.get('password_separators_gte') is not None:  # noqa: E501
            query_params.append(('passwordSeparatorsGte', local_var_params['password_separators_gte']))  # noqa: E501
        if local_var_params.get('password_other_gte') is not None:  # noqa: E501
            query_params.append(('passwordOtherGte', local_var_params['password_other_gte']))  # noqa: E501
        if local_var_params.get('password_entropy_gte') is not None:  # noqa: E501
            query_params.append(('passwordEntropyGte', local_var_params['password_entropy_gte']))  # noqa: E501
        if local_var_params.get('password_plain') is not None:  # noqa: E501
            query_params.append(('passwordPlain', local_var_params['password_plain']))  # noqa: E501
        if local_var_params.get('credential_login') is not None:  # noqa: E501
            query_params.append(('credentialLogin', local_var_params['credential_login']))  # noqa: E501
        if local_var_params.get('detected_malware') is not None:  # noqa: E501
            query_params.append(('detectedMalware', local_var_params['detected_malware']))  # noqa: E501
        if local_var_params.get('accessed_url') is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if local_var_params.get('gir') is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if local_var_params.get('_from') is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if local_var_params.get('until') is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if local_var_params.get('last_updated_from') is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if local_var_params.get('last_updated_until') is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if local_var_params.get('cursor') is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if local_var_params.get('filter_by_gir_set') is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if local_var_params.get('count') is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        response_types_map = {
            200: "CredentialOccurrencesStreamResponse",
            412: "CredentialsStreamGet412Response",
        }

        return self.api_client.call_api(
            '/credentials/occurrences/stream', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def credentials_stream_get(self, **kwargs):  # noqa: E501
        """Credential stream  # noqa: E501

        Returns list of `Credentials` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/credentials` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credentials_stream_get(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credentials.
        :type text: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param affiliation_group: Search by credential affiliation group.
        :type affiliation_group: str
        :param password_strength: Search by password strength.
        :type password_strength: str
        :param password_length_gte: Search by password complexity length field as greater then or equal to input value.
        :type password_length_gte: int
        :param password_lowercase_gte: Search by password complexity lowercase filed as greater then or equal to input value.
        :type password_lowercase_gte: int
        :param password_uppercase_gte: Search by password complexity uppercase filed as greater then or equal to input value.
        :type password_uppercase_gte: int
        :param password_numbers_gte: Search by password complexity numbers filed as greater then or equal to input value.
        :type password_numbers_gte: int
        :param password_punctuation_gte: Search by password complexity punctuation filed as greater then or equal to input value.
        :type password_punctuation_gte: int
        :param password_symbols_gte: Search by password complexity symbols filed as greater then or equal to input value.
        :type password_symbols_gte: int
        :param password_separators_gte: Search by password complexity separators filed as greater then or equal to input value.
        :type password_separators_gte: int
        :param password_other_gte: Search by password complexity other filed as greater then or equal to input value.
        :type password_other_gte: int
        :param password_entropy_gte: Search by password complexity entropy filed as greater then or equal to input value.
        :type password_entropy_gte: int
        :param password_plain: Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded.
        :type password_plain: str
        :param credential_login: Search by credential login.
        :type credential_login: str
        :param detected_malware: Search by credential detected malware.
        :type detected_malware: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param cursor: Continue scrolling from cursor.
        :type cursor: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CredentialsStreamResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.credentials_stream_get_with_http_info(**kwargs)  # noqa: E501

    def credentials_stream_get_with_http_info(self, **kwargs):  # noqa: E501
        """Credential stream  # noqa: E501

        Returns list of `Credentials` matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the `/credentials` endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field. <br />Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credentials_stream_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere in credentials.
        :type text: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param affiliation_group: Search by credential affiliation group.
        :type affiliation_group: str
        :param password_strength: Search by password strength.
        :type password_strength: str
        :param password_length_gte: Search by password complexity length field as greater then or equal to input value.
        :type password_length_gte: int
        :param password_lowercase_gte: Search by password complexity lowercase filed as greater then or equal to input value.
        :type password_lowercase_gte: int
        :param password_uppercase_gte: Search by password complexity uppercase filed as greater then or equal to input value.
        :type password_uppercase_gte: int
        :param password_numbers_gte: Search by password complexity numbers filed as greater then or equal to input value.
        :type password_numbers_gte: int
        :param password_punctuation_gte: Search by password complexity punctuation filed as greater then or equal to input value.
        :type password_punctuation_gte: int
        :param password_symbols_gte: Search by password complexity symbols filed as greater then or equal to input value.
        :type password_symbols_gte: int
        :param password_separators_gte: Search by password complexity separators filed as greater then or equal to input value.
        :type password_separators_gte: int
        :param password_other_gte: Search by password complexity other filed as greater then or equal to input value.
        :type password_other_gte: int
        :param password_entropy_gte: Search by password complexity entropy filed as greater then or equal to input value.
        :type password_entropy_gte: int
        :param password_plain: Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded.
        :type password_plain: str
        :param credential_login: Search by credential login.
        :type credential_login: str
        :param detected_malware: Search by credential detected malware.
        :type detected_malware: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param cursor: Continue scrolling from cursor.
        :type cursor: str
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CredentialsStreamResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'text',
            'credential_uid',
            'credential_set_name',
            'credential_set_uid',
            'domain',
            'affiliation_group',
            'password_strength',
            'password_length_gte',
            'password_lowercase_gte',
            'password_uppercase_gte',
            'password_numbers_gte',
            'password_punctuation_gte',
            'password_symbols_gte',
            'password_separators_gte',
            'password_other_gte',
            'password_entropy_gte',
            'password_plain',
            'credential_login',
            'detected_malware',
            'gir',
            '_from',
            'until',
            'last_updated_from',
            'last_updated_until',
            'cursor',
            'filter_by_gir_set',
            'count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credentials_stream_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'password_length_gte' in local_var_params and local_var_params['password_length_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_length_gte` when calling `credentials_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_lowercase_gte' in local_var_params and local_var_params['password_lowercase_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_lowercase_gte` when calling `credentials_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_uppercase_gte' in local_var_params and local_var_params['password_uppercase_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_uppercase_gte` when calling `credentials_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_numbers_gte' in local_var_params and local_var_params['password_numbers_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_numbers_gte` when calling `credentials_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_punctuation_gte' in local_var_params and local_var_params['password_punctuation_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_punctuation_gte` when calling `credentials_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_symbols_gte' in local_var_params and local_var_params['password_symbols_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_symbols_gte` when calling `credentials_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_separators_gte' in local_var_params and local_var_params['password_separators_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_separators_gte` when calling `credentials_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_other_gte' in local_var_params and local_var_params['password_other_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_other_gte` when calling `credentials_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_entropy_gte' in local_var_params and local_var_params['password_entropy_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_entropy_gte` when calling `credentials_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credentials_stream_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `credentials_stream_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('text') is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if local_var_params.get('credential_uid') is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if local_var_params.get('credential_set_name') is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if local_var_params.get('credential_set_uid') is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if local_var_params.get('domain') is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if local_var_params.get('affiliation_group') is not None:  # noqa: E501
            query_params.append(('affiliationGroup', local_var_params['affiliation_group']))  # noqa: E501
        if local_var_params.get('password_strength') is not None:  # noqa: E501
            query_params.append(('passwordStrength', local_var_params['password_strength']))  # noqa: E501
        if local_var_params.get('password_length_gte') is not None:  # noqa: E501
            query_params.append(('passwordLengthGte', local_var_params['password_length_gte']))  # noqa: E501
        if local_var_params.get('password_lowercase_gte') is not None:  # noqa: E501
            query_params.append(('passwordLowercaseGte', local_var_params['password_lowercase_gte']))  # noqa: E501
        if local_var_params.get('password_uppercase_gte') is not None:  # noqa: E501
            query_params.append(('passwordUppercaseGte', local_var_params['password_uppercase_gte']))  # noqa: E501
        if local_var_params.get('password_numbers_gte') is not None:  # noqa: E501
            query_params.append(('passwordNumbersGte', local_var_params['password_numbers_gte']))  # noqa: E501
        if local_var_params.get('password_punctuation_gte') is not None:  # noqa: E501
            query_params.append(('passwordPunctuationGte', local_var_params['password_punctuation_gte']))  # noqa: E501
        if local_var_params.get('password_symbols_gte') is not None:  # noqa: E501
            query_params.append(('passwordSymbolsGte', local_var_params['password_symbols_gte']))  # noqa: E501
        if local_var_params.get('password_separators_gte') is not None:  # noqa: E501
            query_params.append(('passwordSeparatorsGte', local_var_params['password_separators_gte']))  # noqa: E501
        if local_var_params.get('password_other_gte') is not None:  # noqa: E501
            query_params.append(('passwordOtherGte', local_var_params['password_other_gte']))  # noqa: E501
        if local_var_params.get('password_entropy_gte') is not None:  # noqa: E501
            query_params.append(('passwordEntropyGte', local_var_params['password_entropy_gte']))  # noqa: E501
        if local_var_params.get('password_plain') is not None:  # noqa: E501
            query_params.append(('passwordPlain', local_var_params['password_plain']))  # noqa: E501
        if local_var_params.get('credential_login') is not None:  # noqa: E501
            query_params.append(('credentialLogin', local_var_params['credential_login']))  # noqa: E501
        if local_var_params.get('detected_malware') is not None:  # noqa: E501
            query_params.append(('detectedMalware', local_var_params['detected_malware']))  # noqa: E501
        if local_var_params.get('gir') is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if local_var_params.get('_from') is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if local_var_params.get('until') is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if local_var_params.get('last_updated_from') is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if local_var_params.get('last_updated_until') is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if local_var_params.get('cursor') is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if local_var_params.get('filter_by_gir_set') is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if local_var_params.get('count') is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        response_types_map = {
            200: "CredentialsStreamResponse",
            412: "CredentialsStreamGet412Response",
        }

        return self.api_client.call_api(
            '/credentials/stream', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
