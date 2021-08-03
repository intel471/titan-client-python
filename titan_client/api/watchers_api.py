# coding: utf-8

"""
    Titan API v1

    # Introduction The Intel 471 API is organized around the principles of REST. Our API lets you gather results from our platform with anything that can send a HTTP request, including cURL and modern internet browsers. Access to this API requires an API token which is managed from your account settings.  Intel 471 reserves the right to add fields to our API however we will provide backwards compatibility and older version support so that it will be possible to choose exact versions that provide a response with an older structure. This documentation tracks all API versions and it is possible to compare this version which has changes highlighted. Please consider not storing information provided by API locally as we constantly improving our data set and want you to have the most updated information.  # Authentication Authenticate to the Intel 471 API by providing your API key in the request. Your API key carries many privileges so please do not expose them on public web resources.  Authentication to the API occurs by providing your email address as the login and API key as password in the authorization header via HTTP Basic Auth. Your API key can be found in the [API](https://portal.intel471.com/api) section on the portal.  # Accessing API ## Via internet browser Just open url: `https://api.intel471.com/v1/reports` Browser will ask for credentials, provide your email as login and API key as password. ## Via curl command line utility Type in terminal the following command: ``` curl -u <YOU EMAIL>:<YOUR API KEY> https://api.intel471.com/v1/reports ``` ## CURL usage examples This section covers some Watchers API requests.  ### List watcher groups: Type in terminal the following command:  *curl -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  ### Create watcher group: To create watcher group you need to pass a json body to request. Passing json body possible in two ways:  #### Write json to request *curl -d'{\"name\": \"group_name\", \"description\": \"Description\"}' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  #### Write json to file and call it *curl -d\"@json_file_name\" -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  ### Create free text search watcher: *curl -d'{\"type\": \"search\", \"freeTextPattern\": \"text to search\", \"notificationChannel\": \"website\"}' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups/\"GROUP UID\"/watchers*  ### Create specific search watcher: *curl -d'{\"type\": \"search\", \"patterns\":[ { \"types\": \"Actor\" , \"pattern\": \"swisman\" } ], \"notificationChannel\": \"website\" }' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups/\"GROUP UID\"/watchers*  ## Via Python Execute the following script: ``` import urllib2, base64  username = \"<YOU EMAIL>\" apikey = \"<YOUR API KEY>\"  request = urllib2.Request(\"https://api.intel471.com/v1/reports\") base64string = base64.encodestring('%s:%s' % (username, apikey)).replace('\\n', '') request.add_header(\"Authorization\", \"Basic %s\" % base64string) result = urllib2.urlopen(request) response_in_json = result.read()  print response_in_json ``` # API integration best practice with your application When accessing our API from your application don't do AJAX calls directly from web browser to https://api.intel471.com/. We do not allow CORS requests from browser due to potential security issues. Instead we suggest you look to establish a kind of a server side proxy in your application which will pass requests to our API.  For example: you can send a request from browser javascript to your server side, for instance to url `/apiproxy/actors?actor=hacker` which will be internally passed to `https://api.intel471.com/v1/actors?actor=hacker` (with authentication headers added) and response will be sent back to the browser.  # Versioning support We are consistently improving our API and occasionally bring in changes to the API based on customer feedback. The current API version can be seen in the drop down boxes for each version. We are providing API backwards compatibility when possible. All requests are prefixed with the major version number, for example `/v1`: ``` https://api.intel471.com/v1/reports ```  Different major versions are not compatible and imply significant response structure changes. Minor versions differences might include extra fields in response or provide new request parameter support. To stick to the specific version, just add the following extra parameter to the request, for example: `?v=1.2.0`. If you specify a not existing version, it will be brought down to the nearest existing one. For example, parameter `?v=1.5.4` will call API of version 1.3.0 — the latest available; `?v=1.2.9` will awake version 1.2.0 and so on.  Omitting the version parameter from your request means you will always use the latest version of the API.  We highly recommend you always add the version parameter to be safe on API updates and code your integration in a way to accept possible future extra fields added to the response object. ``` https://api.intel471.com/v1/tags?prettyPrint - will return response for the latest API version (v.1.1.0) https://api.intel471.com/v1/tags?prettyPrint&v=1.1.0 - absolutely the same request with the version explicitly specified https://api.intel471.com/v1/reports?prettyPrint&v=1.0.0 - will return response compatible with the older version ```   # noqa: E501

    The version of the OpenAPI document: 1.16.1
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


class WatchersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def watcher_groups_get(self, **kwargs):  # noqa: E501
        """Get Watcher Group List  # noqa: E501

        Returns list of Watcher groups matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_get(async_req=True)
        >>> result = thread.get()

        :param section: Shows watcher groups from defined section.
        :type section: str
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
        :rtype: WatcherGroupResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.watcher_groups_get_with_http_info(**kwargs)  # noqa: E501

    def watcher_groups_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Watcher Group List  # noqa: E501

        Returns list of Watcher groups matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param section: Shows watcher groups from defined section.
        :type section: str
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
        :rtype: tuple(WatcherGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'section'
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
                    " to method watcher_groups_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'section' in local_var_params and local_var_params['section'] is not None:  # noqa: E501
            query_params.append(('section', local_var_params['section']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501
        
        response_types_map = {
            200: "WatcherGroupResponse",
        }

        return self.api_client.call_api(
            '/watcherGroups', 'GET',
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

    def watcher_groups_group_uid_delete(self, group_uid, **kwargs):  # noqa: E501
        """Delete Watcher Group  # noqa: E501

        Delete defined watcher group. Only groups of type owned_by_me are allowed to be deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_delete(group_uid, async_req=True)
        >>> result = thread.get()

        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
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
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.watcher_groups_group_uid_delete_with_http_info(group_uid, **kwargs)  # noqa: E501

    def watcher_groups_group_uid_delete_with_http_info(self, group_uid, **kwargs):  # noqa: E501
        """Delete Watcher Group  # noqa: E501

        Delete defined watcher group. Only groups of type owned_by_me are allowed to be deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_delete_with_http_info(group_uid, async_req=True)
        >>> result = thread.get()

        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
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
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'group_uid'
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
                    " to method watcher_groups_group_uid_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_uid' is set
        if self.api_client.client_side_validation and ('group_uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_uid` when calling `watcher_groups_group_uid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_uid' in local_var_params:
            path_params['group-uid'] = local_var_params['group_uid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501
        
        response_types_map = {}

        return self.api_client.call_api(
            '/watcherGroups/{group-uid}', 'DELETE',
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

    def watcher_groups_group_uid_get(self, group_uid, **kwargs):  # noqa: E501
        """Get Watcher Group  # noqa: E501

        Get a watcher group by UID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_get(group_uid, async_req=True)
        >>> result = thread.get()

        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
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
        :rtype: SimpleWatcherGroupSchema
        """
        kwargs['_return_http_data_only'] = True
        return self.watcher_groups_group_uid_get_with_http_info(group_uid, **kwargs)  # noqa: E501

    def watcher_groups_group_uid_get_with_http_info(self, group_uid, **kwargs):  # noqa: E501
        """Get Watcher Group  # noqa: E501

        Get a watcher group by UID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_get_with_http_info(group_uid, async_req=True)
        >>> result = thread.get()

        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
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
        :rtype: tuple(SimpleWatcherGroupSchema, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_uid'
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
                    " to method watcher_groups_group_uid_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_uid' is set
        if self.api_client.client_side_validation and ('group_uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_uid` when calling `watcher_groups_group_uid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_uid' in local_var_params:
            path_params['group-uid'] = local_var_params['group_uid']  # noqa: E501

        query_params = []

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
            200: "SimpleWatcherGroupSchema",
            404: "str",
        }

        return self.api_client.call_api(
            '/watcherGroups/{group-uid}', 'GET',
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

    def watcher_groups_group_uid_put(self, group_uid, inline_object1, **kwargs):  # noqa: E501
        """Put Watcher Group  # noqa: E501

        Update watcher group's name or description. Only groups of type `owned_by_me` are allowed to be updated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_put(group_uid, inline_object1, async_req=True)
        >>> result = thread.get()

        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
        :param inline_object1: (required)
        :type inline_object1: InlineObject1
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
        :rtype: SimpleWatcherGroupSchema
        """
        kwargs['_return_http_data_only'] = True
        return self.watcher_groups_group_uid_put_with_http_info(group_uid, inline_object1, **kwargs)  # noqa: E501

    def watcher_groups_group_uid_put_with_http_info(self, group_uid, inline_object1, **kwargs):  # noqa: E501
        """Put Watcher Group  # noqa: E501

        Update watcher group's name or description. Only groups of type `owned_by_me` are allowed to be updated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_put_with_http_info(group_uid, inline_object1, async_req=True)
        >>> result = thread.get()

        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
        :param inline_object1: (required)
        :type inline_object1: InlineObject1
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
        :rtype: tuple(SimpleWatcherGroupSchema, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_uid',
            'inline_object1'
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
                    " to method watcher_groups_group_uid_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_uid' is set
        if self.api_client.client_side_validation and ('group_uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_uid` when calling `watcher_groups_group_uid_put`")  # noqa: E501
        # verify the required parameter 'inline_object1' is set
        if self.api_client.client_side_validation and ('inline_object1' not in local_var_params or  # noqa: E501
                                                        local_var_params['inline_object1'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `inline_object1` when calling `watcher_groups_group_uid_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_uid' in local_var_params:
            path_params['group-uid'] = local_var_params['group_uid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object1' in local_var_params:
            body_params = local_var_params['inline_object1']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501
        
        response_types_map = {
            200: "SimpleWatcherGroupSchema",
            404: "str",
        }

        return self.api_client.call_api(
            '/watcherGroups/{group-uid}', 'PUT',
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

    def watcher_groups_group_uid_watchers_get(self, group_uid, **kwargs):  # noqa: E501
        """Get Watchers list  # noqa: E501

        Returns list of `Watchers` of a given Watcher group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_watchers_get(group_uid, async_req=True)
        >>> result = thread.get()

        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
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
        :rtype: WatcherSchemaResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.watcher_groups_group_uid_watchers_get_with_http_info(group_uid, **kwargs)  # noqa: E501

    def watcher_groups_group_uid_watchers_get_with_http_info(self, group_uid, **kwargs):  # noqa: E501
        """Get Watchers list  # noqa: E501

        Returns list of `Watchers` of a given Watcher group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_watchers_get_with_http_info(group_uid, async_req=True)
        >>> result = thread.get()

        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
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
        :rtype: tuple(WatcherSchemaResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_uid'
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
                    " to method watcher_groups_group_uid_watchers_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_uid' is set
        if self.api_client.client_side_validation and ('group_uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_uid` when calling `watcher_groups_group_uid_watchers_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_uid' in local_var_params:
            path_params['group-uid'] = local_var_params['group_uid']  # noqa: E501

        query_params = []

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
            200: "WatcherSchemaResponse",
            404: "str",
        }

        return self.api_client.call_api(
            '/watcherGroups/{group-uid}/watchers', 'GET',
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

    def watcher_groups_group_uid_watchers_post(self, group_uid, watcher_request_body_post, **kwargs):  # noqa: E501
        """Create Watcher  # noqa: E501

        Create new watcher in a given Watcher group from a json object supplied in request body  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_watchers_post(group_uid, watcher_request_body_post, async_req=True)
        >>> result = thread.get()

        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
        :param watcher_request_body_post: JSON request body (required)
        :type watcher_request_body_post: WatcherRequestBodyPost
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
        :rtype: WatcherSchema
        """
        kwargs['_return_http_data_only'] = True
        return self.watcher_groups_group_uid_watchers_post_with_http_info(group_uid, watcher_request_body_post, **kwargs)  # noqa: E501

    def watcher_groups_group_uid_watchers_post_with_http_info(self, group_uid, watcher_request_body_post, **kwargs):  # noqa: E501
        """Create Watcher  # noqa: E501

        Create new watcher in a given Watcher group from a json object supplied in request body  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_watchers_post_with_http_info(group_uid, watcher_request_body_post, async_req=True)
        >>> result = thread.get()

        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
        :param watcher_request_body_post: JSON request body (required)
        :type watcher_request_body_post: WatcherRequestBodyPost
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
        :rtype: tuple(WatcherSchema, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_uid',
            'watcher_request_body_post'
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
                    " to method watcher_groups_group_uid_watchers_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_uid' is set
        if self.api_client.client_side_validation and ('group_uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_uid` when calling `watcher_groups_group_uid_watchers_post`")  # noqa: E501
        # verify the required parameter 'watcher_request_body_post' is set
        if self.api_client.client_side_validation and ('watcher_request_body_post' not in local_var_params or  # noqa: E501
                                                        local_var_params['watcher_request_body_post'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `watcher_request_body_post` when calling `watcher_groups_group_uid_watchers_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_uid' in local_var_params:
            path_params['group-uid'] = local_var_params['group_uid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'watcher_request_body_post' in local_var_params:
            body_params = local_var_params['watcher_request_body_post']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501
        
        response_types_map = {
            200: "WatcherSchema",
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstring",
        }

        return self.api_client.call_api(
            '/watcherGroups/{group-uid}/watchers', 'POST',
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

    def watcher_groups_group_uid_watchers_watcher_uid_delete(self, watcher_uid, group_uid, **kwargs):  # noqa: E501
        """Delete Watcher  # noqa: E501

        Delete a given watcher in a given watcher group specified by watcher-uid and group-uid parameters. Confirmed with \"No Content\" response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_watchers_watcher_uid_delete(watcher_uid, group_uid, async_req=True)
        >>> result = thread.get()

        :param watcher_uid: Unique identifier of watcher. (required)
        :type watcher_uid: str
        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
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
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.watcher_groups_group_uid_watchers_watcher_uid_delete_with_http_info(watcher_uid, group_uid, **kwargs)  # noqa: E501

    def watcher_groups_group_uid_watchers_watcher_uid_delete_with_http_info(self, watcher_uid, group_uid, **kwargs):  # noqa: E501
        """Delete Watcher  # noqa: E501

        Delete a given watcher in a given watcher group specified by watcher-uid and group-uid parameters. Confirmed with \"No Content\" response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_watchers_watcher_uid_delete_with_http_info(watcher_uid, group_uid, async_req=True)
        >>> result = thread.get()

        :param watcher_uid: Unique identifier of watcher. (required)
        :type watcher_uid: str
        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
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
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'watcher_uid',
            'group_uid'
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
                    " to method watcher_groups_group_uid_watchers_watcher_uid_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'watcher_uid' is set
        if self.api_client.client_side_validation and ('watcher_uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['watcher_uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `watcher_uid` when calling `watcher_groups_group_uid_watchers_watcher_uid_delete`")  # noqa: E501
        # verify the required parameter 'group_uid' is set
        if self.api_client.client_side_validation and ('group_uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_uid` when calling `watcher_groups_group_uid_watchers_watcher_uid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'watcher_uid' in local_var_params:
            path_params['watcher-uid'] = local_var_params['watcher_uid']  # noqa: E501
        if 'group_uid' in local_var_params:
            path_params['group-uid'] = local_var_params['group_uid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501
        
        response_types_map = {}

        return self.api_client.call_api(
            '/watcherGroups/{group-uid}/watchers/{watcher-uid}', 'DELETE',
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

    def watcher_groups_group_uid_watchers_watcher_uid_get(self, watcher_uid, group_uid, **kwargs):  # noqa: E501
        """Get Watcher  # noqa: E501

        Get single Watcher from given Watcher group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_watchers_watcher_uid_get(watcher_uid, group_uid, async_req=True)
        >>> result = thread.get()

        :param watcher_uid: Unique identifier of watcher. (required)
        :type watcher_uid: str
        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
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
        :rtype: WatcherSchema
        """
        kwargs['_return_http_data_only'] = True
        return self.watcher_groups_group_uid_watchers_watcher_uid_get_with_http_info(watcher_uid, group_uid, **kwargs)  # noqa: E501

    def watcher_groups_group_uid_watchers_watcher_uid_get_with_http_info(self, watcher_uid, group_uid, **kwargs):  # noqa: E501
        """Get Watcher  # noqa: E501

        Get single Watcher from given Watcher group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_watchers_watcher_uid_get_with_http_info(watcher_uid, group_uid, async_req=True)
        >>> result = thread.get()

        :param watcher_uid: Unique identifier of watcher. (required)
        :type watcher_uid: str
        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
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
        :rtype: tuple(WatcherSchema, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'watcher_uid',
            'group_uid'
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
                    " to method watcher_groups_group_uid_watchers_watcher_uid_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'watcher_uid' is set
        if self.api_client.client_side_validation and ('watcher_uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['watcher_uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `watcher_uid` when calling `watcher_groups_group_uid_watchers_watcher_uid_get`")  # noqa: E501
        # verify the required parameter 'group_uid' is set
        if self.api_client.client_side_validation and ('group_uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_uid` when calling `watcher_groups_group_uid_watchers_watcher_uid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'watcher_uid' in local_var_params:
            path_params['watcher-uid'] = local_var_params['watcher_uid']  # noqa: E501
        if 'group_uid' in local_var_params:
            path_params['group-uid'] = local_var_params['group_uid']  # noqa: E501

        query_params = []

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
            200: "WatcherSchema",
            404: "str",
        }

        return self.api_client.call_api(
            '/watcherGroups/{group-uid}/watchers/{watcher-uid}', 'GET',
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

    def watcher_groups_group_uid_watchers_watcher_uid_put(self, watcher_uid, group_uid, watcher_request_body_put, **kwargs):  # noqa: E501
        """Put Watcher  # noqa: E501

        Editing of existing watcher in a given Watcher group from a json object supplied in request body. Whole watcher body should be supplied  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_watchers_watcher_uid_put(watcher_uid, group_uid, watcher_request_body_put, async_req=True)
        >>> result = thread.get()

        :param watcher_uid: Unique identifier of watcher. (required)
        :type watcher_uid: str
        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
        :param watcher_request_body_put: JSON request body (required)
        :type watcher_request_body_put: WatcherRequestBodyPut
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
        :rtype: WatcherSchema
        """
        kwargs['_return_http_data_only'] = True
        return self.watcher_groups_group_uid_watchers_watcher_uid_put_with_http_info(watcher_uid, group_uid, watcher_request_body_put, **kwargs)  # noqa: E501

    def watcher_groups_group_uid_watchers_watcher_uid_put_with_http_info(self, watcher_uid, group_uid, watcher_request_body_put, **kwargs):  # noqa: E501
        """Put Watcher  # noqa: E501

        Editing of existing watcher in a given Watcher group from a json object supplied in request body. Whole watcher body should be supplied  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_group_uid_watchers_watcher_uid_put_with_http_info(watcher_uid, group_uid, watcher_request_body_put, async_req=True)
        >>> result = thread.get()

        :param watcher_uid: Unique identifier of watcher. (required)
        :type watcher_uid: str
        :param group_uid: Watcher group identifier. (required)
        :type group_uid: str
        :param watcher_request_body_put: JSON request body (required)
        :type watcher_request_body_put: WatcherRequestBodyPut
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
        :rtype: tuple(WatcherSchema, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'watcher_uid',
            'group_uid',
            'watcher_request_body_put'
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
                    " to method watcher_groups_group_uid_watchers_watcher_uid_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'watcher_uid' is set
        if self.api_client.client_side_validation and ('watcher_uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['watcher_uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `watcher_uid` when calling `watcher_groups_group_uid_watchers_watcher_uid_put`")  # noqa: E501
        # verify the required parameter 'group_uid' is set
        if self.api_client.client_side_validation and ('group_uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_uid` when calling `watcher_groups_group_uid_watchers_watcher_uid_put`")  # noqa: E501
        # verify the required parameter 'watcher_request_body_put' is set
        if self.api_client.client_side_validation and ('watcher_request_body_put' not in local_var_params or  # noqa: E501
                                                        local_var_params['watcher_request_body_put'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `watcher_request_body_put` when calling `watcher_groups_group_uid_watchers_watcher_uid_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'watcher_uid' in local_var_params:
            path_params['watcher-uid'] = local_var_params['watcher_uid']  # noqa: E501
        if 'group_uid' in local_var_params:
            path_params['group-uid'] = local_var_params['group_uid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'watcher_request_body_put' in local_var_params:
            body_params = local_var_params['watcher_request_body_put']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501
        
        response_types_map = {
            200: "WatcherSchema",
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstring",
        }

        return self.api_client.call_api(
            '/watcherGroups/{group-uid}/watchers/{watcher-uid}', 'PUT',
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

    def watcher_groups_post(self, inline_object, **kwargs):  # noqa: E501
        """Create Watcher Group  # noqa: E501

        Create watcher group from json object supplied in a request body which contains name and description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_post(inline_object, async_req=True)
        >>> result = thread.get()

        :param inline_object: (required)
        :type inline_object: InlineObject
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
        :rtype: SimpleWatcherGroupSchema
        """
        kwargs['_return_http_data_only'] = True
        return self.watcher_groups_post_with_http_info(inline_object, **kwargs)  # noqa: E501

    def watcher_groups_post_with_http_info(self, inline_object, **kwargs):  # noqa: E501
        """Create Watcher Group  # noqa: E501

        Create watcher group from json object supplied in a request body which contains name and description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.watcher_groups_post_with_http_info(inline_object, async_req=True)
        >>> result = thread.get()

        :param inline_object: (required)
        :type inline_object: InlineObject
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
        :rtype: tuple(SimpleWatcherGroupSchema, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'inline_object'
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
                    " to method watcher_groups_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'inline_object' is set
        if self.api_client.client_side_validation and ('inline_object' not in local_var_params or  # noqa: E501
                                                        local_var_params['inline_object'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `inline_object` when calling `watcher_groups_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object' in local_var_params:
            body_params = local_var_params['inline_object']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501
        
        response_types_map = {
            200: "SimpleWatcherGroupSchema",
            412: "OneOfstringstring",
        }

        return self.api_client.call_api(
            '/watcherGroups', 'POST',
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
