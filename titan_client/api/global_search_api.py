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
from titan_client.models.search_schema import SearchSchema

from titan_client.api_client import ApiClient, RequestSerialized
from titan_client.api_response import ApiResponse
from titan_client.rest import RESTResponseType


class GlobalSearchApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def search_get(
        self,
        text: Annotated[Optional[StrictStr], Field(description="Search text everywhere.")] = None,
        ip_address: Annotated[Optional[StrictStr], Field(description="IP address search.")] = None,
        url: Annotated[Optional[StrictStr], Field(description="URL search.")] = None,
        contact_info_email: Annotated[Optional[StrictStr], Field(description="E-mail address search.")] = None,
        post: Annotated[Optional[StrictStr], Field(description="Forum post search (including images via OCR).")] = None,
        private_message: Annotated[Optional[StrictStr], Field(description="Forum private message search.")] = None,
        private_message_subject: Annotated[Optional[StrictStr], Field(description="Search text in subjects of Private Messages.")] = None,
        actor: Annotated[Optional[StrictStr], Field(description="Actor search.")] = None,
        entity: Annotated[Optional[StrictStr], Field(description="Entity search.")] = None,
        entity_type: Annotated[Optional[StrictStr], Field(description="Search by entity type.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Purported victim search.")] = None,
        forum: Annotated[Optional[StrictStr], Field(description="Search posts in specific forum.")] = None,
        ioc: Annotated[Optional[StrictStr], Field(description="Indicators of compromise search.")] = None,
        ioc_type: Annotated[Optional[StrictStr], Field(description="Search by IOC type.")] = None,
        report: Annotated[Optional[StrictStr], Field(description="Report search.")] = None,
        report_tag: Annotated[Optional[StrictStr], Field(description="Search reports by tag.")] = None,
        report_location: Annotated[Optional[StrictStr], Field(description="Search reports by location.")] = None,
        report_admiralty_code: Annotated[Optional[StrictStr], Field(description="Search reports by admiralty code.")] = None,
        report_title: Annotated[Optional[StrictStr], Field(description="Report title search.")] = None,
        document_type: Annotated[Optional[StrictStr], Field(description="Search reports by document type.")] = None,
        document_family: Annotated[Optional[StrictStr], Field(description="Search reports by document family.")] = None,
        event: Annotated[Optional[StrictStr], Field(description="Free text event search.")] = None,
        indicator: Annotated[Optional[StrictStr], Field(description="Free text indicator search.")] = None,
        yara: Annotated[Optional[StrictStr], Field(description="Free text YARAs search.")] = None,
        nids: Annotated[Optional[StrictStr], Field(description="Free text NIDS search.")] = None,
        malware_report: Annotated[Optional[StrictStr], Field(description="Free text malware reports search.")] = None,
        spot_report: Annotated[Optional[StrictStr], Field(description="Free text spot reports search.")] = None,
        breach_alert: Annotated[Optional[StrictStr], Field(description="Free text breach alerts search.")] = None,
        situation_report: Annotated[Optional[StrictStr], Field(description="Free text situation reports search.")] = None,
        event_type: Annotated[Optional[StrictStr], Field(description="Search events by type.")] = None,
        indicator_type: Annotated[Optional[StrictStr], Field(description="Search indicators by type.")] = None,
        nids_type: Annotated[Optional[StrictStr], Field(description="Search NIDS by type.")] = None,
        threat_type: Annotated[Optional[StrictStr], Field(description="Search events, indicators, YARAs and malware reports by threat type.")] = None,
        threat_uid: Annotated[Optional[StrictStr], Field(description="Search events, indicators, YARAs and malware reports by threat uid.")] = None,
        malware_family: Annotated[Optional[StrictStr], Field(description="Search events, indicators, YARAs and malware reports by malware family")] = None,
        malware_family_profile_uid: Annotated[Optional[StrictStr], Field(description="Search events, indicators, YARAs and malware reports by malware family profile UID")] = None,
        confidence: Annotated[Optional[StrictStr], Field(description="Search indicators, YARAs, breach alerts and NIDS by confidence")] = None,
        cve_report: Annotated[Optional[StrictStr], Field(description="Free text CVE reports search.")] = None,
        cve_type: Annotated[Optional[StrictStr], Field(description="Search CVE reports by type.")] = None,
        cve_status: Annotated[Optional[StrictStr], Field(description="Search CVE reports by status.")] = None,
        cve_name: Annotated[Optional[StrictStr], Field(description="Search CVE reports by name.")] = None,
        risk_level: Annotated[Optional[StrictStr], Field(description="Search CVE reports by risk level.")] = None,
        patch_status: Annotated[Optional[StrictStr], Field(description="Search CVE reports by patch status.")] = None,
        vendor_name: Annotated[Optional[StrictStr], Field(description="Search CVE reports by vendor name.")] = None,
        product_name: Annotated[Optional[StrictStr], Field(description="Search CVE reports by product name.")] = None,
        instant_message: Annotated[Optional[StrictStr], Field(description="Free text instant messages search (including images via OCR).")] = None,
        instant_message_actor: Annotated[Optional[StrictStr], Field(description="Search instant messages by author handle (actual for the moment message was written).")] = None,
        instant_message_service: Annotated[Optional[StrictStr], Field(description="Search instant messages by service name.")] = None,
        instant_message_server: Annotated[Optional[StrictStr], Field(description="Search instant messages by server name.")] = None,
        instant_message_channel: Annotated[Optional[StrictStr], Field(description="Search instant messages by channel name.")] = None,
        news: Annotated[Optional[StrictStr], Field(description="Free text news search")] = None,
        news_type: Annotated[Optional[StrictStr], Field(description="Search news by type.")] = None,
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        credential_uid: Annotated[Optional[StrictStr], Field(description="Search by credential uid.")] = None,
        credential_set_name: Annotated[Optional[StrictStr], Field(description="Search by credential set name.")] = None,
        credential_set_uid: Annotated[Optional[StrictStr], Field(description="Search by credential set uid.")] = None,
        credential_occurrence_uid: Annotated[Optional[StrictStr], Field(description="Search by credential occurrence uid.")] = None,
        domain: Annotated[Optional[StrictStr], Field(description="Search by credential domain (detection domain).")] = None,
        credential_login: Annotated[Optional[StrictStr], Field(description="Search by credential login.")] = None,
        affiliation_group: Annotated[Optional[StrictStr], Field(description="Search by credential affiliation group.")] = None,
        password_strength: Annotated[Optional[StrictStr], Field(description="Search by password strength.")] = None,
        password_length_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity length field as greater then or equal to input value.")] = None,
        password_lowercase_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity lowercase filed as greater then or equal to input value.")] = None,
        password_uppercase_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity uppercase filed as greater then or equal to input value.")] = None,
        password_numbers_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity numbers filed as greater then or equal to input value.")] = None,
        password_punctuation_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity punctuation filed as greater then or equal to input value.")] = None,
        password_symbols_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity symbols filed as greater then or equal to input value.")] = None,
        password_separators_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity separators filed as greater then or equal to input value.")] = None,
        password_other_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity other filed as greater then or equal to input value.")] = None,
        password_entropy_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity entropy filed as greater then or equal to input value.")] = None,
        password_plain: Annotated[Optional[StrictStr], Field(description="Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded.")] = None,
        accessed_url: Annotated[Optional[StrictStr], Field(description="Search by accessed url.")] = None,
        detected_malware: Annotated[Optional[StrictStr], Field(description="Search by credential detected malware.")] = None,
        data_leak_post: Annotated[Optional[StrictStr], Field(description="Search text in data leak posts and topics (including images via OCR).")] = None,
        data_leak_posts_by_thread_uid: Annotated[Optional[StrictStr], Field(description="Search data leak posts by thread uid.")] = None,
        data_leak_blog: Annotated[Optional[StrictStr], Field(description="Search data leak posts in a given data leak blog.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order.")] = None,
        filter_by_gir_set: Annotated[Optional[StrictStr], Field(description="Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required")] = None,
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
    ) -> SearchSchema:
        """Search - Global Search

        Returns selection of results matching filter criteria. Can include the following entities:   - [Information Reports](#tag/Reports/paths/~1reports/get)   - [Fintel Reports](#tag/Reports/paths/~1reports/get)   - [Actors](#tag/Actors/paths/~1actors/get)   - [Entities](#tag/Entities/paths/~1entities/get)   - [Indicators of Compromise](#tag/Indicators/paths/~1indicators/get)   - [Posts](#tag/Forums/paths/~1posts/get)   - [PrivateMessages](#tag/Forums/paths/~1privateMessages/get)   - [Events](#tag/Events/paths/~1events/get)   - [Indicators](#tag/Indicators/paths/~1indicators/get)   - [YARA](#tag/YARA/paths/~1yara/get)   - [Malware Reports](#tag/Malware/paths/~1malwareReports/get)   - [Breach Alerts](#tag/Reports/paths/~1breachAlerts/get)   - [Spot Reports](#tag/Reports/paths/~1spotReports/get)   - [Situation Reports](#tag/Global-Search/paths/~1search/get)   - [Cve Reports](#tag/Vulnerabilities/paths/~1cve~1reports/get)   - [Instant Messages](#tag/Messaging-Services/paths/~1messagingServices~1instantMessages/get)   - [News](#tag/News/paths/~1news/get)   - [Credential Sets](#tag/Credentials/paths/~1credentialSets/get)   - [Credentials](#tag/Credentials/paths/~1credentials/get)   - [Credential Occurrences](#tag/Credentials/paths/~1credentials~1occurrences/get)   - [Data Leak Blogs](#tag/Data-Leak-Blogs/paths/~1dataleak~1posts/get) 

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
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
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

        _param = self._search_get_serialize(
            text=text,
            ip_address=ip_address,
            url=url,
            contact_info_email=contact_info_email,
            post=post,
            private_message=private_message,
            private_message_subject=private_message_subject,
            actor=actor,
            entity=entity,
            entity_type=entity_type,
            victim=victim,
            forum=forum,
            ioc=ioc,
            ioc_type=ioc_type,
            report=report,
            report_tag=report_tag,
            report_location=report_location,
            report_admiralty_code=report_admiralty_code,
            report_title=report_title,
            document_type=document_type,
            document_family=document_family,
            event=event,
            indicator=indicator,
            yara=yara,
            nids=nids,
            malware_report=malware_report,
            spot_report=spot_report,
            breach_alert=breach_alert,
            situation_report=situation_report,
            event_type=event_type,
            indicator_type=indicator_type,
            nids_type=nids_type,
            threat_type=threat_type,
            threat_uid=threat_uid,
            malware_family=malware_family,
            malware_family_profile_uid=malware_family_profile_uid,
            confidence=confidence,
            cve_report=cve_report,
            cve_type=cve_type,
            cve_status=cve_status,
            cve_name=cve_name,
            risk_level=risk_level,
            patch_status=patch_status,
            vendor_name=vendor_name,
            product_name=product_name,
            instant_message=instant_message,
            instant_message_actor=instant_message_actor,
            instant_message_service=instant_message_service,
            instant_message_server=instant_message_server,
            instant_message_channel=instant_message_channel,
            news=news,
            news_type=news_type,
            gir=gir,
            credential_uid=credential_uid,
            credential_set_name=credential_set_name,
            credential_set_uid=credential_set_uid,
            credential_occurrence_uid=credential_occurrence_uid,
            domain=domain,
            credential_login=credential_login,
            affiliation_group=affiliation_group,
            password_strength=password_strength,
            password_length_gte=password_length_gte,
            password_lowercase_gte=password_lowercase_gte,
            password_uppercase_gte=password_uppercase_gte,
            password_numbers_gte=password_numbers_gte,
            password_punctuation_gte=password_punctuation_gte,
            password_symbols_gte=password_symbols_gte,
            password_separators_gte=password_separators_gte,
            password_other_gte=password_other_gte,
            password_entropy_gte=password_entropy_gte,
            password_plain=password_plain,
            accessed_url=accessed_url,
            detected_malware=detected_malware,
            data_leak_post=data_leak_post,
            data_leak_posts_by_thread_uid=data_leak_posts_by_thread_uid,
            data_leak_blog=data_leak_blog,
            var_from=var_from,
            until=until,
            last_updated_from=last_updated_from,
            last_updated_until=last_updated_until,
            sort=sort,
            filter_by_gir_set=filter_by_gir_set,
            offset=offset,
            count=count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SearchSchema",
            '412': "CredentialSetsGet412Response",
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
    def search_get_with_http_info(
        self,
        text: Annotated[Optional[StrictStr], Field(description="Search text everywhere.")] = None,
        ip_address: Annotated[Optional[StrictStr], Field(description="IP address search.")] = None,
        url: Annotated[Optional[StrictStr], Field(description="URL search.")] = None,
        contact_info_email: Annotated[Optional[StrictStr], Field(description="E-mail address search.")] = None,
        post: Annotated[Optional[StrictStr], Field(description="Forum post search (including images via OCR).")] = None,
        private_message: Annotated[Optional[StrictStr], Field(description="Forum private message search.")] = None,
        private_message_subject: Annotated[Optional[StrictStr], Field(description="Search text in subjects of Private Messages.")] = None,
        actor: Annotated[Optional[StrictStr], Field(description="Actor search.")] = None,
        entity: Annotated[Optional[StrictStr], Field(description="Entity search.")] = None,
        entity_type: Annotated[Optional[StrictStr], Field(description="Search by entity type.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Purported victim search.")] = None,
        forum: Annotated[Optional[StrictStr], Field(description="Search posts in specific forum.")] = None,
        ioc: Annotated[Optional[StrictStr], Field(description="Indicators of compromise search.")] = None,
        ioc_type: Annotated[Optional[StrictStr], Field(description="Search by IOC type.")] = None,
        report: Annotated[Optional[StrictStr], Field(description="Report search.")] = None,
        report_tag: Annotated[Optional[StrictStr], Field(description="Search reports by tag.")] = None,
        report_location: Annotated[Optional[StrictStr], Field(description="Search reports by location.")] = None,
        report_admiralty_code: Annotated[Optional[StrictStr], Field(description="Search reports by admiralty code.")] = None,
        report_title: Annotated[Optional[StrictStr], Field(description="Report title search.")] = None,
        document_type: Annotated[Optional[StrictStr], Field(description="Search reports by document type.")] = None,
        document_family: Annotated[Optional[StrictStr], Field(description="Search reports by document family.")] = None,
        event: Annotated[Optional[StrictStr], Field(description="Free text event search.")] = None,
        indicator: Annotated[Optional[StrictStr], Field(description="Free text indicator search.")] = None,
        yara: Annotated[Optional[StrictStr], Field(description="Free text YARAs search.")] = None,
        nids: Annotated[Optional[StrictStr], Field(description="Free text NIDS search.")] = None,
        malware_report: Annotated[Optional[StrictStr], Field(description="Free text malware reports search.")] = None,
        spot_report: Annotated[Optional[StrictStr], Field(description="Free text spot reports search.")] = None,
        breach_alert: Annotated[Optional[StrictStr], Field(description="Free text breach alerts search.")] = None,
        situation_report: Annotated[Optional[StrictStr], Field(description="Free text situation reports search.")] = None,
        event_type: Annotated[Optional[StrictStr], Field(description="Search events by type.")] = None,
        indicator_type: Annotated[Optional[StrictStr], Field(description="Search indicators by type.")] = None,
        nids_type: Annotated[Optional[StrictStr], Field(description="Search NIDS by type.")] = None,
        threat_type: Annotated[Optional[StrictStr], Field(description="Search events, indicators, YARAs and malware reports by threat type.")] = None,
        threat_uid: Annotated[Optional[StrictStr], Field(description="Search events, indicators, YARAs and malware reports by threat uid.")] = None,
        malware_family: Annotated[Optional[StrictStr], Field(description="Search events, indicators, YARAs and malware reports by malware family")] = None,
        malware_family_profile_uid: Annotated[Optional[StrictStr], Field(description="Search events, indicators, YARAs and malware reports by malware family profile UID")] = None,
        confidence: Annotated[Optional[StrictStr], Field(description="Search indicators, YARAs, breach alerts and NIDS by confidence")] = None,
        cve_report: Annotated[Optional[StrictStr], Field(description="Free text CVE reports search.")] = None,
        cve_type: Annotated[Optional[StrictStr], Field(description="Search CVE reports by type.")] = None,
        cve_status: Annotated[Optional[StrictStr], Field(description="Search CVE reports by status.")] = None,
        cve_name: Annotated[Optional[StrictStr], Field(description="Search CVE reports by name.")] = None,
        risk_level: Annotated[Optional[StrictStr], Field(description="Search CVE reports by risk level.")] = None,
        patch_status: Annotated[Optional[StrictStr], Field(description="Search CVE reports by patch status.")] = None,
        vendor_name: Annotated[Optional[StrictStr], Field(description="Search CVE reports by vendor name.")] = None,
        product_name: Annotated[Optional[StrictStr], Field(description="Search CVE reports by product name.")] = None,
        instant_message: Annotated[Optional[StrictStr], Field(description="Free text instant messages search (including images via OCR).")] = None,
        instant_message_actor: Annotated[Optional[StrictStr], Field(description="Search instant messages by author handle (actual for the moment message was written).")] = None,
        instant_message_service: Annotated[Optional[StrictStr], Field(description="Search instant messages by service name.")] = None,
        instant_message_server: Annotated[Optional[StrictStr], Field(description="Search instant messages by server name.")] = None,
        instant_message_channel: Annotated[Optional[StrictStr], Field(description="Search instant messages by channel name.")] = None,
        news: Annotated[Optional[StrictStr], Field(description="Free text news search")] = None,
        news_type: Annotated[Optional[StrictStr], Field(description="Search news by type.")] = None,
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        credential_uid: Annotated[Optional[StrictStr], Field(description="Search by credential uid.")] = None,
        credential_set_name: Annotated[Optional[StrictStr], Field(description="Search by credential set name.")] = None,
        credential_set_uid: Annotated[Optional[StrictStr], Field(description="Search by credential set uid.")] = None,
        credential_occurrence_uid: Annotated[Optional[StrictStr], Field(description="Search by credential occurrence uid.")] = None,
        domain: Annotated[Optional[StrictStr], Field(description="Search by credential domain (detection domain).")] = None,
        credential_login: Annotated[Optional[StrictStr], Field(description="Search by credential login.")] = None,
        affiliation_group: Annotated[Optional[StrictStr], Field(description="Search by credential affiliation group.")] = None,
        password_strength: Annotated[Optional[StrictStr], Field(description="Search by password strength.")] = None,
        password_length_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity length field as greater then or equal to input value.")] = None,
        password_lowercase_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity lowercase filed as greater then or equal to input value.")] = None,
        password_uppercase_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity uppercase filed as greater then or equal to input value.")] = None,
        password_numbers_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity numbers filed as greater then or equal to input value.")] = None,
        password_punctuation_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity punctuation filed as greater then or equal to input value.")] = None,
        password_symbols_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity symbols filed as greater then or equal to input value.")] = None,
        password_separators_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity separators filed as greater then or equal to input value.")] = None,
        password_other_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity other filed as greater then or equal to input value.")] = None,
        password_entropy_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity entropy filed as greater then or equal to input value.")] = None,
        password_plain: Annotated[Optional[StrictStr], Field(description="Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded.")] = None,
        accessed_url: Annotated[Optional[StrictStr], Field(description="Search by accessed url.")] = None,
        detected_malware: Annotated[Optional[StrictStr], Field(description="Search by credential detected malware.")] = None,
        data_leak_post: Annotated[Optional[StrictStr], Field(description="Search text in data leak posts and topics (including images via OCR).")] = None,
        data_leak_posts_by_thread_uid: Annotated[Optional[StrictStr], Field(description="Search data leak posts by thread uid.")] = None,
        data_leak_blog: Annotated[Optional[StrictStr], Field(description="Search data leak posts in a given data leak blog.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order.")] = None,
        filter_by_gir_set: Annotated[Optional[StrictStr], Field(description="Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required")] = None,
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
    ) -> ApiResponse[SearchSchema]:
        """Search - Global Search

        Returns selection of results matching filter criteria. Can include the following entities:   - [Information Reports](#tag/Reports/paths/~1reports/get)   - [Fintel Reports](#tag/Reports/paths/~1reports/get)   - [Actors](#tag/Actors/paths/~1actors/get)   - [Entities](#tag/Entities/paths/~1entities/get)   - [Indicators of Compromise](#tag/Indicators/paths/~1indicators/get)   - [Posts](#tag/Forums/paths/~1posts/get)   - [PrivateMessages](#tag/Forums/paths/~1privateMessages/get)   - [Events](#tag/Events/paths/~1events/get)   - [Indicators](#tag/Indicators/paths/~1indicators/get)   - [YARA](#tag/YARA/paths/~1yara/get)   - [Malware Reports](#tag/Malware/paths/~1malwareReports/get)   - [Breach Alerts](#tag/Reports/paths/~1breachAlerts/get)   - [Spot Reports](#tag/Reports/paths/~1spotReports/get)   - [Situation Reports](#tag/Global-Search/paths/~1search/get)   - [Cve Reports](#tag/Vulnerabilities/paths/~1cve~1reports/get)   - [Instant Messages](#tag/Messaging-Services/paths/~1messagingServices~1instantMessages/get)   - [News](#tag/News/paths/~1news/get)   - [Credential Sets](#tag/Credentials/paths/~1credentialSets/get)   - [Credentials](#tag/Credentials/paths/~1credentials/get)   - [Credential Occurrences](#tag/Credentials/paths/~1credentials~1occurrences/get)   - [Data Leak Blogs](#tag/Data-Leak-Blogs/paths/~1dataleak~1posts/get) 

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
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
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

        _param = self._search_get_serialize(
            text=text,
            ip_address=ip_address,
            url=url,
            contact_info_email=contact_info_email,
            post=post,
            private_message=private_message,
            private_message_subject=private_message_subject,
            actor=actor,
            entity=entity,
            entity_type=entity_type,
            victim=victim,
            forum=forum,
            ioc=ioc,
            ioc_type=ioc_type,
            report=report,
            report_tag=report_tag,
            report_location=report_location,
            report_admiralty_code=report_admiralty_code,
            report_title=report_title,
            document_type=document_type,
            document_family=document_family,
            event=event,
            indicator=indicator,
            yara=yara,
            nids=nids,
            malware_report=malware_report,
            spot_report=spot_report,
            breach_alert=breach_alert,
            situation_report=situation_report,
            event_type=event_type,
            indicator_type=indicator_type,
            nids_type=nids_type,
            threat_type=threat_type,
            threat_uid=threat_uid,
            malware_family=malware_family,
            malware_family_profile_uid=malware_family_profile_uid,
            confidence=confidence,
            cve_report=cve_report,
            cve_type=cve_type,
            cve_status=cve_status,
            cve_name=cve_name,
            risk_level=risk_level,
            patch_status=patch_status,
            vendor_name=vendor_name,
            product_name=product_name,
            instant_message=instant_message,
            instant_message_actor=instant_message_actor,
            instant_message_service=instant_message_service,
            instant_message_server=instant_message_server,
            instant_message_channel=instant_message_channel,
            news=news,
            news_type=news_type,
            gir=gir,
            credential_uid=credential_uid,
            credential_set_name=credential_set_name,
            credential_set_uid=credential_set_uid,
            credential_occurrence_uid=credential_occurrence_uid,
            domain=domain,
            credential_login=credential_login,
            affiliation_group=affiliation_group,
            password_strength=password_strength,
            password_length_gte=password_length_gte,
            password_lowercase_gte=password_lowercase_gte,
            password_uppercase_gte=password_uppercase_gte,
            password_numbers_gte=password_numbers_gte,
            password_punctuation_gte=password_punctuation_gte,
            password_symbols_gte=password_symbols_gte,
            password_separators_gte=password_separators_gte,
            password_other_gte=password_other_gte,
            password_entropy_gte=password_entropy_gte,
            password_plain=password_plain,
            accessed_url=accessed_url,
            detected_malware=detected_malware,
            data_leak_post=data_leak_post,
            data_leak_posts_by_thread_uid=data_leak_posts_by_thread_uid,
            data_leak_blog=data_leak_blog,
            var_from=var_from,
            until=until,
            last_updated_from=last_updated_from,
            last_updated_until=last_updated_until,
            sort=sort,
            filter_by_gir_set=filter_by_gir_set,
            offset=offset,
            count=count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SearchSchema",
            '412': "CredentialSetsGet412Response",
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
    def search_get_without_preload_content(
        self,
        text: Annotated[Optional[StrictStr], Field(description="Search text everywhere.")] = None,
        ip_address: Annotated[Optional[StrictStr], Field(description="IP address search.")] = None,
        url: Annotated[Optional[StrictStr], Field(description="URL search.")] = None,
        contact_info_email: Annotated[Optional[StrictStr], Field(description="E-mail address search.")] = None,
        post: Annotated[Optional[StrictStr], Field(description="Forum post search (including images via OCR).")] = None,
        private_message: Annotated[Optional[StrictStr], Field(description="Forum private message search.")] = None,
        private_message_subject: Annotated[Optional[StrictStr], Field(description="Search text in subjects of Private Messages.")] = None,
        actor: Annotated[Optional[StrictStr], Field(description="Actor search.")] = None,
        entity: Annotated[Optional[StrictStr], Field(description="Entity search.")] = None,
        entity_type: Annotated[Optional[StrictStr], Field(description="Search by entity type.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Purported victim search.")] = None,
        forum: Annotated[Optional[StrictStr], Field(description="Search posts in specific forum.")] = None,
        ioc: Annotated[Optional[StrictStr], Field(description="Indicators of compromise search.")] = None,
        ioc_type: Annotated[Optional[StrictStr], Field(description="Search by IOC type.")] = None,
        report: Annotated[Optional[StrictStr], Field(description="Report search.")] = None,
        report_tag: Annotated[Optional[StrictStr], Field(description="Search reports by tag.")] = None,
        report_location: Annotated[Optional[StrictStr], Field(description="Search reports by location.")] = None,
        report_admiralty_code: Annotated[Optional[StrictStr], Field(description="Search reports by admiralty code.")] = None,
        report_title: Annotated[Optional[StrictStr], Field(description="Report title search.")] = None,
        document_type: Annotated[Optional[StrictStr], Field(description="Search reports by document type.")] = None,
        document_family: Annotated[Optional[StrictStr], Field(description="Search reports by document family.")] = None,
        event: Annotated[Optional[StrictStr], Field(description="Free text event search.")] = None,
        indicator: Annotated[Optional[StrictStr], Field(description="Free text indicator search.")] = None,
        yara: Annotated[Optional[StrictStr], Field(description="Free text YARAs search.")] = None,
        nids: Annotated[Optional[StrictStr], Field(description="Free text NIDS search.")] = None,
        malware_report: Annotated[Optional[StrictStr], Field(description="Free text malware reports search.")] = None,
        spot_report: Annotated[Optional[StrictStr], Field(description="Free text spot reports search.")] = None,
        breach_alert: Annotated[Optional[StrictStr], Field(description="Free text breach alerts search.")] = None,
        situation_report: Annotated[Optional[StrictStr], Field(description="Free text situation reports search.")] = None,
        event_type: Annotated[Optional[StrictStr], Field(description="Search events by type.")] = None,
        indicator_type: Annotated[Optional[StrictStr], Field(description="Search indicators by type.")] = None,
        nids_type: Annotated[Optional[StrictStr], Field(description="Search NIDS by type.")] = None,
        threat_type: Annotated[Optional[StrictStr], Field(description="Search events, indicators, YARAs and malware reports by threat type.")] = None,
        threat_uid: Annotated[Optional[StrictStr], Field(description="Search events, indicators, YARAs and malware reports by threat uid.")] = None,
        malware_family: Annotated[Optional[StrictStr], Field(description="Search events, indicators, YARAs and malware reports by malware family")] = None,
        malware_family_profile_uid: Annotated[Optional[StrictStr], Field(description="Search events, indicators, YARAs and malware reports by malware family profile UID")] = None,
        confidence: Annotated[Optional[StrictStr], Field(description="Search indicators, YARAs, breach alerts and NIDS by confidence")] = None,
        cve_report: Annotated[Optional[StrictStr], Field(description="Free text CVE reports search.")] = None,
        cve_type: Annotated[Optional[StrictStr], Field(description="Search CVE reports by type.")] = None,
        cve_status: Annotated[Optional[StrictStr], Field(description="Search CVE reports by status.")] = None,
        cve_name: Annotated[Optional[StrictStr], Field(description="Search CVE reports by name.")] = None,
        risk_level: Annotated[Optional[StrictStr], Field(description="Search CVE reports by risk level.")] = None,
        patch_status: Annotated[Optional[StrictStr], Field(description="Search CVE reports by patch status.")] = None,
        vendor_name: Annotated[Optional[StrictStr], Field(description="Search CVE reports by vendor name.")] = None,
        product_name: Annotated[Optional[StrictStr], Field(description="Search CVE reports by product name.")] = None,
        instant_message: Annotated[Optional[StrictStr], Field(description="Free text instant messages search (including images via OCR).")] = None,
        instant_message_actor: Annotated[Optional[StrictStr], Field(description="Search instant messages by author handle (actual for the moment message was written).")] = None,
        instant_message_service: Annotated[Optional[StrictStr], Field(description="Search instant messages by service name.")] = None,
        instant_message_server: Annotated[Optional[StrictStr], Field(description="Search instant messages by server name.")] = None,
        instant_message_channel: Annotated[Optional[StrictStr], Field(description="Search instant messages by channel name.")] = None,
        news: Annotated[Optional[StrictStr], Field(description="Free text news search")] = None,
        news_type: Annotated[Optional[StrictStr], Field(description="Search news by type.")] = None,
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        credential_uid: Annotated[Optional[StrictStr], Field(description="Search by credential uid.")] = None,
        credential_set_name: Annotated[Optional[StrictStr], Field(description="Search by credential set name.")] = None,
        credential_set_uid: Annotated[Optional[StrictStr], Field(description="Search by credential set uid.")] = None,
        credential_occurrence_uid: Annotated[Optional[StrictStr], Field(description="Search by credential occurrence uid.")] = None,
        domain: Annotated[Optional[StrictStr], Field(description="Search by credential domain (detection domain).")] = None,
        credential_login: Annotated[Optional[StrictStr], Field(description="Search by credential login.")] = None,
        affiliation_group: Annotated[Optional[StrictStr], Field(description="Search by credential affiliation group.")] = None,
        password_strength: Annotated[Optional[StrictStr], Field(description="Search by password strength.")] = None,
        password_length_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity length field as greater then or equal to input value.")] = None,
        password_lowercase_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity lowercase filed as greater then or equal to input value.")] = None,
        password_uppercase_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity uppercase filed as greater then or equal to input value.")] = None,
        password_numbers_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity numbers filed as greater then or equal to input value.")] = None,
        password_punctuation_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity punctuation filed as greater then or equal to input value.")] = None,
        password_symbols_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity symbols filed as greater then or equal to input value.")] = None,
        password_separators_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity separators filed as greater then or equal to input value.")] = None,
        password_other_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity other filed as greater then or equal to input value.")] = None,
        password_entropy_gte: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Search by password complexity entropy filed as greater then or equal to input value.")] = None,
        password_plain: Annotated[Optional[StrictStr], Field(description="Search by credential plain password. Note: the value of 'passwordPlain' parameter must be URL-encoded.")] = None,
        accessed_url: Annotated[Optional[StrictStr], Field(description="Search by accessed url.")] = None,
        detected_malware: Annotated[Optional[StrictStr], Field(description="Search by credential detected malware.")] = None,
        data_leak_post: Annotated[Optional[StrictStr], Field(description="Search text in data leak posts and topics (including images via OCR).")] = None,
        data_leak_posts_by_thread_uid: Annotated[Optional[StrictStr], Field(description="Search data leak posts by thread uid.")] = None,
        data_leak_blog: Annotated[Optional[StrictStr], Field(description="Search data leak posts in a given data leak blog.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by relevance or by the object's native time in descending (latest) or ascending (earliest) order.")] = None,
        filter_by_gir_set: Annotated[Optional[StrictStr], Field(description="Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required")] = None,
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
        """Search - Global Search

        Returns selection of results matching filter criteria. Can include the following entities:   - [Information Reports](#tag/Reports/paths/~1reports/get)   - [Fintel Reports](#tag/Reports/paths/~1reports/get)   - [Actors](#tag/Actors/paths/~1actors/get)   - [Entities](#tag/Entities/paths/~1entities/get)   - [Indicators of Compromise](#tag/Indicators/paths/~1indicators/get)   - [Posts](#tag/Forums/paths/~1posts/get)   - [PrivateMessages](#tag/Forums/paths/~1privateMessages/get)   - [Events](#tag/Events/paths/~1events/get)   - [Indicators](#tag/Indicators/paths/~1indicators/get)   - [YARA](#tag/YARA/paths/~1yara/get)   - [Malware Reports](#tag/Malware/paths/~1malwareReports/get)   - [Breach Alerts](#tag/Reports/paths/~1breachAlerts/get)   - [Spot Reports](#tag/Reports/paths/~1spotReports/get)   - [Situation Reports](#tag/Global-Search/paths/~1search/get)   - [Cve Reports](#tag/Vulnerabilities/paths/~1cve~1reports/get)   - [Instant Messages](#tag/Messaging-Services/paths/~1messagingServices~1instantMessages/get)   - [News](#tag/News/paths/~1news/get)   - [Credential Sets](#tag/Credentials/paths/~1credentialSets/get)   - [Credentials](#tag/Credentials/paths/~1credentials/get)   - [Credential Occurrences](#tag/Credentials/paths/~1credentials~1occurrences/get)   - [Data Leak Blogs](#tag/Data-Leak-Blogs/paths/~1dataleak~1posts/get) 

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
        :param filter_by_gir_set: Filters results by user's GIRs (General intel requirements) or user's company PIRs (Prioritized intel requirements) if present. Dedicated user features are required
        :type filter_by_gir_set: str
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

        _param = self._search_get_serialize(
            text=text,
            ip_address=ip_address,
            url=url,
            contact_info_email=contact_info_email,
            post=post,
            private_message=private_message,
            private_message_subject=private_message_subject,
            actor=actor,
            entity=entity,
            entity_type=entity_type,
            victim=victim,
            forum=forum,
            ioc=ioc,
            ioc_type=ioc_type,
            report=report,
            report_tag=report_tag,
            report_location=report_location,
            report_admiralty_code=report_admiralty_code,
            report_title=report_title,
            document_type=document_type,
            document_family=document_family,
            event=event,
            indicator=indicator,
            yara=yara,
            nids=nids,
            malware_report=malware_report,
            spot_report=spot_report,
            breach_alert=breach_alert,
            situation_report=situation_report,
            event_type=event_type,
            indicator_type=indicator_type,
            nids_type=nids_type,
            threat_type=threat_type,
            threat_uid=threat_uid,
            malware_family=malware_family,
            malware_family_profile_uid=malware_family_profile_uid,
            confidence=confidence,
            cve_report=cve_report,
            cve_type=cve_type,
            cve_status=cve_status,
            cve_name=cve_name,
            risk_level=risk_level,
            patch_status=patch_status,
            vendor_name=vendor_name,
            product_name=product_name,
            instant_message=instant_message,
            instant_message_actor=instant_message_actor,
            instant_message_service=instant_message_service,
            instant_message_server=instant_message_server,
            instant_message_channel=instant_message_channel,
            news=news,
            news_type=news_type,
            gir=gir,
            credential_uid=credential_uid,
            credential_set_name=credential_set_name,
            credential_set_uid=credential_set_uid,
            credential_occurrence_uid=credential_occurrence_uid,
            domain=domain,
            credential_login=credential_login,
            affiliation_group=affiliation_group,
            password_strength=password_strength,
            password_length_gte=password_length_gte,
            password_lowercase_gte=password_lowercase_gte,
            password_uppercase_gte=password_uppercase_gte,
            password_numbers_gte=password_numbers_gte,
            password_punctuation_gte=password_punctuation_gte,
            password_symbols_gte=password_symbols_gte,
            password_separators_gte=password_separators_gte,
            password_other_gte=password_other_gte,
            password_entropy_gte=password_entropy_gte,
            password_plain=password_plain,
            accessed_url=accessed_url,
            detected_malware=detected_malware,
            data_leak_post=data_leak_post,
            data_leak_posts_by_thread_uid=data_leak_posts_by_thread_uid,
            data_leak_blog=data_leak_blog,
            var_from=var_from,
            until=until,
            last_updated_from=last_updated_from,
            last_updated_until=last_updated_until,
            sort=sort,
            filter_by_gir_set=filter_by_gir_set,
            offset=offset,
            count=count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SearchSchema",
            '412': "CredentialSetsGet412Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _search_get_serialize(
        self,
        text,
        ip_address,
        url,
        contact_info_email,
        post,
        private_message,
        private_message_subject,
        actor,
        entity,
        entity_type,
        victim,
        forum,
        ioc,
        ioc_type,
        report,
        report_tag,
        report_location,
        report_admiralty_code,
        report_title,
        document_type,
        document_family,
        event,
        indicator,
        yara,
        nids,
        malware_report,
        spot_report,
        breach_alert,
        situation_report,
        event_type,
        indicator_type,
        nids_type,
        threat_type,
        threat_uid,
        malware_family,
        malware_family_profile_uid,
        confidence,
        cve_report,
        cve_type,
        cve_status,
        cve_name,
        risk_level,
        patch_status,
        vendor_name,
        product_name,
        instant_message,
        instant_message_actor,
        instant_message_service,
        instant_message_server,
        instant_message_channel,
        news,
        news_type,
        gir,
        credential_uid,
        credential_set_name,
        credential_set_uid,
        credential_occurrence_uid,
        domain,
        credential_login,
        affiliation_group,
        password_strength,
        password_length_gte,
        password_lowercase_gte,
        password_uppercase_gte,
        password_numbers_gte,
        password_punctuation_gte,
        password_symbols_gte,
        password_separators_gte,
        password_other_gte,
        password_entropy_gte,
        password_plain,
        accessed_url,
        detected_malware,
        data_leak_post,
        data_leak_posts_by_thread_uid,
        data_leak_blog,
        var_from,
        until,
        last_updated_from,
        last_updated_until,
        sort,
        filter_by_gir_set,
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
        if text is not None:
            
            _query_params.append(('text', text))
            
        if ip_address is not None:
            
            _query_params.append(('ipAddress', ip_address))
            
        if url is not None:
            
            _query_params.append(('url', url))
            
        if contact_info_email is not None:
            
            _query_params.append(('contactInfoEmail', contact_info_email))
            
        if post is not None:
            
            _query_params.append(('post', post))
            
        if private_message is not None:
            
            _query_params.append(('privateMessage', private_message))
            
        if private_message_subject is not None:
            
            _query_params.append(('privateMessageSubject', private_message_subject))
            
        if actor is not None:
            
            _query_params.append(('actor', actor))
            
        if entity is not None:
            
            _query_params.append(('entity', entity))
            
        if entity_type is not None:
            
            _query_params.append(('entityType', entity_type))
            
        if victim is not None:
            
            _query_params.append(('victim', victim))
            
        if forum is not None:
            
            _query_params.append(('forum', forum))
            
        if ioc is not None:
            
            _query_params.append(('ioc', ioc))
            
        if ioc_type is not None:
            
            _query_params.append(('iocType', ioc_type))
            
        if report is not None:
            
            _query_params.append(('report', report))
            
        if report_tag is not None:
            
            _query_params.append(('reportTag', report_tag))
            
        if report_location is not None:
            
            _query_params.append(('reportLocation', report_location))
            
        if report_admiralty_code is not None:
            
            _query_params.append(('reportAdmiraltyCode', report_admiralty_code))
            
        if report_title is not None:
            
            _query_params.append(('reportTitle', report_title))
            
        if document_type is not None:
            
            _query_params.append(('documentType', document_type))
            
        if document_family is not None:
            
            _query_params.append(('documentFamily', document_family))
            
        if event is not None:
            
            _query_params.append(('event', event))
            
        if indicator is not None:
            
            _query_params.append(('indicator', indicator))
            
        if yara is not None:
            
            _query_params.append(('yara', yara))
            
        if nids is not None:
            
            _query_params.append(('nids', nids))
            
        if malware_report is not None:
            
            _query_params.append(('malwareReport', malware_report))
            
        if spot_report is not None:
            
            _query_params.append(('spotReport', spot_report))
            
        if breach_alert is not None:
            
            _query_params.append(('breachAlert', breach_alert))
            
        if situation_report is not None:
            
            _query_params.append(('situationReport', situation_report))
            
        if event_type is not None:
            
            _query_params.append(('eventType', event_type))
            
        if indicator_type is not None:
            
            _query_params.append(('indicatorType', indicator_type))
            
        if nids_type is not None:
            
            _query_params.append(('nidsType', nids_type))
            
        if threat_type is not None:
            
            _query_params.append(('threatType', threat_type))
            
        if threat_uid is not None:
            
            _query_params.append(('threatUid', threat_uid))
            
        if malware_family is not None:
            
            _query_params.append(('malwareFamily', malware_family))
            
        if malware_family_profile_uid is not None:
            
            _query_params.append(('malwareFamilyProfileUid', malware_family_profile_uid))
            
        if confidence is not None:
            
            _query_params.append(('confidence', confidence))
            
        if cve_report is not None:
            
            _query_params.append(('cveReport', cve_report))
            
        if cve_type is not None:
            
            _query_params.append(('cveType', cve_type))
            
        if cve_status is not None:
            
            _query_params.append(('cveStatus', cve_status))
            
        if cve_name is not None:
            
            _query_params.append(('cveName', cve_name))
            
        if risk_level is not None:
            
            _query_params.append(('riskLevel', risk_level))
            
        if patch_status is not None:
            
            _query_params.append(('patchStatus', patch_status))
            
        if vendor_name is not None:
            
            _query_params.append(('vendorName', vendor_name))
            
        if product_name is not None:
            
            _query_params.append(('productName', product_name))
            
        if instant_message is not None:
            
            _query_params.append(('instantMessage', instant_message))
            
        if instant_message_actor is not None:
            
            _query_params.append(('instantMessageActor', instant_message_actor))
            
        if instant_message_service is not None:
            
            _query_params.append(('instantMessageService', instant_message_service))
            
        if instant_message_server is not None:
            
            _query_params.append(('instantMessageServer', instant_message_server))
            
        if instant_message_channel is not None:
            
            _query_params.append(('instantMessageChannel', instant_message_channel))
            
        if news is not None:
            
            _query_params.append(('news', news))
            
        if news_type is not None:
            
            _query_params.append(('newsType', news_type))
            
        if gir is not None:
            
            _query_params.append(('gir', gir))
            
        if credential_uid is not None:
            
            _query_params.append(('credentialUid', credential_uid))
            
        if credential_set_name is not None:
            
            _query_params.append(('credentialSetName', credential_set_name))
            
        if credential_set_uid is not None:
            
            _query_params.append(('credentialSetUid', credential_set_uid))
            
        if credential_occurrence_uid is not None:
            
            _query_params.append(('credentialOccurrenceUid', credential_occurrence_uid))
            
        if domain is not None:
            
            _query_params.append(('domain', domain))
            
        if credential_login is not None:
            
            _query_params.append(('credentialLogin', credential_login))
            
        if affiliation_group is not None:
            
            _query_params.append(('affiliationGroup', affiliation_group))
            
        if password_strength is not None:
            
            _query_params.append(('passwordStrength', password_strength))
            
        if password_length_gte is not None:
            
            _query_params.append(('passwordLengthGte', password_length_gte))
            
        if password_lowercase_gte is not None:
            
            _query_params.append(('passwordLowercaseGte', password_lowercase_gte))
            
        if password_uppercase_gte is not None:
            
            _query_params.append(('passwordUppercaseGte', password_uppercase_gte))
            
        if password_numbers_gte is not None:
            
            _query_params.append(('passwordNumbersGte', password_numbers_gte))
            
        if password_punctuation_gte is not None:
            
            _query_params.append(('passwordPunctuationGte', password_punctuation_gte))
            
        if password_symbols_gte is not None:
            
            _query_params.append(('passwordSymbolsGte', password_symbols_gte))
            
        if password_separators_gte is not None:
            
            _query_params.append(('passwordSeparatorsGte', password_separators_gte))
            
        if password_other_gte is not None:
            
            _query_params.append(('passwordOtherGte', password_other_gte))
            
        if password_entropy_gte is not None:
            
            _query_params.append(('passwordEntropyGte', password_entropy_gte))
            
        if password_plain is not None:
            
            _query_params.append(('passwordPlain', password_plain))
            
        if accessed_url is not None:
            
            _query_params.append(('accessedUrl', accessed_url))
            
        if detected_malware is not None:
            
            _query_params.append(('detectedMalware', detected_malware))
            
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
            
        if filter_by_gir_set is not None:
            
            _query_params.append(('filterByGirSet', filter_by_gir_set))
            
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
            resource_path='/search',
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


