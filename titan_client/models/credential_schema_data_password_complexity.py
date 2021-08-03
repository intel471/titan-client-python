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


class CredentialSchemaDataPasswordComplexity(object):
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
        'entropy': 'float',
        'length': 'int',
        'lowercase': 'int',
        'numbers': 'int',
        'other': 'int',
        'punctuation_marks': 'int',
        'score': 'float',
        'separators': 'int',
        'symbols': 'int',
        'uppercase': 'int',
        'weakness': 'float'
    }

    attribute_map = {
        'entropy': 'entropy',
        'length': 'length',
        'lowercase': 'lowercase',
        'numbers': 'numbers',
        'other': 'other',
        'punctuation_marks': 'punctuation_marks',
        'score': 'score',
        'separators': 'separators',
        'symbols': 'symbols',
        'uppercase': 'uppercase',
        'weakness': 'weakness'
    }

    def __init__(self, entropy=None, length=None, lowercase=None, numbers=None, other=None, punctuation_marks=None, score=None, separators=None, symbols=None, uppercase=None, weakness=None, local_vars_configuration=None):  # noqa: E501
        """CredentialSchemaDataPasswordComplexity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._entropy = None
        self._length = None
        self._lowercase = None
        self._numbers = None
        self._other = None
        self._punctuation_marks = None
        self._score = None
        self._separators = None
        self._symbols = None
        self._uppercase = None
        self._weakness = None
        self.discriminator = None

        if entropy is not None:
            self.entropy = entropy
        if length is not None:
            self.length = length
        if lowercase is not None:
            self.lowercase = lowercase
        if numbers is not None:
            self.numbers = numbers
        if other is not None:
            self.other = other
        if punctuation_marks is not None:
            self.punctuation_marks = punctuation_marks
        if score is not None:
            self.score = score
        if separators is not None:
            self.separators = separators
        if symbols is not None:
            self.symbols = symbols
        if uppercase is not None:
            self.uppercase = uppercase
        if weakness is not None:
            self.weakness = weakness

    @property
    def entropy(self):
        """Gets the entropy of this CredentialSchemaDataPasswordComplexity.  # noqa: E501

        The password entropy.  # noqa: E501

        :return: The entropy of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :rtype: float
        """
        return self._entropy

    @entropy.setter
    def entropy(self, entropy):
        """Sets the entropy of this CredentialSchemaDataPasswordComplexity.

        The password entropy.  # noqa: E501

        :param entropy: The entropy of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :type entropy: float
        """

        self._entropy = entropy

    @property
    def length(self):
        """Gets the length of this CredentialSchemaDataPasswordComplexity.  # noqa: E501

        The length of the password.  # noqa: E501

        :return: The length of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this CredentialSchemaDataPasswordComplexity.

        The length of the password.  # noqa: E501

        :param length: The length of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :type length: int
        """

        self._length = length

    @property
    def lowercase(self):
        """Gets the lowercase of this CredentialSchemaDataPasswordComplexity.  # noqa: E501

        The number of lowercase letters in the password.  # noqa: E501

        :return: The lowercase of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :rtype: int
        """
        return self._lowercase

    @lowercase.setter
    def lowercase(self, lowercase):
        """Sets the lowercase of this CredentialSchemaDataPasswordComplexity.

        The number of lowercase letters in the password.  # noqa: E501

        :param lowercase: The lowercase of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :type lowercase: int
        """

        self._lowercase = lowercase

    @property
    def numbers(self):
        """Gets the numbers of this CredentialSchemaDataPasswordComplexity.  # noqa: E501

        The number of digits in the password.  # noqa: E501

        :return: The numbers of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :rtype: int
        """
        return self._numbers

    @numbers.setter
    def numbers(self, numbers):
        """Sets the numbers of this CredentialSchemaDataPasswordComplexity.

        The number of digits in the password.  # noqa: E501

        :param numbers: The numbers of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :type numbers: int
        """

        self._numbers = numbers

    @property
    def other(self):
        """Gets the other of this CredentialSchemaDataPasswordComplexity.  # noqa: E501

        The number of other characters in the password.  # noqa: E501

        :return: The other of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :rtype: int
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this CredentialSchemaDataPasswordComplexity.

        The number of other characters in the password.  # noqa: E501

        :param other: The other of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :type other: int
        """

        self._other = other

    @property
    def punctuation_marks(self):
        """Gets the punctuation_marks of this CredentialSchemaDataPasswordComplexity.  # noqa: E501

        The number of punctuation marks in the password.  # noqa: E501

        :return: The punctuation_marks of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :rtype: int
        """
        return self._punctuation_marks

    @punctuation_marks.setter
    def punctuation_marks(self, punctuation_marks):
        """Sets the punctuation_marks of this CredentialSchemaDataPasswordComplexity.

        The number of punctuation marks in the password.  # noqa: E501

        :param punctuation_marks: The punctuation_marks of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :type punctuation_marks: int
        """

        self._punctuation_marks = punctuation_marks

    @property
    def score(self):
        """Gets the score of this CredentialSchemaDataPasswordComplexity.  # noqa: E501

        The password score.  # noqa: E501

        :return: The score of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this CredentialSchemaDataPasswordComplexity.

        The password score.  # noqa: E501

        :param score: The score of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :type score: float
        """

        self._score = score

    @property
    def separators(self):
        """Gets the separators of this CredentialSchemaDataPasswordComplexity.  # noqa: E501

        The number of separators in the password.  # noqa: E501

        :return: The separators of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :rtype: int
        """
        return self._separators

    @separators.setter
    def separators(self, separators):
        """Sets the separators of this CredentialSchemaDataPasswordComplexity.

        The number of separators in the password.  # noqa: E501

        :param separators: The separators of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :type separators: int
        """

        self._separators = separators

    @property
    def symbols(self):
        """Gets the symbols of this CredentialSchemaDataPasswordComplexity.  # noqa: E501

        The number of symbols in the password.  # noqa: E501

        :return: The symbols of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :rtype: int
        """
        return self._symbols

    @symbols.setter
    def symbols(self, symbols):
        """Sets the symbols of this CredentialSchemaDataPasswordComplexity.

        The number of symbols in the password.  # noqa: E501

        :param symbols: The symbols of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :type symbols: int
        """

        self._symbols = symbols

    @property
    def uppercase(self):
        """Gets the uppercase of this CredentialSchemaDataPasswordComplexity.  # noqa: E501

        The number of uppercase characters in the password.  # noqa: E501

        :return: The uppercase of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :rtype: int
        """
        return self._uppercase

    @uppercase.setter
    def uppercase(self, uppercase):
        """Sets the uppercase of this CredentialSchemaDataPasswordComplexity.

        The number of uppercase characters in the password.  # noqa: E501

        :param uppercase: The uppercase of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :type uppercase: int
        """

        self._uppercase = uppercase

    @property
    def weakness(self):
        """Gets the weakness of this CredentialSchemaDataPasswordComplexity.  # noqa: E501

        The password weakness.  # noqa: E501

        :return: The weakness of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :rtype: float
        """
        return self._weakness

    @weakness.setter
    def weakness(self, weakness):
        """Sets the weakness of this CredentialSchemaDataPasswordComplexity.

        The password weakness.  # noqa: E501

        :param weakness: The weakness of this CredentialSchemaDataPasswordComplexity.  # noqa: E501
        :type weakness: float
        """

        self._weakness = weakness

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
        if not isinstance(other, CredentialSchemaDataPasswordComplexity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CredentialSchemaDataPasswordComplexity):
            return True

        return self.to_dict() != other.to_dict()
