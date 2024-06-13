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


class SimpleCveSchemaDataCveReport(object):
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
        'activity_location': 'SimpleCveSchemaDataCveReportActivityLocation',
        'counter_measure_links': 'list[SimpleCveSchemaDataCveReportCounterMeasureLinksInner]',
        'counter_measures': 'str',
        'cpe': 'object',
        'cve_status': 'str',
        'cve_type': 'str',
        'cvss_score': 'SimpleCveSchemaDataCveReportCvssScore',
        'detection': 'str',
        'exploit_status': 'SimpleCveSchemaDataCveReportExploitStatus',
        'interest_level': 'SimpleCveSchemaDataCveReportInterestLevel',
        'name': 'str',
        'patch_links': 'list[SimpleCveSchemaDataCveReportPatchLinksInner]',
        'patch_status': 'str',
        'poc': 'str',
        'poc_links': 'list[SimpleCveSchemaDataCveReportPocLinksInner]',
        'product_name': 'str',
        'risk_level': 'str',
        'summary': 'str',
        'titan_links': 'list[SimpleCveSchemaDataCveReportTitanLinksInner]',
        'underground_activity': 'str',
        'underground_activity_summary': 'str',
        'vendor_name': 'str'
    }

    attribute_map = {
        'activity_location': 'activity_location',
        'counter_measure_links': 'counter_measure_links',
        'counter_measures': 'counter_measures',
        'cpe': 'cpe',
        'cve_status': 'cve_status',
        'cve_type': 'cve_type',
        'cvss_score': 'cvss_score',
        'detection': 'detection',
        'exploit_status': 'exploit_status',
        'interest_level': 'interest_level',
        'name': 'name',
        'patch_links': 'patch_links',
        'patch_status': 'patch_status',
        'poc': 'poc',
        'poc_links': 'poc_links',
        'product_name': 'product_name',
        'risk_level': 'risk_level',
        'summary': 'summary',
        'titan_links': 'titan_links',
        'underground_activity': 'underground_activity',
        'underground_activity_summary': 'underground_activity_summary',
        'vendor_name': 'vendor_name'
    }

    def __init__(self, activity_location=None, counter_measure_links=None, counter_measures=None, cpe=None, cve_status=None, cve_type=None, cvss_score=None, detection=None, exploit_status=None, interest_level=None, name=None, patch_links=None, patch_status=None, poc=None, poc_links=None, product_name=None, risk_level=None, summary=None, titan_links=None, underground_activity=None, underground_activity_summary=None, vendor_name=None, local_vars_configuration=None):  # noqa: E501
        """SimpleCveSchemaDataCveReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._activity_location = None
        self._counter_measure_links = None
        self._counter_measures = None
        self._cpe = None
        self._cve_status = None
        self._cve_type = None
        self._cvss_score = None
        self._detection = None
        self._exploit_status = None
        self._interest_level = None
        self._name = None
        self._patch_links = None
        self._patch_status = None
        self._poc = None
        self._poc_links = None
        self._product_name = None
        self._risk_level = None
        self._summary = None
        self._titan_links = None
        self._underground_activity = None
        self._underground_activity_summary = None
        self._vendor_name = None
        self.discriminator = None

        if activity_location is not None:
            self.activity_location = activity_location
        if counter_measure_links is not None:
            self.counter_measure_links = counter_measure_links
        if counter_measures is not None:
            self.counter_measures = counter_measures
        if cpe is not None:
            self.cpe = cpe
        self.cve_status = cve_status
        self.cve_type = cve_type
        if cvss_score is not None:
            self.cvss_score = cvss_score
        if detection is not None:
            self.detection = detection
        if exploit_status is not None:
            self.exploit_status = exploit_status
        if interest_level is not None:
            self.interest_level = interest_level
        self.name = name
        if patch_links is not None:
            self.patch_links = patch_links
        if patch_status is not None:
            self.patch_status = patch_status
        self.poc = poc
        if poc_links is not None:
            self.poc_links = poc_links
        if product_name is not None:
            self.product_name = product_name
        self.risk_level = risk_level
        if summary is not None:
            self.summary = summary
        if titan_links is not None:
            self.titan_links = titan_links
        if underground_activity is not None:
            self.underground_activity = underground_activity
        if underground_activity_summary is not None:
            self.underground_activity_summary = underground_activity_summary
        if vendor_name is not None:
            self.vendor_name = vendor_name

    @property
    def activity_location(self):
        """Gets the activity_location of this SimpleCveSchemaDataCveReport.  # noqa: E501


        :return: The activity_location of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: SimpleCveSchemaDataCveReportActivityLocation
        """
        return self._activity_location

    @activity_location.setter
    def activity_location(self, activity_location):
        """Sets the activity_location of this SimpleCveSchemaDataCveReport.


        :param activity_location: The activity_location of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type activity_location: SimpleCveSchemaDataCveReportActivityLocation
        """

        self._activity_location = activity_location

    @property
    def counter_measure_links(self):
        """Gets the counter_measure_links of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Titled URLs to countermeasure information to protect against the CVE.  # noqa: E501

        :return: The counter_measure_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: list[SimpleCveSchemaDataCveReportCounterMeasureLinksInner]
        """
        return self._counter_measure_links

    @counter_measure_links.setter
    def counter_measure_links(self, counter_measure_links):
        """Sets the counter_measure_links of this SimpleCveSchemaDataCveReport.

        Titled URLs to countermeasure information to protect against the CVE.  # noqa: E501

        :param counter_measure_links: The counter_measure_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type counter_measure_links: list[SimpleCveSchemaDataCveReportCounterMeasureLinksInner]
        """

        self._counter_measure_links = counter_measure_links

    @property
    def counter_measures(self):
        """Gets the counter_measures of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Summary of `countermeasures` to protect against the CVE.  # noqa: E501

        :return: The counter_measures of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._counter_measures

    @counter_measures.setter
    def counter_measures(self, counter_measures):
        """Sets the counter_measures of this SimpleCveSchemaDataCveReport.

        Summary of `countermeasures` to protect against the CVE.  # noqa: E501

        :param counter_measures: The counter_measures of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type counter_measures: str
        """

        self._counter_measures = counter_measures

    @property
    def cpe(self):
        """Gets the cpe of this SimpleCveSchemaDataCveReport.  # noqa: E501

        `CPE` (Common Platform Enumeration) is the list of the software affected by the vulnerability. Raw data field.  # noqa: E501

        :return: The cpe of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: object
        """
        return self._cpe

    @cpe.setter
    def cpe(self, cpe):
        """Sets the cpe of this SimpleCveSchemaDataCveReport.

        `CPE` (Common Platform Enumeration) is the list of the software affected by the vulnerability. Raw data field.  # noqa: E501

        :param cpe: The cpe of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type cpe: object
        """

        self._cpe = cpe

    @property
    def cve_status(self):
        """Gets the cve_status of this SimpleCveSchemaDataCveReport.  # noqa: E501

        `status_new` for recently added CVE; `status_existing` for CVE being reported for a while; `status_historical` for phased out and not actual at the moment. Allowed values: `status_existing`, `status_new`, `status_historical`.  # noqa: E501

        :return: The cve_status of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._cve_status

    @cve_status.setter
    def cve_status(self, cve_status):
        """Sets the cve_status of this SimpleCveSchemaDataCveReport.

        `status_new` for recently added CVE; `status_existing` for CVE being reported for a while; `status_historical` for phased out and not actual at the moment. Allowed values: `status_existing`, `status_new`, `status_historical`.  # noqa: E501

        :param cve_status: The cve_status of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type cve_status: str
        """
        if self.local_vars_configuration.client_side_validation and cve_status is None:  # noqa: E501
            raise ValueError("Invalid value for `cve_status`, must not be `None`")  # noqa: E501

        self._cve_status = cve_status

    @property
    def cve_type(self):
        """Gets the cve_type of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Type of CVE, for example: `Buffer overflow`, `Privilege escalation`, `Memory corruption`, etc.  # noqa: E501

        :return: The cve_type of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._cve_type

    @cve_type.setter
    def cve_type(self, cve_type):
        """Sets the cve_type of this SimpleCveSchemaDataCveReport.

        Type of CVE, for example: `Buffer overflow`, `Privilege escalation`, `Memory corruption`, etc.  # noqa: E501

        :param cve_type: The cve_type of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type cve_type: str
        """
        if self.local_vars_configuration.client_side_validation and cve_type is None:  # noqa: E501
            raise ValueError("Invalid value for `cve_type`, must not be `None`")  # noqa: E501

        self._cve_type = cve_type

    @property
    def cvss_score(self):
        """Gets the cvss_score of this SimpleCveSchemaDataCveReport.  # noqa: E501


        :return: The cvss_score of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: SimpleCveSchemaDataCveReportCvssScore
        """
        return self._cvss_score

    @cvss_score.setter
    def cvss_score(self, cvss_score):
        """Sets the cvss_score of this SimpleCveSchemaDataCveReport.


        :param cvss_score: The cvss_score of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type cvss_score: SimpleCveSchemaDataCveReportCvssScore
        """

        self._cvss_score = cvss_score

    @property
    def detection(self):
        """Gets the detection of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Detection (signatures, definitions) exists for the CVE. Allowed values: `available`, `not_available`.  # noqa: E501

        :return: The detection of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._detection

    @detection.setter
    def detection(self, detection):
        """Sets the detection of this SimpleCveSchemaDataCveReport.

        Detection (signatures, definitions) exists for the CVE. Allowed values: `available`, `not_available`.  # noqa: E501

        :param detection: The detection of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type detection: str
        """

        self._detection = detection

    @property
    def exploit_status(self):
        """Gets the exploit_status of this SimpleCveSchemaDataCveReport.  # noqa: E501


        :return: The exploit_status of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: SimpleCveSchemaDataCveReportExploitStatus
        """
        return self._exploit_status

    @exploit_status.setter
    def exploit_status(self, exploit_status):
        """Sets the exploit_status of this SimpleCveSchemaDataCveReport.


        :param exploit_status: The exploit_status of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type exploit_status: SimpleCveSchemaDataCveReportExploitStatus
        """

        self._exploit_status = exploit_status

    @property
    def interest_level(self):
        """Gets the interest_level of this SimpleCveSchemaDataCveReport.  # noqa: E501


        :return: The interest_level of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: SimpleCveSchemaDataCveReportInterestLevel
        """
        return self._interest_level

    @interest_level.setter
    def interest_level(self, interest_level):
        """Sets the interest_level of this SimpleCveSchemaDataCveReport.


        :param interest_level: The interest_level of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type interest_level: SimpleCveSchemaDataCveReportInterestLevel
        """

        self._interest_level = interest_level

    @property
    def name(self):
        """Gets the name of this SimpleCveSchemaDataCveReport.  # noqa: E501

        CVE number.  # noqa: E501

        :return: The name of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimpleCveSchemaDataCveReport.

        CVE number.  # noqa: E501

        :param name: The name of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def patch_links(self):
        """Gets the patch_links of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Titled URLs to available CVE patch.  # noqa: E501

        :return: The patch_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: list[SimpleCveSchemaDataCveReportPatchLinksInner]
        """
        return self._patch_links

    @patch_links.setter
    def patch_links(self, patch_links):
        """Sets the patch_links of this SimpleCveSchemaDataCveReport.

        Titled URLs to available CVE patch.  # noqa: E501

        :param patch_links: The patch_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type patch_links: list[SimpleCveSchemaDataCveReportPatchLinksInner]
        """

        self._patch_links = patch_links

    @property
    def patch_status(self):
        """Gets the patch_status of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Indicates availability of the CVE patch. Allowed values: `available`, `some_available`, `unavailable`.  # noqa: E501

        :return: The patch_status of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._patch_status

    @patch_status.setter
    def patch_status(self, patch_status):
        """Sets the patch_status of this SimpleCveSchemaDataCveReport.

        Indicates availability of the CVE patch. Allowed values: `available`, `some_available`, `unavailable`.  # noqa: E501

        :param patch_status: The patch_status of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type patch_status: str
        """

        self._patch_status = patch_status

    @property
    def poc(self):
        """Gets the poc of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Proof of concept code or demonstration exists. Allowed values: `observed`, `not_observed`, `alleged_observed`.  # noqa: E501

        :return: The poc of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._poc

    @poc.setter
    def poc(self, poc):
        """Sets the poc of this SimpleCveSchemaDataCveReport.

        Proof of concept code or demonstration exists. Allowed values: `observed`, `not_observed`, `alleged_observed`.  # noqa: E501

        :param poc: The poc of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type poc: str
        """
        if self.local_vars_configuration.client_side_validation and poc is None:  # noqa: E501
            raise ValueError("Invalid value for `poc`, must not be `None`")  # noqa: E501

        self._poc = poc

    @property
    def poc_links(self):
        """Gets the poc_links of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Titled URLs to Proofs of Concept of the CVE.  # noqa: E501

        :return: The poc_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: list[SimpleCveSchemaDataCveReportPocLinksInner]
        """
        return self._poc_links

    @poc_links.setter
    def poc_links(self, poc_links):
        """Sets the poc_links of this SimpleCveSchemaDataCveReport.

        Titled URLs to Proofs of Concept of the CVE.  # noqa: E501

        :param poc_links: The poc_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type poc_links: list[SimpleCveSchemaDataCveReportPocLinksInner]
        """

        self._poc_links = poc_links

    @property
    def product_name(self):
        """Gets the product_name of this SimpleCveSchemaDataCveReport.  # noqa: E501

        `Product name` of the affected software.  # noqa: E501

        :return: The product_name of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this SimpleCveSchemaDataCveReport.

        `Product name` of the affected software.  # noqa: E501

        :param product_name: The product_name of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type product_name: str
        """

        self._product_name = product_name

    @property
    def risk_level(self):
        """Gets the risk_level of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Intel471 `risk level` of the described CVE. Allowed values: `high`, `medium`, `low`.  # noqa: E501

        :return: The risk_level of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """Sets the risk_level of this SimpleCveSchemaDataCveReport.

        Intel471 `risk level` of the described CVE. Allowed values: `high`, `medium`, `low`.  # noqa: E501

        :param risk_level: The risk_level of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type risk_level: str
        """
        if self.local_vars_configuration.client_side_validation and risk_level is None:  # noqa: E501
            raise ValueError("Invalid value for `risk_level`, must not be `None`")  # noqa: E501

        self._risk_level = risk_level

    @property
    def summary(self):
        """Gets the summary of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Intel471 `summary` of the CVE.  # noqa: E501

        :return: The summary of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this SimpleCveSchemaDataCveReport.

        Intel471 `summary` of the CVE.  # noqa: E501

        :param summary: The summary of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type summary: str
        """

        self._summary = summary

    @property
    def titan_links(self):
        """Gets the titan_links of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Links to the related titan items.  # noqa: E501

        :return: The titan_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: list[SimpleCveSchemaDataCveReportTitanLinksInner]
        """
        return self._titan_links

    @titan_links.setter
    def titan_links(self, titan_links):
        """Sets the titan_links of this SimpleCveSchemaDataCveReport.

        Links to the related titan items.  # noqa: E501

        :param titan_links: The titan_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type titan_links: list[SimpleCveSchemaDataCveReportTitanLinksInner]
        """

        self._titan_links = titan_links

    @property
    def underground_activity(self):
        """Gets the underground_activity of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Describes whether `underground activity` is observed for given CVE. Allowed values: `observed`, `not_observed`.  # noqa: E501

        :return: The underground_activity of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._underground_activity

    @underground_activity.setter
    def underground_activity(self, underground_activity):
        """Sets the underground_activity of this SimpleCveSchemaDataCveReport.

        Describes whether `underground activity` is observed for given CVE. Allowed values: `observed`, `not_observed`.  # noqa: E501

        :param underground_activity: The underground_activity of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type underground_activity: str
        """

        self._underground_activity = underground_activity

    @property
    def underground_activity_summary(self):
        """Gets the underground_activity_summary of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Describes CVE underground activity.  # noqa: E501

        :return: The underground_activity_summary of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._underground_activity_summary

    @underground_activity_summary.setter
    def underground_activity_summary(self, underground_activity_summary):
        """Sets the underground_activity_summary of this SimpleCveSchemaDataCveReport.

        Describes CVE underground activity.  # noqa: E501

        :param underground_activity_summary: The underground_activity_summary of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type underground_activity_summary: str
        """

        self._underground_activity_summary = underground_activity_summary

    @property
    def vendor_name(self):
        """Gets the vendor_name of this SimpleCveSchemaDataCveReport.  # noqa: E501

        `Vendor name` of the affected software.  # noqa: E501

        :return: The vendor_name of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """Sets the vendor_name of this SimpleCveSchemaDataCveReport.

        `Vendor name` of the affected software.  # noqa: E501

        :param vendor_name: The vendor_name of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type vendor_name: str
        """

        self._vendor_name = vendor_name

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
        if not isinstance(other, SimpleCveSchemaDataCveReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimpleCveSchemaDataCveReport):
            return True

        return self.to_dict() != other.to_dict()
