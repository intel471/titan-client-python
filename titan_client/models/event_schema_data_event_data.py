# coding: utf-8

"""
    Titan API v1

    # Introduction The Intel 471 API is organized around the principles of REST. Our API lets you gather results from our platform with anything that can send a HTTP request, including cURL and modern internet browsers. Access to this API requires an API token which is managed from your account settings.  Intel 471 reserves the right to add fields to our API however we will provide backwards compatibility and older version support so that it will be possible to choose exact versions that provide a response with an older structure. This documentation tracks all API versions and it is possible to compare this version which has changes highlighted. Please consider not storing information provided by API locally as we constantly improving our data set and want you to have the most updated information.  # Authentication Authenticate to the Intel 471 API by providing your API key in the request. Your API key carries many privileges so please do not expose them on public web resources.  Authentication to the API occurs by providing your email address as the login and API key as password in the authorization header via HTTP Basic Auth. Your API key can be found in the [API](https://portal.intel471.com/api) section on the portal.  # Accessing API ## Via internet browser Just open url: `https://api.intel471.com/v1/reports` Browser will ask for credentials, provide your email as login and API key as password. ## Via curl command line utility Type in terminal the following command: ``` curl -u <YOU EMAIL>:<YOUR API KEY> https://api.intel471.com/v1/reports ``` ## CURL usage examples This section covers some Watchers API requests.  ### List watcher groups: Type in terminal the following command:  *curl -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  ### Create watcher group: To create watcher group you need to pass a json body to request. Passing json body possible in two ways:  #### Write json to request *curl -d'{\"name\": \"group_name\", \"description\": \"Description\"}' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  #### Write json to file and call it *curl -d\"@json_file_name\" -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  ### Create free text search watcher: *curl -d'{\"type\": \"search\", \"freeTextPattern\": \"text to search\", \"notificationChannel\": \"website\"}' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups/\"GROUP UID\"/watchers*  ### Create specific search watcher: *curl -d'{\"type\": \"search\", \"patterns\":[ { \"types\": \"Actor\" , \"pattern\": \"swisman\" } ], \"notificationChannel\": \"website\" }' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups/\"GROUP UID\"/watchers*  ## Via Python Execute the following script: ``` import urllib2, base64  username = \"<YOU EMAIL>\" apikey = \"<YOUR API KEY>\"  request = urllib2.Request(\"https://api.intel471.com/v1/reports\") base64string = base64.encodestring('%s:%s' % (username, apikey)).replace('\\n', '') request.add_header(\"Authorization\", \"Basic %s\" % base64string) result = urllib2.urlopen(request) response_in_json = result.read()  print response_in_json ``` # API integration best practice with your application When accessing our API from your application don't do AJAX calls directly from web browser to https://api.intel471.com/. We do not allow CORS requests from browser due to potential security issues. Instead we suggest you look to establish a kind of a server side proxy in your application which will pass requests to our API.  For example: you can send a request from browser javascript to your server side, for instance to url `/apiproxy/actors?actor=hacker` which will be internally passed to `https://api.intel471.com/v1/actors?actor=hacker` (with authentication headers added) and response will be sent back to the browser.  # Versioning support We are consistently improving our API and occasionally bring in changes to the API based on customer feedback. The current API version can be seen in the drop down boxes for each version. We are providing API backwards compatibility when possible. All requests are prefixed with the major version number, for example `/v1`: ``` https://api.intel471.com/v1/reports ```  Different major versions are not compatible and imply significant response structure changes. Minor versions differences might include extra fields in response or provide new request parameter support. To stick to the specific version, just add the following extra parameter to the request, for example: `?v=1.2.0`. If you specify a not existing version, it will be brought down to the nearest existing one. For example, parameter `?v=1.5.4` will call API of version 1.3.0 — the latest available; `?v=1.2.9` will awake version 1.2.0 and so on.  Omitting the version parameter from your request means you will always use the latest version of the API.  We highly recommend you always add the version parameter to be safe on API updates and code your integration in a way to accept possible future extra fields added to the response object. ``` https://api.intel471.com/v1/tags?prettyPrint - will return response for the latest API version (v.1.1.0) https://api.intel471.com/v1/tags?prettyPrint&v=1.1.0 - absolutely the same request with the version explicitly specified https://api.intel471.com/v1/reports?prettyPrint&v=1.0.0 - will return response compatible with the older version ```   # noqa: E501

    The version of the OpenAPI document: 1.16.1
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
        'bot_settings': 'object',
        'command': 'str',
        'component_type': 'str',
        'config_file': 'str',
        'controller': 'EventSchemaDataEventDataController',
        'controllers': 'list[EventSchemaDataEventDataControllers]',
        'encryption': 'list[EventSchemaDataEventDataEncryption]',
        'exfil_location': 'str',
        'file': 'EventSchemaDataEventDataFile',
        'inject_type': 'str',
        'location': 'EventSchemaDataEventDataLocation',
        'plugin_name': 'str',
        'plugin_type': 'str',
        'recipient_domains': 'list[EventSchemaDataEventDataRecipientDomains]',
        'senders': 'list[str]',
        'settings': 'list[object]',
        'target_type': 'str',
        'triggers': 'list[EventSchemaDataEventDataTriggers]'
    }

    attribute_map = {
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
        'plugin_name': 'plugin_name',
        'plugin_type': 'plugin_type',
        'recipient_domains': 'recipient_domains',
        'senders': 'senders',
        'settings': 'settings',
        'target_type': 'target_type',
        'triggers': 'triggers'
    }

    def __init__(self, bot_settings=None, command=None, component_type=None, config_file=None, controller=None, controllers=None, encryption=None, exfil_location=None, file=None, inject_type=None, location=None, plugin_name=None, plugin_type=None, recipient_domains=None, senders=None, settings=None, target_type=None, triggers=None, local_vars_configuration=None):  # noqa: E501
        """EventSchemaDataEventData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

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
        self._plugin_name = None
        self._plugin_type = None
        self._recipient_domains = None
        self._senders = None
        self._settings = None
        self._target_type = None
        self._triggers = None
        self.discriminator = None

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
        :rtype: list[EventSchemaDataEventDataControllers]
        """
        return self._controllers

    @controllers.setter
    def controllers(self, controllers):
        """Sets the controllers of this EventSchemaDataEventData.

        An array of objects, each containing an individual controller's url.  # noqa: E501

        :param controllers: The controllers of this EventSchemaDataEventData.  # noqa: E501
        :type controllers: list[EventSchemaDataEventDataControllers]
        """

        self._controllers = controllers

    @property
    def encryption(self):
        """Gets the encryption of this EventSchemaDataEventData.  # noqa: E501

        An array of `encryption` meta data.  # noqa: E501

        :return: The encryption of this EventSchemaDataEventData.  # noqa: E501
        :rtype: list[EventSchemaDataEventDataEncryption]
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this EventSchemaDataEventData.

        An array of `encryption` meta data.  # noqa: E501

        :param encryption: The encryption of this EventSchemaDataEventData.  # noqa: E501
        :type encryption: list[EventSchemaDataEventDataEncryption]
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
        :rtype: list[EventSchemaDataEventDataRecipientDomains]
        """
        return self._recipient_domains

    @recipient_domains.setter
    def recipient_domains(self, recipient_domains):
        """Sets the recipient_domains of this EventSchemaDataEventData.

        Recipient domains.  # noqa: E501

        :param recipient_domains: The recipient_domains of this EventSchemaDataEventData.  # noqa: E501
        :type recipient_domains: list[EventSchemaDataEventDataRecipientDomains]
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
        :rtype: list[EventSchemaDataEventDataTriggers]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this EventSchemaDataEventData.

        An array of objects, each containing the field `trigger`.  # noqa: E501

        :param triggers: The triggers of this EventSchemaDataEventData.  # noqa: E501
        :type triggers: list[EventSchemaDataEventDataTriggers]
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
