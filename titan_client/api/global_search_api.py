# coding: utf-8

"""
    Titan API v1

    # Introduction The Intel 471 API is organized around the principles of REST. Our API lets you gather results from our platform using anything that can send a HTTP request, including cURL and modern internet browsers. Access to this API requires an API token which is managed from your account settings.  Intel 471 reserves the right to add fields to our API however we will provide backwards compatibility and older version support so that it will be possible to choose exact versions that provide a response with an older structure.  # Authentication Authentication to the API occurs by providing your email address as the login and API key as a password in the authorization header via HTTP Basic Auth. Your API key can be found in the [API](https://portal.intel471.com/api) section on the portal. It carries many privileges so please do not expose it on public web resources.  # Accessing the API  Following examples demonstrate different methods to get the reports from `/reports` endpoint.  ## Internet browser  Just open URL: https://api.intel471.com/v1/reports  Browser will ask you for credentials, provide your email as login and API key as password.  ## cURL command line utility  Execute following command in your terminal:  ``` curl -u <YOU EMAIL>:<YOUR API KEY> https://api.intel471.com/v1/reports ```  ## Python client  We provide a [Python client](https://github.com/intel471/titan-client-python) for Intel 471's Titan API, which aims at providing common ground for all the endpoints. Please note that all the call parameters and response body fields' names are normalized to camel_case, so for example when you search reports by document type using Python client use `document_type` instead of `documentType`.  Install the client using pip (python >= 3.6 required):  ``` pip install titan-client ```  Run following script  ```python import titan_client  configuration = titan_client.Configuration(     username=\"<YOU EMAIL>\",     password=\"<YOUR API KEY>\")  with titan_client.ApiClient(configuration) as api_client:     api_instance = titan_client.ReportsApi(api_client)     api_response = api_instance.reports_get() print(api_response) ```  # Use cases  Below we present several commonly used scenarios in both raw HTTP request format and as a script using Python client. Examples are simplified so that they do not contain the authentication part and for Python client they do not contain configuration and API client object creation portion. For full example please refer to **Accessing the API** section of this document.   ## Paging  One page of the results can carry up to 100 records and you can display up to 11 pages for one query (max offset is 1000) in non-stream API endpoints. Use `count` parameter to set the number of items per page. Use `offset` parameter to shift the window by given number of results.       **HTTP**   ``` # Get 20 reports, sorted by the default field GET https://api.intel471.com/v1/reports?count=20  # Get next 20 reports GET https://api.intel471.com/v1/reports?count=20&offset=20  # Get 40 reports in one go to save API calls GET https://api.intel471.com/v1/reports?count=40 ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(count=20, offset=20) ```  ## Paging beyond the max allowed offset  Paging described in the previous use case is generally sufficient for most needs. If there are more than 1100 objects  to be obtained for a given time period and set of filter criteria, then it is possible to move the filter timestamps  along and then restart the offset sequencing. There is a very small number of situations where this may cause issues,  where there is multiple objects with the same timestamp adjacent to the last object in the response.  For the higher volume or fast changing data (such as malware indicators, malware events, creds) there are stream API endpoints  available where cursors may be used in order to acquire data easily and to avoid the need to shift timestamp ranges.  ``` # Get first 11 pages, 100 objects each  GET https://api.intel471.com/v1/reports?sort=latest&count=100 GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=1000 ... > {\"reports\": [{..., \"created\": 1661867086000}, {..., \"created\": 1661864268000}]} ```  Then the `created` time value from the last response will be used as an upper limit in the next series of calls:  ```   GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&count=100 GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=1000 ```  And so on, until the results are available or until the desired number of objects has been fetched.  ## Paging /alerts endpoint  Alerts endpoint differs from all the other non-stream API endpoints in that the `offset` parameter needs to be set  to the uid of the most recent acquired alert instead of an integer indicating the shift.  **HTTP**   ``` GET https://api.intel471.com/v1/alerts?count=100 > {\"alerts\": [{..., \"uid\": \"abc123\"}, {..., \"uid\": \"abc234\"}]}  GET https://api.intel471.com/v1/alerts?count=100&offset=abc234 > {\"alerts\": [{..., \"uid\": \"abc345\"}, {..., \"uid\": \"abc456\"}]} ```  **Python**  ``` response = titan_client.AlertsApi(api_client).alerts_get(count=100, offset=\"abc456\") ```  ## Stream endpoints paging  Stream endpoints provide the same data as their regular counterparts but they differ in a way of paging.  When working with a stream endpoint, the response always contains `cursorNext` field, which should be provided to the next subsequent  call to fetch potential next page of the results. All the subsequent calls should have the same set of query parameters as the first one,  except the cursor value. Keep calling the endpoint with a new cursor value until it stops yielding results. When new data appear after that, another call will fetch it.  **HTTP**   ``` GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT1\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT1 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT2\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT2 > {\"cursorNext\": \"MTY1NT3\"} ```  **Python**  ``` response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000) print(response.cursor_next, response.indicators) # MTY1NT1, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT1\")) print(response.cursor_next, response.indicators) # MTY1NT2, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT2\")) print(response.cursor_next, response.indicators) # MTY1NT3, None ```  ## Querying using logical operators  ### Array parameters  Any query parameter can be singular or array, if multiple parameters with the same name were provided. All parameters with the same name are internally combined into a query with `AND` operator.  So following query:  ``` GET https://api.intel471.com/v1/reports?report=sources&report=abba ```  Means \"find me reports with `source` AND `abba` in their body\".  This approach is not supported in the Python client. Instead use query string method discussed below.   ### Query string parameters  Query parameters accept Elastic's query string syntax, which allows for even better flexibility.  For example above query can be rephrased as:  **HTTP**   ``` GET https://api.intel471.com/v1/reports?report=sources OR abba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"sources OR abba\") ```  More advanced combination would include both `OR` and `AND` operators and a negation:  **HTTP**  ``` GET https://api.intel471.com/v1/reports?report=(sources OR abba) AND -creaba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"(sources OR abba) AND -creaba\") ```  Means \"find me reports with `source` or `abba` in their body which at the same time do not contain `creaba`\".  The query string \"mini-language\" reference and examples can be found on  [Elastic's query string syntax](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/query-dsl-query-string-query.html#query-dsl-query-string-query) page.  ## Get CVEs using multiple filtering criteria  Get all CVE reports for Chrome product where the risk is high and the patch is not available yet.  **HTTP**   ``` GET https://api.intel471.com/v1/cve/reports?productName=Chrome&riskLevel=high&patchStatus=unavailable ```  **Python**  ``` response = titan_client.VulnerabilitiesApi(api_client).cve_reports_get(     product_name=\"Chrome\",     risk_level=\"high\",     patch_status=\"unavailable\" ) ```  ## List watcher groups   **HTTP**   ``` GET https://api.intel471.com/v1/watcherGroups ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_get() ```  ## Create watcher group   To create a watcher group you need to pass a body along with the request.  **HTTP**   ``` POST https://api.intel471.com/v1/watcherGroups {   \"name\": \"my_group_name\",   \"description\": \"My description\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_post(   {\"name\": \"my_group_name\", \"description\": \"My description\"} ) ```  ## Create free text search watcher  **HTTP**   ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"freeTextPattern\": \"text to search\",   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"freeTextPattern\": \"text to search\",     \"notificationChannel\": \"website\"   } ) ```  ## Create specific search watcher  **HTTP**   ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"patterns\": [     {\"types\": \"Actor\" , \"pattern\": \"swisman\"}   ],   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"patterns\": [       {\"types\": \"Actor\" , \"pattern\": \"swisman\"}     ],     \"notificationChannel\": \"website\"   } ) ```  # API integration best practice with your application CORS requests to the API are not allowed due to security concerns, so please avoid AJAX calls directly from the browser. Instead consider setting up a server side proxy in your application to handle API requests.  Please consider not storing information provided by the API locally as we are constantly improving our data set and want you to have the most updated information.  # Versioning support We consistently improve our API and occasionally introduce the changes based on the customer feedback. The current API version is provided in this documentation's header. We provide API backwards compatibility whenever possible.  All requests are prefixed with the major version number, for example `/v1`:  ``` https://api.intel471.com/v1/reports ```  Different major versions are not compatible and imply significant response structure changes. Minor versions differences might include extra fields in response or provide new request parameter support. To stick to the specific version, just add `v` parameter to the request, for example: `?v=1.19.2`. If you specify a non existing version, it will be brought down to the nearest existing one.  Omitting the version parameter in the request will call the latest version of the API.  We consistently phase out the outdated versions of the API, keeping only several most recent versions. Specific version is getting disabled only when we do not record any requests using it, so it's guaranteed that calls to the outdated ones will work, though we recommend switching to the latest one as soon as possible.  We recommend to always add the version parameter to the request to be safe on API updates in your integrations.   Python client always adds the version parameter in the underlying request. API version matches the Python client's package version.   # noqa: E501

    The version of the OpenAPI document: 1.19.7
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
        :param post: Forum post search (including images via OCR).
        :type post: str
        :param private_message: Forum private message search.
        :type private_message: str
        :param private_message_subject: Search text in subjects of Private Messages.
        :type private_message_subject: str
        :param actor: Actor search.
        :type actor: str
        :param entity: Entity search.
        :type entity: str
        :param entity_type: Search by entity type.
        :type entity_type: str
        :param victim: Purported victim search.
        :type victim: str
        :param forum: Search posts in specific forum.
        :type forum: str
        :param ioc: Indicators of compromise search.
        :type ioc: str
        :param ioc_type: Search by IOC type.
        :type ioc_type: str
        :param report: Report search.
        :type report: str
        :param report_tag: Search reports by tag.
        :type report_tag: str
        :param report_location: Search reports by location.
        :type report_location: str
        :param report_admiralty_code: Search reports by admiralty code.
        :type report_admiralty_code: str
        :param report_title: Report title search.
        :type report_title: str
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
        :param nids: Free text NIDS search.
        :type nids: str
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
        :param nids_type: Search NIDS by type.
        :type nids_type: str
        :param threat_type: Search events, indicators, YARAs and malware reports by threat type.
        :type threat_type: str
        :param threat_uid: Search events, indicators, YARAs and malware reports by threat uid.
        :type threat_uid: str
        :param malware_family: Search events, indicators, YARAs and malware reports by malware family
        :type malware_family: str
        :param malware_family_profile_uid: Search events, indicators, YARAs and malware reports by malware family profile UID
        :type malware_family_profile_uid: str
        :param confidence: Search indicators, YARAs, breach alerts and NIDS by confidence
        :type confidence: str
        :param cve_report: Free text CVE reports search.
        :type cve_report: str
        :param cve_type: Search CVE reports by type.
        :type cve_type: str
        :param cve_status: Search CVE reports by status.
        :type cve_status: str
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
        :param instant_message: Free text instant messages search (including images via OCR).
        :type instant_message: str
        :param instant_message_actor: Search instant messages by author handle (actual for the moment message was written).
        :type instant_message_actor: str
        :param instant_message_service: Search instant messages by service name.
        :type instant_message_service: str
        :param instant_message_server: Search instant messages by server name.
        :type instant_message_server: str
        :param instant_message_channel: Search instant messages by channel name.
        :type instant_message_channel: str
        :param news: Free text news search
        :type news: str
        :param news_type: Search news by type.
        :type news_type: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param credential_occurrence_uid: Search by credential occurrence uid.
        :type credential_occurrence_uid: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param credential_login: Search by credential login.
        :type credential_login: str
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
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
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
        :param images: Allows to get the content with the images or placeholders inside (if present).
        :type images: str
        :param image_src_prefix: Adds defined prefix into `<img src` and `<a href` attributes.
        :type image_src_prefix: str
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
        :param post: Forum post search (including images via OCR).
        :type post: str
        :param private_message: Forum private message search.
        :type private_message: str
        :param private_message_subject: Search text in subjects of Private Messages.
        :type private_message_subject: str
        :param actor: Actor search.
        :type actor: str
        :param entity: Entity search.
        :type entity: str
        :param entity_type: Search by entity type.
        :type entity_type: str
        :param victim: Purported victim search.
        :type victim: str
        :param forum: Search posts in specific forum.
        :type forum: str
        :param ioc: Indicators of compromise search.
        :type ioc: str
        :param ioc_type: Search by IOC type.
        :type ioc_type: str
        :param report: Report search.
        :type report: str
        :param report_tag: Search reports by tag.
        :type report_tag: str
        :param report_location: Search reports by location.
        :type report_location: str
        :param report_admiralty_code: Search reports by admiralty code.
        :type report_admiralty_code: str
        :param report_title: Report title search.
        :type report_title: str
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
        :param nids: Free text NIDS search.
        :type nids: str
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
        :param nids_type: Search NIDS by type.
        :type nids_type: str
        :param threat_type: Search events, indicators, YARAs and malware reports by threat type.
        :type threat_type: str
        :param threat_uid: Search events, indicators, YARAs and malware reports by threat uid.
        :type threat_uid: str
        :param malware_family: Search events, indicators, YARAs and malware reports by malware family
        :type malware_family: str
        :param malware_family_profile_uid: Search events, indicators, YARAs and malware reports by malware family profile UID
        :type malware_family_profile_uid: str
        :param confidence: Search indicators, YARAs, breach alerts and NIDS by confidence
        :type confidence: str
        :param cve_report: Free text CVE reports search.
        :type cve_report: str
        :param cve_type: Search CVE reports by type.
        :type cve_type: str
        :param cve_status: Search CVE reports by status.
        :type cve_status: str
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
        :param instant_message: Free text instant messages search (including images via OCR).
        :type instant_message: str
        :param instant_message_actor: Search instant messages by author handle (actual for the moment message was written).
        :type instant_message_actor: str
        :param instant_message_service: Search instant messages by service name.
        :type instant_message_service: str
        :param instant_message_server: Search instant messages by server name.
        :type instant_message_server: str
        :param instant_message_channel: Search instant messages by channel name.
        :type instant_message_channel: str
        :param news: Free text news search
        :type news: str
        :param news_type: Search news by type.
        :type news_type: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param credential_uid: Search by credential uid.
        :type credential_uid: str
        :param credential_set_name: Search by credential set name.
        :type credential_set_name: str
        :param credential_set_uid: Search by credential set uid.
        :type credential_set_uid: str
        :param credential_occurrence_uid: Search by credential occurrence uid.
        :type credential_occurrence_uid: str
        :param domain: Search by credential domain (detection domain).
        :type domain: str
        :param credential_login: Search by credential login.
        :type credential_login: str
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
        :param accessed_url: Search by accessed url.
        :type accessed_url: str
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
        :param images: Allows to get the content with the images or placeholders inside (if present).
        :type images: str
        :param image_src_prefix: Adds defined prefix into `<img src` and `<a href` attributes.
        :type image_src_prefix: str
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
            'actor',
            'entity',
            'entity_type',
            'victim',
            'forum',
            'ioc',
            'ioc_type',
            'report',
            'report_tag',
            'report_location',
            'report_admiralty_code',
            'report_title',
            'document_type',
            'document_family',
            'event',
            'indicator',
            'yara',
            'nids',
            'malware_report',
            'spot_report',
            'breach_alert',
            'situation_report',
            'event_type',
            'indicator_type',
            'nids_type',
            'threat_type',
            'threat_uid',
            'malware_family',
            'malware_family_profile_uid',
            'confidence',
            'cve_report',
            'cve_type',
            'cve_status',
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
            'gir',
            'credential_uid',
            'credential_set_name',
            'credential_set_uid',
            'credential_occurrence_uid',
            'domain',
            'credential_login',
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
            'accessed_url',
            'detected_malware',
            '_from',
            'until',
            'last_updated_from',
            'last_updated_until',
            'sort',
            'filter_by_gir_set',
            'offset',
            'count',
            'images',
            'image_src_prefix'
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
        if local_var_params.get('text') is not None:  # noqa: E501
            query_params.append(('text', local_var_params['text']))  # noqa: E501
        if local_var_params.get('ip_address') is not None:  # noqa: E501
            query_params.append(('ipAddress', local_var_params['ip_address']))  # noqa: E501
        if local_var_params.get('url') is not None:  # noqa: E501
            query_params.append(('url', local_var_params['url']))  # noqa: E501
        if local_var_params.get('contact_info_email') is not None:  # noqa: E501
            query_params.append(('contactInfoEmail', local_var_params['contact_info_email']))  # noqa: E501
        if local_var_params.get('post') is not None:  # noqa: E501
            query_params.append(('post', local_var_params['post']))  # noqa: E501
        if local_var_params.get('private_message') is not None:  # noqa: E501
            query_params.append(('privateMessage', local_var_params['private_message']))  # noqa: E501
        if local_var_params.get('private_message_subject') is not None:  # noqa: E501
            query_params.append(('privateMessageSubject', local_var_params['private_message_subject']))  # noqa: E501
        if local_var_params.get('actor') is not None:  # noqa: E501
            query_params.append(('actor', local_var_params['actor']))  # noqa: E501
        if local_var_params.get('entity') is not None:  # noqa: E501
            query_params.append(('entity', local_var_params['entity']))  # noqa: E501
        if local_var_params.get('entity_type') is not None:  # noqa: E501
            query_params.append(('entityType', local_var_params['entity_type']))  # noqa: E501
        if local_var_params.get('victim') is not None:  # noqa: E501
            query_params.append(('victim', local_var_params['victim']))  # noqa: E501
        if local_var_params.get('forum') is not None:  # noqa: E501
            query_params.append(('forum', local_var_params['forum']))  # noqa: E501
        if local_var_params.get('ioc') is not None:  # noqa: E501
            query_params.append(('ioc', local_var_params['ioc']))  # noqa: E501
        if local_var_params.get('ioc_type') is not None:  # noqa: E501
            query_params.append(('iocType', local_var_params['ioc_type']))  # noqa: E501
        if local_var_params.get('report') is not None:  # noqa: E501
            query_params.append(('report', local_var_params['report']))  # noqa: E501
        if local_var_params.get('report_tag') is not None:  # noqa: E501
            query_params.append(('reportTag', local_var_params['report_tag']))  # noqa: E501
        if local_var_params.get('report_location') is not None:  # noqa: E501
            query_params.append(('reportLocation', local_var_params['report_location']))  # noqa: E501
        if local_var_params.get('report_admiralty_code') is not None:  # noqa: E501
            query_params.append(('reportAdmiraltyCode', local_var_params['report_admiralty_code']))  # noqa: E501
        if local_var_params.get('report_title') is not None:  # noqa: E501
            query_params.append(('reportTitle', local_var_params['report_title']))  # noqa: E501
        if local_var_params.get('document_type') is not None:  # noqa: E501
            query_params.append(('documentType', local_var_params['document_type']))  # noqa: E501
        if local_var_params.get('document_family') is not None:  # noqa: E501
            query_params.append(('documentFamily', local_var_params['document_family']))  # noqa: E501
        if local_var_params.get('event') is not None:  # noqa: E501
            query_params.append(('event', local_var_params['event']))  # noqa: E501
        if local_var_params.get('indicator') is not None:  # noqa: E501
            query_params.append(('indicator', local_var_params['indicator']))  # noqa: E501
        if local_var_params.get('yara') is not None:  # noqa: E501
            query_params.append(('yara', local_var_params['yara']))  # noqa: E501
        if local_var_params.get('nids') is not None:  # noqa: E501
            query_params.append(('nids', local_var_params['nids']))  # noqa: E501
        if local_var_params.get('malware_report') is not None:  # noqa: E501
            query_params.append(('malwareReport', local_var_params['malware_report']))  # noqa: E501
        if local_var_params.get('spot_report') is not None:  # noqa: E501
            query_params.append(('spotReport', local_var_params['spot_report']))  # noqa: E501
        if local_var_params.get('breach_alert') is not None:  # noqa: E501
            query_params.append(('breachAlert', local_var_params['breach_alert']))  # noqa: E501
        if local_var_params.get('situation_report') is not None:  # noqa: E501
            query_params.append(('situationReport', local_var_params['situation_report']))  # noqa: E501
        if local_var_params.get('event_type') is not None:  # noqa: E501
            query_params.append(('eventType', local_var_params['event_type']))  # noqa: E501
        if local_var_params.get('indicator_type') is not None:  # noqa: E501
            query_params.append(('indicatorType', local_var_params['indicator_type']))  # noqa: E501
        if local_var_params.get('nids_type') is not None:  # noqa: E501
            query_params.append(('nidsType', local_var_params['nids_type']))  # noqa: E501
        if local_var_params.get('threat_type') is not None:  # noqa: E501
            query_params.append(('threatType', local_var_params['threat_type']))  # noqa: E501
        if local_var_params.get('threat_uid') is not None:  # noqa: E501
            query_params.append(('threatUid', local_var_params['threat_uid']))  # noqa: E501
        if local_var_params.get('malware_family') is not None:  # noqa: E501
            query_params.append(('malwareFamily', local_var_params['malware_family']))  # noqa: E501
        if local_var_params.get('malware_family_profile_uid') is not None:  # noqa: E501
            query_params.append(('malwareFamilyProfileUid', local_var_params['malware_family_profile_uid']))  # noqa: E501
        if local_var_params.get('confidence') is not None:  # noqa: E501
            query_params.append(('confidence', local_var_params['confidence']))  # noqa: E501
        if local_var_params.get('cve_report') is not None:  # noqa: E501
            query_params.append(('cveReport', local_var_params['cve_report']))  # noqa: E501
        if local_var_params.get('cve_type') is not None:  # noqa: E501
            query_params.append(('cveType', local_var_params['cve_type']))  # noqa: E501
        if local_var_params.get('cve_status') is not None:  # noqa: E501
            query_params.append(('cveStatus', local_var_params['cve_status']))  # noqa: E501
        if local_var_params.get('cve_name') is not None:  # noqa: E501
            query_params.append(('cveName', local_var_params['cve_name']))  # noqa: E501
        if local_var_params.get('risk_level') is not None:  # noqa: E501
            query_params.append(('riskLevel', local_var_params['risk_level']))  # noqa: E501
        if local_var_params.get('patch_status') is not None:  # noqa: E501
            query_params.append(('patchStatus', local_var_params['patch_status']))  # noqa: E501
        if local_var_params.get('vendor_name') is not None:  # noqa: E501
            query_params.append(('vendorName', local_var_params['vendor_name']))  # noqa: E501
        if local_var_params.get('product_name') is not None:  # noqa: E501
            query_params.append(('productName', local_var_params['product_name']))  # noqa: E501
        if local_var_params.get('instant_message') is not None:  # noqa: E501
            query_params.append(('instantMessage', local_var_params['instant_message']))  # noqa: E501
        if local_var_params.get('instant_message_actor') is not None:  # noqa: E501
            query_params.append(('instantMessageActor', local_var_params['instant_message_actor']))  # noqa: E501
        if local_var_params.get('instant_message_service') is not None:  # noqa: E501
            query_params.append(('instantMessageService', local_var_params['instant_message_service']))  # noqa: E501
        if local_var_params.get('instant_message_server') is not None:  # noqa: E501
            query_params.append(('instantMessageServer', local_var_params['instant_message_server']))  # noqa: E501
        if local_var_params.get('instant_message_channel') is not None:  # noqa: E501
            query_params.append(('instantMessageChannel', local_var_params['instant_message_channel']))  # noqa: E501
        if local_var_params.get('news') is not None:  # noqa: E501
            query_params.append(('news', local_var_params['news']))  # noqa: E501
        if local_var_params.get('news_type') is not None:  # noqa: E501
            query_params.append(('newsType', local_var_params['news_type']))  # noqa: E501
        if local_var_params.get('gir') is not None:  # noqa: E501
            query_params.append(('gir', local_var_params['gir']))  # noqa: E501
        if local_var_params.get('credential_uid') is not None:  # noqa: E501
            query_params.append(('credentialUid', local_var_params['credential_uid']))  # noqa: E501
        if local_var_params.get('credential_set_name') is not None:  # noqa: E501
            query_params.append(('credentialSetName', local_var_params['credential_set_name']))  # noqa: E501
        if local_var_params.get('credential_set_uid') is not None:  # noqa: E501
            query_params.append(('credentialSetUid', local_var_params['credential_set_uid']))  # noqa: E501
        if local_var_params.get('credential_occurrence_uid') is not None:  # noqa: E501
            query_params.append(('credentialOccurrenceUid', local_var_params['credential_occurrence_uid']))  # noqa: E501
        if local_var_params.get('domain') is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if local_var_params.get('credential_login') is not None:  # noqa: E501
            query_params.append(('credentialLogin', local_var_params['credential_login']))  # noqa: E501
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
        if local_var_params.get('accessed_url') is not None:  # noqa: E501
            query_params.append(('accessedUrl', local_var_params['accessed_url']))  # noqa: E501
        if local_var_params.get('detected_malware') is not None:  # noqa: E501
            query_params.append(('detectedMalware', local_var_params['detected_malware']))  # noqa: E501
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
        if local_var_params.get('images') is not None:  # noqa: E501
            query_params.append(('images', local_var_params['images']))  # noqa: E501
        if local_var_params.get('image_src_prefix') is not None:  # noqa: E501
            query_params.append(('imageSrcPrefix', local_var_params['image_src_prefix']))  # noqa: E501

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
            200: "SearchSchema",
            412: "CredentialSetsGet412Response",
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
