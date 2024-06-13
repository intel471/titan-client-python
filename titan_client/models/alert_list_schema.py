# coding: utf-8

"""
    Titan API v1

    # Introduction The Intel 471 API is organized around the principles of REST. Our API lets you gather results from our platform using anything that can send a HTTP request, including cURL and modern internet browsers. Access to this API requires an API token which is managed from your account settings.  Intel 471 reserves the right to add fields to our API however we will provide backwards compatibility and older version support so that it will be possible to choose exact versions that provide a response with an older structure.  # Authentication Authentication to the API occurs by providing your email address as the login and API key as a password in the authorization header via HTTP Basic Auth. Your API key can be found in the [API](https://portal.intel471.com/api) section on the portal. It carries many privileges so please do not expose it on public web resources.  # Accessing the API  Following examples demonstrate different methods to get the reports from `/reports` endpoint.  ## Internet browser  Just open URL: https://api.intel471.com/v1/reports  Browser will ask you for credentials, provide your email as login and API key as password.  ## cURL command line utility  Execute following command in your terminal:  ``` curl -u <YOU EMAIL>:<YOUR API KEY> https://api.intel471.com/v1/reports ```  ## Python client  We provide a [Python client](https://github.com/intel471/titan-client-python) for Intel 471's Titan API, which aims at providing common ground for all the endpoints. Please note that all the call parameters and response body fields' names are normalized to camel_case, so for example when you search reports by document type using Python client use `document_type` instead of `documentType`.  Install the client using pip (python >= 3.6 required):  ``` pip install titan-client ```  Run following script  ```python import titan_client  configuration = titan_client.Configuration(     username=\"<YOU EMAIL>\",     password=\"<YOUR API KEY>\")  with titan_client.ApiClient(configuration) as api_client:     api_instance = titan_client.ReportsApi(api_client)     api_response = api_instance.reports_get() print(api_response) ```  # Use cases  Below we present several commonly used scenarios in both raw HTTP request format and as a script using Python client. Examples are simplified so that they do not contain the authentication part and for Python client they do not contain configuration and API client object creation portion. For full example please refer to **Accessing the API** section of this document.   ## Paging  One page of the results can carry up to 100 records and you can display up to 11 pages for one query (max offset is 1000) in non-stream API endpoints. Use `count` parameter to set the number of items per page. Use `offset` parameter to shift the window by given number of results.  **HTTP**  ``` # Get 20 reports, sorted by the default field GET https://api.intel471.com/v1/reports?count=20  # Get next 20 reports GET https://api.intel471.com/v1/reports?count=20&offset=20  # Get 40 reports in one go to save API calls GET https://api.intel471.com/v1/reports?count=40 ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(count=20, offset=20) ```  ## Paging beyond the max allowed offset  Paging described in the previous use case is generally sufficient for most needs. If there are more than 1100 objects to be obtained for a given time period and set of filter criteria, then it is possible to move the filter timestamps along and then restart the offset sequencing. There is a very small number of situations where this may cause issues, where there is multiple objects with the same timestamp adjacent to the last object in the response.  For the higher volume or fast changing data (such as malware indicators, malware events, creds) there are stream API endpoints available where cursors may be used in order to acquire data easily and to avoid the need to shift timestamp ranges.  ``` # Get first 11 pages, 100 objects each GET https://api.intel471.com/v1/reports?sort=latest&count=100 GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=1000 ... > {\"reports\": [{..., \"created\": 1661867086000}, {..., \"created\": 1661864268000}]} ```  Then the `created` time value from the last response will be used as an upper limit in the next series of calls:  ```  GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&count=100 GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=1000 ```  And so on, until the results are available or until the desired number of objects has been fetched.  ## Paging /alerts endpoint  Alerts endpoint differs from all the other non-stream API endpoints in that the `offset` parameter needs to be set to the uid of the most recent acquired alert instead of an integer indicating the shift.  **HTTP**  ``` GET https://api.intel471.com/v1/alerts?count=100 > {\"alerts\": [{..., \"uid\": \"abc123\"}, {..., \"uid\": \"abc234\"}]}  GET https://api.intel471.com/v1/alerts?count=100&offset=abc234 > {\"alerts\": [{..., \"uid\": \"abc345\"}, {..., \"uid\": \"abc456\"}]} ```  **Python**  ``` response = titan_client.AlertsApi(api_client).alerts_get(count=100, offset=\"abc456\") ```  ## Stream endpoints paging  Stream endpoints provide the same data as their regular counterparts but they differ in a way of paging. When working with a stream endpoint, the response always contains `cursorNext` field, which should be provided to the next subsequent call to fetch potential next page of the results. All the subsequent calls should have the same set of query parameters as the first one, except the cursor value. Keep calling the endpoint with a new cursor value until it stops yielding results. When new data appear after that, another call will fetch it.  **HTTP**  ``` GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT1\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT1 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT2\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT2 > {\"cursorNext\": \"MTY1NT3\"} ```  **Python**  ``` response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000) print(response.cursor_next, response.indicators) # MTY1NT1, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT1\")) print(response.cursor_next, response.indicators) # MTY1NT2, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT2\")) print(response.cursor_next, response.indicators) # MTY1NT3, None ```  ## Querying using logical operators  ### Array parameters  Any query parameter can be singular or array, if multiple parameters with the same name were provided. All parameters with the same name are internally combined into a query with `AND` operator.  So following query:  ``` GET https://api.intel471.com/v1/reports?report=sources&report=abba ```  Means \"find me reports with `source` AND `abba` in their body\".  This approach is not supported in the Python client. Instead use query string method discussed below.  ### Query string parameters  Query parameters accept Elastic's query string syntax, which allows for even better flexibility.  For example above query can be rephrased as:  **HTTP**  ``` GET https://api.intel471.com/v1/reports?report=sources OR abba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"sources OR abba\") ```  More advanced combination would include both `OR` and `AND` operators and a negation:  **HTTP**  ``` GET https://api.intel471.com/v1/reports?report=(sources OR abba) AND -creaba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"(sources OR abba) AND -creaba\") ```  Means \"find me reports with `source` or `abba` in their body which at the same time do not contain `creaba`\".  The query string \"mini-language\" reference and examples can be found on [Elastic's query string syntax](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/query-dsl-query-string-query.html#query-dsl-query-string-query) page.  ## Get CVEs using multiple filtering criteria  Get all CVE reports for Chrome product where the risk is high and the patch is not available yet.  **HTTP**  ``` GET https://api.intel471.com/v1/cve/reports?productName=Chrome&riskLevel=high&patchStatus=unavailable ```  **Python**  ``` response = titan_client.VulnerabilitiesApi(api_client).cve_reports_get(     product_name=\"Chrome\",     risk_level=\"high\",     patch_status=\"unavailable\" ) ```  ## List watcher groups  **HTTP**  ``` GET https://api.intel471.com/v1/watcherGroups ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_get() ```  ## Create watcher group  To create a watcher group you need to pass a body along with the request.  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups {   \"name\": \"my_group_name\",   \"description\": \"My description\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_post(   {\"name\": \"my_group_name\", \"description\": \"My description\"} ) ```  ## Create free text search watcher  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"freeTextPattern\": \"text to search\",   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"freeTextPattern\": \"text to search\",     \"notificationChannel\": \"website\"   } ) ```  ## Create specific search watcher  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"patterns\": [     {\"types\": \"Actor\" , \"pattern\": \"swisman\"}   ],   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"patterns\": [       {\"types\": \"Actor\" , \"pattern\": \"swisman\"}     ],     \"notificationChannel\": \"website\"   } ) ```  # API integration best practice with your application CORS requests to the API are not allowed due to security concerns, so please avoid AJAX calls directly from the browser. Instead consider setting up a server side proxy in your application to handle API requests.  Please consider not storing information provided by the API locally as we are constantly improving our data set and want you to have the most updated information.  # Versioning support We consistently improve our API and occasionally introduce the changes based on the customer feedback. The current API version is provided in this documentation's header. We provide API backwards compatibility whenever possible.  All requests are prefixed with the major version number, for example `/v1`:  ``` https://api.intel471.com/v1/reports ```  Different major versions are not compatible and imply significant response structure changes. Minor versions differences might include extra fields in response or provide new request parameter support. To stick to the specific version, just add `v` parameter to the request, for example: `?v=1.19.2`. If you specify a non existing version, it will be brought down to the nearest existing one.  Omitting the version parameter in the request will call the latest version of the API.  We consistently phase out the outdated versions of the API, keeping only several most recent versions. Specific version is getting disabled only when we do not record any requests using it, so it's guaranteed that calls to the outdated ones will work, though we recommend switching to the latest one as soon as possible.  We recommend to always add the version parameter to the request to be safe on API updates in your integrations.  Python client always adds the version parameter in the underlying request. API version matches the Python client's package version.   # noqa: E501

    The version of the OpenAPI document: 1.20.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from titan_client.configuration import Configuration
from titan_client.titan_stix import STIXMapperSettings
from titan_client.titan_stix.mappers.common import StixMapper


class AlertListSchema(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'actor': 'SimpleActorSchema',
        'breach_alert': 'SimpleBreachAlertSchema',
        'credential': 'CredentialSchema',
        'credential_occurrence': 'CredentialOccurrenceSchema',
        'credential_set': 'CredentialSetSchema',
        'cve_report': 'SimpleCveSchema',
        'data_leak_post': 'DataLeakPostSchema',
        'entity': 'EntitiesSchema',
        'event': 'EventSchema',
        'found_time': 'int',
        'highlights': 'list[AlertListSchemaHighlightsInner]',
        'indicator': 'IndicatorSearchSchema',
        'instant_message': 'InstantMessageSchema',
        'post': 'PostSchema',
        'private_message': 'PrivateMessageSchema',
        'report': 'AlertListSchemaReport',
        'status': 'str',
        'uid': 'str',
        'watcher_group_uid': 'str',
        'watcher_uid': 'str'
    }

    attribute_map = {
        'actor': 'actor',
        'breach_alert': 'breachAlert',
        'credential': 'credential',
        'credential_occurrence': 'credential_occurrence',
        'credential_set': 'credential_set',
        'cve_report': 'cveReport',
        'data_leak_post': 'data_leak_post',
        'entity': 'entity',
        'event': 'event',
        'found_time': 'foundTime',
        'highlights': 'highlights',
        'indicator': 'indicator',
        'instant_message': 'instantMessage',
        'post': 'post',
        'private_message': 'privateMessage',
        'report': 'report',
        'status': 'status',
        'uid': 'uid',
        'watcher_group_uid': 'watcherGroupUid',
        'watcher_uid': 'watcherUid'
    }

    def __init__(self, actor=None, breach_alert=None, credential=None, credential_occurrence=None, credential_set=None, cve_report=None, data_leak_post=None, entity=None, event=None, found_time=None, highlights=None, indicator=None, instant_message=None, post=None, private_message=None, report=None, status=None, uid=None, watcher_group_uid=None, watcher_uid=None, local_vars_configuration=None):  # noqa: E501
        """AlertListSchema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._actor = None
        self._breach_alert = None
        self._credential = None
        self._credential_occurrence = None
        self._credential_set = None
        self._cve_report = None
        self._data_leak_post = None
        self._entity = None
        self._event = None
        self._found_time = None
        self._highlights = None
        self._indicator = None
        self._instant_message = None
        self._post = None
        self._private_message = None
        self._report = None
        self._status = None
        self._uid = None
        self._watcher_group_uid = None
        self._watcher_uid = None
        self.discriminator = None

        if actor is not None:
            self.actor = actor
        if breach_alert is not None:
            self.breach_alert = breach_alert
        if credential is not None:
            self.credential = credential
        if credential_occurrence is not None:
            self.credential_occurrence = credential_occurrence
        if credential_set is not None:
            self.credential_set = credential_set
        if cve_report is not None:
            self.cve_report = cve_report
        if data_leak_post is not None:
            self.data_leak_post = data_leak_post
        if entity is not None:
            self.entity = entity
        if event is not None:
            self.event = event
        self.found_time = found_time
        if highlights is not None:
            self.highlights = highlights
        if indicator is not None:
            self.indicator = indicator
        if instant_message is not None:
            self.instant_message = instant_message
        if post is not None:
            self.post = post
        if private_message is not None:
            self.private_message = private_message
        if report is not None:
            self.report = report
        self.status = status
        self.uid = uid
        if watcher_group_uid is not None:
            self.watcher_group_uid = watcher_group_uid
        if watcher_uid is not None:
            self.watcher_uid = watcher_uid

    @property
    def actor(self):
        """Gets the actor of this AlertListSchema.  # noqa: E501


        :return: The actor of this AlertListSchema.  # noqa: E501
        :rtype: SimpleActorSchema
        """
        return self._actor

    @actor.setter
    def actor(self, actor):
        """Sets the actor of this AlertListSchema.


        :param actor: The actor of this AlertListSchema.  # noqa: E501
        :type actor: SimpleActorSchema
        """

        self._actor = actor

    @property
    def breach_alert(self):
        """Gets the breach_alert of this AlertListSchema.  # noqa: E501


        :return: The breach_alert of this AlertListSchema.  # noqa: E501
        :rtype: SimpleBreachAlertSchema
        """
        return self._breach_alert

    @breach_alert.setter
    def breach_alert(self, breach_alert):
        """Sets the breach_alert of this AlertListSchema.


        :param breach_alert: The breach_alert of this AlertListSchema.  # noqa: E501
        :type breach_alert: SimpleBreachAlertSchema
        """

        self._breach_alert = breach_alert

    @property
    def credential(self):
        """Gets the credential of this AlertListSchema.  # noqa: E501


        :return: The credential of this AlertListSchema.  # noqa: E501
        :rtype: CredentialSchema
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this AlertListSchema.


        :param credential: The credential of this AlertListSchema.  # noqa: E501
        :type credential: CredentialSchema
        """

        self._credential = credential

    @property
    def credential_occurrence(self):
        """Gets the credential_occurrence of this AlertListSchema.  # noqa: E501


        :return: The credential_occurrence of this AlertListSchema.  # noqa: E501
        :rtype: CredentialOccurrenceSchema
        """
        return self._credential_occurrence

    @credential_occurrence.setter
    def credential_occurrence(self, credential_occurrence):
        """Sets the credential_occurrence of this AlertListSchema.


        :param credential_occurrence: The credential_occurrence of this AlertListSchema.  # noqa: E501
        :type credential_occurrence: CredentialOccurrenceSchema
        """

        self._credential_occurrence = credential_occurrence

    @property
    def credential_set(self):
        """Gets the credential_set of this AlertListSchema.  # noqa: E501


        :return: The credential_set of this AlertListSchema.  # noqa: E501
        :rtype: CredentialSetSchema
        """
        return self._credential_set

    @credential_set.setter
    def credential_set(self, credential_set):
        """Sets the credential_set of this AlertListSchema.


        :param credential_set: The credential_set of this AlertListSchema.  # noqa: E501
        :type credential_set: CredentialSetSchema
        """

        self._credential_set = credential_set

    @property
    def cve_report(self):
        """Gets the cve_report of this AlertListSchema.  # noqa: E501


        :return: The cve_report of this AlertListSchema.  # noqa: E501
        :rtype: SimpleCveSchema
        """
        return self._cve_report

    @cve_report.setter
    def cve_report(self, cve_report):
        """Sets the cve_report of this AlertListSchema.


        :param cve_report: The cve_report of this AlertListSchema.  # noqa: E501
        :type cve_report: SimpleCveSchema
        """

        self._cve_report = cve_report

    @property
    def data_leak_post(self):
        """Gets the data_leak_post of this AlertListSchema.  # noqa: E501


        :return: The data_leak_post of this AlertListSchema.  # noqa: E501
        :rtype: DataLeakPostSchema
        """
        return self._data_leak_post

    @data_leak_post.setter
    def data_leak_post(self, data_leak_post):
        """Sets the data_leak_post of this AlertListSchema.


        :param data_leak_post: The data_leak_post of this AlertListSchema.  # noqa: E501
        :type data_leak_post: DataLeakPostSchema
        """

        self._data_leak_post = data_leak_post

    @property
    def entity(self):
        """Gets the entity of this AlertListSchema.  # noqa: E501


        :return: The entity of this AlertListSchema.  # noqa: E501
        :rtype: EntitiesSchema
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this AlertListSchema.


        :param entity: The entity of this AlertListSchema.  # noqa: E501
        :type entity: EntitiesSchema
        """

        self._entity = entity

    @property
    def event(self):
        """Gets the event of this AlertListSchema.  # noqa: E501


        :return: The event of this AlertListSchema.  # noqa: E501
        :rtype: EventSchema
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this AlertListSchema.


        :param event: The event of this AlertListSchema.  # noqa: E501
        :type event: EventSchema
        """

        self._event = event

    @property
    def found_time(self):
        """Gets the found_time of this AlertListSchema.  # noqa: E501

        Date when alert was created.  # noqa: E501

        :return: The found_time of this AlertListSchema.  # noqa: E501
        :rtype: int
        """
        return self._found_time

    @found_time.setter
    def found_time(self, found_time):
        """Sets the found_time of this AlertListSchema.

        Date when alert was created.  # noqa: E501

        :param found_time: The found_time of this AlertListSchema.  # noqa: E501
        :type found_time: int
        """
        if self.local_vars_configuration.client_side_validation and found_time is None:  # noqa: E501
            raise ValueError("Invalid value for `found_time`, must not be `None`")  # noqa: E501

        self._found_time = found_time

    @property
    def highlights(self):
        """Gets the highlights of this AlertListSchema.  # noqa: E501

        Text snippets with `highlights` matching search terms.  # noqa: E501

        :return: The highlights of this AlertListSchema.  # noqa: E501
        :rtype: list[AlertListSchemaHighlightsInner]
        """
        return self._highlights

    @highlights.setter
    def highlights(self, highlights):
        """Sets the highlights of this AlertListSchema.

        Text snippets with `highlights` matching search terms.  # noqa: E501

        :param highlights: The highlights of this AlertListSchema.  # noqa: E501
        :type highlights: list[AlertListSchemaHighlightsInner]
        """

        self._highlights = highlights

    @property
    def indicator(self):
        """Gets the indicator of this AlertListSchema.  # noqa: E501


        :return: The indicator of this AlertListSchema.  # noqa: E501
        :rtype: IndicatorSearchSchema
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this AlertListSchema.


        :param indicator: The indicator of this AlertListSchema.  # noqa: E501
        :type indicator: IndicatorSearchSchema
        """

        self._indicator = indicator

    @property
    def instant_message(self):
        """Gets the instant_message of this AlertListSchema.  # noqa: E501


        :return: The instant_message of this AlertListSchema.  # noqa: E501
        :rtype: InstantMessageSchema
        """
        return self._instant_message

    @instant_message.setter
    def instant_message(self, instant_message):
        """Sets the instant_message of this AlertListSchema.


        :param instant_message: The instant_message of this AlertListSchema.  # noqa: E501
        :type instant_message: InstantMessageSchema
        """

        self._instant_message = instant_message

    @property
    def post(self):
        """Gets the post of this AlertListSchema.  # noqa: E501


        :return: The post of this AlertListSchema.  # noqa: E501
        :rtype: PostSchema
        """
        return self._post

    @post.setter
    def post(self, post):
        """Sets the post of this AlertListSchema.


        :param post: The post of this AlertListSchema.  # noqa: E501
        :type post: PostSchema
        """

        self._post = post

    @property
    def private_message(self):
        """Gets the private_message of this AlertListSchema.  # noqa: E501


        :return: The private_message of this AlertListSchema.  # noqa: E501
        :rtype: PrivateMessageSchema
        """
        return self._private_message

    @private_message.setter
    def private_message(self, private_message):
        """Sets the private_message of this AlertListSchema.


        :param private_message: The private_message of this AlertListSchema.  # noqa: E501
        :type private_message: PrivateMessageSchema
        """

        self._private_message = private_message

    @property
    def report(self):
        """Gets the report of this AlertListSchema.  # noqa: E501


        :return: The report of this AlertListSchema.  # noqa: E501
        :rtype: AlertListSchemaReport
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this AlertListSchema.


        :param report: The report of this AlertListSchema.  # noqa: E501
        :type report: AlertListSchemaReport
        """

        self._report = report

    @property
    def status(self):
        """Gets the status of this AlertListSchema.  # noqa: E501

        Read or unread.  # noqa: E501

        :return: The status of this AlertListSchema.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AlertListSchema.

        Read or unread.  # noqa: E501

        :param status: The status of this AlertListSchema.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def uid(self):
        """Gets the uid of this AlertListSchema.  # noqa: E501

        Unique alert identifier.  # noqa: E501

        :return: The uid of this AlertListSchema.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AlertListSchema.

        Unique alert identifier.  # noqa: E501

        :param uid: The uid of this AlertListSchema.  # noqa: E501
        :type uid: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def watcher_group_uid(self):
        """Gets the watcher_group_uid of this AlertListSchema.  # noqa: E501

        Unique watcher group identifier. Displayed if user has access to this watcher group.  # noqa: E501

        :return: The watcher_group_uid of this AlertListSchema.  # noqa: E501
        :rtype: str
        """
        return self._watcher_group_uid

    @watcher_group_uid.setter
    def watcher_group_uid(self, watcher_group_uid):
        """Sets the watcher_group_uid of this AlertListSchema.

        Unique watcher group identifier. Displayed if user has access to this watcher group.  # noqa: E501

        :param watcher_group_uid: The watcher_group_uid of this AlertListSchema.  # noqa: E501
        :type watcher_group_uid: str
        """

        self._watcher_group_uid = watcher_group_uid

    @property
    def watcher_uid(self):
        """Gets the watcher_uid of this AlertListSchema.  # noqa: E501

        Unique watcher identifier. Displayed if user has access to this watcher.  # noqa: E501

        :return: The watcher_uid of this AlertListSchema.  # noqa: E501
        :rtype: str
        """
        return self._watcher_uid

    @watcher_uid.setter
    def watcher_uid(self, watcher_uid):
        """Sets the watcher_uid of this AlertListSchema.

        Unique watcher identifier. Displayed if user has access to this watcher.  # noqa: E501

        :param watcher_uid: The watcher_uid of this AlertListSchema.  # noqa: E501
        :type watcher_uid: str
        """

        self._watcher_uid = watcher_uid

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_stix(self, settings: STIXMapperSettings = None):
        stix_mapper = StixMapper(settings)
        return stix_mapper.map(self.to_dict(serialize=True))

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AlertListSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertListSchema):
            return True

        return self.to_dict() != other.to_dict()
