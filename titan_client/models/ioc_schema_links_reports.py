# coding: utf-8

"""
    Titan API v1

    # Introduction The Intel 471 API is organized around the principles of REST. Our API lets you gather results from our platform with anything that can send a HTTP request, including cURL and modern internet browsers. Access to this API requires an API token which is managed from your account settings.  Intel 471 reserves the right to add fields to our API however we will provide backwards compatibility and older version support so that it will be possible to choose exact versions that provide a response with an older structure. This documentation tracks all API versions and it is possible to compare this version which has changes highlighted. Please consider not storing information provided by API locally as we constantly improving our data set and want you to have the most updated information.  # Authentication Authenticate to the Intel 471 API by providing your API key in the request. Your API key carries many privileges so please do not expose them on public web resources.  Authentication to the API occurs by providing your email address as the login and API key as password in the authorization header via HTTP Basic Auth. Your API key can be found in the [API](https://portal.intel471.com/api) section on the portal.  # Accessing API ## Via internet browser Just open url: `https://api.intel471.com/v1/reports` Browser will ask for credentials, provide your email as login and API key as password. ## Via curl command line utility Type in terminal the following command: ``` curl -u <YOU EMAIL>:<YOUR API KEY> https://api.intel471.com/v1/reports ``` ## CURL usage examples This section covers some Watchers API requests.  ### List watcher groups: Type in terminal the following command:  *curl -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  ### Create watcher group: To create watcher group you need to pass a json body to request. Passing json body possible in two ways:  #### Write json to request *curl -d'{\"name\": \"group_name\", \"description\": \"Description\"}' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  #### Write json to file and call it *curl -d\"@json_file_name\" -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups*  ### Create free text search watcher: *curl -d'{\"type\": \"search\", \"freeTextPattern\": \"text to search\", \"notificationChannel\": \"website\"}' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups/\"GROUP UID\"/watchers*  ### Create specific search watcher: *curl -d'{\"type\": \"search\", \"patterns\":[ { \"types\": \"Actor\" , \"pattern\": \"swisman\" } ], \"notificationChannel\": \"website\" }' -X POST -u \"YOUR EMAIL\":\"YOUR API KEY\" https://api.intel471.com/v1/watcherGroups/\"GROUP UID\"/watchers*  ## Via Python Execute the following script: ``` import urllib2, base64  username = \"<YOU EMAIL>\" apikey = \"<YOUR API KEY>\"  request = urllib2.Request(\"https://api.intel471.com/v1/reports\") base64string = base64.encodestring('%s:%s' % (username, apikey)).replace('\\n', '') request.add_header(\"Authorization\", \"Basic %s\" % base64string) result = urllib2.urlopen(request) response_in_json = result.read()  print response_in_json ``` # API integration best practice with your application When accessing our API from your application don't do AJAX calls directly from web browser to https://api.intel471.com/. We do not allow CORS requests from browser due to potential security issues. Instead we suggest you look to establish a kind of a server side proxy in your application which will pass requests to our API.  For example: you can send a request from browser javascript to your server side, for instance to url `/apiproxy/actors?actor=hacker` which will be internally passed to `https://api.intel471.com/v1/actors?actor=hacker` (with authentication headers added) and response will be sent back to the browser.  # Versioning support We are consistently improving our API and occasionally bring in changes to the API based on customer feedback. The current API version can be seen in the drop down boxes for each version. We are providing API backwards compatibility when possible. All requests are prefixed with the major version number, for example `/v1`: ``` https://api.intel471.com/v1/reports ```  Different major versions are not compatible and imply significant response structure changes. Minor versions differences might include extra fields in response or provide new request parameter support. To stick to the specific version, just add the following extra parameter to the request, for example: `?v=1.2.0`. If you specify a not existing version, it will be brought down to the nearest existing one. For example, parameter `?v=1.5.4` will call API of version 1.3.0 ??? the latest available; `?v=1.2.9` will awake version 1.2.0 and so on.  Omitting the version parameter from your request means you will always use the latest version of the API.  We highly recommend you always add the version parameter to be safe on API updates and code your integration in a way to accept possible future extra fields added to the response object. ``` https://api.intel471.com/v1/tags?prettyPrint - will return response for the latest API version (v.1.1.0) https://api.intel471.com/v1/tags?prettyPrint&v=1.1.0 - absolutely the same request with the version explicitly specified https://api.intel471.com/v1/reports?prettyPrint&v=1.0.0 - will return response compatible with the older version ```   # noqa: E501

    The version of the OpenAPI document: 1.19.2
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


class IocSchemaLinksReports(object):
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
        'admiralty_code': 'str',
        'date_of_information': 'int',
        'motivation': 'list[str]',
        'portal_report_url': 'str',
        'released': 'int',
        'source_characterization': 'str',
        'subject': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'admiralty_code': 'admiraltyCode',
        'date_of_information': 'dateOfInformation',
        'motivation': 'motivation',
        'portal_report_url': 'portalReportUrl',
        'released': 'released',
        'source_characterization': 'sourceCharacterization',
        'subject': 'subject',
        'uid': 'uid'
    }

    def __init__(self, admiralty_code=None, date_of_information=None, motivation=None, portal_report_url=None, released=None, source_characterization=None, subject=None, uid=None, local_vars_configuration=None):  # noqa: E501
        """IocSchemaLinksReports - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._admiralty_code = None
        self._date_of_information = None
        self._motivation = None
        self._portal_report_url = None
        self._released = None
        self._source_characterization = None
        self._subject = None
        self._uid = None
        self.discriminator = None

        if admiralty_code is not None:
            self.admiralty_code = admiralty_code
        if date_of_information is not None:
            self.date_of_information = date_of_information
        if motivation is not None:
            self.motivation = motivation
        self.portal_report_url = portal_report_url
        self.released = released
        if source_characterization is not None:
            self.source_characterization = source_characterization
        self.subject = subject
        self.uid = uid

    @property
    def admiralty_code(self):
        """Gets the admiralty_code of this IocSchemaLinksReports.  # noqa: E501

        Code as described [here](http://en.wikipedia.org/wiki/Admiralty_code). All Fintel reports have admiraltyCode=`A1`.  # noqa: E501

        :return: The admiralty_code of this IocSchemaLinksReports.  # noqa: E501
        :rtype: str
        """
        return self._admiralty_code

    @admiralty_code.setter
    def admiralty_code(self, admiralty_code):
        """Sets the admiralty_code of this IocSchemaLinksReports.

        Code as described [here](http://en.wikipedia.org/wiki/Admiralty_code). All Fintel reports have admiraltyCode=`A1`.  # noqa: E501

        :param admiralty_code: The admiralty_code of this IocSchemaLinksReports.  # noqa: E501
        :type admiralty_code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                admiralty_code is not None and not re.search(r'^[A-F][1-6]$', admiralty_code)):  # noqa: E501
            raise ValueError(r"Invalid value for `admiralty_code`, must be a follow pattern or equal to `/^[A-F][1-6]$/`")  # noqa: E501

        self._admiralty_code = admiralty_code

    @property
    def date_of_information(self):
        """Gets the date_of_information of this IocSchemaLinksReports.  # noqa: E501

        Date of information as Epoch Time.  # noqa: E501

        :return: The date_of_information of this IocSchemaLinksReports.  # noqa: E501
        :rtype: int
        """
        return self._date_of_information

    @date_of_information.setter
    def date_of_information(self, date_of_information):
        """Sets the date_of_information of this IocSchemaLinksReports.

        Date of information as Epoch Time.  # noqa: E501

        :param date_of_information: The date_of_information of this IocSchemaLinksReports.  # noqa: E501
        :type date_of_information: int
        """

        self._date_of_information = date_of_information

    @property
    def motivation(self):
        """Gets the motivation of this IocSchemaLinksReports.  # noqa: E501

        Actor's `motivation`. `CC` for Cyber Crime, `CE` for Cyber Espionage, `HA` for Hacktivism.  # noqa: E501

        :return: The motivation of this IocSchemaLinksReports.  # noqa: E501
        :rtype: list[str]
        """
        return self._motivation

    @motivation.setter
    def motivation(self, motivation):
        """Sets the motivation of this IocSchemaLinksReports.

        Actor's `motivation`. `CC` for Cyber Crime, `CE` for Cyber Espionage, `HA` for Hacktivism.  # noqa: E501

        :param motivation: The motivation of this IocSchemaLinksReports.  # noqa: E501
        :type motivation: list[str]
        """

        self._motivation = motivation

    @property
    def portal_report_url(self):
        """Gets the portal_report_url of this IocSchemaLinksReports.  # noqa: E501

        URL to the report on the portal.  # noqa: E501

        :return: The portal_report_url of this IocSchemaLinksReports.  # noqa: E501
        :rtype: str
        """
        return self._portal_report_url

    @portal_report_url.setter
    def portal_report_url(self, portal_report_url):
        """Sets the portal_report_url of this IocSchemaLinksReports.

        URL to the report on the portal.  # noqa: E501

        :param portal_report_url: The portal_report_url of this IocSchemaLinksReports.  # noqa: E501
        :type portal_report_url: str
        """
        if self.local_vars_configuration.client_side_validation and portal_report_url is None:  # noqa: E501
            raise ValueError("Invalid value for `portal_report_url`, must not be `None`")  # noqa: E501

        self._portal_report_url = portal_report_url

    @property
    def released(self):
        """Gets the released of this IocSchemaLinksReports.  # noqa: E501

        Date of report was `released`.  # noqa: E501

        :return: The released of this IocSchemaLinksReports.  # noqa: E501
        :rtype: int
        """
        return self._released

    @released.setter
    def released(self, released):
        """Sets the released of this IocSchemaLinksReports.

        Date of report was `released`.  # noqa: E501

        :param released: The released of this IocSchemaLinksReports.  # noqa: E501
        :type released: int
        """
        if self.local_vars_configuration.client_side_validation and released is None:  # noqa: E501
            raise ValueError("Invalid value for `released`, must not be `None`")  # noqa: E501

        self._released = released

    @property
    def source_characterization(self):
        """Gets the source_characterization of this IocSchemaLinksReports.  # noqa: E501

        Source characterization.  # noqa: E501

        :return: The source_characterization of this IocSchemaLinksReports.  # noqa: E501
        :rtype: str
        """
        return self._source_characterization

    @source_characterization.setter
    def source_characterization(self, source_characterization):
        """Sets the source_characterization of this IocSchemaLinksReports.

        Source characterization.  # noqa: E501

        :param source_characterization: The source_characterization of this IocSchemaLinksReports.  # noqa: E501
        :type source_characterization: str
        """

        self._source_characterization = source_characterization

    @property
    def subject(self):
        """Gets the subject of this IocSchemaLinksReports.  # noqa: E501

        Report's `subject`.  # noqa: E501

        :return: The subject of this IocSchemaLinksReports.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this IocSchemaLinksReports.

        Report's `subject`.  # noqa: E501

        :param subject: The subject of this IocSchemaLinksReports.  # noqa: E501
        :type subject: str
        """
        if self.local_vars_configuration.client_side_validation and subject is None:  # noqa: E501
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def uid(self):
        """Gets the uid of this IocSchemaLinksReports.  # noqa: E501

        Unique report identifier.  # noqa: E501

        :return: The uid of this IocSchemaLinksReports.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this IocSchemaLinksReports.

        Unique report identifier.  # noqa: E501

        :param uid: The uid of this IocSchemaLinksReports.  # noqa: E501
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
        if not isinstance(other, IocSchemaLinksReports):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IocSchemaLinksReports):
            return True

        return self.to_dict() != other.to_dict()
