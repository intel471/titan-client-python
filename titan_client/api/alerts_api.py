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


class AlertsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def alerts_get(self, **kwargs):  # noqa: E501
        """Get Alerts  # noqa: E501

        Returns list of `Alerts` matching filter criteria excluding the following types: Malware reports, YARA, NIDS  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.alerts_get(async_req=True)
        >>> result = thread.get()

        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param watcher_group: Show `Alerts` from specified watcher group only. Object field: watcherGroupUid. Multiple values allowed.
        :type watcher_group: str
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param show_read: Show read alerts.
        :type show_read: bool
        :param display_watchers: Show watcher groups info.
        :type display_watchers: bool
        :param mark_as_read: Mark displayed alerts as read.
        :type mark_as_read: bool
        :param sort: Sort results by the object's native time in descending (latest) or ascending (earliest) order
        :type sort: str
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
        :rtype: AlertListSchemaResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.alerts_get_with_http_info(**kwargs)  # noqa: E501

    def alerts_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Alerts  # noqa: E501

        Returns list of `Alerts` matching filter criteria excluding the following types: Malware reports, YARA, NIDS  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.alerts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param offset: Skip leading number of records.
        :type offset: int
        :param watcher_group: Show `Alerts` from specified watcher group only. Object field: watcherGroupUid. Multiple values allowed.
        :type watcher_group: str
        :param count: Returns given number of records starting from `offset` position.
        :type count: int
        :param show_read: Show read alerts.
        :type show_read: bool
        :param display_watchers: Show watcher groups info.
        :type display_watchers: bool
        :param mark_as_read: Mark displayed alerts as read.
        :type mark_as_read: bool
        :param sort: Sort results by the object's native time in descending (latest) or ascending (earliest) order
        :type sort: str
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
        :rtype: tuple(AlertListSchemaResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            '_from',
            'until',
            'offset',
            'watcher_group',
            'count',
            'show_read',
            'display_watchers',
            'mark_as_read',
            'sort'
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
                    " to method alerts_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `alerts_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `alerts_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `alerts_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `alerts_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'until' in local_var_params and local_var_params['until'] is not None:  # noqa: E501
            query_params.append(('until', local_var_params['until']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'watcher_group' in local_var_params and local_var_params['watcher_group'] is not None:  # noqa: E501
            query_params.append(('watcherGroup', local_var_params['watcher_group']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501
        if 'show_read' in local_var_params and local_var_params['show_read'] is not None:  # noqa: E501
            query_params.append(('showRead', local_var_params['show_read']))  # noqa: E501
        if 'display_watchers' in local_var_params and local_var_params['display_watchers'] is not None:  # noqa: E501
            query_params.append(('displayWatchers', local_var_params['display_watchers']))  # noqa: E501
        if 'mark_as_read' in local_var_params and local_var_params['mark_as_read'] is not None:  # noqa: E501
            query_params.append(('markAsRead', local_var_params['mark_as_read']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501

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
            200: "AlertListSchemaResponse",
            412: "OneOfstringstringstringstringstringstringstringstringstring",
        }

        return self.api_client.call_api(
            '/alerts', 'GET',
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

    def alerts_subscriptions_delete(self, endpoint, **kwargs):  # noqa: E501
        """Alerts - Alert Subscriptions - Delete  # noqa: E501

        Deletes registered endpoint. Data should be sent in request body in JSON format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.alerts_subscriptions_delete(endpoint, async_req=True)
        >>> result = thread.get()

        :param endpoint: The endpoint url to delete (required)
        :type endpoint: str
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
        return self.alerts_subscriptions_delete_with_http_info(endpoint, **kwargs)  # noqa: E501

    def alerts_subscriptions_delete_with_http_info(self, endpoint, **kwargs):  # noqa: E501
        """Alerts - Alert Subscriptions - Delete  # noqa: E501

        Deletes registered endpoint. Data should be sent in request body in JSON format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.alerts_subscriptions_delete_with_http_info(endpoint, async_req=True)
        >>> result = thread.get()

        :param endpoint: The endpoint url to delete (required)
        :type endpoint: str
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
            'endpoint'
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
                    " to method alerts_subscriptions_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'endpoint' is set
        if self.api_client.client_side_validation and ('endpoint' not in local_var_params or  # noqa: E501
                                                        local_var_params['endpoint'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `endpoint` when calling `alerts_subscriptions_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'endpoint' in local_var_params and local_var_params['endpoint'] is not None:  # noqa: E501
            query_params.append(('endpoint', local_var_params['endpoint']))  # noqa: E501

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
            '/alerts/subscriptions', 'DELETE',
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

    def alerts_subscriptions_get(self, **kwargs):  # noqa: E501
        """Alerts - Alert Subscriptions - Get  # noqa: E501

        Returns list of registered user's endpoints and their statuses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.alerts_subscriptions_get(async_req=True)
        >>> result = thread.get()

        :param endpoint: The endpoint url to receive ping notifications on new alerts.
        :type endpoint: str
        :param status: Optionally specify status of the new endpoint
        :type status: str
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
        :rtype: AlertSubscriptionSubscribeResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.alerts_subscriptions_get_with_http_info(**kwargs)  # noqa: E501

    def alerts_subscriptions_get_with_http_info(self, **kwargs):  # noqa: E501
        """Alerts - Alert Subscriptions - Get  # noqa: E501

        Returns list of registered user's endpoints and their statuses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.alerts_subscriptions_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param endpoint: The endpoint url to receive ping notifications on new alerts.
        :type endpoint: str
        :param status: Optionally specify status of the new endpoint
        :type status: str
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
        :rtype: tuple(AlertSubscriptionSubscribeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'endpoint',
            'status'
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
                    " to method alerts_subscriptions_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'endpoint' in local_var_params and local_var_params['endpoint'] is not None:  # noqa: E501
            query_params.append(('endpoint', local_var_params['endpoint']))  # noqa: E501
        if 'status' in local_var_params and local_var_params['status'] is not None:  # noqa: E501
            query_params.append(('status', local_var_params['status']))  # noqa: E501

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
            200: "AlertSubscriptionSubscribeResponse",
        }

        return self.api_client.call_api(
            '/alerts/subscriptions', 'GET',
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

    def alerts_subscriptions_post(self, alert_subscription_schema, **kwargs):  # noqa: E501
        """Alerts - Alert Subscriptions - Subscribe | Ping  # noqa: E501

        We strongly suggest to register your endpoint url to receive [ping notifications] from Intel 471 on new alerts available. Once registered, our server will send POST request to your endpoint when new alerts are fired for you. During registration our server will send a POST handshake request in JSON format with param `handshakeString` — a randomly generated string. Your endpoint should echo this response back with the same string and status 200. After this verification procedure endpoint will be registered. You can register up to 10 endpoints. <br />Handshake request example:  ```{ \"handshakeString\": \"/9fa1969e-6324-11e7-814c-0401beb96201/\" }``` <br />Example python client with ping subscription you can download here: [intel471_alert_api_client_example.py](https://titan.intel471.com/api/docs/intel471_alert_api_client_example.py) <br /><h3>Alert Subscriptions - Ping</h3> When new alerts are fired, Intel 471 API will send a POST request to all of a user's `active` endpoints. Endpoints should reply with HTTP status 200 OK. If there is no answer received from endpoint or connection with endpoint could not be established, Intel 471 API will try to ping endpoint with increasing frequency up to 24 hours. If endpoint still does not reply after that period, its status will be changed to suspended and no more requests will be sent. To enable this endpoint again, user should fix issues and change status back to active as described in section Alert subscriptions — put. <br />Ping request example: <br />```{ \"newAlertsAvailable\": true }``` <br />Example python client with ping subscription you can download here: [intel471_alert_api_client_example.py](https://titan.intel471.com/api/docs/intel471_alert_api_client_example.py) <br />   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.alerts_subscriptions_post(alert_subscription_schema, async_req=True)
        >>> result = thread.get()

        :param alert_subscription_schema: (required)
        :type alert_subscription_schema: AlertSubscriptionSchema
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
        :rtype: AlertSubscriptionSubscribeResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.alerts_subscriptions_post_with_http_info(alert_subscription_schema, **kwargs)  # noqa: E501

    def alerts_subscriptions_post_with_http_info(self, alert_subscription_schema, **kwargs):  # noqa: E501
        """Alerts - Alert Subscriptions - Subscribe | Ping  # noqa: E501

        We strongly suggest to register your endpoint url to receive [ping notifications] from Intel 471 on new alerts available. Once registered, our server will send POST request to your endpoint when new alerts are fired for you. During registration our server will send a POST handshake request in JSON format with param `handshakeString` — a randomly generated string. Your endpoint should echo this response back with the same string and status 200. After this verification procedure endpoint will be registered. You can register up to 10 endpoints. <br />Handshake request example:  ```{ \"handshakeString\": \"/9fa1969e-6324-11e7-814c-0401beb96201/\" }``` <br />Example python client with ping subscription you can download here: [intel471_alert_api_client_example.py](https://titan.intel471.com/api/docs/intel471_alert_api_client_example.py) <br /><h3>Alert Subscriptions - Ping</h3> When new alerts are fired, Intel 471 API will send a POST request to all of a user's `active` endpoints. Endpoints should reply with HTTP status 200 OK. If there is no answer received from endpoint or connection with endpoint could not be established, Intel 471 API will try to ping endpoint with increasing frequency up to 24 hours. If endpoint still does not reply after that period, its status will be changed to suspended and no more requests will be sent. To enable this endpoint again, user should fix issues and change status back to active as described in section Alert subscriptions — put. <br />Ping request example: <br />```{ \"newAlertsAvailable\": true }``` <br />Example python client with ping subscription you can download here: [intel471_alert_api_client_example.py](https://titan.intel471.com/api/docs/intel471_alert_api_client_example.py) <br />   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.alerts_subscriptions_post_with_http_info(alert_subscription_schema, async_req=True)
        >>> result = thread.get()

        :param alert_subscription_schema: (required)
        :type alert_subscription_schema: AlertSubscriptionSchema
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
        :rtype: tuple(AlertSubscriptionSubscribeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'alert_subscription_schema'
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
                    " to method alerts_subscriptions_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'alert_subscription_schema' is set
        if self.api_client.client_side_validation and ('alert_subscription_schema' not in local_var_params or  # noqa: E501
                                                        local_var_params['alert_subscription_schema'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `alert_subscription_schema` when calling `alerts_subscriptions_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'alert_subscription_schema' in local_var_params:
            body_params = local_var_params['alert_subscription_schema']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501
        
        response_types_map = {
            200: "AlertSubscriptionSubscribeResponse",
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstring",
        }

        return self.api_client.call_api(
            '/alerts/subscriptions', 'POST',
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

    def alerts_subscriptions_put(self, alert_subscription_schema, **kwargs):  # noqa: E501
        """Alerts - Alert Subscriptions - Put  # noqa: E501

        Updates status of `endpoint` url. Status should be `active` or `inactive`. Data should be sent in request body in JSON format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.alerts_subscriptions_put(alert_subscription_schema, async_req=True)
        >>> result = thread.get()

        :param alert_subscription_schema: (required)
        :type alert_subscription_schema: AlertSubscriptionSchema
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
        :rtype: AlertSubscriptionSubscribeResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.alerts_subscriptions_put_with_http_info(alert_subscription_schema, **kwargs)  # noqa: E501

    def alerts_subscriptions_put_with_http_info(self, alert_subscription_schema, **kwargs):  # noqa: E501
        """Alerts - Alert Subscriptions - Put  # noqa: E501

        Updates status of `endpoint` url. Status should be `active` or `inactive`. Data should be sent in request body in JSON format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.alerts_subscriptions_put_with_http_info(alert_subscription_schema, async_req=True)
        >>> result = thread.get()

        :param alert_subscription_schema: (required)
        :type alert_subscription_schema: AlertSubscriptionSchema
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
        :rtype: tuple(AlertSubscriptionSubscribeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'alert_subscription_schema'
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
                    " to method alerts_subscriptions_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'alert_subscription_schema' is set
        if self.api_client.client_side_validation and ('alert_subscription_schema' not in local_var_params or  # noqa: E501
                                                        local_var_params['alert_subscription_schema'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `alert_subscription_schema` when calling `alerts_subscriptions_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'alert_subscription_schema' in local_var_params:
            body_params = local_var_params['alert_subscription_schema']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501
        
        response_types_map = {
            200: "AlertSubscriptionSubscribeResponse",
            412: "OneOfstringstringstringstringstring",
        }

        return self.api_client.call_api(
            '/alerts/subscriptions', 'PUT',
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
