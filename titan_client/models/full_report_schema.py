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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from titan_client.models.simple_report_schema_actor_subject_of_report_inner import SimpleReportSchemaActorSubjectOfReportInner
from titan_client.models.simple_report_schema_classification import SimpleReportSchemaClassification
from titan_client.models.simple_report_schema_entities_inner import SimpleReportSchemaEntitiesInner
from titan_client.models.simple_report_schema_locations_inner import SimpleReportSchemaLocationsInner
from titan_client.models.simple_report_schema_related_reports_inner import SimpleReportSchemaRelatedReportsInner
from titan_client.models.simple_report_schema_report_attachments_inner import SimpleReportSchemaReportAttachmentsInner
from titan_client.models.simple_report_schema_sources_inner import SimpleReportSchemaSourcesInner
from titan_client.models.simple_report_schema_victims_inner import SimpleReportSchemaVictimsInner
from typing import Optional, Set
from typing_extensions import Self
from titan_client.titan_stix import STIXMapperSettings
from titan_client.titan_stix.mappers.common import StixMapper

class FullReportSchema(BaseModel):
    """
    FullReportSchema
    """ # noqa: E501
    actor_handle: Optional[StrictStr] = Field(default=None, description="Actor's handle", alias="actorHandle")
    actor_subject_of_report: Optional[List[SimpleReportSchemaActorSubjectOfReportInner]] = Field(default=None, description="List of actors mentioned in report subject.", alias="actorSubjectOfReport")
    admiralty_code: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Code as described [here](http://en.wikipedia.org/wiki/Admiralty_code). All Fintel reports have admiraltyCode=`A1`.", alias="admiraltyCode")
    classification: Optional[SimpleReportSchemaClassification] = None
    created: Optional[StrictInt] = Field(default=None, description="Date the report was `created` as Epoch Time.")
    date_of_information: Optional[StrictInt] = Field(default=None, description="Date of information as Epoch Time.", alias="dateOfInformation")
    document_family: Optional[StrictStr] = Field(default=None, description="Document family.", alias="documentFamily")
    document_type: Optional[StrictStr] = Field(default=None, description="Document type.", alias="documentType")
    entities: Optional[List[SimpleReportSchemaEntitiesInner]] = Field(default=None, description="List of entities.")
    last_updated: Optional[StrictInt] = Field(default=None, description="Last modification date as Epoch Time.", alias="lastUpdated")
    locations: Optional[List[SimpleReportSchemaLocationsInner]] = Field(default=None, description="Report `locations`.")
    motivation: Optional[List[StrictStr]] = Field(default=None, description="Actor's `motivation`. CC for Cyber Crime, CE for Cyber Espionage, HA for Hacktivism.")
    portal_report_url: StrictStr = Field(description="URL to the report on the portal.", alias="portalReportUrl")
    related_reports: Optional[List[SimpleReportSchemaRelatedReportsInner]] = Field(default=None, description="List of related reports.", alias="relatedReports")
    released: Optional[StrictInt] = Field(default=None, description="Date the report was `released` as Epoch Time.")
    report_attachments: Optional[List[SimpleReportSchemaReportAttachmentsInner]] = Field(default=None, description="List of report attachments.", alias="reportAttachments")
    sensitive_source: Optional[StrictBool] = Field(default=None, description="Indicates if the document contains sensitive source derived information.", alias="sensitiveSource")
    source_characterization: Optional[StrictStr] = Field(default=None, description="Source characterization.", alias="sourceCharacterization")
    sources: Optional[List[SimpleReportSchemaSourcesInner]] = Field(default=None, description="List of `sources`.")
    subject: StrictStr = Field(description="Report's `subject`.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Report's assigned `tags`.")
    uid: StrictStr = Field(description="Unique report identifier.")
    victims: Optional[List[SimpleReportSchemaVictimsInner]] = Field(default=None, description="Purported victims list.")
    executive_summary: Optional[StrictStr] = Field(default=None, description="Executive summary in HTML format.", alias="executiveSummary")
    raw_text: StrictStr = Field(description="Raw text in HTML format.", alias="rawText")
    raw_text_translated: Optional[StrictStr] = Field(default=None, description="Translated text in HTML format.", alias="rawTextTranslated")
    researcher_comments: Optional[StrictStr] = Field(default=None, description="Researcher's comments in HTML format.", alias="researcherComments")
    __properties: ClassVar[List[str]] = ["actorHandle", "actorSubjectOfReport", "admiraltyCode", "classification", "created", "dateOfInformation", "documentFamily", "documentType", "entities", "lastUpdated", "locations", "motivation", "portalReportUrl", "relatedReports", "released", "reportAttachments", "sensitiveSource", "sourceCharacterization", "sources", "subject", "tags", "uid", "victims", "executiveSummary", "rawText", "rawTextTranslated", "researcherComments"]

    @field_validator('admiralty_code')
    def admiralty_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[A-F][1-6]$", value):
            raise ValueError(r"must validate the regular expression /^[A-F][1-6]$/")
        return value

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
        """Create an instance of FullReportSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in actor_subject_of_report (list)
        _items = []
        if self.actor_subject_of_report:
            for _item in self.actor_subject_of_report:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actorSubjectOfReport'] = _items
        # override the default output from pydantic by calling `to_dict()` of classification
        if self.classification:
            _dict['classification'] = self.classification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item in self.entities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in locations (list)
        _items = []
        if self.locations:
            for _item in self.locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['locations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in related_reports (list)
        _items = []
        if self.related_reports:
            for _item in self.related_reports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relatedReports'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in report_attachments (list)
        _items = []
        if self.report_attachments:
            for _item in self.report_attachments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['reportAttachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sources (list)
        _items = []
        if self.sources:
            for _item in self.sources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in victims (list)
        _items = []
        if self.victims:
            for _item in self.victims:
                if _item:
                    _items.append(_item.to_dict())
            _dict['victims'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FullReportSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actorHandle": obj.get("actorHandle"),
            "actorSubjectOfReport": [SimpleReportSchemaActorSubjectOfReportInner.from_dict(_item) for _item in obj["actorSubjectOfReport"]] if obj.get("actorSubjectOfReport") is not None else None,
            "admiraltyCode": obj.get("admiraltyCode"),
            "classification": SimpleReportSchemaClassification.from_dict(obj["classification"]) if obj.get("classification") is not None else None,
            "created": obj.get("created"),
            "dateOfInformation": obj.get("dateOfInformation"),
            "documentFamily": obj.get("documentFamily"),
            "documentType": obj.get("documentType"),
            "entities": [SimpleReportSchemaEntitiesInner.from_dict(_item) for _item in obj["entities"]] if obj.get("entities") is not None else None,
            "lastUpdated": obj.get("lastUpdated"),
            "locations": [SimpleReportSchemaLocationsInner.from_dict(_item) for _item in obj["locations"]] if obj.get("locations") is not None else None,
            "motivation": obj.get("motivation"),
            "portalReportUrl": obj.get("portalReportUrl"),
            "relatedReports": [SimpleReportSchemaRelatedReportsInner.from_dict(_item) for _item in obj["relatedReports"]] if obj.get("relatedReports") is not None else None,
            "released": obj.get("released"),
            "reportAttachments": [SimpleReportSchemaReportAttachmentsInner.from_dict(_item) for _item in obj["reportAttachments"]] if obj.get("reportAttachments") is not None else None,
            "sensitiveSource": obj.get("sensitiveSource"),
            "sourceCharacterization": obj.get("sourceCharacterization"),
            "sources": [SimpleReportSchemaSourcesInner.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None,
            "subject": obj.get("subject"),
            "tags": obj.get("tags"),
            "uid": obj.get("uid"),
            "victims": [SimpleReportSchemaVictimsInner.from_dict(_item) for _item in obj["victims"]] if obj.get("victims") is not None else None,
            "executiveSummary": obj.get("executiveSummary"),
            "rawText": obj.get("rawText"),
            "rawTextTranslated": obj.get("rawTextTranslated"),
            "researcherComments": obj.get("researcherComments")
        })
        return _obj


