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


class GlobalSearchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_get(self, **kwargs):  # noqa: E501
        """Search - Global Search  # noqa: E501

        Returns selection of results matching filter criteria. Can include the following entities:   - [Information Reports](#tag/Reports/paths/~1reports/get)   - [Fintel Reports](#tag/Reports/paths/~1reports/get)   - [Actors](#tag/Actors/paths/~1actors/get)   - [Entities](#tag/Entities/paths/~1entities/get)   - [Indicators of Compromise](#tag/Indicators/paths/~1indicators/get)   - [Posts](#tag/Forums/paths/~1posts/get)   - [PrivateMessages](#tag/Forums/paths/~1privateMessages/get)   - [Events](#tag/Events/paths/~1events/get)   - [Indicators](#tag/Indicators/paths/~1indicators/get)   - [YARA](#tag/YARA/paths/~1yara/get)   - [Malware Reports](#tag/Malware/paths/~1malwareReports/get)   - [Breach Alerts](#tag/Reports/paths/~1breachAlerts/get)   - [Spot Reports](#tag/Reports/paths/~1spotReports/get)   - [Situation Reports](#tag/Global-Search/paths/~1search/get)   - [Cve Reports](#tag/Vulnerabilities/paths/~1cve~1reports/get)   - [Instant Messages](#tag/Messaging-Services/paths/~1messagingServices~1instantMessages/get)   - [News](#tag/News/paths/~1news/get)   - [Credential Sets](#tag/Credentials/paths/~1credentialSets/get)   - [Credentials](#tag/Credentials/paths/~1credentials/get)   - [Credential Occurrences](#tag/Credentials/paths/~1credentials~1occurrences/get)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_get(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere.
        :type text: str
        :param ip_address: IP address search.
        :type ip_address: str
        :param url: URL search.
        :type url: str
        :param contact_info_email: E-mail address search.
        :type contact_info_email: str
        :param post: Forum post search.
        :type post: str
        :param private_message: Forum private message search.
        :type private_message: str
        :param private_message_subject: Search text in subjects of Private Messages.
        :type private_message_subject: str
        :param actors: Actor search.
        :type actors: str
        :param entity: Entity Search.
        :type entity: str
        :param victim: Purported victim search.
        :type victim: str
        :param ioc: Indicators of compromise search.
        :type ioc: str
        :param report: Report search.
        :type report: str
        :param report_tag: Search reports by tag.
        :type report_tag: str
        :param report_location: Search reports by location.
        :type report_location: str
        :param report_admiralty_code: Search reports by admiralty code.
        :type report_admiralty_code: str
        :param document_type: Search reports by document type.
        :type document_type: str
        :param document_family: Search reports by document family.
        :type document_family: str
        :param event: Free text event search.
        :type event: str
        :param indicator: Free text indicator search.
        :type indicator: str
        :param yara: Free text YARAs search.
        :type yara: str
        :param malware_report: Free text malware reports search.
        :type malware_report: str
        :param spot_report: Free text spot reports search.
        :type spot_report: str
        :param breach_alert: Free text breach alerts search.
        :type breach_alert: str
        :param situation_report: Free text situation reports search.
        :type situation_report: str
        :param event_type: Search events by type.
        :type event_type: str
        :param indicator_type: Search indicators by type.
        :type indicator_type: str
        :param threat_type: Search events, indicators, YARAs and malware reports by threat type.
        :type threat_type: str
        :param threat_uid: Search events, indicators, YARAs and malware reports by threat uid.
        :type threat_uid: str
        :param malware_family: Search events, indicators, YARAs and malware reports by malware family
        :type malware_family: str
        :param malware_family_profile_uid: Search events, indicators, YARAs and malware reports by malware family profile UID
        :type malware_family_profile_uid: str
        :param confidence: Search indicators and YARAs by confidence
        :type confidence: str
        :param cve_report: Free text CVE reports search.
        :type cve_report: str
        :param cve_type: Search CVE reports by type.
        :type cve_type: str
        :param cve_name: Search CVE reports by name.
        :type cve_name: str
        :param risk_level: Search CVE reports by risk level.
        :type risk_level: str
        :param patch_status: Search CVE reports by patch status.
        :type patch_status: str
        :param vendor_name: Search CVE reports by vendor name.
        :type vendor_name: str
        :param product_name: Search CVE reports by product name.
        :type product_name: str
        :param instant_message: Free text instant messages search.
        :type instant_message: str
        :param instant_message_actor: Search instant messages by author handle (actual for the moment message was written).
        :type instant_message_actor: str
        :param instant_message_service: Search instant messages by service name (e.g. Telegram, Discord, WhatsApp etc.).
        :type instant_message_service: str
        :param instant_message_server: Search instant messages by server name.
        :type instant_message_server: str
        :param instant_message_channel: Search instant messages by channel name.
        :type instant_message_channel: str
        :param news: Free text news search
        :type news: str
        :param news_type: Search news by type (e.g. BLOG, ANNOUNCEMENT).
        :type news_type: str
        :param entity_type: Search by entity type.
        :type entity_type: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
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
        :param detected_malware: Search by credential detected malware.
        :type detected_malware: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order.
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
        :rtype: SearchSchema
        """
        kwargs['_return_http_data_only'] = True
        return self.search_get_with_http_info(**kwargs)  # noqa: E501

    def search_get_with_http_info(self, **kwargs):  # noqa: E501
        """Search - Global Search  # noqa: E501

        Returns selection of results matching filter criteria. Can include the following entities:   - [Information Reports](#tag/Reports/paths/~1reports/get)   - [Fintel Reports](#tag/Reports/paths/~1reports/get)   - [Actors](#tag/Actors/paths/~1actors/get)   - [Entities](#tag/Entities/paths/~1entities/get)   - [Indicators of Compromise](#tag/Indicators/paths/~1indicators/get)   - [Posts](#tag/Forums/paths/~1posts/get)   - [PrivateMessages](#tag/Forums/paths/~1privateMessages/get)   - [Events](#tag/Events/paths/~1events/get)   - [Indicators](#tag/Indicators/paths/~1indicators/get)   - [YARA](#tag/YARA/paths/~1yara/get)   - [Malware Reports](#tag/Malware/paths/~1malwareReports/get)   - [Breach Alerts](#tag/Reports/paths/~1breachAlerts/get)   - [Spot Reports](#tag/Reports/paths/~1spotReports/get)   - [Situation Reports](#tag/Global-Search/paths/~1search/get)   - [Cve Reports](#tag/Vulnerabilities/paths/~1cve~1reports/get)   - [Instant Messages](#tag/Messaging-Services/paths/~1messagingServices~1instantMessages/get)   - [News](#tag/News/paths/~1news/get)   - [Credential Sets](#tag/Credentials/paths/~1credentialSets/get)   - [Credentials](#tag/Credentials/paths/~1credentials/get)   - [Credential Occurrences](#tag/Credentials/paths/~1credentials~1occurrences/get)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param text: Search text everywhere.
        :type text: str
        :param ip_address: IP address search.
        :type ip_address: str
        :param url: URL search.
        :type url: str
        :param contact_info_email: E-mail address search.
        :type contact_info_email: str
        :param post: Forum post search.
        :type post: str
        :param private_message: Forum private message search.
        :type private_message: str
        :param private_message_subject: Search text in subjects of Private Messages.
        :type private_message_subject: str
        :param actors: Actor search.
        :type actors: str
        :param entity: Entity Search.
        :type entity: str
        :param victim: Purported victim search.
        :type victim: str
        :param ioc: Indicators of compromise search.
        :type ioc: str
        :param report: Report search.
        :type report: str
        :param report_tag: Search reports by tag.
        :type report_tag: str
        :param report_location: Search reports by location.
        :type report_location: str
        :param report_admiralty_code: Search reports by admiralty code.
        :type report_admiralty_code: str
        :param document_type: Search reports by document type.
        :type document_type: str
        :param document_family: Search reports by document family.
        :type document_family: str
        :param event: Free text event search.
        :type event: str
        :param indicator: Free text indicator search.
        :type indicator: str
        :param yara: Free text YARAs search.
        :type yara: str
        :param malware_report: Free text malware reports search.
        :type malware_report: str
        :param spot_report: Free text spot reports search.
        :type spot_report: str
        :param breach_alert: Free text breach alerts search.
        :type breach_alert: str
        :param situation_report: Free text situation reports search.
        :type situation_report: str
        :param event_type: Search events by type.
        :type event_type: str
        :param indicator_type: Search indicators by type.
        :type indicator_type: str
        :param threat_type: Search events, indicators, YARAs and malware reports by threat type.
        :type threat_type: str
        :param threat_uid: Search events, indicators, YARAs and malware reports by threat uid.
        :type threat_uid: str
        :param malware_family: Search events, indicators, YARAs and malware reports by malware family
        :type malware_family: str
        :param malware_family_profile_uid: Search events, indicators, YARAs and malware reports by malware family profile UID
        :type malware_family_profile_uid: str
        :param confidence: Search indicators and YARAs by confidence
        :type confidence: str
        :param cve_report: Free text CVE reports search.
        :type cve_report: str
        :param cve_type: Search CVE reports by type.
        :type cve_type: str
        :param cve_name: Search CVE reports by name.
        :type cve_name: str
        :param risk_level: Search CVE reports by risk level.
        :type risk_level: str
        :param patch_status: Search CVE reports by patch status.
        :type patch_status: str
        :param vendor_name: Search CVE reports by vendor name.
        :type vendor_name: str
        :param product_name: Search CVE reports by product name.
        :type product_name: str
        :param instant_message: Free text instant messages search.
        :type instant_message: str
        :param instant_message_actor: Search instant messages by author handle (actual for the moment message was written).
        :type instant_message_actor: str
        :param instant_message_service: Search instant messages by service name (e.g. Telegram, Discord, WhatsApp etc.).
        :type instant_message_service: str
        :param instant_message_server: Search instant messages by server name.
        :type instant_message_server: str
        :param instant_message_channel: Search instant messages by channel name.
        :type instant_message_channel: str
        :param news: Free text news search
        :type news: str
        :param news_type: Search news by type (e.g. BLOG, ANNOUNCEMENT).
        :type news_type: str
        :param entity_type: Search by entity type.
        :type entity_type: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
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
        :param detected_malware: Search by credential detected malware.
        :type detected_malware: str
        :param _from: Long unix time or string time range. Search data starting from given creation time (including).
        :type _from: str
        :param until: Long unix time or string time range. Search data ending before given creation time (excluding).
        :type until: str
        :param last_updated_from: Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.
        :type last_updated_from: str
        :param last_updated_until: Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.
        :type last_updated_until: str
        :param sort: Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order.
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
        :rtype: tuple(SearchSchema, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'text',
            'ip_address',
            'url',
            'contact_info_email',
            'post',
            'private_message',
            'private_message_subject',
            'actors',
            'entity',
            'victim',
            'ioc',
            'report',
            'report_tag',
            'report_location',
            'report_admiralty_code',
            'document_type',
            'document_family',
            'event',
            'indicator',
            'yara',
            'malware_report',
            'spot_report',
            'breach_alert',
            'situation_report',
            'event_type',
            'indicator_type',
            'threat_type',
            'threat_uid',
            'malware_family',
            'malware_family_profile_uid',
            'confidence',
            'cve_report',
            'cve_type',
            'cve_name',
            'risk_level',
            'patch_status',
            'vendor_name',
            'product_name',
            'instant_message',
            'instant_message_actor',
            'instant_message_service',
            'instant_message_server',
            'instant_message_channel',
            'news',
            'news_type',
            'entity_type',
            'gir',
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
            'detected_malware',
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
                    " to method search_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'password_length_gte' in local_var_params and local_var_params['password_length_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_length_gte` when calling `search_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_lowercase_gte' in local_var_params and local_var_params['password_lowercase_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_lowercase_gte` when calling `search_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_uppercase_gte' in local_var_params and local_var_params['password_uppercase_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_uppercase_gte` when calling `search_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_numbers_gte' in local_var_params and local_var_params['password_numbers_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_numbers_gte` when calling `search_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_punctuation_gte' in local_var_params and local_var_params['password_punctuation_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_punctuation_gte` when calling `search_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_symbols_gte' in local_var_params and local_var_params['password_symbols_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_symbols_gte` when calling `search_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_separators_gte' in local_var_params and local_var_params['password_separators_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_separators_gte` when calling `search_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_other_gte' in local_var_params and local_var_params['password_other_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_other_gte` when calling `search_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'password_entropy_gte' in local_var_params and local_var_params['password_entropy_gte'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `password_entropy_gte` when calling `search_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `search_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `search_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `search_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `search_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text' in local_var_params and local_var_params['text'] is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if 'ip_address' in local_var_params and local_var_params['ip_address'] is not None:  # noqa: E501
            query_params.append(('ipAddress', local_var_params['ip_address']))  # noqa: E501
        if 'url' in local_var_params and local_var_params['url'] is not None:  # noqa: E501
            query_params.append(('url', local_var_params['url']))  # noqa: E501
        if 'contact_info_email' in local_var_params and local_var_params['contact_info_email'] is not None:  # noqa: E501
            query_params.append(('contactInfoEmail', local_var_params['contact_info_email']))  # noqa: E501
        if 'post' in local_var_params and local_var_params['post'] is not None:  # noqa: E501
            query_params.append(('post', local_var_params['post']))  # noqa: E501
        if 'private_message' in local_var_params and local_var_params['private_message'] is not None:  # noqa: E501
            query_params.append(('privateMessage', local_var_params['private_message']))  # noqa: E501
        if 'private_message_subject' in local_var_params and local_var_params['private_message_subject'] is not None:  # noqa: E501
            query_params.append(('privateMessageSubject', local_var_params['private_message_subject']))  # noqa: E501
        if 'actors' in local_var_params and local_var_params['actors'] is not None:  # noqa: E501
            query_params.append(('actors', local_var_params['actors']))  # noqa: E501
        if 'entity' in local_var_params and local_var_params['entity'] is not None:  # noqa: E501
            query_params.append(('entity', local_var_params['entity']))  # noqa: E501
        if 'victim' in local_var_params and local_var_params['victim'] is not None:  # noqa: E501
            query_params.append(('victim', local_var_params['victim']))  # noqa: E501
        if 'ioc' in local_var_params and local_var_params['ioc'] is not None:  # noqa: E501
            query_params.append(('ioc', local_var_params['ioc']))  # noqa: E501
        if 'report' in local_var_params and local_var_params['report'] is not None:  # noqa: E501
            query_params.append(('report', local_var_params['report']))  # noqa: E501
        if 'report_tag' in local_var_params and local_var_params['report_tag'] is not None:  # noqa: E501
            query_params.append(('reportTag', local_var_params['report_tag']))  # noqa: E501
        if 'report_location' in local_var_params and local_var_params['report_location'] is not None:  # noqa: E501
            query_params.append(('reportLocation', local_var_params['report_location']))  # noqa: E501
        if 'report_admiralty_code' in local_var_params and local_var_params['report_admiralty_code'] is not None:  # noqa: E501
            query_params.append(('reportAdmiraltyCode', local_var_params['report_admiralty_code']))  # noqa: E501
        if 'document_type' in local_var_params and local_var_params['document_type'] is not None:  # noqa: E501
            query_params.append(('documentType', local_var_params['document_type']))  # noqa: E501
        if 'document_family' in local_var_params and local_var_params['document_family'] is not None:  # noqa: E501
            query_params.append(('documentFamily', local_var_params['document_family']))  # noqa: E501
        if 'event' in local_var_params and local_var_params['event'] is not None:  # noqa: E501
            query_params.append(('event', local_var_params['event']))  # noqa: E501
        if 'indicator' in local_var_params and local_var_params['indicator'] is not None:  # noqa: E501
            query_params.append(('indicator', local_var_params['indicator']))  # noqa: E501
        if 'yara' in local_var_params and local_var_params['yara'] is not None:  # noqa: E501
            query_params.append(('yara', local_var_params['yara']))  # noqa: E501
        if 'malware_report' in local_var_params and local_var_params['malware_report'] is not None:  # noqa: E501
            query_params.append(('malwareReport', local_var_params['malware_report']))  # noqa: E501
        if 'spot_report' in local_var_params and local_var_params['spot_report'] is not None:  # noqa: E501
            query_params.append(('spotReport', local_var_params['spot_report']))  # noqa: E501
        if 'breach_alert' in local_var_params and local_var_params['breach_alert'] is not None:  # noqa: E501
            query_params.append(('breachAlert', local_var_params['breach_alert']))  # noqa: E501
        if 'situation_report' in local_var_params and local_var_params['situation_report'] is not None:  # noqa: E501
            query_params.append(('situationReport', local_var_params['situation_report']))  # noqa: E501
        if 'event_type' in local_var_params and local_var_params['event_type'] is not None:  # noqa: E501
            query_params.append(('eventType', local_var_params['event_type']))  # noqa: E501
        if 'indicator_type' in local_var_params and local_var_params['indicator_type'] is not None:  # noqa: E501
            query_params.append(('indicatorType', local_var_params['indicator_type']))  # noqa: E501
        if 'threat_type' in local_var_params and local_var_params['threat_type'] is not None:  # noqa: E501
            query_params.append(('threatType', local_var_params['threat_type']))  # noqa: E501
        if 'threat_uid' in local_var_params and local_var_params['threat_uid'] is not None:  # noqa: E501
            query_params.append(('threatUid', local_var_params['threat_uid']))  # noqa: E501
        if 'malware_family' in local_var_params and local_var_params['malware_family'] is not None:  # noqa: E501
            query_params.append(('malwareFamily', local_var_params['malware_family']))  # noqa: E501
        if 'malware_family_profile_uid' in local_var_params and local_var_params['malware_family_profile_uid'] is not None:  # noqa: E501
            query_params.append(('malwareFamilyProfileUid', local_var_params['malware_family_profile_uid']))  # noqa: E501
        if 'confidence' in local_var_params and local_var_params['confidence'] is not None:  # noqa: E501
            query_params.append(('confidence', local_var_params['confidence']))  # noqa: E501
        if 'cve_report' in local_var_params and local_var_params['cve_report'] is not None:  # noqa: E501
            query_params.append(('cveReport', local_var_params['cve_report']))  # noqa: E501
        if 'cve_type' in local_var_params and local_var_params['cve_type'] is not None:  # noqa: E501
            query_params.append(('cveType', local_var_params['cve_type']))  # noqa: E501
        if 'cve_name' in local_var_params and local_var_params['cve_name'] is not None:  # noqa: E501
            query_params.append(('cveName', local_var_params['cve_name']))  # noqa: E501
        if 'risk_level' in local_var_params and local_var_params['risk_level'] is not None:  # noqa: E501
            query_params.append(('riskLevel', local_var_params['risk_level']))  # noqa: E501
        if 'patch_status' in local_var_params and local_var_params['patch_status'] is not None:  # noqa: E501
            query_params.append(('patchStatus', local_var_params['patch_status']))  # noqa: E501
        if 'vendor_name' in local_var_params and local_var_params['vendor_name'] is not None:  # noqa: E501
            query_params.append(('vendorName', local_var_params['vendor_name']))  # noqa: E501
        if 'product_name' in local_var_params and local_var_params['product_name'] is not None:  # noqa: E501
            query_params.append(('productName', local_var_params['product_name']))  # noqa: E501
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
        if 'news' in local_var_params and local_var_params['news'] is not None:  # noqa: E501
            query_params.append(('news', local_var_params['news']))  # noqa: E501
        if 'news_type' in local_var_params and local_var_params['news_type'] is not None:  # noqa: E501
            query_params.append(('newsType', local_var_params['news_type']))  # noqa: E501
        if 'entity_type' in local_var_params and local_var_params['entity_type'] is not None:  # noqa: E501
            query_params.append(('entityType', local_var_params['entity_type']))  # noqa: E501
        if 'gir' in local_var_params and local_var_params['gir'] is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
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
        if 'detected_malware' in local_var_params and local_var_params['detected_malware'] is not None:  # noqa: E501
            query_params.append(('detectedMalware', local_var_params['detected_malware']))  # noqa: E501
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
            200: "SearchSchema",
            412: "OneOfstringstringstringstringstringstringstringstringstringstringstringstringstringstringstring",
        }

        return self.api_client.call_api(
            '/search', 'GET',
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
