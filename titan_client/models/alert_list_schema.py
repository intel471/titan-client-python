# coding: utf-8

"""
    Titan API v1

    # Introduction The Intel 471 API is organized around the principles of REST. Our API lets you gather results from our platform using anything that can send a HTTP request, including cURL and modern internet browsers. Access to this API requires an API token which is managed from your account settings.  Intel 471 reserves the right to add fields to our API however we will provide backwards compatibility and older version support so that it will be possible to choose exact versions that provide a response with an older structure.  # Authentication Authentication to the API occurs by providing your email address as the login and API key as a password in the authorization header via HTTP Basic Auth. Your API key can be found in the [API](https://portal.intel471.com/api) section on the portal. It carries many privileges so please do not expose it on public web resources.  # Accessing the API  Following examples demonstrate different methods to get the reports from `/reports` endpoint.  ## Internet browser  Just open URL: https://api.intel471.com/v1/reports  Browser will ask you for credentials, provide your email as login and API key as password.  ## cURL command line utility  Execute following command in your terminal:  ``` curl -u <YOU EMAIL>:<YOUR API KEY> https://api.intel471.com/v1/reports ```  ## Python client  We provide a [Python client](https://github.com/intel471/titan-client-python) for Intel 471's Titan API, which aims at providing common ground for all the endpoints. Please note that all the call parameters and response body fields' names are normalized to camel_case, so for example when you search reports by document type using Python client use `document_type` instead of `documentType`.  Install the client using pip (python >= 3.6 required):  ``` pip install titan-client ```  Run following script  ```python import titan_client  configuration = titan_client.Configuration(     username=\"<YOU EMAIL>\",     password=\"<YOUR API KEY>\")  with titan_client.ApiClient(configuration) as api_client:     api_instance = titan_client.ReportsApi(api_client)     api_response = api_instance.reports_get() print(api_response) ```  # Use cases  Below we present several commonly used scenarios in both raw HTTP request format and as a script using Python client. Examples are simplified so that they do not contain the authentication part and for Python client they do not contain configuration and API client object creation portion. For full example please refer to **Accessing the API** section of this document.   ## Paging  One page of the results can carry up to 100 records and you can display up to 11 pages for one query (max offset is 1000) in non-stream API endpoints. Use `count` parameter to set the number of items per page. Use `offset` parameter to shift the window by given number of results.  **HTTP**  ``` # Get 20 reports, sorted by the default field GET https://api.intel471.com/v1/reports?count=20  # Get next 20 reports GET https://api.intel471.com/v1/reports?count=20&offset=20  # Get 40 reports in one go to save API calls GET https://api.intel471.com/v1/reports?count=40 ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(count=20, offset=20) ```  ## Paging beyond the max allowed offset  Paging described in the previous use case is generally sufficient for most needs. If there are more than 1100 objects to be obtained for a given time period and set of filter criteria, then it is possible to move the filter timestamps along and then restart the offset sequencing. There is a very small number of situations where this may cause issues, where there is multiple objects with the same timestamp adjacent to the last object in the response.  For the higher volume or fast changing data (such as malware indicators, malware events, creds) there are stream API endpoints available where cursors may be used in order to acquire data easily and to avoid the need to shift timestamp ranges.  ``` # Get first 11 pages, 100 objects each GET https://api.intel471.com/v1/reports?sort=latest&count=100 GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=1000 ... > {\"reports\": [{..., \"created\": 1661867086000}, {..., \"created\": 1661864268000}]} ```  Then the `created` time value from the last response will be used as an upper limit in the next series of calls:  ```  GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&count=100 GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=1000 ```  And so on, until the results are available or until the desired number of objects has been fetched.  ## Paging /alerts endpoint  Alerts endpoint differs from all the other non-stream API endpoints in that the `offset` parameter needs to be set to the uid of the most recent acquired alert instead of an integer indicating the shift.  **HTTP**  ``` GET https://api.intel471.com/v1/alerts?count=100 > {\"alerts\": [{..., \"uid\": \"abc123\"}, {..., \"uid\": \"abc234\"}]}  GET https://api.intel471.com/v1/alerts?count=100&offset=abc234 > {\"alerts\": [{..., \"uid\": \"abc345\"}, {..., \"uid\": \"abc456\"}]} ```  **Python**  ``` response = titan_client.AlertsApi(api_client).alerts_get(count=100, offset=\"abc456\") ```  ## Stream endpoints paging  Stream endpoints provide the same data as their regular counterparts but they differ in a way of paging. When working with a stream endpoint, the response always contains `cursorNext` field, which should be provided to the next subsequent call to fetch potential next page of the results. All the subsequent calls should have the same set of query parameters as the first one, except the cursor value. Keep calling the endpoint with a new cursor value until it stops yielding results. When new data appear after that, another call will fetch it.  **HTTP**  ``` GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT1\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT1 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT2\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT2 > {\"cursorNext\": \"MTY1NT3\"} ```  **Python**  ``` response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000) print(response.cursor_next, response.indicators) # MTY1NT1, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT1\")) print(response.cursor_next, response.indicators) # MTY1NT2, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT2\")) print(response.cursor_next, response.indicators) # MTY1NT3, None ```  ## Querying using logical operators  ### Array parameters  Any query parameter can be singular or array, if multiple parameters with the same name were provided. All parameters with the same name are internally combined into a query with `AND` operator.  So following query:  ``` GET https://api.intel471.com/v1/reports?report=sources&report=abba ```  Means \"find me reports with `source` AND `abba` in their body\".  This approach is not supported in the Python client. Instead use query string method discussed below.  ### Query string parameters  Query parameters accept Elastic's query string syntax, which allows for even better flexibility.  For example above query can be rephrased as:  **HTTP**  ``` GET https://api.intel471.com/v1/reports?report=sources OR abba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"sources OR abba\") ```  More advanced combination would include both `OR` and `AND` operators and a negation:  **HTTP**  ``` GET https://api.intel471.com/v1/reports?report=(sources OR abba) AND -creaba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"(sources OR abba) AND -creaba\") ```  Means \"find me reports with `source` or `abba` in their body which at the same time do not contain `creaba`\".  The query string \"mini-language\" reference and examples can be found on [Elastic's query string syntax](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/query-dsl-query-string-query.html#query-dsl-query-string-query) page.  ## Get CVEs using multiple filtering criteria  Get all CVE reports for Chrome product where the risk is high and the patch is not available yet.  **HTTP**  ``` GET https://api.intel471.com/v1/cve/reports?productName=Chrome&riskLevel=high&patchStatus=unavailable ```  **Python**  ``` response = titan_client.VulnerabilitiesApi(api_client).cve_reports_get(     product_name=\"Chrome\",     risk_level=\"high\",     patch_status=\"unavailable\" ) ```  ## List watcher groups  **HTTP**  ``` GET https://api.intel471.com/v1/watcherGroups ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_get() ```  ## Create watcher group  To create a watcher group you need to pass a body along with the request.  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups {   \"name\": \"my_group_name\",   \"description\": \"My description\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_post(   {\"name\": \"my_group_name\", \"description\": \"My description\"} ) ```  ## Create free text search watcher  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"freeTextPattern\": \"text to search\",   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"freeTextPattern\": \"text to search\",     \"notificationChannel\": \"website\"   } ) ```  ## Create specific search watcher  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"patterns\": [     {\"types\": \"Actor\" , \"pattern\": \"swisman\"}   ],   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"patterns\": [       {\"types\": \"Actor\" , \"pattern\": \"swisman\"}     ],     \"notificationChannel\": \"website\"   } ) ```  # API integration best practice with your application CORS requests to the API are not allowed due to security concerns, so please avoid AJAX calls directly from the browser. Instead consider setting up a server side proxy in your application to handle API requests.  Please consider not storing information provided by the API locally as we are constantly improving our data set and want you to have the most updated information.  # Versioning support We consistently improve our API and occasionally introduce the changes based on the customer feedback. The current API version is provided in this documentation's header. We provide API backwards compatibility whenever possible.  All requests are prefixed with the major version number, for example `/v1`:  ``` https://api.intel471.com/v1/reports ```  Different major versions are not compatible and imply significant response structure changes. Minor versions differences might include extra fields in response or provide new request parameter support. To stick to the specific version, just add `v` parameter to the request, for example: `?v=1.19.2`. If you specify a non existing version, it will be brought down to the nearest existing one.  Omitting the version parameter in the request will call the latest version of the API.  We consistently phase out the outdated versions of the API, keeping only several most recent versions. Specific version is getting disabled only when we do not record any requests using it, so it's guaranteed that calls to the outdated ones will work, though we recommend switching to the latest one as soon as possible.  We recommend to always add the version parameter to the request to be safe on API updates in your integrations.  Python client always adds the version parameter in the underlying request. API version matches the Python client's package version. 

    The version of the OpenAPI document: 1.20.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from titan_client.models.alert_list_schema_highlights_inner import AlertListSchemaHighlightsInner
from titan_client.models.alert_list_schema_report import AlertListSchemaReport
from titan_client.models.credential_occurrence_schema import CredentialOccurrenceSchema
from titan_client.models.credential_schema import CredentialSchema
from titan_client.models.credential_set_schema import CredentialSetSchema
from titan_client.models.data_leak_post_schema import DataLeakPostSchema
from titan_client.models.entities_schema import EntitiesSchema
from titan_client.models.event_schema import EventSchema
from titan_client.models.indicator_search_schema import IndicatorSearchSchema
from titan_client.models.instant_message_schema import InstantMessageSchema
from titan_client.models.post_schema import PostSchema
from titan_client.models.private_message_schema import PrivateMessageSchema
from titan_client.models.simple_actor_schema import SimpleActorSchema
from titan_client.models.simple_breach_alert_schema import SimpleBreachAlertSchema
from titan_client.models.simple_cve_schema import SimpleCveSchema
from typing import Optional, Set
from typing_extensions import Self
from titan_client.titan_stix import STIXMapperSettings
from titan_client.titan_stix.mappers.common import StixMapper

class AlertListSchema(BaseModel):
    """
    Returns list of Alerts matching filter criteria excluding the following types: Malware reports, YARA
    """ # noqa: E501
    actor: Optional[SimpleActorSchema] = None
    breach_alert: Optional[SimpleBreachAlertSchema] = Field(default=None, alias="breachAlert")
    credential: Optional[CredentialSchema] = None
    credential_occurrence: Optional[CredentialOccurrenceSchema] = None
    credential_set: Optional[CredentialSetSchema] = None
    cve_report: Optional[SimpleCveSchema] = Field(default=None, alias="cveReport")
    data_leak_post: Optional[DataLeakPostSchema] = None
    entity: Optional[EntitiesSchema] = None
    event: Optional[EventSchema] = None
    found_time: StrictInt = Field(description="Date when alert was created.", alias="foundTime")
    highlights: Optional[List[AlertListSchemaHighlightsInner]] = Field(default=None, description="Text snippets with `highlights` matching search terms.")
    indicator: Optional[IndicatorSearchSchema] = None
    instant_message: Optional[InstantMessageSchema] = Field(default=None, alias="instantMessage")
    post: Optional[PostSchema] = None
    private_message: Optional[PrivateMessageSchema] = Field(default=None, alias="privateMessage")
    report: Optional[AlertListSchemaReport] = None
    status: StrictStr = Field(description="Read or unread.")
    uid: StrictStr = Field(description="Unique alert identifier.")
    watcher_group_uid: Optional[StrictStr] = Field(default=None, description="Unique watcher group identifier. Displayed if user has access to this watcher group.", alias="watcherGroupUid")
    watcher_uid: Optional[StrictStr] = Field(default=None, description="Unique watcher identifier. Displayed if user has access to this watcher.", alias="watcherUid")
    __properties: ClassVar[List[str]] = ["actor", "breachAlert", "credential", "credential_occurrence", "credential_set", "cveReport", "data_leak_post", "entity", "event", "foundTime", "highlights", "indicator", "instantMessage", "post", "privateMessage", "report", "status", "uid", "watcherGroupUid", "watcherUid"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    def to_stix(self, settings: STIXMapperSettings = None):
        stix_mapper = StixMapper(settings)
        return stix_mapper.map(self.to_dict(serialize=True))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AlertListSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of actor
        if self.actor:
            _dict['actor'] = self.actor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of breach_alert
        if self.breach_alert:
            _dict['breachAlert'] = self.breach_alert.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credential
        if self.credential:
            _dict['credential'] = self.credential.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credential_occurrence
        if self.credential_occurrence:
            _dict['credential_occurrence'] = self.credential_occurrence.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credential_set
        if self.credential_set:
            _dict['credential_set'] = self.credential_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cve_report
        if self.cve_report:
            _dict['cveReport'] = self.cve_report.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_leak_post
        if self.data_leak_post:
            _dict['data_leak_post'] = self.data_leak_post.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entity
        if self.entity:
            _dict['entity'] = self.entity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event
        if self.event:
            _dict['event'] = self.event.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in highlights (list)
        _items = []
        if self.highlights:
            for _item in self.highlights:
                if _item:
                    _items.append(_item.to_dict())
            _dict['highlights'] = _items
        # override the default output from pydantic by calling `to_dict()` of indicator
        if self.indicator:
            _dict['indicator'] = self.indicator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of instant_message
        if self.instant_message:
            _dict['instantMessage'] = self.instant_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of post
        if self.post:
            _dict['post'] = self.post.to_dict()
        # override the default output from pydantic by calling `to_dict()` of private_message
        if self.private_message:
            _dict['privateMessage'] = self.private_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of report
        if self.report:
            _dict['report'] = self.report.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlertListSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actor": SimpleActorSchema.from_dict(obj["actor"]) if obj.get("actor") is not None else None,
            "breachAlert": SimpleBreachAlertSchema.from_dict(obj["breachAlert"]) if obj.get("breachAlert") is not None else None,
            "credential": CredentialSchema.from_dict(obj["credential"]) if obj.get("credential") is not None else None,
            "credential_occurrence": CredentialOccurrenceSchema.from_dict(obj["credential_occurrence"]) if obj.get("credential_occurrence") is not None else None,
            "credential_set": CredentialSetSchema.from_dict(obj["credential_set"]) if obj.get("credential_set") is not None else None,
            "cveReport": SimpleCveSchema.from_dict(obj["cveReport"]) if obj.get("cveReport") is not None else None,
            "data_leak_post": DataLeakPostSchema.from_dict(obj["data_leak_post"]) if obj.get("data_leak_post") is not None else None,
            "entity": EntitiesSchema.from_dict(obj["entity"]) if obj.get("entity") is not None else None,
            "event": EventSchema.from_dict(obj["event"]) if obj.get("event") is not None else None,
            "foundTime": obj.get("foundTime"),
            "highlights": [AlertListSchemaHighlightsInner.from_dict(_item) for _item in obj["highlights"]] if obj.get("highlights") is not None else None,
            "indicator": IndicatorSearchSchema.from_dict(obj["indicator"]) if obj.get("indicator") is not None else None,
            "instantMessage": InstantMessageSchema.from_dict(obj["instantMessage"]) if obj.get("instantMessage") is not None else None,
            "post": PostSchema.from_dict(obj["post"]) if obj.get("post") is not None else None,
            "privateMessage": PrivateMessageSchema.from_dict(obj["privateMessage"]) if obj.get("privateMessage") is not None else None,
            "report": AlertListSchemaReport.from_dict(obj["report"]) if obj.get("report") is not None else None,
            "status": obj.get("status"),
            "uid": obj.get("uid"),
            "watcherGroupUid": obj.get("watcherGroupUid"),
            "watcherUid": obj.get("watcherUid")
        })
        return _obj


