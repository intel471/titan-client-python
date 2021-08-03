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


class MessagingServicesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def messaging_services_instant_messages_get(self, **kwargs):  # noqa: E501
        """Search Instant Messages  # noqa: E501

        Returns list of `Instant messages` matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.messaging_services_instant_messages_get(async_req=True)
        >>> result = thread.get()

        :param instant_message: Free text instant messages search. At least one of `instantMessage`, `instantMessageActor`, `instantMessageService`, `instantMessageServer`, `instantMessageChannel` is required.
        :type instant_message: str
        :param instant_message_actor: Search instant messages by actor name (actual for the moment message was written).
        :type instant_message_actor: str
        :param instant_message_service: Search instant messages by service.
        :type instant_message_service: str
        :param instant_message_server: Search instant messages by server.
        :type instant_message_server: str
        :param instant_message_channel: Search instant messages by channel.
        :type instant_message_channel: str
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
        :rtype: MessagingServicesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.messaging_services_instant_messages_get_with_http_info(**kwargs)  # noqa: E501

    def messaging_services_instant_messages_get_with_http_info(self, **kwargs):  # noqa: E501
        """Search Instant Messages  # noqa: E501

        Returns list of `Instant messages` matching filter criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.messaging_services_instant_messages_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param instant_message: Free text instant messages search. At least one of `instantMessage`, `instantMessageActor`, `instantMessageService`, `instantMessageServer`, `instantMessageChannel` is required.
        :type instant_message: str
        :param instant_message_actor: Search instant messages by actor name (actual for the moment message was written).
        :type instant_message_actor: str
        :param instant_message_service: Search instant messages by service.
        :type instant_message_service: str
        :param instant_message_server: Search instant messages by server.
        :type instant_message_server: str
        :param instant_message_channel: Search instant messages by channel.
        :type instant_message_channel: str
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
        :rtype: tuple(MessagingServicesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'instant_message',
            'instant_message_actor',
            'instant_message_service',
            'instant_message_server',
            'instant_message_channel',
            '_from',
            'until',
            'last_updated_from',
            'last_updated_until',
            'sort',
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
                    " to method messaging_services_instant_messages_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `messaging_services_instant_messages_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `messaging_services_instant_messages_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `messaging_services_instant_messages_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `messaging_services_instant_messages_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instant_message' in local_var_params and local_var_params['instant_message'] is not None:  # noqa: E501
            query_params.append(('instantMessage', local_var_params['instant_message']))  # noqa: E501
        if 'instant_message_actor' in local_var_params and local_var_params['instant_message_actor'] is not None:  # noqa: E501
            query_params.append(('instantMessageActor', local_var_params['instant_message_actor']))  # noqa: E501
        if 'instant_message_service' in local_var_params and local_var_params['instant_message_service'] is not None:  # noqa: E501
            query_params.append(('instantMessageService', local_var_params['instant_message_service']))  # noqa: E501
        if 'instant_message_server' in local_var_params and local_var_params['instant_message_server'] is not None:  # noqa: E501
            query_params.append(('instantMessageServer', local_var_params['instant_message_server']))  # noqa: E501
        if 'instant_message_channel' in local_var_params and local_var_params['instant_message_channel'] is not None:  # noqa: E501
            query_params.append(('instantMessageChannel', local_var_params['instant_message_channel']))  # noqa: E501
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
            200: "MessagingServicesResponse",
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstringstring",
        }

        return self.api_client.call_api(
            '/messagingServices/instantMessages', 'GET',
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
