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


class SimpleCveSchemaDataCveReport(object):
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
        'activity_location': 'SimpleCveSchemaDataCveReportActivityLocation',
        'counter_measure_links': 'list[SimpleCveSchemaDataCveReportCounterMeasureLinks]',
        'counter_measures': 'str',
        'cpe': 'object',
        'cve_status': 'str',
        'cve_type': 'str',
        'cvss_score': 'SimpleCveSchemaDataCveReportCvssScore',
        'detection': 'str',
        'exploit_status': 'SimpleCveSchemaDataCveReportExploitStatus',
        'interest_level': 'SimpleCveSchemaDataCveReportInterestLevel',
        'name': 'str',
        'patch_links': 'list[SimpleCveSchemaDataCveReportPatchLinks]',
        'patch_status': 'str',
        'poc': 'str',
        'poc_links': 'list[SimpleCveSchemaDataCveReportPocLinks]',
        'product_name': 'str',
        'risk_level': 'str',
        'summary': 'str',
        'titan_links': 'list[SimpleCveSchemaDataCveReportTitanLinks]',
        'underground_activity': 'str',
        'underground_activity_summary': 'str',
        'vendor_name': 'str'
    }

    attribute_map = {
        'activity_location': 'activity_location',
        'counter_measure_links': 'counter_measure_links',
        'counter_measures': 'counter_measures',
        'cpe': 'cpe',
        'cve_status': 'cve_status',
        'cve_type': 'cve_type',
        'cvss_score': 'cvss_score',
        'detection': 'detection',
        'exploit_status': 'exploit_status',
        'interest_level': 'interest_level',
        'name': 'name',
        'patch_links': 'patch_links',
        'patch_status': 'patch_status',
        'poc': 'poc',
        'poc_links': 'poc_links',
        'product_name': 'product_name',
        'risk_level': 'risk_level',
        'summary': 'summary',
        'titan_links': 'titan_links',
        'underground_activity': 'underground_activity',
        'underground_activity_summary': 'underground_activity_summary',
        'vendor_name': 'vendor_name'
    }

    def __init__(self, activity_location=None, counter_measure_links=None, counter_measures=None, cpe=None, cve_status=None, cve_type=None, cvss_score=None, detection=None, exploit_status=None, interest_level=None, name=None, patch_links=None, patch_status=None, poc=None, poc_links=None, product_name=None, risk_level=None, summary=None, titan_links=None, underground_activity=None, underground_activity_summary=None, vendor_name=None, local_vars_configuration=None):  # noqa: E501
        """SimpleCveSchemaDataCveReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._activity_location = None
        self._counter_measure_links = None
        self._counter_measures = None
        self._cpe = None
        self._cve_status = None
        self._cve_type = None
        self._cvss_score = None
        self._detection = None
        self._exploit_status = None
        self._interest_level = None
        self._name = None
        self._patch_links = None
        self._patch_status = None
        self._poc = None
        self._poc_links = None
        self._product_name = None
        self._risk_level = None
        self._summary = None
        self._titan_links = None
        self._underground_activity = None
        self._underground_activity_summary = None
        self._vendor_name = None
        self.discriminator = None

        if activity_location is not None:
            self.activity_location = activity_location
        if counter_measure_links is not None:
            self.counter_measure_links = counter_measure_links
        if counter_measures is not None:
            self.counter_measures = counter_measures
        if cpe is not None:
            self.cpe = cpe
        self.cve_status = cve_status
        self.cve_type = cve_type
        if cvss_score is not None:
            self.cvss_score = cvss_score
        if detection is not None:
            self.detection = detection
        if exploit_status is not None:
            self.exploit_status = exploit_status
        if interest_level is not None:
            self.interest_level = interest_level
        self.name = name
        if patch_links is not None:
            self.patch_links = patch_links
        if patch_status is not None:
            self.patch_status = patch_status
        self.poc = poc
        if poc_links is not None:
            self.poc_links = poc_links
        if product_name is not None:
            self.product_name = product_name
        self.risk_level = risk_level
        if summary is not None:
            self.summary = summary
        if titan_links is not None:
            self.titan_links = titan_links
        if underground_activity is not None:
            self.underground_activity = underground_activity
        if underground_activity_summary is not None:
            self.underground_activity_summary = underground_activity_summary
        if vendor_name is not None:
            self.vendor_name = vendor_name

    @property
    def activity_location(self):
        """Gets the activity_location of this SimpleCveSchemaDataCveReport.  # noqa: E501


        :return: The activity_location of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: SimpleCveSchemaDataCveReportActivityLocation
        """
        return self._activity_location

    @activity_location.setter
    def activity_location(self, activity_location):
        """Sets the activity_location of this SimpleCveSchemaDataCveReport.


        :param activity_location: The activity_location of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type activity_location: SimpleCveSchemaDataCveReportActivityLocation
        """

        self._activity_location = activity_location

    @property
    def counter_measure_links(self):
        """Gets the counter_measure_links of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Titled URLs to countermeasure information to protect against the CVE.  # noqa: E501

        :return: The counter_measure_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: list[SimpleCveSchemaDataCveReportCounterMeasureLinks]
        """
        return self._counter_measure_links

    @counter_measure_links.setter
    def counter_measure_links(self, counter_measure_links):
        """Sets the counter_measure_links of this SimpleCveSchemaDataCveReport.

        Titled URLs to countermeasure information to protect against the CVE.  # noqa: E501

        :param counter_measure_links: The counter_measure_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type counter_measure_links: list[SimpleCveSchemaDataCveReportCounterMeasureLinks]
        """

        self._counter_measure_links = counter_measure_links

    @property
    def counter_measures(self):
        """Gets the counter_measures of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Summary of `countermeasures` to protect against the CVE.  # noqa: E501

        :return: The counter_measures of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._counter_measures

    @counter_measures.setter
    def counter_measures(self, counter_measures):
        """Sets the counter_measures of this SimpleCveSchemaDataCveReport.

        Summary of `countermeasures` to protect against the CVE.  # noqa: E501

        :param counter_measures: The counter_measures of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type counter_measures: str
        """

        self._counter_measures = counter_measures

    @property
    def cpe(self):
        """Gets the cpe of this SimpleCveSchemaDataCveReport.  # noqa: E501

        `CPE` (Common Platform Enumeration) is the list of the software affected by the vulnerability. Raw data field.  # noqa: E501

        :return: The cpe of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: object
        """
        return self._cpe

    @cpe.setter
    def cpe(self, cpe):
        """Sets the cpe of this SimpleCveSchemaDataCveReport.

        `CPE` (Common Platform Enumeration) is the list of the software affected by the vulnerability. Raw data field.  # noqa: E501

        :param cpe: The cpe of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type cpe: object
        """

        self._cpe = cpe

    @property
    def cve_status(self):
        """Gets the cve_status of this SimpleCveSchemaDataCveReport.  # noqa: E501

        `status_new` for recently added CVE; `status_existing` for CVE being reported for a while; `status_historical` for phased out and not actual at the moment. Allowed values: `status_existing`, `status_new`, `status_historical`.  # noqa: E501

        :return: The cve_status of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._cve_status

    @cve_status.setter
    def cve_status(self, cve_status):
        """Sets the cve_status of this SimpleCveSchemaDataCveReport.

        `status_new` for recently added CVE; `status_existing` for CVE being reported for a while; `status_historical` for phased out and not actual at the moment. Allowed values: `status_existing`, `status_new`, `status_historical`.  # noqa: E501

        :param cve_status: The cve_status of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type cve_status: str
        """
        if self.local_vars_configuration.client_side_validation and cve_status is None:  # noqa: E501
            raise ValueError("Invalid value for `cve_status`, must not be `None`")  # noqa: E501

        self._cve_status = cve_status

    @property
    def cve_type(self):
        """Gets the cve_type of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Type of CVE, for example: `Buffer overflow`, `Privilege escalation`, `Memory corruption`, etc.  # noqa: E501

        :return: The cve_type of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._cve_type

    @cve_type.setter
    def cve_type(self, cve_type):
        """Sets the cve_type of this SimpleCveSchemaDataCveReport.

        Type of CVE, for example: `Buffer overflow`, `Privilege escalation`, `Memory corruption`, etc.  # noqa: E501

        :param cve_type: The cve_type of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type cve_type: str
        """
        if self.local_vars_configuration.client_side_validation and cve_type is None:  # noqa: E501
            raise ValueError("Invalid value for `cve_type`, must not be `None`")  # noqa: E501

        self._cve_type = cve_type

    @property
    def cvss_score(self):
        """Gets the cvss_score of this SimpleCveSchemaDataCveReport.  # noqa: E501


        :return: The cvss_score of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: SimpleCveSchemaDataCveReportCvssScore
        """
        return self._cvss_score

    @cvss_score.setter
    def cvss_score(self, cvss_score):
        """Sets the cvss_score of this SimpleCveSchemaDataCveReport.


        :param cvss_score: The cvss_score of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type cvss_score: SimpleCveSchemaDataCveReportCvssScore
        """

        self._cvss_score = cvss_score

    @property
    def detection(self):
        """Gets the detection of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Detection (signatures, definitions) exists for the CVE. Allowed values: `available`, `not_available`.  # noqa: E501

        :return: The detection of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._detection

    @detection.setter
    def detection(self, detection):
        """Sets the detection of this SimpleCveSchemaDataCveReport.

        Detection (signatures, definitions) exists for the CVE. Allowed values: `available`, `not_available`.  # noqa: E501

        :param detection: The detection of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type detection: str
        """

        self._detection = detection

    @property
    def exploit_status(self):
        """Gets the exploit_status of this SimpleCveSchemaDataCveReport.  # noqa: E501


        :return: The exploit_status of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: SimpleCveSchemaDataCveReportExploitStatus
        """
        return self._exploit_status

    @exploit_status.setter
    def exploit_status(self, exploit_status):
        """Sets the exploit_status of this SimpleCveSchemaDataCveReport.


        :param exploit_status: The exploit_status of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type exploit_status: SimpleCveSchemaDataCveReportExploitStatus
        """

        self._exploit_status = exploit_status

    @property
    def interest_level(self):
        """Gets the interest_level of this SimpleCveSchemaDataCveReport.  # noqa: E501


        :return: The interest_level of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: SimpleCveSchemaDataCveReportInterestLevel
        """
        return self._interest_level

    @interest_level.setter
    def interest_level(self, interest_level):
        """Sets the interest_level of this SimpleCveSchemaDataCveReport.


        :param interest_level: The interest_level of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type interest_level: SimpleCveSchemaDataCveReportInterestLevel
        """

        self._interest_level = interest_level

    @property
    def name(self):
        """Gets the name of this SimpleCveSchemaDataCveReport.  # noqa: E501

        CVE number.  # noqa: E501

        :return: The name of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimpleCveSchemaDataCveReport.

        CVE number.  # noqa: E501

        :param name: The name of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def patch_links(self):
        """Gets the patch_links of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Titled URLs to available CVE patch.  # noqa: E501

        :return: The patch_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: list[SimpleCveSchemaDataCveReportPatchLinks]
        """
        return self._patch_links

    @patch_links.setter
    def patch_links(self, patch_links):
        """Sets the patch_links of this SimpleCveSchemaDataCveReport.

        Titled URLs to available CVE patch.  # noqa: E501

        :param patch_links: The patch_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type patch_links: list[SimpleCveSchemaDataCveReportPatchLinks]
        """

        self._patch_links = patch_links

    @property
    def patch_status(self):
        """Gets the patch_status of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Indicates availability of the CVE patch. Allowed values: `available`, `some_available`, `unavailable`.  # noqa: E501

        :return: The patch_status of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._patch_status

    @patch_status.setter
    def patch_status(self, patch_status):
        """Sets the patch_status of this SimpleCveSchemaDataCveReport.

        Indicates availability of the CVE patch. Allowed values: `available`, `some_available`, `unavailable`.  # noqa: E501

        :param patch_status: The patch_status of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type patch_status: str
        """

        self._patch_status = patch_status

    @property
    def poc(self):
        """Gets the poc of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Proof of concept code or demonstration exists. Allowed values: `observed`, `not_observed`, `alleged_observed`.  # noqa: E501

        :return: The poc of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._poc

    @poc.setter
    def poc(self, poc):
        """Sets the poc of this SimpleCveSchemaDataCveReport.

        Proof of concept code or demonstration exists. Allowed values: `observed`, `not_observed`, `alleged_observed`.  # noqa: E501

        :param poc: The poc of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type poc: str
        """
        if self.local_vars_configuration.client_side_validation and poc is None:  # noqa: E501
            raise ValueError("Invalid value for `poc`, must not be `None`")  # noqa: E501

        self._poc = poc

    @property
    def poc_links(self):
        """Gets the poc_links of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Titled URLs to Proofs of Concept of the CVE.  # noqa: E501

        :return: The poc_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: list[SimpleCveSchemaDataCveReportPocLinks]
        """
        return self._poc_links

    @poc_links.setter
    def poc_links(self, poc_links):
        """Sets the poc_links of this SimpleCveSchemaDataCveReport.

        Titled URLs to Proofs of Concept of the CVE.  # noqa: E501

        :param poc_links: The poc_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type poc_links: list[SimpleCveSchemaDataCveReportPocLinks]
        """

        self._poc_links = poc_links

    @property
    def product_name(self):
        """Gets the product_name of this SimpleCveSchemaDataCveReport.  # noqa: E501

        `Product name` of the affected software.  # noqa: E501

        :return: The product_name of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this SimpleCveSchemaDataCveReport.

        `Product name` of the affected software.  # noqa: E501

        :param product_name: The product_name of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type product_name: str
        """

        self._product_name = product_name

    @property
    def risk_level(self):
        """Gets the risk_level of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Intel471 `risk level` of the described CVE. Allowed values: `high`, `medium`, `low`.  # noqa: E501

        :return: The risk_level of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """Sets the risk_level of this SimpleCveSchemaDataCveReport.

        Intel471 `risk level` of the described CVE. Allowed values: `high`, `medium`, `low`.  # noqa: E501

        :param risk_level: The risk_level of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type risk_level: str
        """
        if self.local_vars_configuration.client_side_validation and risk_level is None:  # noqa: E501
            raise ValueError("Invalid value for `risk_level`, must not be `None`")  # noqa: E501

        self._risk_level = risk_level

    @property
    def summary(self):
        """Gets the summary of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Intel471 `summary` of the CVE.  # noqa: E501

        :return: The summary of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this SimpleCveSchemaDataCveReport.

        Intel471 `summary` of the CVE.  # noqa: E501

        :param summary: The summary of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type summary: str
        """

        self._summary = summary

    @property
    def titan_links(self):
        """Gets the titan_links of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Links to the related titan items.  # noqa: E501

        :return: The titan_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: list[SimpleCveSchemaDataCveReportTitanLinks]
        """
        return self._titan_links

    @titan_links.setter
    def titan_links(self, titan_links):
        """Sets the titan_links of this SimpleCveSchemaDataCveReport.

        Links to the related titan items.  # noqa: E501

        :param titan_links: The titan_links of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type titan_links: list[SimpleCveSchemaDataCveReportTitanLinks]
        """

        self._titan_links = titan_links

    @property
    def underground_activity(self):
        """Gets the underground_activity of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Describes whether `underground activity` is observed for given CVE. Allowed values: `observed`, `not_observed`.  # noqa: E501

        :return: The underground_activity of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._underground_activity

    @underground_activity.setter
    def underground_activity(self, underground_activity):
        """Sets the underground_activity of this SimpleCveSchemaDataCveReport.

        Describes whether `underground activity` is observed for given CVE. Allowed values: `observed`, `not_observed`.  # noqa: E501

        :param underground_activity: The underground_activity of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type underground_activity: str
        """

        self._underground_activity = underground_activity

    @property
    def underground_activity_summary(self):
        """Gets the underground_activity_summary of this SimpleCveSchemaDataCveReport.  # noqa: E501

        Describes CVE underground activity.  # noqa: E501

        :return: The underground_activity_summary of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._underground_activity_summary

    @underground_activity_summary.setter
    def underground_activity_summary(self, underground_activity_summary):
        """Sets the underground_activity_summary of this SimpleCveSchemaDataCveReport.

        Describes CVE underground activity.  # noqa: E501

        :param underground_activity_summary: The underground_activity_summary of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type underground_activity_summary: str
        """

        self._underground_activity_summary = underground_activity_summary

    @property
    def vendor_name(self):
        """Gets the vendor_name of this SimpleCveSchemaDataCveReport.  # noqa: E501

        `Vendor name` of the affected software.  # noqa: E501

        :return: The vendor_name of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """Sets the vendor_name of this SimpleCveSchemaDataCveReport.

        `Vendor name` of the affected software.  # noqa: E501

        :param vendor_name: The vendor_name of this SimpleCveSchemaDataCveReport.  # noqa: E501
        :type vendor_name: str
        """

        self._vendor_name = vendor_name

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
        if not isinstance(other, SimpleCveSchemaDataCveReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimpleCveSchemaDataCveReport):
            return True

        return self.to_dict() != other.to_dict()
