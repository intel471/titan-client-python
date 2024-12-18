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


class SearchSchema(object):
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
        'actor_total_count': 'int',
        'actors': 'list[SimpleActorSchema]',
        'breach_alerts': 'list[SimpleBreachAlertSchema]',
        'breach_alerts_total_count': 'int',
        'credential_occurrences': 'list[CredentialOccurrenceSchema]',
        'credential_occurrences_total_count': 'int',
        'credential_sets': 'list[CredentialSetSchema]',
        'credential_sets_total_count': 'int',
        'credentials': 'list[CredentialSchema]',
        'credentials_total_count': 'int',
        'cve_reports': 'list[SimpleCveSchema]',
        'cve_reports_total_count': 'int',
        'data_leak_post_total_count': 'int',
        'data_leak_posts': 'list[DataLeakPostSchema]',
        'entities': 'list[EntitiesSchema]',
        'entity_total_count': 'int',
        'event_total_count': 'int',
        'events': 'list[EventSchema]',
        'indicator_total_count': 'int',
        'indicators': 'list[IndicatorSearchSchema]',
        'instant_message_total_count': 'int',
        'instant_messages': 'list[InstantMessageSchema]',
        'ioc_total_count': 'int',
        'iocs': 'list[IocSchema]',
        'malware_report_total_count': 'int',
        'malware_reports': 'list[MalwareReportsSearchSchema]',
        'news': 'list[NewsSchema]',
        'news_total_count': 'int',
        'post_total_count': 'int',
        'posts': 'list[PostSchema]',
        'private_message_total_count': 'int',
        'private_messages': 'list[PrivateMessageSchema]',
        'report_total_count': 'int',
        'reports': 'list[SimpleReportSchema]',
        'situation_reports': 'list[SituationReportSchema]',
        'situation_reports_total_count': 'int',
        'spot_reports': 'list[SimpleSpotReportSchema]',
        'spot_reports_total_count': 'int',
        'yara_total_count': 'int',
        'yaras': 'list[YARASearchSchema]'
    }

    attribute_map = {
        'actor_total_count': 'actorTotalCount',
        'actors': 'actors',
        'breach_alerts': 'breach_alerts',
        'breach_alerts_total_count': 'breach_alerts_total_count',
        'credential_occurrences': 'credential_occurrences',
        'credential_occurrences_total_count': 'credential_occurrences_total_count',
        'credential_sets': 'credential_sets',
        'credential_sets_total_count': 'credential_sets_total_count',
        'credentials': 'credentials',
        'credentials_total_count': 'credentials_total_count',
        'cve_reports': 'cveReports',
        'cve_reports_total_count': 'cveReportsTotalCount',
        'data_leak_post_total_count': 'data_leak_post_total_count',
        'data_leak_posts': 'data_leak_posts',
        'entities': 'entities',
        'entity_total_count': 'entityTotalCount',
        'event_total_count': 'eventTotalCount',
        'events': 'events',
        'indicator_total_count': 'indicatorTotalCount',
        'indicators': 'indicators',
        'instant_message_total_count': 'instantMessageTotalCount',
        'instant_messages': 'instantMessages',
        'ioc_total_count': 'iocTotalCount',
        'iocs': 'iocs',
        'malware_report_total_count': 'malwareReportTotalCount',
        'malware_reports': 'malwareReports',
        'news': 'news',
        'news_total_count': 'newsTotalCount',
        'post_total_count': 'postTotalCount',
        'posts': 'posts',
        'private_message_total_count': 'privateMessageTotalCount',
        'private_messages': 'privateMessages',
        'report_total_count': 'reportTotalCount',
        'reports': 'reports',
        'situation_reports': 'situationReports',
        'situation_reports_total_count': 'situationReportsTotalCount',
        'spot_reports': 'spotReports',
        'spot_reports_total_count': 'spotReportsTotalCount',
        'yara_total_count': 'yaraTotalCount',
        'yaras': 'yaras'
    }

    def __init__(self, actor_total_count=None, actors=None, breach_alerts=None, breach_alerts_total_count=None, credential_occurrences=None, credential_occurrences_total_count=None, credential_sets=None, credential_sets_total_count=None, credentials=None, credentials_total_count=None, cve_reports=None, cve_reports_total_count=None, data_leak_post_total_count=None, data_leak_posts=None, entities=None, entity_total_count=None, event_total_count=None, events=None, indicator_total_count=None, indicators=None, instant_message_total_count=None, instant_messages=None, ioc_total_count=None, iocs=None, malware_report_total_count=None, malware_reports=None, news=None, news_total_count=None, post_total_count=None, posts=None, private_message_total_count=None, private_messages=None, report_total_count=None, reports=None, situation_reports=None, situation_reports_total_count=None, spot_reports=None, spot_reports_total_count=None, yara_total_count=None, yaras=None, local_vars_configuration=None):  # noqa: E501
        """SearchSchema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._actor_total_count = None
        self._actors = None
        self._breach_alerts = None
        self._breach_alerts_total_count = None
        self._credential_occurrences = None
        self._credential_occurrences_total_count = None
        self._credential_sets = None
        self._credential_sets_total_count = None
        self._credentials = None
        self._credentials_total_count = None
        self._cve_reports = None
        self._cve_reports_total_count = None
        self._data_leak_post_total_count = None
        self._data_leak_posts = None
        self._entities = None
        self._entity_total_count = None
        self._event_total_count = None
        self._events = None
        self._indicator_total_count = None
        self._indicators = None
        self._instant_message_total_count = None
        self._instant_messages = None
        self._ioc_total_count = None
        self._iocs = None
        self._malware_report_total_count = None
        self._malware_reports = None
        self._news = None
        self._news_total_count = None
        self._post_total_count = None
        self._posts = None
        self._private_message_total_count = None
        self._private_messages = None
        self._report_total_count = None
        self._reports = None
        self._situation_reports = None
        self._situation_reports_total_count = None
        self._spot_reports = None
        self._spot_reports_total_count = None
        self._yara_total_count = None
        self._yaras = None
        self.discriminator = None

        if actor_total_count is not None:
            self.actor_total_count = actor_total_count
        if actors is not None:
            self.actors = actors
        if breach_alerts is not None:
            self.breach_alerts = breach_alerts
        if breach_alerts_total_count is not None:
            self.breach_alerts_total_count = breach_alerts_total_count
        if credential_occurrences is not None:
            self.credential_occurrences = credential_occurrences
        if credential_occurrences_total_count is not None:
            self.credential_occurrences_total_count = credential_occurrences_total_count
        if credential_sets is not None:
            self.credential_sets = credential_sets
        if credential_sets_total_count is not None:
            self.credential_sets_total_count = credential_sets_total_count
        if credentials is not None:
            self.credentials = credentials
        if credentials_total_count is not None:
            self.credentials_total_count = credentials_total_count
        if cve_reports is not None:
            self.cve_reports = cve_reports
        if cve_reports_total_count is not None:
            self.cve_reports_total_count = cve_reports_total_count
        if data_leak_post_total_count is not None:
            self.data_leak_post_total_count = data_leak_post_total_count
        if data_leak_posts is not None:
            self.data_leak_posts = data_leak_posts
        if entities is not None:
            self.entities = entities
        if entity_total_count is not None:
            self.entity_total_count = entity_total_count
        if event_total_count is not None:
            self.event_total_count = event_total_count
        if events is not None:
            self.events = events
        if indicator_total_count is not None:
            self.indicator_total_count = indicator_total_count
        if indicators is not None:
            self.indicators = indicators
        if instant_message_total_count is not None:
            self.instant_message_total_count = instant_message_total_count
        if instant_messages is not None:
            self.instant_messages = instant_messages
        if ioc_total_count is not None:
            self.ioc_total_count = ioc_total_count
        if iocs is not None:
            self.iocs = iocs
        if malware_report_total_count is not None:
            self.malware_report_total_count = malware_report_total_count
        if malware_reports is not None:
            self.malware_reports = malware_reports
        if news is not None:
            self.news = news
        if news_total_count is not None:
            self.news_total_count = news_total_count
        if post_total_count is not None:
            self.post_total_count = post_total_count
        if posts is not None:
            self.posts = posts
        if private_message_total_count is not None:
            self.private_message_total_count = private_message_total_count
        if private_messages is not None:
            self.private_messages = private_messages
        if report_total_count is not None:
            self.report_total_count = report_total_count
        if reports is not None:
            self.reports = reports
        if situation_reports is not None:
            self.situation_reports = situation_reports
        if situation_reports_total_count is not None:
            self.situation_reports_total_count = situation_reports_total_count
        if spot_reports is not None:
            self.spot_reports = spot_reports
        if spot_reports_total_count is not None:
            self.spot_reports_total_count = spot_reports_total_count
        if yara_total_count is not None:
            self.yara_total_count = yara_total_count
        if yaras is not None:
            self.yaras = yaras

    @property
    def actor_total_count(self):
        """Gets the actor_total_count of this SearchSchema.  # noqa: E501

        Total count of matched actors.  # noqa: E501

        :return: The actor_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._actor_total_count

    @actor_total_count.setter
    def actor_total_count(self, actor_total_count):
        """Sets the actor_total_count of this SearchSchema.

        Total count of matched actors.  # noqa: E501

        :param actor_total_count: The actor_total_count of this SearchSchema.  # noqa: E501
        :type actor_total_count: int
        """

        self._actor_total_count = actor_total_count

    @property
    def actors(self):
        """Gets the actors of this SearchSchema.  # noqa: E501

        List of [Actors](#tag/Actors/paths/~1actors/get).  # noqa: E501

        :return: The actors of this SearchSchema.  # noqa: E501
        :rtype: list[SimpleActorSchema]
        """
        return self._actors

    @actors.setter
    def actors(self, actors):
        """Sets the actors of this SearchSchema.

        List of [Actors](#tag/Actors/paths/~1actors/get).  # noqa: E501

        :param actors: The actors of this SearchSchema.  # noqa: E501
        :type actors: list[SimpleActorSchema]
        """

        self._actors = actors

    @property
    def breach_alerts(self):
        """Gets the breach_alerts of this SearchSchema.  # noqa: E501

        List of [Breach Alerts](#tag/Reports/paths/~1breachAlerts/get).  # noqa: E501

        :return: The breach_alerts of this SearchSchema.  # noqa: E501
        :rtype: list[SimpleBreachAlertSchema]
        """
        return self._breach_alerts

    @breach_alerts.setter
    def breach_alerts(self, breach_alerts):
        """Sets the breach_alerts of this SearchSchema.

        List of [Breach Alerts](#tag/Reports/paths/~1breachAlerts/get).  # noqa: E501

        :param breach_alerts: The breach_alerts of this SearchSchema.  # noqa: E501
        :type breach_alerts: list[SimpleBreachAlertSchema]
        """

        self._breach_alerts = breach_alerts

    @property
    def breach_alerts_total_count(self):
        """Gets the breach_alerts_total_count of this SearchSchema.  # noqa: E501

        Total count of matched breach alerts.  # noqa: E501

        :return: The breach_alerts_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._breach_alerts_total_count

    @breach_alerts_total_count.setter
    def breach_alerts_total_count(self, breach_alerts_total_count):
        """Sets the breach_alerts_total_count of this SearchSchema.

        Total count of matched breach alerts.  # noqa: E501

        :param breach_alerts_total_count: The breach_alerts_total_count of this SearchSchema.  # noqa: E501
        :type breach_alerts_total_count: int
        """

        self._breach_alerts_total_count = breach_alerts_total_count

    @property
    def credential_occurrences(self):
        """Gets the credential_occurrences of this SearchSchema.  # noqa: E501

        List of [Credential occurrences](#tag/Credentials/paths/~1credentials~1occurrences/get).  # noqa: E501

        :return: The credential_occurrences of this SearchSchema.  # noqa: E501
        :rtype: list[CredentialOccurrenceSchema]
        """
        return self._credential_occurrences

    @credential_occurrences.setter
    def credential_occurrences(self, credential_occurrences):
        """Sets the credential_occurrences of this SearchSchema.

        List of [Credential occurrences](#tag/Credentials/paths/~1credentials~1occurrences/get).  # noqa: E501

        :param credential_occurrences: The credential_occurrences of this SearchSchema.  # noqa: E501
        :type credential_occurrences: list[CredentialOccurrenceSchema]
        """

        self._credential_occurrences = credential_occurrences

    @property
    def credential_occurrences_total_count(self):
        """Gets the credential_occurrences_total_count of this SearchSchema.  # noqa: E501

        Total count of matched credentials occurrences.  # noqa: E501

        :return: The credential_occurrences_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._credential_occurrences_total_count

    @credential_occurrences_total_count.setter
    def credential_occurrences_total_count(self, credential_occurrences_total_count):
        """Sets the credential_occurrences_total_count of this SearchSchema.

        Total count of matched credentials occurrences.  # noqa: E501

        :param credential_occurrences_total_count: The credential_occurrences_total_count of this SearchSchema.  # noqa: E501
        :type credential_occurrences_total_count: int
        """

        self._credential_occurrences_total_count = credential_occurrences_total_count

    @property
    def credential_sets(self):
        """Gets the credential_sets of this SearchSchema.  # noqa: E501

        List of [Credential sets](#tag/Credentials/paths/~1credentialSets/get).  # noqa: E501

        :return: The credential_sets of this SearchSchema.  # noqa: E501
        :rtype: list[CredentialSetSchema]
        """
        return self._credential_sets

    @credential_sets.setter
    def credential_sets(self, credential_sets):
        """Sets the credential_sets of this SearchSchema.

        List of [Credential sets](#tag/Credentials/paths/~1credentialSets/get).  # noqa: E501

        :param credential_sets: The credential_sets of this SearchSchema.  # noqa: E501
        :type credential_sets: list[CredentialSetSchema]
        """

        self._credential_sets = credential_sets

    @property
    def credential_sets_total_count(self):
        """Gets the credential_sets_total_count of this SearchSchema.  # noqa: E501

        Total count of matched credential sets.  # noqa: E501

        :return: The credential_sets_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._credential_sets_total_count

    @credential_sets_total_count.setter
    def credential_sets_total_count(self, credential_sets_total_count):
        """Sets the credential_sets_total_count of this SearchSchema.

        Total count of matched credential sets.  # noqa: E501

        :param credential_sets_total_count: The credential_sets_total_count of this SearchSchema.  # noqa: E501
        :type credential_sets_total_count: int
        """

        self._credential_sets_total_count = credential_sets_total_count

    @property
    def credentials(self):
        """Gets the credentials of this SearchSchema.  # noqa: E501

        List of [Credentials](#tag/Credentials/paths/~1credentials/get).  # noqa: E501

        :return: The credentials of this SearchSchema.  # noqa: E501
        :rtype: list[CredentialSchema]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this SearchSchema.

        List of [Credentials](#tag/Credentials/paths/~1credentials/get).  # noqa: E501

        :param credentials: The credentials of this SearchSchema.  # noqa: E501
        :type credentials: list[CredentialSchema]
        """

        self._credentials = credentials

    @property
    def credentials_total_count(self):
        """Gets the credentials_total_count of this SearchSchema.  # noqa: E501

        Total count of matched credentials.  # noqa: E501

        :return: The credentials_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._credentials_total_count

    @credentials_total_count.setter
    def credentials_total_count(self, credentials_total_count):
        """Sets the credentials_total_count of this SearchSchema.

        Total count of matched credentials.  # noqa: E501

        :param credentials_total_count: The credentials_total_count of this SearchSchema.  # noqa: E501
        :type credentials_total_count: int
        """

        self._credentials_total_count = credentials_total_count

    @property
    def cve_reports(self):
        """Gets the cve_reports of this SearchSchema.  # noqa: E501

        List of [Cve Reports](#tag/Vulnerabilities/paths/~1cve~1reports/get).  # noqa: E501

        :return: The cve_reports of this SearchSchema.  # noqa: E501
        :rtype: list[SimpleCveSchema]
        """
        return self._cve_reports

    @cve_reports.setter
    def cve_reports(self, cve_reports):
        """Sets the cve_reports of this SearchSchema.

        List of [Cve Reports](#tag/Vulnerabilities/paths/~1cve~1reports/get).  # noqa: E501

        :param cve_reports: The cve_reports of this SearchSchema.  # noqa: E501
        :type cve_reports: list[SimpleCveSchema]
        """

        self._cve_reports = cve_reports

    @property
    def cve_reports_total_count(self):
        """Gets the cve_reports_total_count of this SearchSchema.  # noqa: E501

        Total count of matched vulnerability reports.  # noqa: E501

        :return: The cve_reports_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._cve_reports_total_count

    @cve_reports_total_count.setter
    def cve_reports_total_count(self, cve_reports_total_count):
        """Sets the cve_reports_total_count of this SearchSchema.

        Total count of matched vulnerability reports.  # noqa: E501

        :param cve_reports_total_count: The cve_reports_total_count of this SearchSchema.  # noqa: E501
        :type cve_reports_total_count: int
        """

        self._cve_reports_total_count = cve_reports_total_count

    @property
    def data_leak_post_total_count(self):
        """Gets the data_leak_post_total_count of this SearchSchema.  # noqa: E501

        Total count of matched data leak posts.  # noqa: E501

        :return: The data_leak_post_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._data_leak_post_total_count

    @data_leak_post_total_count.setter
    def data_leak_post_total_count(self, data_leak_post_total_count):
        """Sets the data_leak_post_total_count of this SearchSchema.

        Total count of matched data leak posts.  # noqa: E501

        :param data_leak_post_total_count: The data_leak_post_total_count of this SearchSchema.  # noqa: E501
        :type data_leak_post_total_count: int
        """

        self._data_leak_post_total_count = data_leak_post_total_count

    @property
    def data_leak_posts(self):
        """Gets the data_leak_posts of this SearchSchema.  # noqa: E501

        List of [Data Leak Blogs](#tag/Data-Leak-Blogs/paths/~1dataleak~1posts/get).  # noqa: E501

        :return: The data_leak_posts of this SearchSchema.  # noqa: E501
        :rtype: list[DataLeakPostSchema]
        """
        return self._data_leak_posts

    @data_leak_posts.setter
    def data_leak_posts(self, data_leak_posts):
        """Sets the data_leak_posts of this SearchSchema.

        List of [Data Leak Blogs](#tag/Data-Leak-Blogs/paths/~1dataleak~1posts/get).  # noqa: E501

        :param data_leak_posts: The data_leak_posts of this SearchSchema.  # noqa: E501
        :type data_leak_posts: list[DataLeakPostSchema]
        """

        self._data_leak_posts = data_leak_posts

    @property
    def entities(self):
        """Gets the entities of this SearchSchema.  # noqa: E501

        List of [Entities](#tag/Entities/paths/~1entities/get).  # noqa: E501

        :return: The entities of this SearchSchema.  # noqa: E501
        :rtype: list[EntitiesSchema]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this SearchSchema.

        List of [Entities](#tag/Entities/paths/~1entities/get).  # noqa: E501

        :param entities: The entities of this SearchSchema.  # noqa: E501
        :type entities: list[EntitiesSchema]
        """

        self._entities = entities

    @property
    def entity_total_count(self):
        """Gets the entity_total_count of this SearchSchema.  # noqa: E501

        Total count of matched entities.  # noqa: E501

        :return: The entity_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._entity_total_count

    @entity_total_count.setter
    def entity_total_count(self, entity_total_count):
        """Sets the entity_total_count of this SearchSchema.

        Total count of matched entities.  # noqa: E501

        :param entity_total_count: The entity_total_count of this SearchSchema.  # noqa: E501
        :type entity_total_count: int
        """

        self._entity_total_count = entity_total_count

    @property
    def event_total_count(self):
        """Gets the event_total_count of this SearchSchema.  # noqa: E501

        Total count of matched events.  # noqa: E501

        :return: The event_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._event_total_count

    @event_total_count.setter
    def event_total_count(self, event_total_count):
        """Sets the event_total_count of this SearchSchema.

        Total count of matched events.  # noqa: E501

        :param event_total_count: The event_total_count of this SearchSchema.  # noqa: E501
        :type event_total_count: int
        """

        self._event_total_count = event_total_count

    @property
    def events(self):
        """Gets the events of this SearchSchema.  # noqa: E501

        List of [Events](#tag/Events/paths/~1events/get).  # noqa: E501

        :return: The events of this SearchSchema.  # noqa: E501
        :rtype: list[EventSchema]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this SearchSchema.

        List of [Events](#tag/Events/paths/~1events/get).  # noqa: E501

        :param events: The events of this SearchSchema.  # noqa: E501
        :type events: list[EventSchema]
        """

        self._events = events

    @property
    def indicator_total_count(self):
        """Gets the indicator_total_count of this SearchSchema.  # noqa: E501

        Total count of matched indicators.  # noqa: E501

        :return: The indicator_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._indicator_total_count

    @indicator_total_count.setter
    def indicator_total_count(self, indicator_total_count):
        """Sets the indicator_total_count of this SearchSchema.

        Total count of matched indicators.  # noqa: E501

        :param indicator_total_count: The indicator_total_count of this SearchSchema.  # noqa: E501
        :type indicator_total_count: int
        """

        self._indicator_total_count = indicator_total_count

    @property
    def indicators(self):
        """Gets the indicators of this SearchSchema.  # noqa: E501

        List of [Indicators](#tag/Indicators/paths/~1indicators/get).  # noqa: E501

        :return: The indicators of this SearchSchema.  # noqa: E501
        :rtype: list[IndicatorSearchSchema]
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators):
        """Sets the indicators of this SearchSchema.

        List of [Indicators](#tag/Indicators/paths/~1indicators/get).  # noqa: E501

        :param indicators: The indicators of this SearchSchema.  # noqa: E501
        :type indicators: list[IndicatorSearchSchema]
        """

        self._indicators = indicators

    @property
    def instant_message_total_count(self):
        """Gets the instant_message_total_count of this SearchSchema.  # noqa: E501

        Total count of matched instant messages.  # noqa: E501

        :return: The instant_message_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._instant_message_total_count

    @instant_message_total_count.setter
    def instant_message_total_count(self, instant_message_total_count):
        """Sets the instant_message_total_count of this SearchSchema.

        Total count of matched instant messages.  # noqa: E501

        :param instant_message_total_count: The instant_message_total_count of this SearchSchema.  # noqa: E501
        :type instant_message_total_count: int
        """

        self._instant_message_total_count = instant_message_total_count

    @property
    def instant_messages(self):
        """Gets the instant_messages of this SearchSchema.  # noqa: E501

        List of [Instant Messages](#tag/Messaging-Services/paths/~1messagingServices~1instantMessages/get).  # noqa: E501

        :return: The instant_messages of this SearchSchema.  # noqa: E501
        :rtype: list[InstantMessageSchema]
        """
        return self._instant_messages

    @instant_messages.setter
    def instant_messages(self, instant_messages):
        """Sets the instant_messages of this SearchSchema.

        List of [Instant Messages](#tag/Messaging-Services/paths/~1messagingServices~1instantMessages/get).  # noqa: E501

        :param instant_messages: The instant_messages of this SearchSchema.  # noqa: E501
        :type instant_messages: list[InstantMessageSchema]
        """

        self._instant_messages = instant_messages

    @property
    def ioc_total_count(self):
        """Gets the ioc_total_count of this SearchSchema.  # noqa: E501

        Total count of matched IOCs.  # noqa: E501

        :return: The ioc_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._ioc_total_count

    @ioc_total_count.setter
    def ioc_total_count(self, ioc_total_count):
        """Sets the ioc_total_count of this SearchSchema.

        Total count of matched IOCs.  # noqa: E501

        :param ioc_total_count: The ioc_total_count of this SearchSchema.  # noqa: E501
        :type ioc_total_count: int
        """

        self._ioc_total_count = ioc_total_count

    @property
    def iocs(self):
        """Gets the iocs of this SearchSchema.  # noqa: E501

        List of [Indicators of compromise](#tag/Indicators/paths/~1indicators/get).  # noqa: E501

        :return: The iocs of this SearchSchema.  # noqa: E501
        :rtype: list[IocSchema]
        """
        return self._iocs

    @iocs.setter
    def iocs(self, iocs):
        """Sets the iocs of this SearchSchema.

        List of [Indicators of compromise](#tag/Indicators/paths/~1indicators/get).  # noqa: E501

        :param iocs: The iocs of this SearchSchema.  # noqa: E501
        :type iocs: list[IocSchema]
        """

        self._iocs = iocs

    @property
    def malware_report_total_count(self):
        """Gets the malware_report_total_count of this SearchSchema.  # noqa: E501

        Total count of matched malware reports.  # noqa: E501

        :return: The malware_report_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._malware_report_total_count

    @malware_report_total_count.setter
    def malware_report_total_count(self, malware_report_total_count):
        """Sets the malware_report_total_count of this SearchSchema.

        Total count of matched malware reports.  # noqa: E501

        :param malware_report_total_count: The malware_report_total_count of this SearchSchema.  # noqa: E501
        :type malware_report_total_count: int
        """

        self._malware_report_total_count = malware_report_total_count

    @property
    def malware_reports(self):
        """Gets the malware_reports of this SearchSchema.  # noqa: E501

        List of [Malware Reports](#tag/Malware/paths/~1malwareReports/get).  # noqa: E501

        :return: The malware_reports of this SearchSchema.  # noqa: E501
        :rtype: list[MalwareReportsSearchSchema]
        """
        return self._malware_reports

    @malware_reports.setter
    def malware_reports(self, malware_reports):
        """Sets the malware_reports of this SearchSchema.

        List of [Malware Reports](#tag/Malware/paths/~1malwareReports/get).  # noqa: E501

        :param malware_reports: The malware_reports of this SearchSchema.  # noqa: E501
        :type malware_reports: list[MalwareReportsSearchSchema]
        """

        self._malware_reports = malware_reports

    @property
    def news(self):
        """Gets the news of this SearchSchema.  # noqa: E501

        List of [News](#tag/News/paths/~1news/get).  # noqa: E501

        :return: The news of this SearchSchema.  # noqa: E501
        :rtype: list[NewsSchema]
        """
        return self._news

    @news.setter
    def news(self, news):
        """Sets the news of this SearchSchema.

        List of [News](#tag/News/paths/~1news/get).  # noqa: E501

        :param news: The news of this SearchSchema.  # noqa: E501
        :type news: list[NewsSchema]
        """

        self._news = news

    @property
    def news_total_count(self):
        """Gets the news_total_count of this SearchSchema.  # noqa: E501

        Total count of matched news.  # noqa: E501

        :return: The news_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._news_total_count

    @news_total_count.setter
    def news_total_count(self, news_total_count):
        """Sets the news_total_count of this SearchSchema.

        Total count of matched news.  # noqa: E501

        :param news_total_count: The news_total_count of this SearchSchema.  # noqa: E501
        :type news_total_count: int
        """

        self._news_total_count = news_total_count

    @property
    def post_total_count(self):
        """Gets the post_total_count of this SearchSchema.  # noqa: E501

        Total count of matched posts.  # noqa: E501

        :return: The post_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._post_total_count

    @post_total_count.setter
    def post_total_count(self, post_total_count):
        """Sets the post_total_count of this SearchSchema.

        Total count of matched posts.  # noqa: E501

        :param post_total_count: The post_total_count of this SearchSchema.  # noqa: E501
        :type post_total_count: int
        """

        self._post_total_count = post_total_count

    @property
    def posts(self):
        """Gets the posts of this SearchSchema.  # noqa: E501

        List of [Posts](#tag/Forums/paths/~1posts/get).  # noqa: E501

        :return: The posts of this SearchSchema.  # noqa: E501
        :rtype: list[PostSchema]
        """
        return self._posts

    @posts.setter
    def posts(self, posts):
        """Sets the posts of this SearchSchema.

        List of [Posts](#tag/Forums/paths/~1posts/get).  # noqa: E501

        :param posts: The posts of this SearchSchema.  # noqa: E501
        :type posts: list[PostSchema]
        """

        self._posts = posts

    @property
    def private_message_total_count(self):
        """Gets the private_message_total_count of this SearchSchema.  # noqa: E501

        Total count of matched private messages.  # noqa: E501

        :return: The private_message_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._private_message_total_count

    @private_message_total_count.setter
    def private_message_total_count(self, private_message_total_count):
        """Sets the private_message_total_count of this SearchSchema.

        Total count of matched private messages.  # noqa: E501

        :param private_message_total_count: The private_message_total_count of this SearchSchema.  # noqa: E501
        :type private_message_total_count: int
        """

        self._private_message_total_count = private_message_total_count

    @property
    def private_messages(self):
        """Gets the private_messages of this SearchSchema.  # noqa: E501

        List of [PrivateMessages](#tag/Forums/paths/~1privateMessages/get).  # noqa: E501

        :return: The private_messages of this SearchSchema.  # noqa: E501
        :rtype: list[PrivateMessageSchema]
        """
        return self._private_messages

    @private_messages.setter
    def private_messages(self, private_messages):
        """Sets the private_messages of this SearchSchema.

        List of [PrivateMessages](#tag/Forums/paths/~1privateMessages/get).  # noqa: E501

        :param private_messages: The private_messages of this SearchSchema.  # noqa: E501
        :type private_messages: list[PrivateMessageSchema]
        """

        self._private_messages = private_messages

    @property
    def report_total_count(self):
        """Gets the report_total_count of this SearchSchema.  # noqa: E501

        Total count of matched information or fintel reports.  # noqa: E501

        :return: The report_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._report_total_count

    @report_total_count.setter
    def report_total_count(self, report_total_count):
        """Sets the report_total_count of this SearchSchema.

        Total count of matched information or fintel reports.  # noqa: E501

        :param report_total_count: The report_total_count of this SearchSchema.  # noqa: E501
        :type report_total_count: int
        """

        self._report_total_count = report_total_count

    @property
    def reports(self):
        """Gets the reports of this SearchSchema.  # noqa: E501

        List of [Information Reports] or [Fintel Reports]() ordered by creation time descending.  In version 1.3.0 reports also include new field `actorSubjectOfReport` with actors, mentioned in report subject.  # noqa: E501

        :return: The reports of this SearchSchema.  # noqa: E501
        :rtype: list[SimpleReportSchema]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this SearchSchema.

        List of [Information Reports] or [Fintel Reports]() ordered by creation time descending.  In version 1.3.0 reports also include new field `actorSubjectOfReport` with actors, mentioned in report subject.  # noqa: E501

        :param reports: The reports of this SearchSchema.  # noqa: E501
        :type reports: list[SimpleReportSchema]
        """

        self._reports = reports

    @property
    def situation_reports(self):
        """Gets the situation_reports of this SearchSchema.  # noqa: E501

        List of [Situation Reports](#tag/Global-Search/paths/~1search/get).  # noqa: E501

        :return: The situation_reports of this SearchSchema.  # noqa: E501
        :rtype: list[SituationReportSchema]
        """
        return self._situation_reports

    @situation_reports.setter
    def situation_reports(self, situation_reports):
        """Sets the situation_reports of this SearchSchema.

        List of [Situation Reports](#tag/Global-Search/paths/~1search/get).  # noqa: E501

        :param situation_reports: The situation_reports of this SearchSchema.  # noqa: E501
        :type situation_reports: list[SituationReportSchema]
        """

        self._situation_reports = situation_reports

    @property
    def situation_reports_total_count(self):
        """Gets the situation_reports_total_count of this SearchSchema.  # noqa: E501

        Total count of matched situation reports.  # noqa: E501

        :return: The situation_reports_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._situation_reports_total_count

    @situation_reports_total_count.setter
    def situation_reports_total_count(self, situation_reports_total_count):
        """Sets the situation_reports_total_count of this SearchSchema.

        Total count of matched situation reports.  # noqa: E501

        :param situation_reports_total_count: The situation_reports_total_count of this SearchSchema.  # noqa: E501
        :type situation_reports_total_count: int
        """

        self._situation_reports_total_count = situation_reports_total_count

    @property
    def spot_reports(self):
        """Gets the spot_reports of this SearchSchema.  # noqa: E501

        List of [Spot Reports](#tag/Reports/paths/~1spotReports/get).  # noqa: E501

        :return: The spot_reports of this SearchSchema.  # noqa: E501
        :rtype: list[SimpleSpotReportSchema]
        """
        return self._spot_reports

    @spot_reports.setter
    def spot_reports(self, spot_reports):
        """Sets the spot_reports of this SearchSchema.

        List of [Spot Reports](#tag/Reports/paths/~1spotReports/get).  # noqa: E501

        :param spot_reports: The spot_reports of this SearchSchema.  # noqa: E501
        :type spot_reports: list[SimpleSpotReportSchema]
        """

        self._spot_reports = spot_reports

    @property
    def spot_reports_total_count(self):
        """Gets the spot_reports_total_count of this SearchSchema.  # noqa: E501

        Total count of matched spot reports.  # noqa: E501

        :return: The spot_reports_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._spot_reports_total_count

    @spot_reports_total_count.setter
    def spot_reports_total_count(self, spot_reports_total_count):
        """Sets the spot_reports_total_count of this SearchSchema.

        Total count of matched spot reports.  # noqa: E501

        :param spot_reports_total_count: The spot_reports_total_count of this SearchSchema.  # noqa: E501
        :type spot_reports_total_count: int
        """

        self._spot_reports_total_count = spot_reports_total_count

    @property
    def yara_total_count(self):
        """Gets the yara_total_count of this SearchSchema.  # noqa: E501

        Total count of matched yaras.  # noqa: E501

        :return: The yara_total_count of this SearchSchema.  # noqa: E501
        :rtype: int
        """
        return self._yara_total_count

    @yara_total_count.setter
    def yara_total_count(self, yara_total_count):
        """Sets the yara_total_count of this SearchSchema.

        Total count of matched yaras.  # noqa: E501

        :param yara_total_count: The yara_total_count of this SearchSchema.  # noqa: E501
        :type yara_total_count: int
        """

        self._yara_total_count = yara_total_count

    @property
    def yaras(self):
        """Gets the yaras of this SearchSchema.  # noqa: E501

        List of [YARA](#tag/YARA/paths/~1yara/get).  # noqa: E501

        :return: The yaras of this SearchSchema.  # noqa: E501
        :rtype: list[YARASearchSchema]
        """
        return self._yaras

    @yaras.setter
    def yaras(self, yaras):
        """Sets the yaras of this SearchSchema.

        List of [YARA](#tag/YARA/paths/~1yara/get).  # noqa: E501

        :param yaras: The yaras of this SearchSchema.  # noqa: E501
        :type yaras: list[YARASearchSchema]
        """

        self._yaras = yaras

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
        if not isinstance(other, SearchSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchSchema):
            return True

        return self.to_dict() != other.to_dict()
