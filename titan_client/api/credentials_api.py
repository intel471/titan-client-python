# coding: utf-8

"""
    Titan API v1

    # Introduction The Intel 471 API is organized around the principles of REST. Our API lets you gather results from our platform with anything that can send a HTTP request, including cURL and modern internet browsers. Access to this API requires an API token which is managed from your account settings.  Intel 471 reserves the right to add fields to our API however we will provide backwards compatibility and older version support so that it will be possible to choose exact versions that provide a response with an older structure. This documentation tracks all API versions and it is possible to compare this version which has changes highlighted. Please consider not storing information provided by API locally as we constantly improving our data set and want you to have the most updated information.  # Authentication Authenticate to the Intel 471 API by providing your API key in the request. Your API key carries many privileges so please do not expose them on public web resources.  Authentication to the API occurs by providing your email address as the login and API key as password in the authorization header via HTTP Basic Auth. Your API key can be found in the [API](https://portal.intel471.com/api) section on the portal.  # Accessing API ## Via internet browser Just open url: `https://api.intel471.com/v1/reports` Browser will ask for credentials, provide your email as login and API key as password. ## Via curl command line utility Type in terminal the following command: ``` curl -u <YOU EMAIL>:<YOUR API KEY> https://api.intel471.com/v1/reports ``` ## CURL usage examples This section covers some Watchers API requests.  ### List watcher groups: Type in terminal the following command:  *curl -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  ### Create watcher group: To create watcher group you need to pass a json body to request. Passing json body possible in two ways:  #### Write json to request *curl -d'{\"name\": \"group_name\", \"description\": \"Description\"}' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  #### Write json to file and call it *curl -d\"@json_file_name\" -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  ### Create free text search watcher: *curl -d'{\"type\": \"search\", \"freeTextPattern\": \"text to search\", \"notificationChannel\": \"website\"}' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups/\"GROUP UID\"/watchers*  ### Create specific search watcher: *curl -d'{\"type\": \"search\", \"patterns\":[ { \"types\": \"Actor\" , \"pattern\": \"swisman\" } ], \"notificationChannel\": \"website\" }' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups/\"GROUP UID\"/watchers*  ## Via Python Execute the following script: ``` import urllib2, base64  username = \"<YOU EMAIL>\" apikey = \"<YOUR API KEY>\"  request = urllib2.Request(\"https://api.intel471.com/v1/reports\") base64string = base64.encodestring('%s:%s' % (username, apikey)).replace('\\n', '') request.add_header(\"Authorization\", \"Basic %s\" % base64string) result = urllib2.urlopen(request) response_in_json = result.read()  print response_in_json ``` # API integration best practice with your application When accessing our API from your application don't do AJAX calls directly from web browser to https://api.intel471.com/. We do not allow CORS requests from browser due to potential security issues. Instead we suggest you look to establish a kind of a server side proxy in your application which will pass requests to our API.  For example: you can send a request from browser javascript to your server side, for instance to url `/apiproxy/actors?actor=hacker` which will be internally passed to `https://api.intel471.com/v1/actors?actor=hacker` (with authentication headers added) and response will be sent back to the browser.  # Versioning support We are consistently improving our API and occasionally bring in changes to the API based on customer feedback. The current API version can be seen in the drop down boxes for each version. We are providing API backwards compatibility when possible. All requests are prefixed with the major version number, for example `/v1`: ``` https://api.intel471.com/v1/reports ```  Different major versions are not compatible and imply significant response structure changes. Minor versions differences might include extra fields in response or provide new request parameter support. To stick to the specific version, just add the following extra parameter to the request, for example: `?v=1.2.0`. If you specify a not existing version, it will be brought down to the nearest existing one. For example, parameter `?v=1.5.4` will call API of version 1.3.0 — the latest available; `?v=1.2.9` will awake version 1.2.0 and so on.  Omitting the version parameter from your request means you will always use the latest version of the API.  We highly recommend you always add the version parameter to be safe on API updates and code your integration in a way to accept possible future extra fields added to the response object. ``` https://api.intel471.com/v1/tags?prettyPrint - will return response for the latest API version (v.1.1.0) https://api.intel471.com/v1/tags?prettyPrint&v=1.1.0 - absolutely the same request with the version explicitly specified https://api.intel471.com/v1/reports?prettyPrint&v=1.0.0 - will return response compatible with the older version ```   # noqa: E501

    The version of the OpenAPI document: 1.19.0
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
                '_request_auth'
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
        if 'text' in local_var_params and local_var_params['text'] is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if 'credential_set_name' in local_var_params and local_var_params['credential_set_name'] is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if 'credential_set_uid' in local_var_params and local_var_params['credential_set_uid'] is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if 'accessed_url' in local_var_params and local_var_params['accessed_url'] is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if 'gir' in local_var_params and local_var_params['gir'] is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if 'victim' in local_var_params and local_var_params['victim'] is not None:  # noqa: E501
            query_params.append(('victim', local_var_params['victim']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'until' in local_var_params and local_var_params['until'] is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if 'last_updated_from' in local_var_params and local_var_params['last_updated_from'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if 'last_updated_until' in local_var_params and local_var_params['last_updated_until'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'filter_by_gir_set' in local_var_params and local_var_params['filter_by_gir_set'] is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

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
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstringstringstringstringstring",
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
                '_request_auth'
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
        if 'text' in local_var_params and local_var_params['text'] is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if 'credential_set_name' in local_var_params and local_var_params['credential_set_name'] is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if 'credential_set_uid' in local_var_params and local_var_params['credential_set_uid'] is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if 'accessed_url' in local_var_params and local_var_params['accessed_url'] is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if 'gir' in local_var_params and local_var_params['gir'] is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if 'victim' in local_var_params and local_var_params['victim'] is not None:  # noqa: E501
            query_params.append(('victim', local_var_params['victim']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'until' in local_var_params and local_var_params['until'] is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if 'last_updated_from' in local_var_params and local_var_params['last_updated_from'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if 'last_updated_until' in local_var_params and local_var_params['last_updated_until'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if 'cursor' in local_var_params and local_var_params['cursor'] is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if 'filter_by_gir_set' in local_var_params and local_var_params['filter_by_gir_set'] is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

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
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstringstringstringstringstring",
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
                '_request_auth'
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
        if 'text' in local_var_params and local_var_params['text'] is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if 'credential_set_name' in local_var_params and local_var_params['credential_set_name'] is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if 'credential_set_uid' in local_var_params and local_var_params['credential_set_uid'] is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if 'gir' in local_var_params and local_var_params['gir'] is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if 'victim' in local_var_params and local_var_params['victim'] is not None:  # noqa: E501
            query_params.append(('victim', local_var_params['victim']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'until' in local_var_params and local_var_params['until'] is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if 'last_updated_from' in local_var_params and local_var_params['last_updated_from'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if 'last_updated_until' in local_var_params and local_var_params['last_updated_until'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'filter_by_gir_set' in local_var_params and local_var_params['filter_by_gir_set'] is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

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
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstringstringstringstringstring",
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
                '_request_auth'
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
        if 'text' in local_var_params and local_var_params['text'] is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if 'credential_set_name' in local_var_params and local_var_params['credential_set_name'] is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if 'gir' in local_var_params and local_var_params['gir'] is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if 'victim' in local_var_params and local_var_params['victim'] is not None:  # noqa: E501
            query_params.append(('victim', local_var_params['victim']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'until' in local_var_params and local_var_params['until'] is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if 'last_updated_from' in local_var_params and local_var_params['last_updated_from'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if 'last_updated_until' in local_var_params and local_var_params['last_updated_until'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if 'cursor' in local_var_params and local_var_params['cursor'] is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if 'filter_by_gir_set' in local_var_params and local_var_params['filter_by_gir_set'] is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

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
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstringstringstringstringstring",
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
                '_request_auth'
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
        if 'text' in local_var_params and local_var_params['text'] is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if 'credential_uid' in local_var_params and local_var_params['credential_uid'] is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if 'accessed_url' in local_var_params and local_var_params['accessed_url'] is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if 'domain' in local_var_params and local_var_params['domain'] is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if 'affiliation_group' in local_var_params and local_var_params['affiliation_group'] is not None:  # noqa: E501
            query_params.append(('affiliationGroup', local_var_params['affiliation_group']))  # noqa: E501
        if 'gir' in local_var_params and local_var_params['gir'] is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'until' in local_var_params and local_var_params['until'] is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if 'last_updated_from' in local_var_params and local_var_params['last_updated_from'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if 'last_updated_until' in local_var_params and local_var_params['last_updated_until'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'filter_by_gir_set' in local_var_params and local_var_params['filter_by_gir_set'] is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

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
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstring",
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
                '_request_auth'
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
        if 'text' in local_var_params and local_var_params['text'] is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if 'credential_uid' in local_var_params and local_var_params['credential_uid'] is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if 'accessed_url' in local_var_params and local_var_params['accessed_url'] is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if 'domain' in local_var_params and local_var_params['domain'] is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if 'affiliation_group' in local_var_params and local_var_params['affiliation_group'] is not None:  # noqa: E501
            query_params.append(('affiliationGroup', local_var_params['affiliation_group']))  # noqa: E501
        if 'gir' in local_var_params and local_var_params['gir'] is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'until' in local_var_params and local_var_params['until'] is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if 'last_updated_from' in local_var_params and local_var_params['last_updated_from'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if 'last_updated_until' in local_var_params and local_var_params['last_updated_until'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if 'cursor' in local_var_params and local_var_params['cursor'] is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if 'filter_by_gir_set' in local_var_params and local_var_params['filter_by_gir_set'] is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

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
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstring",
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
                '_request_auth'
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
        if 'text' in local_var_params and local_var_params['text'] is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if 'credential_uid' in local_var_params and local_var_params['credential_uid'] is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if 'credential_set_name' in local_var_params and local_var_params['credential_set_name'] is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if 'credential_set_uid' in local_var_params and local_var_params['credential_set_uid'] is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if 'domain' in local_var_params and local_var_params['domain'] is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if 'affiliation_group' in local_var_params and local_var_params['affiliation_group'] is not None:  # noqa: E501
            query_params.append(('affiliationGroup', local_var_params['affiliation_group']))  # noqa: E501
        if 'password_strength' in local_var_params and local_var_params['password_strength'] is not None:  # noqa: E501
            query_params.append(('passwordStrength', local_var_params['password_strength']))  # noqa: E501
        if 'password_length_gte' in local_var_params and local_var_params['password_length_gte'] is not None:  # noqa: E501
            query_params.append(('passwordLengthGte', local_var_params['password_length_gte']))  # noqa: E501
        if 'password_lowercase_gte' in local_var_params and local_var_params['password_lowercase_gte'] is not None:  # noqa: E501
            query_params.append(('passwordLowercaseGte', local_var_params['password_lowercase_gte']))  # noqa: E501
        if 'password_uppercase_gte' in local_var_params and local_var_params['password_uppercase_gte'] is not None:  # noqa: E501
            query_params.append(('passwordUppercaseGte', local_var_params['password_uppercase_gte']))  # noqa: E501
        if 'password_numbers_gte' in local_var_params and local_var_params['password_numbers_gte'] is not None:  # noqa: E501
            query_params.append(('passwordNumbersGte', local_var_params['password_numbers_gte']))  # noqa: E501
        if 'password_punctuation_gte' in local_var_params and local_var_params['password_punctuation_gte'] is not None:  # noqa: E501
            query_params.append(('passwordPunctuationGte', local_var_params['password_punctuation_gte']))  # noqa: E501
        if 'password_symbols_gte' in local_var_params and local_var_params['password_symbols_gte'] is not None:  # noqa: E501
            query_params.append(('passwordSymbolsGte', local_var_params['password_symbols_gte']))  # noqa: E501
        if 'password_separators_gte' in local_var_params and local_var_params['password_separators_gte'] is not None:  # noqa: E501
            query_params.append(('passwordSeparatorsGte', local_var_params['password_separators_gte']))  # noqa: E501
        if 'password_other_gte' in local_var_params and local_var_params['password_other_gte'] is not None:  # noqa: E501
            query_params.append(('passwordOtherGte', local_var_params['password_other_gte']))  # noqa: E501
        if 'password_entropy_gte' in local_var_params and local_var_params['password_entropy_gte'] is not None:  # noqa: E501
            query_params.append(('passwordEntropyGte', local_var_params['password_entropy_gte']))  # noqa: E501
        if 'password_plain' in local_var_params and local_var_params['password_plain'] is not None:  # noqa: E501
            query_params.append(('passwordPlain', local_var_params['password_plain']))  # noqa: E501
        if 'credential_login' in local_var_params and local_var_params['credential_login'] is not None:  # noqa: E501
            query_params.append(('credentialLogin', local_var_params['credential_login']))  # noqa: E501
        if 'detected_malware' in local_var_params and local_var_params['detected_malware'] is not None:  # noqa: E501
            query_params.append(('detectedMalware', local_var_params['detected_malware']))  # noqa: E501
        if 'gir' in local_var_params and local_var_params['gir'] is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'until' in local_var_params and local_var_params['until'] is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if 'last_updated_from' in local_var_params and local_var_params['last_updated_from'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if 'last_updated_until' in local_var_params and local_var_params['last_updated_until'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'filter_by_gir_set' in local_var_params and local_var_params['filter_by_gir_set'] is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

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
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstring",
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
                '_request_auth'
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
        if 'text' in local_var_params and local_var_params['text'] is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if 'credential_occurrence_uid' in local_var_params and local_var_params['credential_occurrence_uid'] is not None:  # noqa: E501
            query_params.append(('credentialOccurrenceUid', local_var_params['credential_occurrence_uid']))  # noqa: E501
        if 'credential_uid' in local_var_params and local_var_params['credential_uid'] is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if 'credential_set_name' in local_var_params and local_var_params['credential_set_name'] is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if 'credential_set_uid' in local_var_params and local_var_params['credential_set_uid'] is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if 'domain' in local_var_params and local_var_params['domain'] is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if 'affiliation_group' in local_var_params and local_var_params['affiliation_group'] is not None:  # noqa: E501
            query_params.append(('affiliationGroup', local_var_params['affiliation_group']))  # noqa: E501
        if 'password_strength' in local_var_params and local_var_params['password_strength'] is not None:  # noqa: E501
            query_params.append(('passwordStrength', local_var_params['password_strength']))  # noqa: E501
        if 'password_length_gte' in local_var_params and local_var_params['password_length_gte'] is not None:  # noqa: E501
            query_params.append(('passwordLengthGte', local_var_params['password_length_gte']))  # noqa: E501
        if 'password_lowercase_gte' in local_var_params and local_var_params['password_lowercase_gte'] is not None:  # noqa: E501
            query_params.append(('passwordLowercaseGte', local_var_params['password_lowercase_gte']))  # noqa: E501
        if 'password_uppercase_gte' in local_var_params and local_var_params['password_uppercase_gte'] is not None:  # noqa: E501
            query_params.append(('passwordUppercaseGte', local_var_params['password_uppercase_gte']))  # noqa: E501
        if 'password_numbers_gte' in local_var_params and local_var_params['password_numbers_gte'] is not None:  # noqa: E501
            query_params.append(('passwordNumbersGte', local_var_params['password_numbers_gte']))  # noqa: E501
        if 'password_punctuation_gte' in local_var_params and local_var_params['password_punctuation_gte'] is not None:  # noqa: E501
            query_params.append(('passwordPunctuationGte', local_var_params['password_punctuation_gte']))  # noqa: E501
        if 'password_symbols_gte' in local_var_params and local_var_params['password_symbols_gte'] is not None:  # noqa: E501
            query_params.append(('passwordSymbolsGte', local_var_params['password_symbols_gte']))  # noqa: E501
        if 'password_separators_gte' in local_var_params and local_var_params['password_separators_gte'] is not None:  # noqa: E501
            query_params.append(('passwordSeparatorsGte', local_var_params['password_separators_gte']))  # noqa: E501
        if 'password_other_gte' in local_var_params and local_var_params['password_other_gte'] is not None:  # noqa: E501
            query_params.append(('passwordOtherGte', local_var_params['password_other_gte']))  # noqa: E501
        if 'password_entropy_gte' in local_var_params and local_var_params['password_entropy_gte'] is not None:  # noqa: E501
            query_params.append(('passwordEntropyGte', local_var_params['password_entropy_gte']))  # noqa: E501
        if 'password_plain' in local_var_params and local_var_params['password_plain'] is not None:  # noqa: E501
            query_params.append(('passwordPlain', local_var_params['password_plain']))  # noqa: E501
        if 'credential_login' in local_var_params and local_var_params['credential_login'] is not None:  # noqa: E501
            query_params.append(('credentialLogin', local_var_params['credential_login']))  # noqa: E501
        if 'detected_malware' in local_var_params and local_var_params['detected_malware'] is not None:  # noqa: E501
            query_params.append(('detectedMalware', local_var_params['detected_malware']))  # noqa: E501
        if 'accessed_url' in local_var_params and local_var_params['accessed_url'] is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if 'gir' in local_var_params and local_var_params['gir'] is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'until' in local_var_params and local_var_params['until'] is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if 'last_updated_from' in local_var_params and local_var_params['last_updated_from'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if 'last_updated_until' in local_var_params and local_var_params['last_updated_until'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'filter_by_gir_set' in local_var_params and local_var_params['filter_by_gir_set'] is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

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
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstring",
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
                '_request_auth'
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
        if 'text' in local_var_params and local_var_params['text'] is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if 'credential_occurrence_uid' in local_var_params and local_var_params['credential_occurrence_uid'] is not None:  # noqa: E501
            query_params.append(('credentialOccurrenceUid', local_var_params['credential_occurrence_uid']))  # noqa: E501
        if 'credential_uid' in local_var_params and local_var_params['credential_uid'] is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if 'credential_set_name' in local_var_params and local_var_params['credential_set_name'] is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if 'credential_set_uid' in local_var_params and local_var_params['credential_set_uid'] is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if 'domain' in local_var_params and local_var_params['domain'] is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if 'affiliation_group' in local_var_params and local_var_params['affiliation_group'] is not None:  # noqa: E501
            query_params.append(('affiliationGroup', local_var_params['affiliation_group']))  # noqa: E501
        if 'password_strength' in local_var_params and local_var_params['password_strength'] is not None:  # noqa: E501
            query_params.append(('passwordStrength', local_var_params['password_strength']))  # noqa: E501
        if 'password_length_gte' in local_var_params and local_var_params['password_length_gte'] is not None:  # noqa: E501
            query_params.append(('passwordLengthGte', local_var_params['password_length_gte']))  # noqa: E501
        if 'password_lowercase_gte' in local_var_params and local_var_params['password_lowercase_gte'] is not None:  # noqa: E501
            query_params.append(('passwordLowercaseGte', local_var_params['password_lowercase_gte']))  # noqa: E501
        if 'password_uppercase_gte' in local_var_params and local_var_params['password_uppercase_gte'] is not None:  # noqa: E501
            query_params.append(('passwordUppercaseGte', local_var_params['password_uppercase_gte']))  # noqa: E501
        if 'password_numbers_gte' in local_var_params and local_var_params['password_numbers_gte'] is not None:  # noqa: E501
            query_params.append(('passwordNumbersGte', local_var_params['password_numbers_gte']))  # noqa: E501
        if 'password_punctuation_gte' in local_var_params and local_var_params['password_punctuation_gte'] is not None:  # noqa: E501
            query_params.append(('passwordPunctuationGte', local_var_params['password_punctuation_gte']))  # noqa: E501
        if 'password_symbols_gte' in local_var_params and local_var_params['password_symbols_gte'] is not None:  # noqa: E501
            query_params.append(('passwordSymbolsGte', local_var_params['password_symbols_gte']))  # noqa: E501
        if 'password_separators_gte' in local_var_params and local_var_params['password_separators_gte'] is not None:  # noqa: E501
            query_params.append(('passwordSeparatorsGte', local_var_params['password_separators_gte']))  # noqa: E501
        if 'password_other_gte' in local_var_params and local_var_params['password_other_gte'] is not None:  # noqa: E501
            query_params.append(('passwordOtherGte', local_var_params['password_other_gte']))  # noqa: E501
        if 'password_entropy_gte' in local_var_params and local_var_params['password_entropy_gte'] is not None:  # noqa: E501
            query_params.append(('passwordEntropyGte', local_var_params['password_entropy_gte']))  # noqa: E501
        if 'password_plain' in local_var_params and local_var_params['password_plain'] is not None:  # noqa: E501
            query_params.append(('passwordPlain', local_var_params['password_plain']))  # noqa: E501
        if 'credential_login' in local_var_params and local_var_params['credential_login'] is not None:  # noqa: E501
            query_params.append(('credentialLogin', local_var_params['credential_login']))  # noqa: E501
        if 'detected_malware' in local_var_params and local_var_params['detected_malware'] is not None:  # noqa: E501
            query_params.append(('detectedMalware', local_var_params['detected_malware']))  # noqa: E501
        if 'accessed_url' in local_var_params and local_var_params['accessed_url'] is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if 'gir' in local_var_params and local_var_params['gir'] is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'until' in local_var_params and local_var_params['until'] is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if 'last_updated_from' in local_var_params and local_var_params['last_updated_from'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if 'last_updated_until' in local_var_params and local_var_params['last_updated_until'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if 'cursor' in local_var_params and local_var_params['cursor'] is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if 'filter_by_gir_set' in local_var_params and local_var_params['filter_by_gir_set'] is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

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
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstring",
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
                '_request_auth'
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
        if 'text' in local_var_params and local_var_params['text'] is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if 'credential_uid' in local_var_params and local_var_params['credential_uid'] is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if 'credential_set_name' in local_var_params and local_var_params['credential_set_name'] is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if 'credential_set_uid' in local_var_params and local_var_params['credential_set_uid'] is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if 'domain' in local_var_params and local_var_params['domain'] is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if 'affiliation_group' in local_var_params and local_var_params['affiliation_group'] is not None:  # noqa: E501
            query_params.append(('affiliationGroup', local_var_params['affiliation_group']))  # noqa: E501
        if 'password_strength' in local_var_params and local_var_params['password_strength'] is not None:  # noqa: E501
            query_params.append(('passwordStrength', local_var_params['password_strength']))  # noqa: E501
        if 'password_length_gte' in local_var_params and local_var_params['password_length_gte'] is not None:  # noqa: E501
            query_params.append(('passwordLengthGte', local_var_params['password_length_gte']))  # noqa: E501
        if 'password_lowercase_gte' in local_var_params and local_var_params['password_lowercase_gte'] is not None:  # noqa: E501
            query_params.append(('passwordLowercaseGte', local_var_params['password_lowercase_gte']))  # noqa: E501
        if 'password_uppercase_gte' in local_var_params and local_var_params['password_uppercase_gte'] is not None:  # noqa: E501
            query_params.append(('passwordUppercaseGte', local_var_params['password_uppercase_gte']))  # noqa: E501
        if 'password_numbers_gte' in local_var_params and local_var_params['password_numbers_gte'] is not None:  # noqa: E501
            query_params.append(('passwordNumbersGte', local_var_params['password_numbers_gte']))  # noqa: E501
        if 'password_punctuation_gte' in local_var_params and local_var_params['password_punctuation_gte'] is not None:  # noqa: E501
            query_params.append(('passwordPunctuationGte', local_var_params['password_punctuation_gte']))  # noqa: E501
        if 'password_symbols_gte' in local_var_params and local_var_params['password_symbols_gte'] is not None:  # noqa: E501
            query_params.append(('passwordSymbolsGte', local_var_params['password_symbols_gte']))  # noqa: E501
        if 'password_separators_gte' in local_var_params and local_var_params['password_separators_gte'] is not None:  # noqa: E501
            query_params.append(('passwordSeparatorsGte', local_var_params['password_separators_gte']))  # noqa: E501
        if 'password_other_gte' in local_var_params and local_var_params['password_other_gte'] is not None:  # noqa: E501
            query_params.append(('passwordOtherGte', local_var_params['password_other_gte']))  # noqa: E501
        if 'password_entropy_gte' in local_var_params and local_var_params['password_entropy_gte'] is not None:  # noqa: E501
            query_params.append(('passwordEntropyGte', local_var_params['password_entropy_gte']))  # noqa: E501
        if 'password_plain' in local_var_params and local_var_params['password_plain'] is not None:  # noqa: E501
            query_params.append(('passwordPlain', local_var_params['password_plain']))  # noqa: E501
        if 'credential_login' in local_var_params and local_var_params['credential_login'] is not None:  # noqa: E501
            query_params.append(('credentialLogin', local_var_params['credential_login']))  # noqa: E501
        if 'detected_malware' in local_var_params and local_var_params['detected_malware'] is not None:  # noqa: E501
            query_params.append(('detectedMalware', local_var_params['detected_malware']))  # noqa: E501
        if 'gir' in local_var_params and local_var_params['gir'] is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'until' in local_var_params and local_var_params['until'] is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if 'last_updated_from' in local_var_params and local_var_params['last_updated_from'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedFrom', local_var_params['last_updated_from']))  # noqa: E501
        if 'last_updated_until' in local_var_params and local_var_params['last_updated_until'] is not None:  # noqa: E501
            query_params.append(('lastUpdatedUntil', local_var_params['last_updated_until']))  # noqa: E501
        if 'cursor' in local_var_params and local_var_params['cursor'] is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if 'filter_by_gir_set' in local_var_params and local_var_params['filter_by_gir_set'] is not None:  # noqa: E501
            query_params.append(('filterByGirSet', local_var_params['filter_by_gir_set']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

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
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstring",
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
