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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from titan_client.models.event_schema_data_event_data_controller import EventSchemaDataEventDataController
from titan_client.models.event_schema_data_event_data_controllers_inner import EventSchemaDataEventDataControllersInner
from titan_client.models.event_schema_data_event_data_encryption_inner import EventSchemaDataEventDataEncryptionInner
from titan_client.models.event_schema_data_event_data_file import EventSchemaDataEventDataFile
from titan_client.models.event_schema_data_event_data_location import EventSchemaDataEventDataLocation
from titan_client.models.event_schema_data_event_data_recipient_domains_inner import EventSchemaDataEventDataRecipientDomainsInner
from titan_client.models.event_schema_data_event_data_triggers_inner import EventSchemaDataEventDataTriggersInner
from typing import Optional, Set
from typing_extensions import Self
from titan_client.titan_stix import STIXMapperSettings
from titan_client.titan_stix.mappers.common import StixMapper

class EventSchemaDataEventData(BaseModel):
    """
    Sub-document containing event data.
    """ # noqa: E501
    bot_settings: Optional[Dict[str, Any]] = Field(default=None, description="An object containing varying data types showing malware bot settings data. Contains any of but not limited the following fields: `exit_country`, `config`, `encryption`.")
    command: Optional[StrictStr] = Field(default=None, description="Command.")
    component_type: Optional[StrictStr] = Field(default=None, description="Type of component i.e. `CORE`.")
    config_file: Optional[StrictStr] = Field(default=None, description="Config file.")
    controller: Optional[EventSchemaDataEventDataController] = None
    controllers: Optional[List[EventSchemaDataEventDataControllersInner]] = Field(default=None, description="An array of objects, each containing an individual controller's url.")
    encryption: Optional[List[EventSchemaDataEventDataEncryptionInner]] = Field(default=None, description="An array of `encryption` meta data.")
    exfil_location: Optional[StrictStr] = Field(default=None, description="Contains the url location of the exfiltration event.")
    file: Optional[EventSchemaDataEventDataFile] = None
    inject_type: Optional[StrictStr] = Field(default=None, description="Inject type.")
    location: Optional[EventSchemaDataEventDataLocation] = None
    plugin_name: Optional[StrictStr] = Field(default=None, description="Plugin's name.")
    plugin_type: Optional[StrictStr] = Field(default=None, description="Type of plugin. i.e. `REMOTE_ACCESS`, `CREDENTIAL_STEALER`, `OTHER`.")
    recipient_domains: Optional[List[EventSchemaDataEventDataRecipientDomainsInner]] = Field(default=None, description="Recipient domains.")
    senders: Optional[List[StrictStr]] = Field(default=None, description="Senders.")
    settings: Optional[List[Dict[str, Any]]] = Field(default=None, description="An array of event related `settings` objects containing any of but not limited the following fields: `plugin_location`, `bot_version`, `compaign_id`, etc.")
    target_type: Optional[StrictStr] = Field(default=None, description="Type of target.")
    triggers: Optional[List[EventSchemaDataEventDataTriggersInner]] = Field(default=None, description="An array of objects, each containing the field `trigger`.")
    __properties: ClassVar[List[str]] = ["bot_settings", "command", "component_type", "config_file", "controller", "controllers", "encryption", "exfil_location", "file", "inject_type", "location", "plugin_name", "plugin_type", "recipient_domains", "senders", "settings", "target_type", "triggers"]

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
        """Create an instance of EventSchemaDataEventData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of controller
        if self.controller:
            _dict['controller'] = self.controller.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in controllers (list)
        _items = []
        if self.controllers:
            for _item in self.controllers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['controllers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in encryption (list)
        _items = []
        if self.encryption:
            for _item in self.encryption:
                if _item:
                    _items.append(_item.to_dict())
            _dict['encryption'] = _items
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict['file'] = self.file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in recipient_domains (list)
        _items = []
        if self.recipient_domains:
            for _item in self.recipient_domains:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recipient_domains'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in triggers (list)
        _items = []
        if self.triggers:
            for _item in self.triggers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['triggers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventSchemaDataEventData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bot_settings": obj.get("bot_settings"),
            "command": obj.get("command"),
            "component_type": obj.get("component_type"),
            "config_file": obj.get("config_file"),
            "controller": EventSchemaDataEventDataController.from_dict(obj["controller"]) if obj.get("controller") is not None else None,
            "controllers": [EventSchemaDataEventDataControllersInner.from_dict(_item) for _item in obj["controllers"]] if obj.get("controllers") is not None else None,
            "encryption": [EventSchemaDataEventDataEncryptionInner.from_dict(_item) for _item in obj["encryption"]] if obj.get("encryption") is not None else None,
            "exfil_location": obj.get("exfil_location"),
            "file": EventSchemaDataEventDataFile.from_dict(obj["file"]) if obj.get("file") is not None else None,
            "inject_type": obj.get("inject_type"),
            "location": EventSchemaDataEventDataLocation.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "plugin_name": obj.get("plugin_name"),
            "plugin_type": obj.get("plugin_type"),
            "recipient_domains": [EventSchemaDataEventDataRecipientDomainsInner.from_dict(_item) for _item in obj["recipient_domains"]] if obj.get("recipient_domains") is not None else None,
            "senders": obj.get("senders"),
            "settings": obj.get("settings"),
            "target_type": obj.get("target_type"),
            "triggers": [EventSchemaDataEventDataTriggersInner.from_dict(_item) for _item in obj["triggers"]] if obj.get("triggers") is not None else None
        })
        return _obj


