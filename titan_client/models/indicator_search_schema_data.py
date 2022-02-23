# coding: utf-8

"""
    Titan API v1

    # Introduction The Intel 471 API is organized around the principles of REST. Our API lets you gather results from our platform with anything that can send a HTTP request, including cURL and modern internet browsers. Access to this API requires an API token which is managed from your account settings.  Intel 471 reserves the right to add fields to our API however we will provide backwards compatibility and older version support so that it will be possible to choose exact versions that provide a response with an older structure. This documentation tracks all API versions and it is possible to compare this version which has changes highlighted. Please consider not storing information provided by API locally as we constantly improving our data set and want you to have the most updated information.  # Authentication Authenticate to the Intel 471 API by providing your API key in the request. Your API key carries many privileges so please do not expose them on public web resources.  Authentication to the API occurs by providing your email address as the login and API key as password in the authorization header via HTTP Basic Auth. Your API key can be found in the [API](https://portal.intel471.com/api) section on the portal.  # Accessing API ## Via internet browser Just open url: `https://api.intel471.com/v1/reports` Browser will ask for credentials, provide your email as login and API key as password. ## Via curl command line utility Type in terminal the following command: ``` curl -u <YOU EMAIL>:<YOUR API KEY> https://api.intel471.com/v1/reports ``` ## CURL usage examples This section covers some Watchers API requests.  ### List watcher groups: Type in terminal the following command:  *curl -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  ### Create watcher group: To create watcher group you need to pass a json body to request. Passing json body possible in two ways:  #### Write json to request *curl -d'{\"name\": \"group_name\", \"description\": \"Description\"}' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  #### Write json to file and call it *curl -d\"@json_file_name\" -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  ### Create free text search watcher: *curl -d'{\"type\": \"search\", \"freeTextPattern\": \"text to search\", \"notificationChannel\": \"website\"}' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups/\"GROUP UID\"/watchers*  ### Create specific search watcher: *curl -d'{\"type\": \"search\", \"patterns\":[ { \"types\": \"Actor\" , \"pattern\": \"swisman\" } ], \"notificationChannel\": \"website\" }' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups/\"GROUP UID\"/watchers*  ## Via Python Execute the following script: ``` import urllib2, base64  username = \"<YOU EMAIL>\" apikey = \"<YOUR API KEY>\"  request = urllib2.Request(\"https://api.intel471.com/v1/reports\") base64string = base64.encodestring('%s:%s' % (username, apikey)).replace('\\n', '') request.add_header(\"Authorization\", \"Basic %s\" % base64string) result = urllib2.urlopen(request) response_in_json = result.read()  print response_in_json ``` # API integration best practice with your application When accessing our API from your application don't do AJAX calls directly from web browser to https://api.intel471.com/. We do not allow CORS requests from browser due to potential security issues. Instead we suggest you look to establish a kind of a server side proxy in your application which will pass requests to our API.  For example: you can send a request from browser javascript to your server side, for instance to url `/apiproxy/actors?actor=hacker` which will be internally passed to `https://api.intel471.com/v1/actors?actor=hacker` (with authentication headers added) and response will be sent back to the browser.  # Versioning support We are consistently improving our API and occasionally bring in changes to the API based on customer feedback. The current API version can be seen in the drop down boxes for each version. We are providing API backwards compatibility when possible. All requests are prefixed with the major version number, for example `/v1`: ``` https://api.intel471.com/v1/reports ```  Different major versions are not compatible and imply significant response structure changes. Minor versions differences might include extra fields in response or provide new request parameter support. To stick to the specific version, just add the following extra parameter to the request, for example: `?v=1.2.0`. If you specify a not existing version, it will be brought down to the nearest existing one. For example, parameter `?v=1.5.4` will call API of version 1.3.0 — the latest available; `?v=1.2.9` will awake version 1.2.0 and so on.  Omitting the version parameter from your request means you will always use the latest version of the API.  We highly recommend you always add the version parameter to be safe on API updates and code your integration in a way to accept possible future extra fields added to the response object. ``` https://api.intel471.com/v1/tags?prettyPrint - will return response for the latest API version (v.1.1.0) https://api.intel471.com/v1/tags?prettyPrint&v=1.1.0 - absolutely the same request with the version explicitly specified https://api.intel471.com/v1/reports?prettyPrint&v=1.0.0 - will return response compatible with the older version ```   # noqa: E501

    The version of the OpenAPI document: 1.19.0
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


class IndicatorSearchSchemaData(object):
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
        'confidence': 'str',
        'context': 'IndicatorSearchSchemaDataContext',
        'expiration': 'int',
        'indicator_data': 'IndicatorSearchSchemaDataIndicatorData',
        'indicator_type': 'str',
        'intel_requirements': 'list[str]',
        'mitre_tactics': 'str',
        'threat': 'IndicatorSearchSchemaDataThreat',
        'uid': 'str'
    }

    attribute_map = {
        'confidence': 'confidence',
        'context': 'context',
        'expiration': 'expiration',
        'indicator_data': 'indicator_data',
        'indicator_type': 'indicator_type',
        'intel_requirements': 'intel_requirements',
        'mitre_tactics': 'mitre_tactics',
        'threat': 'threat',
        'uid': 'uid'
    }

    def __init__(self, confidence=None, context=None, expiration=None, indicator_data=None, indicator_type=None, intel_requirements=None, mitre_tactics=None, threat=None, uid=None, local_vars_configuration=None):  # noqa: E501
        """IndicatorSearchSchemaData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._confidence = None
        self._context = None
        self._expiration = None
        self._indicator_data = None
        self._indicator_type = None
        self._intel_requirements = None
        self._mitre_tactics = None
        self._threat = None
        self._uid = None
        self.discriminator = None

        self.confidence = confidence
        if context is not None:
            self.context = context
        self.expiration = expiration
        self.indicator_data = indicator_data
        self.indicator_type = indicator_type
        if intel_requirements is not None:
            self.intel_requirements = intel_requirements
        if mitre_tactics is not None:
            self.mitre_tactics = mitre_tactics
        self.threat = threat
        self.uid = uid

    @property
    def confidence(self):
        """Gets the confidence of this IndicatorSearchSchemaData.  # noqa: E501

        Indicators with `high` confidence are derived from a primary source and are verified. They can safely be used for blocking. If indicators are from a primary source, but they have not been verified, then the confidence rating is reduced to `medium`. We recommend them for alerting or threat hunting. An example of this is a controller URL extracted from a malware configuration file. The file is verified (high), but the controller URLs inside it’s configuration are not (medium). Indicators that are derived from a third party source via pivoting are marked as `low` confidence unless they have been verified. We don’t publish many low confidence indicators.  # noqa: E501

        :return: The confidence of this IndicatorSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this IndicatorSearchSchemaData.

        Indicators with `high` confidence are derived from a primary source and are verified. They can safely be used for blocking. If indicators are from a primary source, but they have not been verified, then the confidence rating is reduced to `medium`. We recommend them for alerting or threat hunting. An example of this is a controller URL extracted from a malware configuration file. The file is verified (high), but the controller URLs inside it’s configuration are not (medium). Indicators that are derived from a third party source via pivoting are marked as `low` confidence unless they have been verified. We don’t publish many low confidence indicators.  # noqa: E501

        :param confidence: The confidence of this IndicatorSearchSchemaData.  # noqa: E501
        :type confidence: str
        """
        if self.local_vars_configuration.client_side_validation and confidence is None:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must not be `None`")  # noqa: E501

        self._confidence = confidence

    @property
    def context(self):
        """Gets the context of this IndicatorSearchSchemaData.  # noqa: E501


        :return: The context of this IndicatorSearchSchemaData.  # noqa: E501
        :rtype: IndicatorSearchSchemaDataContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this IndicatorSearchSchemaData.


        :param context: The context of this IndicatorSearchSchemaData.  # noqa: E501
        :type context: IndicatorSearchSchemaDataContext
        """

        self._context = context

    @property
    def expiration(self):
        """Gets the expiration of this IndicatorSearchSchemaData.  # noqa: E501

        Indicator should be removed from block lists at this date.  # noqa: E501

        :return: The expiration of this IndicatorSearchSchemaData.  # noqa: E501
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this IndicatorSearchSchemaData.

        Indicator should be removed from block lists at this date.  # noqa: E501

        :param expiration: The expiration of this IndicatorSearchSchemaData.  # noqa: E501
        :type expiration: int
        """
        if self.local_vars_configuration.client_side_validation and expiration is None:  # noqa: E501
            raise ValueError("Invalid value for `expiration`, must not be `None`")  # noqa: E501

        self._expiration = expiration

    @property
    def indicator_data(self):
        """Gets the indicator_data of this IndicatorSearchSchemaData.  # noqa: E501


        :return: The indicator_data of this IndicatorSearchSchemaData.  # noqa: E501
        :rtype: IndicatorSearchSchemaDataIndicatorData
        """
        return self._indicator_data

    @indicator_data.setter
    def indicator_data(self, indicator_data):
        """Sets the indicator_data of this IndicatorSearchSchemaData.


        :param indicator_data: The indicator_data of this IndicatorSearchSchemaData.  # noqa: E501
        :type indicator_data: IndicatorSearchSchemaDataIndicatorData
        """
        if self.local_vars_configuration.client_side_validation and indicator_data is None:  # noqa: E501
            raise ValueError("Invalid value for `indicator_data`, must not be `None`")  # noqa: E501

        self._indicator_data = indicator_data

    @property
    def indicator_type(self):
        """Gets the indicator_type of this IndicatorSearchSchemaData.  # noqa: E501

        Describes the type of indicator: (e.g. file, ipv4, url).  # noqa: E501

        :return: The indicator_type of this IndicatorSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._indicator_type

    @indicator_type.setter
    def indicator_type(self, indicator_type):
        """Sets the indicator_type of this IndicatorSearchSchemaData.

        Describes the type of indicator: (e.g. file, ipv4, url).  # noqa: E501

        :param indicator_type: The indicator_type of this IndicatorSearchSchemaData.  # noqa: E501
        :type indicator_type: str
        """
        if self.local_vars_configuration.client_side_validation and indicator_type is None:  # noqa: E501
            raise ValueError("Invalid value for `indicator_type`, must not be `None`")  # noqa: E501

        self._indicator_type = indicator_type

    @property
    def intel_requirements(self):
        """Gets the intel_requirements of this IndicatorSearchSchemaData.  # noqa: E501

        List of General Intelligence Requirements matching this indicator.  # noqa: E501

        :return: The intel_requirements of this IndicatorSearchSchemaData.  # noqa: E501
        :rtype: list[str]
        """
        return self._intel_requirements

    @intel_requirements.setter
    def intel_requirements(self, intel_requirements):
        """Sets the intel_requirements of this IndicatorSearchSchemaData.

        List of General Intelligence Requirements matching this indicator.  # noqa: E501

        :param intel_requirements: The intel_requirements of this IndicatorSearchSchemaData.  # noqa: E501
        :type intel_requirements: list[str]
        """

        self._intel_requirements = intel_requirements

    @property
    def mitre_tactics(self):
        """Gets the mitre_tactics of this IndicatorSearchSchemaData.  # noqa: E501

        The MITRE ATT&CK tactic classification.  # noqa: E501

        :return: The mitre_tactics of this IndicatorSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._mitre_tactics

    @mitre_tactics.setter
    def mitre_tactics(self, mitre_tactics):
        """Sets the mitre_tactics of this IndicatorSearchSchemaData.

        The MITRE ATT&CK tactic classification.  # noqa: E501

        :param mitre_tactics: The mitre_tactics of this IndicatorSearchSchemaData.  # noqa: E501
        :type mitre_tactics: str
        """

        self._mitre_tactics = mitre_tactics

    @property
    def threat(self):
        """Gets the threat of this IndicatorSearchSchemaData.  # noqa: E501


        :return: The threat of this IndicatorSearchSchemaData.  # noqa: E501
        :rtype: IndicatorSearchSchemaDataThreat
        """
        return self._threat

    @threat.setter
    def threat(self, threat):
        """Sets the threat of this IndicatorSearchSchemaData.


        :param threat: The threat of this IndicatorSearchSchemaData.  # noqa: E501
        :type threat: IndicatorSearchSchemaDataThreat
        """
        if self.local_vars_configuration.client_side_validation and threat is None:  # noqa: E501
            raise ValueError("Invalid value for `threat`, must not be `None`")  # noqa: E501

        self._threat = threat

    @property
    def uid(self):
        """Gets the uid of this IndicatorSearchSchemaData.  # noqa: E501

        Indicator's UID  # noqa: E501

        :return: The uid of this IndicatorSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this IndicatorSearchSchemaData.

        Indicator's UID  # noqa: E501

        :param uid: The uid of this IndicatorSearchSchemaData.  # noqa: E501
        :type uid: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

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

    def to_stix(self):
        return StixMapper.map(self.to_dict(serialize=True))

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IndicatorSearchSchemaData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IndicatorSearchSchemaData):
            return True

        return self.to_dict() != other.to_dict()
