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


class EntitiesSchema(object):
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
        'active_from': 'int',
        'active_till': 'int',
        'last_updated': 'int',
        'links': 'EntitiesSchemaLinks',
        'type': 'str',
        'uid': 'str',
        'value': 'str'
    }

    attribute_map = {
        'active_from': 'activeFrom',
        'active_till': 'activeTill',
        'last_updated': 'lastUpdated',
        'links': 'links',
        'type': 'type',
        'uid': 'uid',
        'value': 'value'
    }

    def __init__(self, active_from=None, active_till=None, last_updated=None, links=None, type=None, uid=None, value=None, local_vars_configuration=None):  # noqa: E501
        """EntitiesSchema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._active_from = None
        self._active_till = None
        self._last_updated = None
        self._links = None
        self._type = None
        self._uid = None
        self._value = None
        self.discriminator = None

        if active_from is not None:
            self.active_from = active_from
        if active_till is not None:
            self.active_till = active_till
        if last_updated is not None:
            self.last_updated = last_updated
        self.links = links
        self.type = type
        self.uid = uid
        self.value = value

    @property
    def active_from(self):
        """Gets the active_from of this EntitiesSchema.  # noqa: E501

        Date first seen.  # noqa: E501

        :return: The active_from of this EntitiesSchema.  # noqa: E501
        :rtype: int
        """
        return self._active_from

    @active_from.setter
    def active_from(self, active_from):
        """Sets the active_from of this EntitiesSchema.

        Date first seen.  # noqa: E501

        :param active_from: The active_from of this EntitiesSchema.  # noqa: E501
        :type active_from: int
        """

        self._active_from = active_from

    @property
    def active_till(self):
        """Gets the active_till of this EntitiesSchema.  # noqa: E501

        Date last seen.  # noqa: E501

        :return: The active_till of this EntitiesSchema.  # noqa: E501
        :rtype: int
        """
        return self._active_till

    @active_till.setter
    def active_till(self, active_till):
        """Sets the active_till of this EntitiesSchema.

        Date last seen.  # noqa: E501

        :param active_till: The active_till of this EntitiesSchema.  # noqa: E501
        :type active_till: int
        """

        self._active_till = active_till

    @property
    def last_updated(self):
        """Gets the last_updated of this EntitiesSchema.  # noqa: E501

        Last modification date.  # noqa: E501

        :return: The last_updated of this EntitiesSchema.  # noqa: E501
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this EntitiesSchema.

        Last modification date.  # noqa: E501

        :param last_updated: The last_updated of this EntitiesSchema.  # noqa: E501
        :type last_updated: int
        """

        self._last_updated = last_updated

    @property
    def links(self):
        """Gets the links of this EntitiesSchema.  # noqa: E501


        :return: The links of this EntitiesSchema.  # noqa: E501
        :rtype: EntitiesSchemaLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this EntitiesSchema.


        :param links: The links of this EntitiesSchema.  # noqa: E501
        :type links: EntitiesSchemaLinks
        """
        if self.local_vars_configuration.client_side_validation and links is None:  # noqa: E501
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def type(self):
        """Gets the type of this EntitiesSchema.  # noqa: E501

        Entity `type`.  # noqa: E501

        :return: The type of this EntitiesSchema.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntitiesSchema.

        Entity `type`.  # noqa: E501

        :param type: The type of this EntitiesSchema.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this EntitiesSchema.  # noqa: E501

        Unique entity identifier.  # noqa: E501

        :return: The uid of this EntitiesSchema.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this EntitiesSchema.

        Unique entity identifier.  # noqa: E501

        :param uid: The uid of this EntitiesSchema.  # noqa: E501
        :type uid: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def value(self):
        """Gets the value of this EntitiesSchema.  # noqa: E501

        Entity `value`.  # noqa: E501

        :return: The value of this EntitiesSchema.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EntitiesSchema.

        Entity `value`.  # noqa: E501

        :param value: The value of this EntitiesSchema.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, EntitiesSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntitiesSchema):
            return True

        return self.to_dict() != other.to_dict()
