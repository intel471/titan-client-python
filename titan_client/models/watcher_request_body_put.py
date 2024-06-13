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


class WatcherRequestBodyPut(object):
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
        'data_sets': 'list[str]',
        'description': 'str',
        'filter_by_gir_set': 'str',
        'filters': 'list[WatcherRequestBodyFiltersInner]',
        'free_text_pattern': 'str',
        'girs': 'list[str]',
        'notification_channel': 'str',
        'notification_frequency': 'str',
        'patterns': 'list[WatcherRequestBodyPatternsInner]',
        'thread_uid': 'str',
        'muted': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'data_sets': 'dataSets',
        'description': 'description',
        'filter_by_gir_set': 'filterByGirSet',
        'filters': 'filters',
        'free_text_pattern': 'freeTextPattern',
        'girs': 'girs',
        'notification_channel': 'notificationChannel',
        'notification_frequency': 'notificationFrequency',
        'patterns': 'patterns',
        'thread_uid': 'threadUid',
        'muted': 'muted',
        'type': 'type'
    }

    def __init__(self, data_sets=None, description=None, filter_by_gir_set=None, filters=None, free_text_pattern=None, girs=None, notification_channel=None, notification_frequency=None, patterns=None, thread_uid=None, muted=None, type=None, local_vars_configuration=None):  # noqa: E501
        """WatcherRequestBodyPut - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._data_sets = None
        self._description = None
        self._filter_by_gir_set = None
        self._filters = None
        self._free_text_pattern = None
        self._girs = None
        self._notification_channel = None
        self._notification_frequency = None
        self._patterns = None
        self._thread_uid = None
        self._muted = None
        self._type = None
        self.discriminator = None

        if data_sets is not None:
            self.data_sets = data_sets
        if description is not None:
            self.description = description
        if filter_by_gir_set is not None:
            self.filter_by_gir_set = filter_by_gir_set
        if filters is not None:
            self.filters = filters
        if free_text_pattern is not None:
            self.free_text_pattern = free_text_pattern
        if girs is not None:
            self.girs = girs
        if notification_channel is not None:
            self.notification_channel = notification_channel
        if notification_frequency is not None:
            self.notification_frequency = notification_frequency
        if patterns is not None:
            self.patterns = patterns
        if thread_uid is not None:
            self.thread_uid = thread_uid
        if muted is not None:
            self.muted = muted
        if type is not None:
            self.type = type

    @property
    def data_sets(self):
        """Gets the data_sets of this WatcherRequestBodyPut.  # noqa: E501

        Limiting watcher by data sets. Defaults to all accessible data sets if empty. Please pay attention, that `Malware Reports` belongs to `malware` data set and `Vulnerability Reports` belong to cve data set.  # noqa: E501

        :return: The data_sets of this WatcherRequestBodyPut.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_sets

    @data_sets.setter
    def data_sets(self, data_sets):
        """Sets the data_sets of this WatcherRequestBodyPut.

        Limiting watcher by data sets. Defaults to all accessible data sets if empty. Please pay attention, that `Malware Reports` belongs to `malware` data set and `Vulnerability Reports` belong to cve data set.  # noqa: E501

        :param data_sets: The data_sets of this WatcherRequestBodyPut.  # noqa: E501
        :type data_sets: list[str]
        """
        allowed_values = ["reports", "cve", "forums", "messagingServices", "malware", "marketplaces"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(data_sets).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `data_sets` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(data_sets) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._data_sets = data_sets

    @property
    def description(self):
        """Gets the description of this WatcherRequestBodyPut.  # noqa: E501

        Watcher description.  # noqa: E501

        :return: The description of this WatcherRequestBodyPut.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WatcherRequestBodyPut.

        Watcher description.  # noqa: E501

        :param description: The description of this WatcherRequestBodyPut.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def filter_by_gir_set(self):
        """Gets the filter_by_gir_set of this WatcherRequestBodyPut.  # noqa: E501

        GIR set filter.  # noqa: E501

        :return: The filter_by_gir_set of this WatcherRequestBodyPut.  # noqa: E501
        :rtype: str
        """
        return self._filter_by_gir_set

    @filter_by_gir_set.setter
    def filter_by_gir_set(self, filter_by_gir_set):
        """Sets the filter_by_gir_set of this WatcherRequestBodyPut.

        GIR set filter.  # noqa: E501

        :param filter_by_gir_set: The filter_by_gir_set of this WatcherRequestBodyPut.  # noqa: E501
        :type filter_by_gir_set: str
        """
        allowed_values = ["my_girs", "company_pirs", "custom"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and filter_by_gir_set not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `filter_by_gir_set` ({0}), must be one of {1}"  # noqa: E501
                .format(filter_by_gir_set, allowed_values)
            )

        self._filter_by_gir_set = filter_by_gir_set

    @property
    def filters(self):
        """Gets the filters of this WatcherRequestBodyPut.  # noqa: E501

        Search filters. Can be used with `search` watchers for narrowing results. More information about search filter types and their compatibility with search pattern types is [here](https://titan.intel471.com/api/docs/#api-_footer).  # noqa: E501

        :return: The filters of this WatcherRequestBodyPut.  # noqa: E501
        :rtype: list[WatcherRequestBodyFiltersInner]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this WatcherRequestBodyPut.

        Search filters. Can be used with `search` watchers for narrowing results. More information about search filter types and their compatibility with search pattern types is [here](https://titan.intel471.com/api/docs/#api-_footer).  # noqa: E501

        :param filters: The filters of this WatcherRequestBodyPut.  # noqa: E501
        :type filters: list[WatcherRequestBodyFiltersInner]
        """

        self._filters = filters

    @property
    def free_text_pattern(self):
        """Gets the free_text_pattern of this WatcherRequestBodyPut.  # noqa: E501

        Simplified form of adding search pattern. Search type will be automatically set to `FreeText` and pattern will be filled with a given value.  # noqa: E501

        :return: The free_text_pattern of this WatcherRequestBodyPut.  # noqa: E501
        :rtype: str
        """
        return self._free_text_pattern

    @free_text_pattern.setter
    def free_text_pattern(self, free_text_pattern):
        """Sets the free_text_pattern of this WatcherRequestBodyPut.

        Simplified form of adding search pattern. Search type will be automatically set to `FreeText` and pattern will be filled with a given value.  # noqa: E501

        :param free_text_pattern: The free_text_pattern of this WatcherRequestBodyPut.  # noqa: E501
        :type free_text_pattern: str
        """

        self._free_text_pattern = free_text_pattern

    @property
    def girs(self):
        """Gets the girs of this WatcherRequestBodyPut.  # noqa: E501

        GIR paths selected by user. Ignored if `filterByGirSet` isn't `custom`.  # noqa: E501

        :return: The girs of this WatcherRequestBodyPut.  # noqa: E501
        :rtype: list[str]
        """
        return self._girs

    @girs.setter
    def girs(self, girs):
        """Sets the girs of this WatcherRequestBodyPut.

        GIR paths selected by user. Ignored if `filterByGirSet` isn't `custom`.  # noqa: E501

        :param girs: The girs of this WatcherRequestBodyPut.  # noqa: E501
        :type girs: list[str]
        """

        self._girs = girs

    @property
    def notification_channel(self):
        """Gets the notification_channel of this WatcherRequestBodyPut.  # noqa: E501

        Notifications channel. email channel will send `email` notifications either `immediately` or `daily` (frequency has to be specified in another field). `website` channel doesn't send emails and keeps all notifications in the website. Regardless of the field value alerts are always accessible via API.  # noqa: E501

        :return: The notification_channel of this WatcherRequestBodyPut.  # noqa: E501
        :rtype: str
        """
        return self._notification_channel

    @notification_channel.setter
    def notification_channel(self, notification_channel):
        """Sets the notification_channel of this WatcherRequestBodyPut.

        Notifications channel. email channel will send `email` notifications either `immediately` or `daily` (frequency has to be specified in another field). `website` channel doesn't send emails and keeps all notifications in the website. Regardless of the field value alerts are always accessible via API.  # noqa: E501

        :param notification_channel: The notification_channel of this WatcherRequestBodyPut.  # noqa: E501
        :type notification_channel: str
        """
        allowed_values = ["website", "email"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and notification_channel not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `notification_channel` ({0}), must be one of {1}"  # noqa: E501
                .format(notification_channel, allowed_values)
            )

        self._notification_channel = notification_channel

    @property
    def notification_frequency(self):
        """Gets the notification_frequency of this WatcherRequestBodyPut.  # noqa: E501

        Notification frequency. Applicable to `email` channel only.  # noqa: E501

        :return: The notification_frequency of this WatcherRequestBodyPut.  # noqa: E501
        :rtype: str
        """
        return self._notification_frequency

    @notification_frequency.setter
    def notification_frequency(self, notification_frequency):
        """Sets the notification_frequency of this WatcherRequestBodyPut.

        Notification frequency. Applicable to `email` channel only.  # noqa: E501

        :param notification_frequency: The notification_frequency of this WatcherRequestBodyPut.  # noqa: E501
        :type notification_frequency: str
        """
        allowed_values = ["immediately", "daily"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and notification_frequency not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `notification_frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(notification_frequency, allowed_values)
            )

        self._notification_frequency = notification_frequency

    @property
    def patterns(self):
        """Gets the patterns of this WatcherRequestBodyPut.  # noqa: E501

        Extended form of adding search patterns to a `search` type watcher. Used to specify search pattern type (handle, IP address, hash, etc.).  # noqa: E501

        :return: The patterns of this WatcherRequestBodyPut.  # noqa: E501
        :rtype: list[WatcherRequestBodyPatternsInner]
        """
        return self._patterns

    @patterns.setter
    def patterns(self, patterns):
        """Sets the patterns of this WatcherRequestBodyPut.

        Extended form of adding search patterns to a `search` type watcher. Used to specify search pattern type (handle, IP address, hash, etc.).  # noqa: E501

        :param patterns: The patterns of this WatcherRequestBodyPut.  # noqa: E501
        :type patterns: list[WatcherRequestBodyPatternsInner]
        """

        self._patterns = patterns

    @property
    def thread_uid(self):
        """Gets the thread_uid of this WatcherRequestBodyPut.  # noqa: E501

        Forum thread identifier. Applicable only for `thread` watcher type.  # noqa: E501

        :return: The thread_uid of this WatcherRequestBodyPut.  # noqa: E501
        :rtype: str
        """
        return self._thread_uid

    @thread_uid.setter
    def thread_uid(self, thread_uid):
        """Sets the thread_uid of this WatcherRequestBodyPut.

        Forum thread identifier. Applicable only for `thread` watcher type.  # noqa: E501

        :param thread_uid: The thread_uid of this WatcherRequestBodyPut.  # noqa: E501
        :type thread_uid: str
        """

        self._thread_uid = thread_uid

    @property
    def muted(self):
        """Gets the muted of this WatcherRequestBodyPut.  # noqa: E501

        Watcher's mute status (if a watcher is muted, no alerts are received during its mute period)  # noqa: E501

        :return: The muted of this WatcherRequestBodyPut.  # noqa: E501
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """Sets the muted of this WatcherRequestBodyPut.

        Watcher's mute status (if a watcher is muted, no alerts are received during its mute period)  # noqa: E501

        :param muted: The muted of this WatcherRequestBodyPut.  # noqa: E501
        :type muted: bool
        """

        self._muted = muted

    @property
    def type(self):
        """Gets the type of this WatcherRequestBodyPut.  # noqa: E501

        Watcher type.<br />Only watchers of type `search` can be edited.  # noqa: E501

        :return: The type of this WatcherRequestBodyPut.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WatcherRequestBodyPut.

        Watcher type.<br />Only watchers of type `search` can be edited.  # noqa: E501

        :param type: The type of this WatcherRequestBodyPut.  # noqa: E501
        :type type: str
        """
        allowed_values = ["search"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, WatcherRequestBodyPut):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WatcherRequestBodyPut):
            return True

        return self.to_dict() != other.to_dict()
