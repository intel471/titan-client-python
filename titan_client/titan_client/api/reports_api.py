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
from titan_client.models.full_report_schema import FullReportSchema
from titan_client.models.full_spot_report_schema import FullSpotReportSchema
from titan_client.models.malware_reports_search_response import MalwareReportsSearchResponse
from titan_client.models.malware_reports_search_schema import MalwareReportsSearchSchema
from titan_client.models.simple_breach_alert_response import SimpleBreachAlertResponse
from titan_client.models.simple_breach_alert_schema import SimpleBreachAlertSchema
from titan_client.models.simple_reports_response import SimpleReportsResponse
from titan_client.models.simple_spot_reports_response import SimpleSpotReportsResponse
from titan_client.models.situation_report_response import SituationReportResponse
from titan_client.models.situation_report_schema import SituationReportSchema

from titan_client.api_client import ApiClient, RequestSerialized
from titan_client.api_response import ApiResponse
from titan_client.rest import RESTResponseType


class ReportsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def breach_alerts_get(
        self,
        breach_alert: Annotated[Optional[StrictStr], Field(description="Free text reports search - all fields included. At least one of `breachAlert`, `actor`, `victim` is required.")] = None,
        actor: Annotated[Optional[StrictStr], Field(description="Search by actor or actor group names. At least one of `breachAlert`, `actor`, `victim` is required.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Search by victim. At least one of `breachAlert`, `actor`, `victim` is required.")] = None,
        confidence: Annotated[Optional[StrictStr], Field(description="Search by confidence level")] = None,
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by the object's native time in descending (latest) or ascending (earliest) order")] = None,
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
    ) -> SimpleBreachAlertResponse:
        """Search Breach Alerts

        Returns list of `Breach alerts` matching filter criteria.

        :param breach_alert: Free text reports search - all fields included. At least one of `breachAlert`, `actor`, `victim` is required.
        :type breach_alert: str
        :param actor: Search by actor or actor group names. At least one of `breachAlert`, `actor`, `victim` is required.
        :type actor: str
        :param victim: Search by victim. At least one of `breachAlert`, `actor`, `victim` is required.
        :type victim: str
        :param confidence: Search by confidence level
        :type confidence: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
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

        _param = self._breach_alerts_get_serialize(
            breach_alert=breach_alert,
            actor=actor,
            victim=victim,
            confidence=confidence,
            gir=gir,
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
            '200': "SimpleBreachAlertResponse",
            '412': "BreachAlertsGet412Response",
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
    def breach_alerts_get_with_http_info(
        self,
        breach_alert: Annotated[Optional[StrictStr], Field(description="Free text reports search - all fields included. At least one of `breachAlert`, `actor`, `victim` is required.")] = None,
        actor: Annotated[Optional[StrictStr], Field(description="Search by actor or actor group names. At least one of `breachAlert`, `actor`, `victim` is required.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Search by victim. At least one of `breachAlert`, `actor`, `victim` is required.")] = None,
        confidence: Annotated[Optional[StrictStr], Field(description="Search by confidence level")] = None,
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by the object's native time in descending (latest) or ascending (earliest) order")] = None,
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
    ) -> ApiResponse[SimpleBreachAlertResponse]:
        """Search Breach Alerts

        Returns list of `Breach alerts` matching filter criteria.

        :param breach_alert: Free text reports search - all fields included. At least one of `breachAlert`, `actor`, `victim` is required.
        :type breach_alert: str
        :param actor: Search by actor or actor group names. At least one of `breachAlert`, `actor`, `victim` is required.
        :type actor: str
        :param victim: Search by victim. At least one of `breachAlert`, `actor`, `victim` is required.
        :type victim: str
        :param confidence: Search by confidence level
        :type confidence: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
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

        _param = self._breach_alerts_get_serialize(
            breach_alert=breach_alert,
            actor=actor,
            victim=victim,
            confidence=confidence,
            gir=gir,
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
            '200': "SimpleBreachAlertResponse",
            '412': "BreachAlertsGet412Response",
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
    def breach_alerts_get_without_preload_content(
        self,
        breach_alert: Annotated[Optional[StrictStr], Field(description="Free text reports search - all fields included. At least one of `breachAlert`, `actor`, `victim` is required.")] = None,
        actor: Annotated[Optional[StrictStr], Field(description="Search by actor or actor group names. At least one of `breachAlert`, `actor`, `victim` is required.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Search by victim. At least one of `breachAlert`, `actor`, `victim` is required.")] = None,
        confidence: Annotated[Optional[StrictStr], Field(description="Search by confidence level")] = None,
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by the object's native time in descending (latest) or ascending (earliest) order")] = None,
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
        """Search Breach Alerts

        Returns list of `Breach alerts` matching filter criteria.

        :param breach_alert: Free text reports search - all fields included. At least one of `breachAlert`, `actor`, `victim` is required.
        :type breach_alert: str
        :param actor: Search by actor or actor group names. At least one of `breachAlert`, `actor`, `victim` is required.
        :type actor: str
        :param victim: Search by victim. At least one of `breachAlert`, `actor`, `victim` is required.
        :type victim: str
        :param confidence: Search by confidence level
        :type confidence: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
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

        _param = self._breach_alerts_get_serialize(
            breach_alert=breach_alert,
            actor=actor,
            victim=victim,
            confidence=confidence,
            gir=gir,
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
            '200': "SimpleBreachAlertResponse",
            '412': "BreachAlertsGet412Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _breach_alerts_get_serialize(
        self,
        breach_alert,
        actor,
        victim,
        confidence,
        gir,
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
        if breach_alert is not None:
            
            _query_params.append(('breachAlert', breach_alert))
            
        if actor is not None:
            
            _query_params.append(('actor', actor))
            
        if victim is not None:
            
            _query_params.append(('victim', victim))
            
        if confidence is not None:
            
            _query_params.append(('confidence', confidence))
            
        if gir is not None:
            
            _query_params.append(('gir', gir))
            
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
            resource_path='/breachAlerts',
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




    @validate_call
    def breach_alerts_uid_get(
        self,
        uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
    ) -> SimpleBreachAlertSchema:
        """Get Breach Alert

        Returns a `Breach alert` with specified id.

        :param uid: Report identifier. (required)
        :type uid: str
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

        _param = self._breach_alerts_uid_get_serialize(
            uid=uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SimpleBreachAlertSchema",
            '404': "str",
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
    def breach_alerts_uid_get_with_http_info(
        self,
        uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
    ) -> ApiResponse[SimpleBreachAlertSchema]:
        """Get Breach Alert

        Returns a `Breach alert` with specified id.

        :param uid: Report identifier. (required)
        :type uid: str
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

        _param = self._breach_alerts_uid_get_serialize(
            uid=uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SimpleBreachAlertSchema",
            '404': "str",
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
    def breach_alerts_uid_get_without_preload_content(
        self,
        uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
        """Get Breach Alert

        Returns a `Breach alert` with specified id.

        :param uid: Report identifier. (required)
        :type uid: str
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

        _param = self._breach_alerts_uid_get_serialize(
            uid=uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SimpleBreachAlertSchema",
            '404': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _breach_alerts_uid_get_serialize(
        self,
        uid,
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
        if uid is not None:
            _path_params['uid'] = uid
        # process the query parameters
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
            resource_path='/breachAlerts/{uid}',
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




    @validate_call
    def malware_reports_get(
        self,
        malware_report: Annotated[Optional[StrictStr], Field(description="Free text Malware reports search (all fields included). At least one of `malwareReport`, `threatType`, `reportTitle`, `malwareFamily`, 'malwareFamilyProfileUid` is required.")] = None,
        threat_type: Annotated[Optional[StrictStr], Field(description="Search Malware reports by threat type")] = None,
        report_title: Annotated[Optional[StrictStr], Field(description="Search Malware reports by threat UID")] = None,
        malware_family: Annotated[Optional[StrictStr], Field(description="Search Malware reports by malware family (e.g. `gozi_isfb`, `smokeloader`, `trickbot`).")] = None,
        malware_family_profile_uid: Annotated[Optional[StrictStr], Field(description="Search Malware reports by malware family profile UID. Useful for getting context for everything we have around specific malware family, for instance https://api.intel471.com/v1/search?malwareFamilyProfileUid=20eb1f82621001883ea0c2085aff5729.")] = None,
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by the object's native time in descending (latest) or ascending (earliest) order")] = None,
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
    ) -> MalwareReportsSearchResponse:
        """Search Malware Intelligence Reports

        Returns list of `Malware reports` matching filter criteria. Malware Intelligence is a different product from Intel 471 to adversary intelligence.

        :param malware_report: Free text Malware reports search (all fields included). At least one of `malwareReport`, `threatType`, `reportTitle`, `malwareFamily`, 'malwareFamilyProfileUid` is required.
        :type malware_report: str
        :param threat_type: Search Malware reports by threat type
        :type threat_type: str
        :param report_title: Search Malware reports by threat UID
        :type report_title: str
        :param malware_family: Search Malware reports by malware family (e.g. `gozi_isfb`, `smokeloader`, `trickbot`).
        :type malware_family: str
        :param malware_family_profile_uid: Search Malware reports by malware family profile UID. Useful for getting context for everything we have around specific malware family, for instance https://api.intel471.com/v1/search?malwareFamilyProfileUid=20eb1f82621001883ea0c2085aff5729.
        :type malware_family_profile_uid: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
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

        _param = self._malware_reports_get_serialize(
            malware_report=malware_report,
            threat_type=threat_type,
            report_title=report_title,
            malware_family=malware_family,
            malware_family_profile_uid=malware_family_profile_uid,
            gir=gir,
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
            '200': "MalwareReportsSearchResponse",
            '412': "BreachAlertsGet412Response",
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
    def malware_reports_get_with_http_info(
        self,
        malware_report: Annotated[Optional[StrictStr], Field(description="Free text Malware reports search (all fields included). At least one of `malwareReport`, `threatType`, `reportTitle`, `malwareFamily`, 'malwareFamilyProfileUid` is required.")] = None,
        threat_type: Annotated[Optional[StrictStr], Field(description="Search Malware reports by threat type")] = None,
        report_title: Annotated[Optional[StrictStr], Field(description="Search Malware reports by threat UID")] = None,
        malware_family: Annotated[Optional[StrictStr], Field(description="Search Malware reports by malware family (e.g. `gozi_isfb`, `smokeloader`, `trickbot`).")] = None,
        malware_family_profile_uid: Annotated[Optional[StrictStr], Field(description="Search Malware reports by malware family profile UID. Useful for getting context for everything we have around specific malware family, for instance https://api.intel471.com/v1/search?malwareFamilyProfileUid=20eb1f82621001883ea0c2085aff5729.")] = None,
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by the object's native time in descending (latest) or ascending (earliest) order")] = None,
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
    ) -> ApiResponse[MalwareReportsSearchResponse]:
        """Search Malware Intelligence Reports

        Returns list of `Malware reports` matching filter criteria. Malware Intelligence is a different product from Intel 471 to adversary intelligence.

        :param malware_report: Free text Malware reports search (all fields included). At least one of `malwareReport`, `threatType`, `reportTitle`, `malwareFamily`, 'malwareFamilyProfileUid` is required.
        :type malware_report: str
        :param threat_type: Search Malware reports by threat type
        :type threat_type: str
        :param report_title: Search Malware reports by threat UID
        :type report_title: str
        :param malware_family: Search Malware reports by malware family (e.g. `gozi_isfb`, `smokeloader`, `trickbot`).
        :type malware_family: str
        :param malware_family_profile_uid: Search Malware reports by malware family profile UID. Useful for getting context for everything we have around specific malware family, for instance https://api.intel471.com/v1/search?malwareFamilyProfileUid=20eb1f82621001883ea0c2085aff5729.
        :type malware_family_profile_uid: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
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

        _param = self._malware_reports_get_serialize(
            malware_report=malware_report,
            threat_type=threat_type,
            report_title=report_title,
            malware_family=malware_family,
            malware_family_profile_uid=malware_family_profile_uid,
            gir=gir,
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
            '200': "MalwareReportsSearchResponse",
            '412': "BreachAlertsGet412Response",
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
    def malware_reports_get_without_preload_content(
        self,
        malware_report: Annotated[Optional[StrictStr], Field(description="Free text Malware reports search (all fields included). At least one of `malwareReport`, `threatType`, `reportTitle`, `malwareFamily`, 'malwareFamilyProfileUid` is required.")] = None,
        threat_type: Annotated[Optional[StrictStr], Field(description="Search Malware reports by threat type")] = None,
        report_title: Annotated[Optional[StrictStr], Field(description="Search Malware reports by threat UID")] = None,
        malware_family: Annotated[Optional[StrictStr], Field(description="Search Malware reports by malware family (e.g. `gozi_isfb`, `smokeloader`, `trickbot`).")] = None,
        malware_family_profile_uid: Annotated[Optional[StrictStr], Field(description="Search Malware reports by malware family profile UID. Useful for getting context for everything we have around specific malware family, for instance https://api.intel471.com/v1/search?malwareFamilyProfileUid=20eb1f82621001883ea0c2085aff5729.")] = None,
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by the object's native time in descending (latest) or ascending (earliest) order")] = None,
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
        """Search Malware Intelligence Reports

        Returns list of `Malware reports` matching filter criteria. Malware Intelligence is a different product from Intel 471 to adversary intelligence.

        :param malware_report: Free text Malware reports search (all fields included). At least one of `malwareReport`, `threatType`, `reportTitle`, `malwareFamily`, 'malwareFamilyProfileUid` is required.
        :type malware_report: str
        :param threat_type: Search Malware reports by threat type
        :type threat_type: str
        :param report_title: Search Malware reports by threat UID
        :type report_title: str
        :param malware_family: Search Malware reports by malware family (e.g. `gozi_isfb`, `smokeloader`, `trickbot`).
        :type malware_family: str
        :param malware_family_profile_uid: Search Malware reports by malware family profile UID. Useful for getting context for everything we have around specific malware family, for instance https://api.intel471.com/v1/search?malwareFamilyProfileUid=20eb1f82621001883ea0c2085aff5729.
        :type malware_family_profile_uid: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
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

        _param = self._malware_reports_get_serialize(
            malware_report=malware_report,
            threat_type=threat_type,
            report_title=report_title,
            malware_family=malware_family,
            malware_family_profile_uid=malware_family_profile_uid,
            gir=gir,
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
            '200': "MalwareReportsSearchResponse",
            '412': "BreachAlertsGet412Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _malware_reports_get_serialize(
        self,
        malware_report,
        threat_type,
        report_title,
        malware_family,
        malware_family_profile_uid,
        gir,
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
        if malware_report is not None:
            
            _query_params.append(('malwareReport', malware_report))
            
        if threat_type is not None:
            
            _query_params.append(('threatType', threat_type))
            
        if report_title is not None:
            
            _query_params.append(('reportTitle', report_title))
            
        if malware_family is not None:
            
            _query_params.append(('malwareFamily', malware_family))
            
        if malware_family_profile_uid is not None:
            
            _query_params.append(('malwareFamilyProfileUid', malware_family_profile_uid))
            
        if gir is not None:
            
            _query_params.append(('gir', gir))
            
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
            resource_path='/malwareReports',
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




    @validate_call
    def malware_reports_uid_get(
        self,
        uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
    ) -> MalwareReportsSearchSchema:
        """Get Malware Intelligence Report

        Returns single Malware report with specified unique id.

        :param uid: Report identifier. (required)
        :type uid: str
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

        _param = self._malware_reports_uid_get_serialize(
            uid=uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MalwareReportsSearchSchema",
            '404': "str",
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
    def malware_reports_uid_get_with_http_info(
        self,
        uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
    ) -> ApiResponse[MalwareReportsSearchSchema]:
        """Get Malware Intelligence Report

        Returns single Malware report with specified unique id.

        :param uid: Report identifier. (required)
        :type uid: str
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

        _param = self._malware_reports_uid_get_serialize(
            uid=uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MalwareReportsSearchSchema",
            '404': "str",
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
    def malware_reports_uid_get_without_preload_content(
        self,
        uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
        """Get Malware Intelligence Report

        Returns single Malware report with specified unique id.

        :param uid: Report identifier. (required)
        :type uid: str
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

        _param = self._malware_reports_uid_get_serialize(
            uid=uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MalwareReportsSearchSchema",
            '404': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _malware_reports_uid_get_serialize(
        self,
        uid,
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
        if uid is not None:
            _path_params['uid'] = uid
        # process the query parameters
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
            resource_path='/malwareReports/{uid}',
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




    @validate_call
    def reports_get(
        self,
        report: Annotated[Optional[StrictStr], Field(description="Search text in reports, subjects, and entities.")] = None,
        report_location: Annotated[Optional[StrictStr], Field(description="Country or region.")] = None,
        report_tag: Annotated[Optional[StrictStr], Field(description="Tag.")] = None,
        report_admiralty_code: Annotated[Optional[StrictStr], Field(description="Search reports by admiralty code.")] = None,
        report_title: Annotated[Optional[StrictStr], Field(description="Search reports by title.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Search by purported victim.")] = None,
        document_type: Annotated[Optional[StrictStr], Field(description="Search reports by document type.")] = None,
        document_family: Annotated[Optional[StrictStr], Field(description="Search reports by document family.")] = None,
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
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
    ) -> SimpleReportsResponse:
        """Search Reports

        Returns list of [Information Reports or Fintel Reports](#tag/Reports/paths/~1reports~1{uid}/get) matching filter criteria ordered by creation date descending (the most recent are on the top). Filtering parameters combined with AND criteria and can be present multiple times in query string. In version 1.3.0 reports also include new field `actorSubjectOfReport` with actors, mentioned in report subject

        :param report: Search text in reports, subjects, and entities.
        :type report: str
        :param report_location: Country or region.
        :type report_location: str
        :param report_tag: Tag.
        :type report_tag: str
        :param report_admiralty_code: Search reports by admiralty code.
        :type report_admiralty_code: str
        :param report_title: Search reports by title.
        :type report_title: str
        :param victim: Search by purported victim.
        :type victim: str
        :param document_type: Search reports by document type.
        :type document_type: str
        :param document_family: Search reports by document family.
        :type document_family: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
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

        _param = self._reports_get_serialize(
            report=report,
            report_location=report_location,
            report_tag=report_tag,
            report_admiralty_code=report_admiralty_code,
            report_title=report_title,
            victim=victim,
            document_type=document_type,
            document_family=document_family,
            gir=gir,
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
            '200': "SimpleReportsResponse",
            '412': "ReportsGet412Response",
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
    def reports_get_with_http_info(
        self,
        report: Annotated[Optional[StrictStr], Field(description="Search text in reports, subjects, and entities.")] = None,
        report_location: Annotated[Optional[StrictStr], Field(description="Country or region.")] = None,
        report_tag: Annotated[Optional[StrictStr], Field(description="Tag.")] = None,
        report_admiralty_code: Annotated[Optional[StrictStr], Field(description="Search reports by admiralty code.")] = None,
        report_title: Annotated[Optional[StrictStr], Field(description="Search reports by title.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Search by purported victim.")] = None,
        document_type: Annotated[Optional[StrictStr], Field(description="Search reports by document type.")] = None,
        document_family: Annotated[Optional[StrictStr], Field(description="Search reports by document family.")] = None,
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
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
    ) -> ApiResponse[SimpleReportsResponse]:
        """Search Reports

        Returns list of [Information Reports or Fintel Reports](#tag/Reports/paths/~1reports~1{uid}/get) matching filter criteria ordered by creation date descending (the most recent are on the top). Filtering parameters combined with AND criteria and can be present multiple times in query string. In version 1.3.0 reports also include new field `actorSubjectOfReport` with actors, mentioned in report subject

        :param report: Search text in reports, subjects, and entities.
        :type report: str
        :param report_location: Country or region.
        :type report_location: str
        :param report_tag: Tag.
        :type report_tag: str
        :param report_admiralty_code: Search reports by admiralty code.
        :type report_admiralty_code: str
        :param report_title: Search reports by title.
        :type report_title: str
        :param victim: Search by purported victim.
        :type victim: str
        :param document_type: Search reports by document type.
        :type document_type: str
        :param document_family: Search reports by document family.
        :type document_family: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
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

        _param = self._reports_get_serialize(
            report=report,
            report_location=report_location,
            report_tag=report_tag,
            report_admiralty_code=report_admiralty_code,
            report_title=report_title,
            victim=victim,
            document_type=document_type,
            document_family=document_family,
            gir=gir,
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
            '200': "SimpleReportsResponse",
            '412': "ReportsGet412Response",
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
    def reports_get_without_preload_content(
        self,
        report: Annotated[Optional[StrictStr], Field(description="Search text in reports, subjects, and entities.")] = None,
        report_location: Annotated[Optional[StrictStr], Field(description="Country or region.")] = None,
        report_tag: Annotated[Optional[StrictStr], Field(description="Tag.")] = None,
        report_admiralty_code: Annotated[Optional[StrictStr], Field(description="Search reports by admiralty code.")] = None,
        report_title: Annotated[Optional[StrictStr], Field(description="Search reports by title.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Search by purported victim.")] = None,
        document_type: Annotated[Optional[StrictStr], Field(description="Search reports by document type.")] = None,
        document_family: Annotated[Optional[StrictStr], Field(description="Search reports by document family.")] = None,
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
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
        """Search Reports

        Returns list of [Information Reports or Fintel Reports](#tag/Reports/paths/~1reports~1{uid}/get) matching filter criteria ordered by creation date descending (the most recent are on the top). Filtering parameters combined with AND criteria and can be present multiple times in query string. In version 1.3.0 reports also include new field `actorSubjectOfReport` with actors, mentioned in report subject

        :param report: Search text in reports, subjects, and entities.
        :type report: str
        :param report_location: Country or region.
        :type report_location: str
        :param report_tag: Tag.
        :type report_tag: str
        :param report_admiralty_code: Search reports by admiralty code.
        :type report_admiralty_code: str
        :param report_title: Search reports by title.
        :type report_title: str
        :param victim: Search by purported victim.
        :type victim: str
        :param document_type: Search reports by document type.
        :type document_type: str
        :param document_family: Search reports by document family.
        :type document_family: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
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

        _param = self._reports_get_serialize(
            report=report,
            report_location=report_location,
            report_tag=report_tag,
            report_admiralty_code=report_admiralty_code,
            report_title=report_title,
            victim=victim,
            document_type=document_type,
            document_family=document_family,
            gir=gir,
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
            '200': "SimpleReportsResponse",
            '412': "ReportsGet412Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _reports_get_serialize(
        self,
        report,
        report_location,
        report_tag,
        report_admiralty_code,
        report_title,
        victim,
        document_type,
        document_family,
        gir,
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
        if report is not None:
            
            _query_params.append(('report', report))
            
        if report_location is not None:
            
            _query_params.append(('reportLocation', report_location))
            
        if report_tag is not None:
            
            _query_params.append(('reportTag', report_tag))
            
        if report_admiralty_code is not None:
            
            _query_params.append(('reportAdmiraltyCode', report_admiralty_code))
            
        if report_title is not None:
            
            _query_params.append(('reportTitle', report_title))
            
        if victim is not None:
            
            _query_params.append(('victim', victim))
            
        if document_type is not None:
            
            _query_params.append(('documentType', document_type))
            
        if document_family is not None:
            
            _query_params.append(('documentFamily', document_family))
            
        if gir is not None:
            
            _query_params.append(('gir', gir))
            
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
            resource_path='/reports',
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




    @validate_call
    def reports_uid_get(
        self,
        uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
    ) -> FullReportSchema:
        """Get Report

        Returns a single *Information Report* or *Fintel Report* object.

        :param uid: Report identifier. (required)
        :type uid: str
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

        _param = self._reports_uid_get_serialize(
            uid=uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FullReportSchema",
            '412': "str",
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
    def reports_uid_get_with_http_info(
        self,
        uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
    ) -> ApiResponse[FullReportSchema]:
        """Get Report

        Returns a single *Information Report* or *Fintel Report* object.

        :param uid: Report identifier. (required)
        :type uid: str
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

        _param = self._reports_uid_get_serialize(
            uid=uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FullReportSchema",
            '412': "str",
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
    def reports_uid_get_without_preload_content(
        self,
        uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
        """Get Report

        Returns a single *Information Report* or *Fintel Report* object.

        :param uid: Report identifier. (required)
        :type uid: str
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

        _param = self._reports_uid_get_serialize(
            uid=uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FullReportSchema",
            '412': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _reports_uid_get_serialize(
        self,
        uid,
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
        if uid is not None:
            _path_params['uid'] = uid
        # process the query parameters
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
            resource_path='/reports/{uid}',
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




    @validate_call
    def situation_reports_get(
        self,
        situation_report: Annotated[StrictStr, Field(description="Free text reports search (all fields included).")],
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Search reports by purported victim.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by the object's native time in descending (latest) or ascending (earliest) order")] = None,
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
    ) -> SituationReportResponse:
        """Search Situation Reports

        Returns list of Situation reports matching filter criteria.

        :param situation_report: Free text reports search (all fields included). (required)
        :type situation_report: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search reports by purported victim.
        :type victim: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
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

        _param = self._situation_reports_get_serialize(
            situation_report=situation_report,
            gir=gir,
            victim=victim,
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
            '200': "SituationReportResponse",
            '412': "CveReportsGet412Response",
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
    def situation_reports_get_with_http_info(
        self,
        situation_report: Annotated[StrictStr, Field(description="Free text reports search (all fields included).")],
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Search reports by purported victim.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by the object's native time in descending (latest) or ascending (earliest) order")] = None,
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
    ) -> ApiResponse[SituationReportResponse]:
        """Search Situation Reports

        Returns list of Situation reports matching filter criteria.

        :param situation_report: Free text reports search (all fields included). (required)
        :type situation_report: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search reports by purported victim.
        :type victim: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
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

        _param = self._situation_reports_get_serialize(
            situation_report=situation_report,
            gir=gir,
            victim=victim,
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
            '200': "SituationReportResponse",
            '412': "CveReportsGet412Response",
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
    def situation_reports_get_without_preload_content(
        self,
        situation_report: Annotated[StrictStr, Field(description="Free text reports search (all fields included).")],
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Search reports by purported victim.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by the object's native time in descending (latest) or ascending (earliest) order")] = None,
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
        """Search Situation Reports

        Returns list of Situation reports matching filter criteria.

        :param situation_report: Free text reports search (all fields included). (required)
        :type situation_report: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search reports by purported victim.
        :type victim: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
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

        _param = self._situation_reports_get_serialize(
            situation_report=situation_report,
            gir=gir,
            victim=victim,
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
            '200': "SituationReportResponse",
            '412': "CveReportsGet412Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _situation_reports_get_serialize(
        self,
        situation_report,
        gir,
        victim,
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
        if situation_report is not None:
            
            _query_params.append(('situationReport', situation_report))
            
        if gir is not None:
            
            _query_params.append(('gir', gir))
            
        if victim is not None:
            
            _query_params.append(('victim', victim))
            
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
            resource_path='/situationReports',
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




    @validate_call
    def situation_reports_report_uid_get(
        self,
        report_uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
    ) -> SituationReportSchema:
        """Get Situation Report

        Returns Situation report with specified id.

        :param report_uid: Report identifier. (required)
        :type report_uid: str
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

        _param = self._situation_reports_report_uid_get_serialize(
            report_uid=report_uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SituationReportSchema",
            '404': "str",
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
    def situation_reports_report_uid_get_with_http_info(
        self,
        report_uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
    ) -> ApiResponse[SituationReportSchema]:
        """Get Situation Report

        Returns Situation report with specified id.

        :param report_uid: Report identifier. (required)
        :type report_uid: str
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

        _param = self._situation_reports_report_uid_get_serialize(
            report_uid=report_uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SituationReportSchema",
            '404': "str",
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
    def situation_reports_report_uid_get_without_preload_content(
        self,
        report_uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
        """Get Situation Report

        Returns Situation report with specified id.

        :param report_uid: Report identifier. (required)
        :type report_uid: str
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

        _param = self._situation_reports_report_uid_get_serialize(
            report_uid=report_uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SituationReportSchema",
            '404': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _situation_reports_report_uid_get_serialize(
        self,
        report_uid,
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
        if report_uid is not None:
            _path_params['reportUid'] = report_uid
        # process the query parameters
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
            resource_path='/situationReports/{reportUid}',
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




    @validate_call
    def spot_reports_get(
        self,
        spot_report: Annotated[StrictStr, Field(description="Free text reports search (all fields included).")],
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Search by purported victim.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by the object's native time in descending (latest) or ascending (earliest) order")] = None,
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
    ) -> SimpleSpotReportsResponse:
        """Search Spot Reports

        Returns list of `Spot reports` matching filter criteria.

        :param spot_report: Free text reports search (all fields included). (required)
        :type spot_report: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search by purported victim.
        :type victim: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
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

        _param = self._spot_reports_get_serialize(
            spot_report=spot_report,
            gir=gir,
            victim=victim,
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
            '200': "SimpleSpotReportsResponse",
            '412': "BreachAlertsGet412Response",
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
    def spot_reports_get_with_http_info(
        self,
        spot_report: Annotated[StrictStr, Field(description="Free text reports search (all fields included).")],
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Search by purported victim.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by the object's native time in descending (latest) or ascending (earliest) order")] = None,
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
    ) -> ApiResponse[SimpleSpotReportsResponse]:
        """Search Spot Reports

        Returns list of `Spot reports` matching filter criteria.

        :param spot_report: Free text reports search (all fields included). (required)
        :type spot_report: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search by purported victim.
        :type victim: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
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

        _param = self._spot_reports_get_serialize(
            spot_report=spot_report,
            gir=gir,
            victim=victim,
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
            '200': "SimpleSpotReportsResponse",
            '412': "BreachAlertsGet412Response",
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
    def spot_reports_get_without_preload_content(
        self,
        spot_report: Annotated[StrictStr, Field(description="Free text reports search (all fields included).")],
        gir: Annotated[Optional[StrictStr], Field(description="Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.")] = None,
        victim: Annotated[Optional[StrictStr], Field(description="Search by purported victim.")] = None,
        var_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given creation time (including).")] = None,
        until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given creation time (excluding).")] = None,
        last_updated_from: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data starting from given last updated time (including). Empty indicates unbounded.")] = None,
        last_updated_until: Annotated[Optional[StrictStr], Field(description="Long unix time or string time range. Search data ending before given last updated time (excluding). Empty indicates unbounded.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort results by the object's native time in descending (latest) or ascending (earliest) order")] = None,
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
        """Search Spot Reports

        Returns list of `Spot reports` matching filter criteria.

        :param spot_report: Free text reports search (all fields included). (required)
        :type spot_report: str
        :param gir: Search by General Intel Requirements (GIR). <br />Consult your collection manager for a General Intelligence Requirements program.
        :type gir: str
        :param victim: Search by purported victim.
        :type victim: str
        :param var_from: Long unix time or string time range. Search data starting from given creation time (including).
        :type var_from: str
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

        _param = self._spot_reports_get_serialize(
            spot_report=spot_report,
            gir=gir,
            victim=victim,
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
            '200': "SimpleSpotReportsResponse",
            '412': "BreachAlertsGet412Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _spot_reports_get_serialize(
        self,
        spot_report,
        gir,
        victim,
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
        if spot_report is not None:
            
            _query_params.append(('spotReport', spot_report))
            
        if gir is not None:
            
            _query_params.append(('gir', gir))
            
        if victim is not None:
            
            _query_params.append(('victim', victim))
            
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
            resource_path='/spotReports',
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




    @validate_call
    def spot_reports_uid_get(
        self,
        uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
    ) -> FullSpotReportSchema:
        """Get Spot Report

        Returns list of `Spot reports` matching filter criteria.

        :param uid: Report identifier. (required)
        :type uid: str
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

        _param = self._spot_reports_uid_get_serialize(
            uid=uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FullSpotReportSchema",
            '404': "str",
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
    def spot_reports_uid_get_with_http_info(
        self,
        uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
    ) -> ApiResponse[FullSpotReportSchema]:
        """Get Spot Report

        Returns list of `Spot reports` matching filter criteria.

        :param uid: Report identifier. (required)
        :type uid: str
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

        _param = self._spot_reports_uid_get_serialize(
            uid=uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FullSpotReportSchema",
            '404': "str",
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
    def spot_reports_uid_get_without_preload_content(
        self,
        uid: Annotated[StrictStr, Field(description="Report identifier.")],
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
        """Get Spot Report

        Returns list of `Spot reports` matching filter criteria.

        :param uid: Report identifier. (required)
        :type uid: str
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

        _param = self._spot_reports_uid_get_serialize(
            uid=uid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FullSpotReportSchema",
            '404': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _spot_reports_uid_get_serialize(
        self,
        uid,
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
        if uid is not None:
            _path_params['uid'] = uid
        # process the query parameters
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
            resource_path='/spotReports/{uid}',
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


