# coding: utf-8

"""
    Titan API v1

    # Introduction The Intel 471 API is organized around the principles of REST. Our API lets you gather results from our platform using anything that can send a HTTP request, including cURL and modern internet browsers. Access to this API requires an API token which is managed from your account settings.  Intel 471 reserves the right to add fields to our API however we will provide backwards compatibility and older version support so that it will be possible to choose exact versions that provide a response with an older structure.  # Authentication Authentication to the API occurs by providing your email address as the login and API key as a password in the authorization header via HTTP Basic Auth. Your API key can be found in the [API](https://portal.intel471.com/api) section on the portal. It carries many privileges so please do not expose it on public web resources.  # Accessing the API  Following examples demonstrate different methods to get the reports from `/reports` endpoint.  ## Internet browser  Just open URL: https://api.intel471.com/v1/reports  Browser will ask you for credentials, provide your email as login and API key as password.  ## cURL command line utility  Execute following command in your terminal:  ``` curl -u <YOU EMAIL>:<YOUR API KEY> https://api.intel471.com/v1/reports ```  ## Python client  We provide a [Python client](https://github.com/intel471/titan-client-python) for Intel 471's Titan API, which aims at providing common ground for all the endpoints. Please note that all the call parameters and response body fields' names are normalized to camel_case, so for example when you search reports by document type using Python client use `document_type` instead of `documentType`.  Install the client using pip (python >= 3.6 required):  ``` pip install titan-client ```  Run following script  ```python import titan_client  configuration = titan_client.Configuration(     username=\"<YOU EMAIL>\",     password=\"<YOUR API KEY>\")  with titan_client.ApiClient(configuration) as api_client:     api_instance = titan_client.ReportsApi(api_client)     api_response = api_instance.reports_get() print(api_response) ```  # Use cases  Below we present several commonly used scenarios in both raw HTTP request format and as a script using Python client. Examples are simplified so that they do not contain the authentication part and for Python client they do not contain configuration and API client object creation portion. For full example please refer to **Accessing the API** section of this document.   ## Paging  One page of the results can carry up to 100 records and you can display up to 11 pages for one query (max offset is 1000) in non-stream API endpoints. Use `count` parameter to set the number of items per page. Use `offset` parameter to shift the window by given number of results.       **HTTP**   ``` # Get 20 reports, sorted by the default field GET https://api.intel471.com/v1/reports?count=20  # Get next 20 reports GET https://api.intel471.com/v1/reports?count=20&offset=20  # Get 40 reports in one go to save API calls GET https://api.intel471.com/v1/reports?count=40 ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(count=20, offset=20) ```  ## Paging beyond the max allowed offset  Paging described in the previous use case is generally sufficient for most needs. If there are more than 1100 objects  to be obtained for a given time period and set of filter criteria, then it is possible to move the filter timestamps  along and then restart the offset sequencing. There is a very small number of situations where this may cause issues,  where there is multiple objects with the same timestamp adjacent to the last object in the response.  For the higher volume or fast changing data (such as malware indicators, malware events, creds) there are stream API endpoints  available where cursors may be used in order to acquire data easily and to avoid the need to shift timestamp ranges.  ``` # Get first 11 pages, 100 objects each  GET https://api.intel471.com/v1/reports?sort=latest&count=100 GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=1000 ... > {\"reports\": [{..., \"created\": 1661867086000}, {..., \"created\": 1661864268000}]} ```  Then the `created` time value from the last response will be used as an upper limit in the next series of calls:  ```   GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&count=100 GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=1000 ```  And so on, until the results are available or until the desired number of objects has been fetched.  ## Paging /alerts endpoint  Alerts endpoint differs from all the other non-stream API endpoints in that the `offset` parameter needs to be set  to the uid of the most recent acquired alert instead of an integer indicating the shift.  **HTTP**   ``` GET https://api.intel471.com/v1/alerts?count=100 > {\"alerts\": [{..., \"uid\": \"abc123\"}, {..., \"uid\": \"abc234\"}]}  GET https://api.intel471.com/v1/alerts?count=100&offset=abc234 > {\"alerts\": [{..., \"uid\": \"abc345\"}, {..., \"uid\": \"abc456\"}]} ```  **Python**  ``` response = titan_client.AlertsApi(api_client).alerts_get(count=100, offset=\"abc456\") ```  ## Stream endpoints paging  Stream endpoints provide the same data as their regular counterparts but they differ in a way of paging.  When working with a stream endpoint, the response always contains `cursorNext` field, which should be provided to the next subsequent  call to fetch potential next page of the results. All the subsequent calls should have the same set of query parameters as the first one,  except the cursor value. Keep calling the endpoint with a new cursor value until it stops yielding results. When new data appear after that, another call will fetch it.  **HTTP**   ``` GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT1\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT1 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT2\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT2 > {\"cursorNext\": \"MTY1NT3\"} ```  **Python**  ``` response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000) print(response.cursor_next, response.indicators) # MTY1NT1, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT1\")) print(response.cursor_next, response.indicators) # MTY1NT2, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT2\")) print(response.cursor_next, response.indicators) # MTY1NT3, None ```  ## Querying using logical operators  ### Array parameters  Any query parameter can be singular or array, if multiple parameters with the same name were provided. All parameters with the same name are internally combined into a query with `AND` operator.  So following query:  ``` GET https://api.intel471.com/v1/reports?report=sources&report=abba ```  Means \"find me reports with `source` AND `abba` in their body\".  This approach is not supported in the Python client. Instead use query string method discussed below.   ### Query string parameters  Query parameters accept Elastic's query string syntax, which allows for even better flexibility.  For example above query can be rephrased as:  **HTTP**   ``` GET https://api.intel471.com/v1/reports?report=sources OR abba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"sources OR abba\") ```  More advanced combination would include both `OR` and `AND` operators and a negation:  **HTTP**  ``` GET https://api.intel471.com/v1/reports?report=(sources OR abba) AND -creaba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"(sources OR abba) AND -creaba\") ```  Means \"find me reports with `source` or `abba` in their body which at the same time do not contain `creaba`\".  The query string \"mini-language\" reference and examples can be found on  [Elastic's query string syntax](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/query-dsl-query-string-query.html#query-dsl-query-string-query) page.  ## Get CVEs using multiple filtering criteria  Get all CVE reports for Chrome product where the risk is high and the patch is not available yet.  **HTTP**   ``` GET https://api.intel471.com/v1/cve/reports?productName=Chrome&riskLevel=high&patchStatus=unavailable ```  **Python**  ``` response = titan_client.VulnerabilitiesApi(api_client).cve_reports_get(     product_name=\"Chrome\",     risk_level=\"high\",     patch_status=\"unavailable\" ) ```  ## List watcher groups   **HTTP**   ``` GET https://api.intel471.com/v1/watcherGroups ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_get() ```  ## Create watcher group   To create a watcher group you need to pass a body along with the request.  **HTTP**   ``` POST https://api.intel471.com/v1/watcherGroups {   \"name\": \"my_group_name\",   \"description\": \"My description\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_post(   {\"name\": \"my_group_name\", \"description\": \"My description\"} ) ```  ## Create free text search watcher  **HTTP**   ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"freeTextPattern\": \"text to search\",   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"freeTextPattern\": \"text to search\",     \"notificationChannel\": \"website\"   } ) ```  ## Create specific search watcher  **HTTP**   ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"patterns\": [     {\"types\": \"Actor\" , \"pattern\": \"swisman\"}   ],   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"patterns\": [       {\"types\": \"Actor\" , \"pattern\": \"swisman\"}     ],     \"notificationChannel\": \"website\"   } ) ```  # API integration best practice with your application CORS requests to the API are not allowed due to security concerns, so please avoid AJAX calls directly from the browser. Instead consider setting up a server side proxy in your application to handle API requests.  Please consider not storing information provided by the API locally as we are constantly improving our data set and want you to have the most updated information.  # Versioning support We consistently improve our API and occasionally introduce the changes based on the customer feedback. The current API version is provided in this documentation's header. We provide API backwards compatibility whenever possible.  All requests are prefixed with the major version number, for example `/v1`:  ``` https://api.intel471.com/v1/reports ```  Different major versions are not compatible and imply significant response structure changes. Minor versions differences might include extra fields in response or provide new request parameter support. To stick to the specific version, just add `v` parameter to the request, for example: `?v=1.19.2`. If you specify a non existing version, it will be brought down to the nearest existing one.  Omitting the version parameter in the request will call the latest version of the API.  We consistently phase out the outdated versions of the API, keeping only several most recent versions. Specific version is getting disabled only when we do not record any requests using it, so it's guaranteed that calls to the outdated ones will work, though we recommend switching to the latest one as soon as possible.  We recommend to always add the version parameter to the request to be safe on API updates in your integrations.   Python client always adds the version parameter in the underlying request. API version matches the Python client's package version.   # noqa: E501

    The version of the OpenAPI document: 1.19.3
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
from titan_client.titan_stix.mappers.common import StixMapper


class SituationReportSchemaDataSituationReport(object):
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
        'entities': 'list[SituationReportSchemaDataSituationReportEntitiesInner]',
        'link': 'SituationReportSchemaDataSituationReportLink',
        'related_reports': 'list[str]',
        'released_at': 'int',
        'sensitive_source': 'bool',
        'text': 'str',
        'title': 'str',
        'victims': 'list[SituationReportSchemaDataSituationReportVictimsInner]'
    }

    attribute_map = {
        'entities': 'entities',
        'link': 'link',
        'related_reports': 'related_reports',
        'released_at': 'released_at',
        'sensitive_source': 'sensitive_source',
        'text': 'text',
        'title': 'title',
        'victims': 'victims'
    }

    def __init__(self, entities=None, link=None, related_reports=None, released_at=None, sensitive_source=None, text=None, title=None, victims=None, local_vars_configuration=None):  # noqa: E501
        """SituationReportSchemaDataSituationReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._entities = None
        self._link = None
        self._related_reports = None
        self._released_at = None
        self._sensitive_source = None
        self._text = None
        self._title = None
        self._victims = None
        self.discriminator = None

        if entities is not None:
            self.entities = entities
        self.link = link
        if related_reports is not None:
            self.related_reports = related_reports
        self.released_at = released_at
        if sensitive_source is not None:
            self.sensitive_source = sensitive_source
        self.text = text
        if title is not None:
            self.title = title
        if victims is not None:
            self.victims = victims

    @property
    def entities(self):
        """Gets the entities of this SituationReportSchemaDataSituationReport.  # noqa: E501

        List of entities. Contains the type and value fields of an `entity` object from the entities endpoint.  # noqa: E501

        :return: The entities of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :rtype: list[SituationReportSchemaDataSituationReportEntitiesInner]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this SituationReportSchemaDataSituationReport.

        List of entities. Contains the type and value fields of an `entity` object from the entities endpoint.  # noqa: E501

        :param entities: The entities of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :type entities: list[SituationReportSchemaDataSituationReportEntitiesInner]
        """

        self._entities = entities

    @property
    def link(self):
        """Gets the link of this SituationReportSchemaDataSituationReport.  # noqa: E501


        :return: The link of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :rtype: SituationReportSchemaDataSituationReportLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this SituationReportSchemaDataSituationReport.


        :param link: The link of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :type link: SituationReportSchemaDataSituationReportLink
        """
        if self.local_vars_configuration.client_side_validation and link is None:  # noqa: E501
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def related_reports(self):
        """Gets the related_reports of this SituationReportSchemaDataSituationReport.  # noqa: E501

        Situation report links to related reports like \"Information Report\" or \"Malware Report\".  # noqa: E501

        :return: The related_reports of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_reports

    @related_reports.setter
    def related_reports(self, related_reports):
        """Sets the related_reports of this SituationReportSchemaDataSituationReport.

        Situation report links to related reports like \"Information Report\" or \"Malware Report\".  # noqa: E501

        :param related_reports: The related_reports of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :type related_reports: list[str]
        """

        self._related_reports = related_reports

    @property
    def released_at(self):
        """Gets the released_at of this SituationReportSchemaDataSituationReport.  # noqa: E501

        Situation report released date.  # noqa: E501

        :return: The released_at of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :rtype: int
        """
        return self._released_at

    @released_at.setter
    def released_at(self, released_at):
        """Sets the released_at of this SituationReportSchemaDataSituationReport.

        Situation report released date.  # noqa: E501

        :param released_at: The released_at of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :type released_at: int
        """
        if self.local_vars_configuration.client_side_validation and released_at is None:  # noqa: E501
            raise ValueError("Invalid value for `released_at`, must not be `None`")  # noqa: E501

        self._released_at = released_at

    @property
    def sensitive_source(self):
        """Gets the sensitive_source of this SituationReportSchemaDataSituationReport.  # noqa: E501

        Indicates if the document contains sensitive source derived information.  # noqa: E501

        :return: The sensitive_source of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :rtype: bool
        """
        return self._sensitive_source

    @sensitive_source.setter
    def sensitive_source(self, sensitive_source):
        """Sets the sensitive_source of this SituationReportSchemaDataSituationReport.

        Indicates if the document contains sensitive source derived information.  # noqa: E501

        :param sensitive_source: The sensitive_source of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :type sensitive_source: bool
        """

        self._sensitive_source = sensitive_source

    @property
    def text(self):
        """Gets the text of this SituationReportSchemaDataSituationReport.  # noqa: E501

        Situation report text.  # noqa: E501

        :return: The text of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SituationReportSchemaDataSituationReport.

        Situation report text.  # noqa: E501

        :param text: The text of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :type text: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def title(self):
        """Gets the title of this SituationReportSchemaDataSituationReport.  # noqa: E501

        Situation report title.  # noqa: E501

        :return: The title of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SituationReportSchemaDataSituationReport.

        Situation report title.  # noqa: E501

        :param title: The title of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def victims(self):
        """Gets the victims of this SituationReportSchemaDataSituationReport.  # noqa: E501

        Purported victims list.  # noqa: E501

        :return: The victims of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :rtype: list[SituationReportSchemaDataSituationReportVictimsInner]
        """
        return self._victims

    @victims.setter
    def victims(self, victims):
        """Sets the victims of this SituationReportSchemaDataSituationReport.

        Purported victims list.  # noqa: E501

        :param victims: The victims of this SituationReportSchemaDataSituationReport.  # noqa: E501
        :type victims: list[SituationReportSchemaDataSituationReportVictimsInner]
        """

        self._victims = victims

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

    def to_stix(self, titan_client=None, api_client=None):
        stix_mapper = StixMapper(titan_client, api_client)
        return stix_mapper.map(self.to_dict(serialize=True))

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SituationReportSchemaDataSituationReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SituationReportSchemaDataSituationReport):
            return True

        return self.to_dict() != other.to_dict()
