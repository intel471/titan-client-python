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


class EventSchemaDataEventData(object):
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
        'attack_targets': 'list[object]',
        'attack_type': 'str',
        'bot_settings': 'object',
        'command': 'str',
        'component_type': 'str',
        'config_file': 'str',
        'controller': 'EventSchemaDataEventDataController',
        'controllers': 'list[EventSchemaDataEventDataControllersInner]',
        'encryption': 'list[EventSchemaDataEventDataEncryptionInner]',
        'exfil_location': 'str',
        'file': 'EventSchemaDataEventDataFile',
        'inject_type': 'str',
        'location': 'EventSchemaDataEventDataLocation',
        'parameters': 'list[object]',
        'plugin_name': 'str',
        'plugin_type': 'str',
        'recipient_domains': 'list[EventSchemaDataEventDataRecipientDomainsInner]',
        'senders': 'list[str]',
        'settings': 'list[object]',
        'target_type': 'str',
        'triggers': 'list[EventSchemaDataEventDataTriggersInner]'
    }

    attribute_map = {
        'attack_targets': 'attack_targets',
        'attack_type': 'attack_type',
        'bot_settings': 'bot_settings',
        'command': 'command',
        'component_type': 'component_type',
        'config_file': 'config_file',
        'controller': 'controller',
        'controllers': 'controllers',
        'encryption': 'encryption',
        'exfil_location': 'exfil_location',
        'file': 'file',
        'inject_type': 'inject_type',
        'location': 'location',
        'parameters': 'parameters',
        'plugin_name': 'plugin_name',
        'plugin_type': 'plugin_type',
        'recipient_domains': 'recipient_domains',
        'senders': 'senders',
        'settings': 'settings',
        'target_type': 'target_type',
        'triggers': 'triggers'
    }

    def __init__(self, attack_targets=None, attack_type=None, bot_settings=None, command=None, component_type=None, config_file=None, controller=None, controllers=None, encryption=None, exfil_location=None, file=None, inject_type=None, location=None, parameters=None, plugin_name=None, plugin_type=None, recipient_domains=None, senders=None, settings=None, target_type=None, triggers=None, local_vars_configuration=None):  # noqa: E501
        """EventSchemaDataEventData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._attack_targets = None
        self._attack_type = None
        self._bot_settings = None
        self._command = None
        self._component_type = None
        self._config_file = None
        self._controller = None
        self._controllers = None
        self._encryption = None
        self._exfil_location = None
        self._file = None
        self._inject_type = None
        self._location = None
        self._parameters = None
        self._plugin_name = None
        self._plugin_type = None
        self._recipient_domains = None
        self._senders = None
        self._settings = None
        self._target_type = None
        self._triggers = None
        self.discriminator = None

        if attack_targets is not None:
            self.attack_targets = attack_targets
        if attack_type is not None:
            self.attack_type = attack_type
        if bot_settings is not None:
            self.bot_settings = bot_settings
        if command is not None:
            self.command = command
        if component_type is not None:
            self.component_type = component_type
        if config_file is not None:
            self.config_file = config_file
        if controller is not None:
            self.controller = controller
        if controllers is not None:
            self.controllers = controllers
        if encryption is not None:
            self.encryption = encryption
        if exfil_location is not None:
            self.exfil_location = exfil_location
        if file is not None:
            self.file = file
        if inject_type is not None:
            self.inject_type = inject_type
        if location is not None:
            self.location = location
        if parameters is not None:
            self.parameters = parameters
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_type is not None:
            self.plugin_type = plugin_type
        if recipient_domains is not None:
            self.recipient_domains = recipient_domains
        if senders is not None:
            self.senders = senders
        if settings is not None:
            self.settings = settings
        if target_type is not None:
            self.target_type = target_type
        if triggers is not None:
            self.triggers = triggers

    @property
    def attack_targets(self):
        """Gets the attack_targets of this EventSchemaDataEventData.  # noqa: E501


        :return: The attack_targets of this EventSchemaDataEventData.  # noqa: E501
        :rtype: list[object]
        """
        return self._attack_targets

    @attack_targets.setter
    def attack_targets(self, attack_targets):
        """Sets the attack_targets of this EventSchemaDataEventData.


        :param attack_targets: The attack_targets of this EventSchemaDataEventData.  # noqa: E501
        :type attack_targets: list[object]
        """

        self._attack_targets = attack_targets

    @property
    def attack_type(self):
        """Gets the attack_type of this EventSchemaDataEventData.  # noqa: E501


        :return: The attack_type of this EventSchemaDataEventData.  # noqa: E501
        :rtype: str
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        """Sets the attack_type of this EventSchemaDataEventData.


        :param attack_type: The attack_type of this EventSchemaDataEventData.  # noqa: E501
        :type attack_type: str
        """

        self._attack_type = attack_type

    @property
    def bot_settings(self):
        """Gets the bot_settings of this EventSchemaDataEventData.  # noqa: E501

        An object containing varying data types showing malware bot settings data. Contains any of but not limited the following fields: `exit_country`, `config`, `encryption`.  # noqa: E501

        :return: The bot_settings of this EventSchemaDataEventData.  # noqa: E501
        :rtype: object
        """
        return self._bot_settings

    @bot_settings.setter
    def bot_settings(self, bot_settings):
        """Sets the bot_settings of this EventSchemaDataEventData.

        An object containing varying data types showing malware bot settings data. Contains any of but not limited the following fields: `exit_country`, `config`, `encryption`.  # noqa: E501

        :param bot_settings: The bot_settings of this EventSchemaDataEventData.  # noqa: E501
        :type bot_settings: object
        """

        self._bot_settings = bot_settings

    @property
    def command(self):
        """Gets the command of this EventSchemaDataEventData.  # noqa: E501

        Command.  # noqa: E501

        :return: The command of this EventSchemaDataEventData.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this EventSchemaDataEventData.

        Command.  # noqa: E501

        :param command: The command of this EventSchemaDataEventData.  # noqa: E501
        :type command: str
        """

        self._command = command

    @property
    def component_type(self):
        """Gets the component_type of this EventSchemaDataEventData.  # noqa: E501

        Type of component i.e. `CORE`.  # noqa: E501

        :return: The component_type of this EventSchemaDataEventData.  # noqa: E501
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this EventSchemaDataEventData.

        Type of component i.e. `CORE`.  # noqa: E501

        :param component_type: The component_type of this EventSchemaDataEventData.  # noqa: E501
        :type component_type: str
        """

        self._component_type = component_type

    @property
    def config_file(self):
        """Gets the config_file of this EventSchemaDataEventData.  # noqa: E501

        Config file.  # noqa: E501

        :return: The config_file of this EventSchemaDataEventData.  # noqa: E501
        :rtype: str
        """
        return self._config_file

    @config_file.setter
    def config_file(self, config_file):
        """Sets the config_file of this EventSchemaDataEventData.

        Config file.  # noqa: E501

        :param config_file: The config_file of this EventSchemaDataEventData.  # noqa: E501
        :type config_file: str
        """

        self._config_file = config_file

    @property
    def controller(self):
        """Gets the controller of this EventSchemaDataEventData.  # noqa: E501


        :return: The controller of this EventSchemaDataEventData.  # noqa: E501
        :rtype: EventSchemaDataEventDataController
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Sets the controller of this EventSchemaDataEventData.


        :param controller: The controller of this EventSchemaDataEventData.  # noqa: E501
        :type controller: EventSchemaDataEventDataController
        """

        self._controller = controller

    @property
    def controllers(self):
        """Gets the controllers of this EventSchemaDataEventData.  # noqa: E501

        An array of objects, each containing an individual controller's url.  # noqa: E501

        :return: The controllers of this EventSchemaDataEventData.  # noqa: E501
        :rtype: list[EventSchemaDataEventDataControllersInner]
        """
        return self._controllers

    @controllers.setter
    def controllers(self, controllers):
        """Sets the controllers of this EventSchemaDataEventData.

        An array of objects, each containing an individual controller's url.  # noqa: E501

        :param controllers: The controllers of this EventSchemaDataEventData.  # noqa: E501
        :type controllers: list[EventSchemaDataEventDataControllersInner]
        """

        self._controllers = controllers

    @property
    def encryption(self):
        """Gets the encryption of this EventSchemaDataEventData.  # noqa: E501

        An array of `encryption` meta data.  # noqa: E501

        :return: The encryption of this EventSchemaDataEventData.  # noqa: E501
        :rtype: list[EventSchemaDataEventDataEncryptionInner]
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this EventSchemaDataEventData.

        An array of `encryption` meta data.  # noqa: E501

        :param encryption: The encryption of this EventSchemaDataEventData.  # noqa: E501
        :type encryption: list[EventSchemaDataEventDataEncryptionInner]
        """

        self._encryption = encryption

    @property
    def exfil_location(self):
        """Gets the exfil_location of this EventSchemaDataEventData.  # noqa: E501

        Contains the url location of the exfiltration event.  # noqa: E501

        :return: The exfil_location of this EventSchemaDataEventData.  # noqa: E501
        :rtype: str
        """
        return self._exfil_location

    @exfil_location.setter
    def exfil_location(self, exfil_location):
        """Sets the exfil_location of this EventSchemaDataEventData.

        Contains the url location of the exfiltration event.  # noqa: E501

        :param exfil_location: The exfil_location of this EventSchemaDataEventData.  # noqa: E501
        :type exfil_location: str
        """

        self._exfil_location = exfil_location

    @property
    def file(self):
        """Gets the file of this EventSchemaDataEventData.  # noqa: E501


        :return: The file of this EventSchemaDataEventData.  # noqa: E501
        :rtype: EventSchemaDataEventDataFile
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this EventSchemaDataEventData.


        :param file: The file of this EventSchemaDataEventData.  # noqa: E501
        :type file: EventSchemaDataEventDataFile
        """

        self._file = file

    @property
    def inject_type(self):
        """Gets the inject_type of this EventSchemaDataEventData.  # noqa: E501

        Inject type.  # noqa: E501

        :return: The inject_type of this EventSchemaDataEventData.  # noqa: E501
        :rtype: str
        """
        return self._inject_type

    @inject_type.setter
    def inject_type(self, inject_type):
        """Sets the inject_type of this EventSchemaDataEventData.

        Inject type.  # noqa: E501

        :param inject_type: The inject_type of this EventSchemaDataEventData.  # noqa: E501
        :type inject_type: str
        """

        self._inject_type = inject_type

    @property
    def location(self):
        """Gets the location of this EventSchemaDataEventData.  # noqa: E501


        :return: The location of this EventSchemaDataEventData.  # noqa: E501
        :rtype: EventSchemaDataEventDataLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EventSchemaDataEventData.


        :param location: The location of this EventSchemaDataEventData.  # noqa: E501
        :type location: EventSchemaDataEventDataLocation
        """

        self._location = location

    @property
    def parameters(self):
        """Gets the parameters of this EventSchemaDataEventData.  # noqa: E501


        :return: The parameters of this EventSchemaDataEventData.  # noqa: E501
        :rtype: list[object]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this EventSchemaDataEventData.


        :param parameters: The parameters of this EventSchemaDataEventData.  # noqa: E501
        :type parameters: list[object]
        """

        self._parameters = parameters

    @property
    def plugin_name(self):
        """Gets the plugin_name of this EventSchemaDataEventData.  # noqa: E501

        Plugin's name.  # noqa: E501

        :return: The plugin_name of this EventSchemaDataEventData.  # noqa: E501
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this EventSchemaDataEventData.

        Plugin's name.  # noqa: E501

        :param plugin_name: The plugin_name of this EventSchemaDataEventData.  # noqa: E501
        :type plugin_name: str
        """

        self._plugin_name = plugin_name

    @property
    def plugin_type(self):
        """Gets the plugin_type of this EventSchemaDataEventData.  # noqa: E501

        Type of plugin. i.e. `REMOTE_ACCESS`, `CREDENTIAL_STEALER`, `OTHER`.  # noqa: E501

        :return: The plugin_type of this EventSchemaDataEventData.  # noqa: E501
        :rtype: str
        """
        return self._plugin_type

    @plugin_type.setter
    def plugin_type(self, plugin_type):
        """Sets the plugin_type of this EventSchemaDataEventData.

        Type of plugin. i.e. `REMOTE_ACCESS`, `CREDENTIAL_STEALER`, `OTHER`.  # noqa: E501

        :param plugin_type: The plugin_type of this EventSchemaDataEventData.  # noqa: E501
        :type plugin_type: str
        """

        self._plugin_type = plugin_type

    @property
    def recipient_domains(self):
        """Gets the recipient_domains of this EventSchemaDataEventData.  # noqa: E501

        Recipient domains.  # noqa: E501

        :return: The recipient_domains of this EventSchemaDataEventData.  # noqa: E501
        :rtype: list[EventSchemaDataEventDataRecipientDomainsInner]
        """
        return self._recipient_domains

    @recipient_domains.setter
    def recipient_domains(self, recipient_domains):
        """Sets the recipient_domains of this EventSchemaDataEventData.

        Recipient domains.  # noqa: E501

        :param recipient_domains: The recipient_domains of this EventSchemaDataEventData.  # noqa: E501
        :type recipient_domains: list[EventSchemaDataEventDataRecipientDomainsInner]
        """

        self._recipient_domains = recipient_domains

    @property
    def senders(self):
        """Gets the senders of this EventSchemaDataEventData.  # noqa: E501

        Senders.  # noqa: E501

        :return: The senders of this EventSchemaDataEventData.  # noqa: E501
        :rtype: list[str]
        """
        return self._senders

    @senders.setter
    def senders(self, senders):
        """Sets the senders of this EventSchemaDataEventData.

        Senders.  # noqa: E501

        :param senders: The senders of this EventSchemaDataEventData.  # noqa: E501
        :type senders: list[str]
        """

        self._senders = senders

    @property
    def settings(self):
        """Gets the settings of this EventSchemaDataEventData.  # noqa: E501

        An array of event related `settings` objects containing any of but not limited the following fields: `plugin_location`, `bot_version`, `compaign_id`, etc.  # noqa: E501

        :return: The settings of this EventSchemaDataEventData.  # noqa: E501
        :rtype: list[object]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this EventSchemaDataEventData.

        An array of event related `settings` objects containing any of but not limited the following fields: `plugin_location`, `bot_version`, `compaign_id`, etc.  # noqa: E501

        :param settings: The settings of this EventSchemaDataEventData.  # noqa: E501
        :type settings: list[object]
        """

        self._settings = settings

    @property
    def target_type(self):
        """Gets the target_type of this EventSchemaDataEventData.  # noqa: E501

        Type of target.  # noqa: E501

        :return: The target_type of this EventSchemaDataEventData.  # noqa: E501
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this EventSchemaDataEventData.

        Type of target.  # noqa: E501

        :param target_type: The target_type of this EventSchemaDataEventData.  # noqa: E501
        :type target_type: str
        """

        self._target_type = target_type

    @property
    def triggers(self):
        """Gets the triggers of this EventSchemaDataEventData.  # noqa: E501

        An array of objects, each containing the field `trigger`.  # noqa: E501

        :return: The triggers of this EventSchemaDataEventData.  # noqa: E501
        :rtype: list[EventSchemaDataEventDataTriggersInner]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this EventSchemaDataEventData.

        An array of objects, each containing the field `trigger`.  # noqa: E501

        :param triggers: The triggers of this EventSchemaDataEventData.  # noqa: E501
        :type triggers: list[EventSchemaDataEventDataTriggersInner]
        """

        self._triggers = triggers

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
        if not isinstance(other, EventSchemaDataEventData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventSchemaDataEventData):
            return True

        return self.to_dict() != other.to_dict()
