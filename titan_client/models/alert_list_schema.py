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


class AlertListSchema(object):
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
        'actor': 'SimpleActorSchema',
        'breach_alert': 'SimpleBreachAlertSchema',
        'credential': 'CredentialSchema',
        'credential_occurrence': 'CredentialOccurrenceSchema',
        'credential_set': 'CredentialSetSchema',
        'cve_report': 'SimpleCveSchema',
        'entity': 'EntitiesSchema',
        'event': 'EventSchema',
        'found_time': 'int',
        'highlights': 'list[AlertListSchemaHighlights]',
        'indicator': 'IndicatorSearchSchema',
        'instant_message': 'InstantMessageSchema',
        'post': 'PostSchema',
        'private_message': 'PrivateMessageSchema',
        'report': 'AlertListSchemaReport',
        'status': 'str',
        'uid': 'str',
        'watcher_group_uid': 'str',
        'watcher_uid': 'str'
    }

    attribute_map = {
        'actor': 'actor',
        'breach_alert': 'breach_alert',
        'credential': 'credential',
        'credential_occurrence': 'credential_occurrence',
        'credential_set': 'credential_set',
        'cve_report': 'cveReport',
        'entity': 'entity',
        'event': 'event',
        'found_time': 'foundTime',
        'highlights': 'highlights',
        'indicator': 'indicator',
        'instant_message': 'instantMessage',
        'post': 'post',
        'private_message': 'privateMessage',
        'report': 'report',
        'status': 'status',
        'uid': 'uid',
        'watcher_group_uid': 'watcherGroupUid',
        'watcher_uid': 'watcherUid'
    }

    def __init__(self, actor=None, breach_alert=None, credential=None, credential_occurrence=None, credential_set=None, cve_report=None, entity=None, event=None, found_time=None, highlights=None, indicator=None, instant_message=None, post=None, private_message=None, report=None, status=None, uid=None, watcher_group_uid=None, watcher_uid=None, local_vars_configuration=None):  # noqa: E501
        """AlertListSchema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._actor = None
        self._breach_alert = None
        self._credential = None
        self._credential_occurrence = None
        self._credential_set = None
        self._cve_report = None
        self._entity = None
        self._event = None
        self._found_time = None
        self._highlights = None
        self._indicator = None
        self._instant_message = None
        self._post = None
        self._private_message = None
        self._report = None
        self._status = None
        self._uid = None
        self._watcher_group_uid = None
        self._watcher_uid = None
        self.discriminator = None

        if actor is not None:
            self.actor = actor
        if breach_alert is not None:
            self.breach_alert = breach_alert
        if credential is not None:
            self.credential = credential
        if credential_occurrence is not None:
            self.credential_occurrence = credential_occurrence
        if credential_set is not None:
            self.credential_set = credential_set
        if cve_report is not None:
            self.cve_report = cve_report
        if entity is not None:
            self.entity = entity
        if event is not None:
            self.event = event
        self.found_time = found_time
        if highlights is not None:
            self.highlights = highlights
        if indicator is not None:
            self.indicator = indicator
        if instant_message is not None:
            self.instant_message = instant_message
        if post is not None:
            self.post = post
        if private_message is not None:
            self.private_message = private_message
        if report is not None:
            self.report = report
        self.status = status
        self.uid = uid
        if watcher_group_uid is not None:
            self.watcher_group_uid = watcher_group_uid
        if watcher_uid is not None:
            self.watcher_uid = watcher_uid

    @property
    def actor(self):
        """Gets the actor of this AlertListSchema.  # noqa: E501


        :return: The actor of this AlertListSchema.  # noqa: E501
        :rtype: SimpleActorSchema
        """
        return self._actor

    @actor.setter
    def actor(self, actor):
        """Sets the actor of this AlertListSchema.


        :param actor: The actor of this AlertListSchema.  # noqa: E501
        :type actor: SimpleActorSchema
        """

        self._actor = actor

    @property
    def breach_alert(self):
        """Gets the breach_alert of this AlertListSchema.  # noqa: E501


        :return: The breach_alert of this AlertListSchema.  # noqa: E501
        :rtype: SimpleBreachAlertSchema
        """
        return self._breach_alert

    @breach_alert.setter
    def breach_alert(self, breach_alert):
        """Sets the breach_alert of this AlertListSchema.


        :param breach_alert: The breach_alert of this AlertListSchema.  # noqa: E501
        :type breach_alert: SimpleBreachAlertSchema
        """

        self._breach_alert = breach_alert

    @property
    def credential(self):
        """Gets the credential of this AlertListSchema.  # noqa: E501


        :return: The credential of this AlertListSchema.  # noqa: E501
        :rtype: CredentialSchema
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this AlertListSchema.


        :param credential: The credential of this AlertListSchema.  # noqa: E501
        :type credential: CredentialSchema
        """

        self._credential = credential

    @property
    def credential_occurrence(self):
        """Gets the credential_occurrence of this AlertListSchema.  # noqa: E501


        :return: The credential_occurrence of this AlertListSchema.  # noqa: E501
        :rtype: CredentialOccurrenceSchema
        """
        return self._credential_occurrence

    @credential_occurrence.setter
    def credential_occurrence(self, credential_occurrence):
        """Sets the credential_occurrence of this AlertListSchema.


        :param credential_occurrence: The credential_occurrence of this AlertListSchema.  # noqa: E501
        :type credential_occurrence: CredentialOccurrenceSchema
        """

        self._credential_occurrence = credential_occurrence

    @property
    def credential_set(self):
        """Gets the credential_set of this AlertListSchema.  # noqa: E501


        :return: The credential_set of this AlertListSchema.  # noqa: E501
        :rtype: CredentialSetSchema
        """
        return self._credential_set

    @credential_set.setter
    def credential_set(self, credential_set):
        """Sets the credential_set of this AlertListSchema.


        :param credential_set: The credential_set of this AlertListSchema.  # noqa: E501
        :type credential_set: CredentialSetSchema
        """

        self._credential_set = credential_set

    @property
    def cve_report(self):
        """Gets the cve_report of this AlertListSchema.  # noqa: E501


        :return: The cve_report of this AlertListSchema.  # noqa: E501
        :rtype: SimpleCveSchema
        """
        return self._cve_report

    @cve_report.setter
    def cve_report(self, cve_report):
        """Sets the cve_report of this AlertListSchema.


        :param cve_report: The cve_report of this AlertListSchema.  # noqa: E501
        :type cve_report: SimpleCveSchema
        """

        self._cve_report = cve_report

    @property
    def entity(self):
        """Gets the entity of this AlertListSchema.  # noqa: E501


        :return: The entity of this AlertListSchema.  # noqa: E501
        :rtype: EntitiesSchema
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this AlertListSchema.


        :param entity: The entity of this AlertListSchema.  # noqa: E501
        :type entity: EntitiesSchema
        """

        self._entity = entity

    @property
    def event(self):
        """Gets the event of this AlertListSchema.  # noqa: E501


        :return: The event of this AlertListSchema.  # noqa: E501
        :rtype: EventSchema
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this AlertListSchema.


        :param event: The event of this AlertListSchema.  # noqa: E501
        :type event: EventSchema
        """

        self._event = event

    @property
    def found_time(self):
        """Gets the found_time of this AlertListSchema.  # noqa: E501

        Date when alert was created.  # noqa: E501

        :return: The found_time of this AlertListSchema.  # noqa: E501
        :rtype: int
        """
        return self._found_time

    @found_time.setter
    def found_time(self, found_time):
        """Sets the found_time of this AlertListSchema.

        Date when alert was created.  # noqa: E501

        :param found_time: The found_time of this AlertListSchema.  # noqa: E501
        :type found_time: int
        """
        if self.local_vars_configuration.client_side_validation and found_time is None:  # noqa: E501
            raise ValueError("Invalid value for `found_time`, must not be `None`")  # noqa: E501

        self._found_time = found_time

    @property
    def highlights(self):
        """Gets the highlights of this AlertListSchema.  # noqa: E501

        Text snippets with `highlights` matching search terms.  # noqa: E501

        :return: The highlights of this AlertListSchema.  # noqa: E501
        :rtype: list[AlertListSchemaHighlights]
        """
        return self._highlights

    @highlights.setter
    def highlights(self, highlights):
        """Sets the highlights of this AlertListSchema.

        Text snippets with `highlights` matching search terms.  # noqa: E501

        :param highlights: The highlights of this AlertListSchema.  # noqa: E501
        :type highlights: list[AlertListSchemaHighlights]
        """

        self._highlights = highlights

    @property
    def indicator(self):
        """Gets the indicator of this AlertListSchema.  # noqa: E501


        :return: The indicator of this AlertListSchema.  # noqa: E501
        :rtype: IndicatorSearchSchema
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this AlertListSchema.


        :param indicator: The indicator of this AlertListSchema.  # noqa: E501
        :type indicator: IndicatorSearchSchema
        """

        self._indicator = indicator

    @property
    def instant_message(self):
        """Gets the instant_message of this AlertListSchema.  # noqa: E501


        :return: The instant_message of this AlertListSchema.  # noqa: E501
        :rtype: InstantMessageSchema
        """
        return self._instant_message

    @instant_message.setter
    def instant_message(self, instant_message):
        """Sets the instant_message of this AlertListSchema.


        :param instant_message: The instant_message of this AlertListSchema.  # noqa: E501
        :type instant_message: InstantMessageSchema
        """

        self._instant_message = instant_message

    @property
    def post(self):
        """Gets the post of this AlertListSchema.  # noqa: E501


        :return: The post of this AlertListSchema.  # noqa: E501
        :rtype: PostSchema
        """
        return self._post

    @post.setter
    def post(self, post):
        """Sets the post of this AlertListSchema.


        :param post: The post of this AlertListSchema.  # noqa: E501
        :type post: PostSchema
        """

        self._post = post

    @property
    def private_message(self):
        """Gets the private_message of this AlertListSchema.  # noqa: E501


        :return: The private_message of this AlertListSchema.  # noqa: E501
        :rtype: PrivateMessageSchema
        """
        return self._private_message

    @private_message.setter
    def private_message(self, private_message):
        """Sets the private_message of this AlertListSchema.


        :param private_message: The private_message of this AlertListSchema.  # noqa: E501
        :type private_message: PrivateMessageSchema
        """

        self._private_message = private_message

    @property
    def report(self):
        """Gets the report of this AlertListSchema.  # noqa: E501


        :return: The report of this AlertListSchema.  # noqa: E501
        :rtype: AlertListSchemaReport
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this AlertListSchema.


        :param report: The report of this AlertListSchema.  # noqa: E501
        :type report: AlertListSchemaReport
        """

        self._report = report

    @property
    def status(self):
        """Gets the status of this AlertListSchema.  # noqa: E501

        Read or unread.  # noqa: E501

        :return: The status of this AlertListSchema.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AlertListSchema.

        Read or unread.  # noqa: E501

        :param status: The status of this AlertListSchema.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def uid(self):
        """Gets the uid of this AlertListSchema.  # noqa: E501

        Unique alert identifier.  # noqa: E501

        :return: The uid of this AlertListSchema.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AlertListSchema.

        Unique alert identifier.  # noqa: E501

        :param uid: The uid of this AlertListSchema.  # noqa: E501
        :type uid: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def watcher_group_uid(self):
        """Gets the watcher_group_uid of this AlertListSchema.  # noqa: E501

        Unique watcher group identifier. Displayed if user has access to this watcher group.  # noqa: E501

        :return: The watcher_group_uid of this AlertListSchema.  # noqa: E501
        :rtype: str
        """
        return self._watcher_group_uid

    @watcher_group_uid.setter
    def watcher_group_uid(self, watcher_group_uid):
        """Sets the watcher_group_uid of this AlertListSchema.

        Unique watcher group identifier. Displayed if user has access to this watcher group.  # noqa: E501

        :param watcher_group_uid: The watcher_group_uid of this AlertListSchema.  # noqa: E501
        :type watcher_group_uid: str
        """

        self._watcher_group_uid = watcher_group_uid

    @property
    def watcher_uid(self):
        """Gets the watcher_uid of this AlertListSchema.  # noqa: E501

        Unique watcher identifier. Displayed if user has access to this watcher.  # noqa: E501

        :return: The watcher_uid of this AlertListSchema.  # noqa: E501
        :rtype: str
        """
        return self._watcher_uid

    @watcher_uid.setter
    def watcher_uid(self, watcher_uid):
        """Sets the watcher_uid of this AlertListSchema.

        Unique watcher identifier. Displayed if user has access to this watcher.  # noqa: E501

        :param watcher_uid: The watcher_uid of this AlertListSchema.  # noqa: E501
        :type watcher_uid: str
        """

        self._watcher_uid = watcher_uid

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
        if not isinstance(other, AlertListSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertListSchema):
            return True

        return self.to_dict() != other.to_dict()
