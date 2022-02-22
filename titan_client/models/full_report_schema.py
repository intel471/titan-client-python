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


class FullReportSchema(object):
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
        'actor_handle': 'str',
        'actor_subject_of_report': 'list[SimpleReportSchemaActorSubjectOfReport]',
        'admiralty_code': 'str',
        'classification': 'SimpleReportSchemaClassification',
        'created': 'int',
        'date_of_information': 'int',
        'document_family': 'str',
        'document_type': 'str',
        'entities': 'list[SimpleReportSchemaEntities]',
        'last_updated': 'int',
        'locations': 'list[SimpleReportSchemaLocations]',
        'motivation': 'list[str]',
        'portal_report_url': 'str',
        'related_reports': 'list[SimpleReportSchemaRelatedReports]',
        'released': 'int',
        'report_attachments': 'list[SimpleReportSchemaReportAttachments]',
        'sensitive_source': 'bool',
        'source_characterization': 'str',
        'sources': 'list[SimpleReportSchemaSources]',
        'subject': 'str',
        'tags': 'list[str]',
        'uid': 'str',
        'victims': 'list[SimpleReportSchemaVictims]',
        'executive_summary': 'str',
        'raw_text': 'str',
        'raw_text_translated': 'str',
        'researcher_comments': 'str'
    }

    attribute_map = {
        'actor_handle': 'actorHandle',
        'actor_subject_of_report': 'actorSubjectOfReport',
        'admiralty_code': 'admiraltyCode',
        'classification': 'classification',
        'created': 'created',
        'date_of_information': 'dateOfInformation',
        'document_family': 'documentFamily',
        'document_type': 'documentType',
        'entities': 'entities',
        'last_updated': 'lastUpdated',
        'locations': 'locations',
        'motivation': 'motivation',
        'portal_report_url': 'portalReportUrl',
        'related_reports': 'relatedReports',
        'released': 'released',
        'report_attachments': 'reportAttachments',
        'sensitive_source': 'sensitiveSource',
        'source_characterization': 'sourceCharacterization',
        'sources': 'sources',
        'subject': 'subject',
        'tags': 'tags',
        'uid': 'uid',
        'victims': 'victims',
        'executive_summary': 'executiveSummary',
        'raw_text': 'rawText',
        'raw_text_translated': 'rawTextTranslated',
        'researcher_comments': 'researcherComments'
    }

    def __init__(self, actor_handle=None, actor_subject_of_report=None, admiralty_code=None, classification=None, created=None, date_of_information=None, document_family=None, document_type=None, entities=None, last_updated=None, locations=None, motivation=None, portal_report_url=None, related_reports=None, released=None, report_attachments=None, sensitive_source=None, source_characterization=None, sources=None, subject=None, tags=None, uid=None, victims=None, executive_summary=None, raw_text=None, raw_text_translated=None, researcher_comments=None, local_vars_configuration=None):  # noqa: E501
        """FullReportSchema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._actor_handle = None
        self._actor_subject_of_report = None
        self._admiralty_code = None
        self._classification = None
        self._created = None
        self._date_of_information = None
        self._document_family = None
        self._document_type = None
        self._entities = None
        self._last_updated = None
        self._locations = None
        self._motivation = None
        self._portal_report_url = None
        self._related_reports = None
        self._released = None
        self._report_attachments = None
        self._sensitive_source = None
        self._source_characterization = None
        self._sources = None
        self._subject = None
        self._tags = None
        self._uid = None
        self._victims = None
        self._executive_summary = None
        self._raw_text = None
        self._raw_text_translated = None
        self._researcher_comments = None
        self.discriminator = None

        if actor_handle is not None:
            self.actor_handle = actor_handle
        if actor_subject_of_report is not None:
            self.actor_subject_of_report = actor_subject_of_report
        self.admiralty_code = admiralty_code
        if classification is not None:
            self.classification = classification
        if created is not None:
            self.created = created
        self.date_of_information = date_of_information
        if document_family is not None:
            self.document_family = document_family
        if document_type is not None:
            self.document_type = document_type
        if entities is not None:
            self.entities = entities
        if last_updated is not None:
            self.last_updated = last_updated
        if locations is not None:
            self.locations = locations
        if motivation is not None:
            self.motivation = motivation
        self.portal_report_url = portal_report_url
        if related_reports is not None:
            self.related_reports = related_reports
        if released is not None:
            self.released = released
        if report_attachments is not None:
            self.report_attachments = report_attachments
        if sensitive_source is not None:
            self.sensitive_source = sensitive_source
        if source_characterization is not None:
            self.source_characterization = source_characterization
        if sources is not None:
            self.sources = sources
        self.subject = subject
        if tags is not None:
            self.tags = tags
        self.uid = uid
        if victims is not None:
            self.victims = victims
        if executive_summary is not None:
            self.executive_summary = executive_summary
        self.raw_text = raw_text
        if raw_text_translated is not None:
            self.raw_text_translated = raw_text_translated
        if researcher_comments is not None:
            self.researcher_comments = researcher_comments

    @property
    def actor_handle(self):
        """Gets the actor_handle of this FullReportSchema.  # noqa: E501

        Actor's handle  # noqa: E501

        :return: The actor_handle of this FullReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._actor_handle

    @actor_handle.setter
    def actor_handle(self, actor_handle):
        """Sets the actor_handle of this FullReportSchema.

        Actor's handle  # noqa: E501

        :param actor_handle: The actor_handle of this FullReportSchema.  # noqa: E501
        :type actor_handle: str
        """

        self._actor_handle = actor_handle

    @property
    def actor_subject_of_report(self):
        """Gets the actor_subject_of_report of this FullReportSchema.  # noqa: E501

        List of actors mentioned in report subject.  # noqa: E501

        :return: The actor_subject_of_report of this FullReportSchema.  # noqa: E501
        :rtype: list[SimpleReportSchemaActorSubjectOfReport]
        """
        return self._actor_subject_of_report

    @actor_subject_of_report.setter
    def actor_subject_of_report(self, actor_subject_of_report):
        """Sets the actor_subject_of_report of this FullReportSchema.

        List of actors mentioned in report subject.  # noqa: E501

        :param actor_subject_of_report: The actor_subject_of_report of this FullReportSchema.  # noqa: E501
        :type actor_subject_of_report: list[SimpleReportSchemaActorSubjectOfReport]
        """

        self._actor_subject_of_report = actor_subject_of_report

    @property
    def admiralty_code(self):
        """Gets the admiralty_code of this FullReportSchema.  # noqa: E501

        Code as described [here](http://en.wikipedia.org/wiki/Admiralty_code). All Fintel reports have admiraltyCode=`A1`.  # noqa: E501

        :return: The admiralty_code of this FullReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._admiralty_code

    @admiralty_code.setter
    def admiralty_code(self, admiralty_code):
        """Sets the admiralty_code of this FullReportSchema.

        Code as described [here](http://en.wikipedia.org/wiki/Admiralty_code). All Fintel reports have admiraltyCode=`A1`.  # noqa: E501

        :param admiralty_code: The admiralty_code of this FullReportSchema.  # noqa: E501
        :type admiralty_code: str
        """
        if self.local_vars_configuration.client_side_validation and admiralty_code is None:  # noqa: E501
            raise ValueError("Invalid value for `admiralty_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                admiralty_code is not None and not re.search(r'^[A-F][1-6]$', admiralty_code)):  # noqa: E501
            raise ValueError(r"Invalid value for `admiralty_code`, must be a follow pattern or equal to `/^[A-F][1-6]$/`")  # noqa: E501

        self._admiralty_code = admiralty_code

    @property
    def classification(self):
        """Gets the classification of this FullReportSchema.  # noqa: E501


        :return: The classification of this FullReportSchema.  # noqa: E501
        :rtype: SimpleReportSchemaClassification
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this FullReportSchema.


        :param classification: The classification of this FullReportSchema.  # noqa: E501
        :type classification: SimpleReportSchemaClassification
        """

        self._classification = classification

    @property
    def created(self):
        """Gets the created of this FullReportSchema.  # noqa: E501

        Date the report was `created` as Epoch Time.  # noqa: E501

        :return: The created of this FullReportSchema.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FullReportSchema.

        Date the report was `created` as Epoch Time.  # noqa: E501

        :param created: The created of this FullReportSchema.  # noqa: E501
        :type created: int
        """

        self._created = created

    @property
    def date_of_information(self):
        """Gets the date_of_information of this FullReportSchema.  # noqa: E501

        Date of information as Epoch Time.  # noqa: E501

        :return: The date_of_information of this FullReportSchema.  # noqa: E501
        :rtype: int
        """
        return self._date_of_information

    @date_of_information.setter
    def date_of_information(self, date_of_information):
        """Sets the date_of_information of this FullReportSchema.

        Date of information as Epoch Time.  # noqa: E501

        :param date_of_information: The date_of_information of this FullReportSchema.  # noqa: E501
        :type date_of_information: int
        """
        if self.local_vars_configuration.client_side_validation and date_of_information is None:  # noqa: E501
            raise ValueError("Invalid value for `date_of_information`, must not be `None`")  # noqa: E501

        self._date_of_information = date_of_information

    @property
    def document_family(self):
        """Gets the document_family of this FullReportSchema.  # noqa: E501

        Document family.  # noqa: E501

        :return: The document_family of this FullReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._document_family

    @document_family.setter
    def document_family(self, document_family):
        """Sets the document_family of this FullReportSchema.

        Document family.  # noqa: E501

        :param document_family: The document_family of this FullReportSchema.  # noqa: E501
        :type document_family: str
        """

        self._document_family = document_family

    @property
    def document_type(self):
        """Gets the document_type of this FullReportSchema.  # noqa: E501

        Document type.  # noqa: E501

        :return: The document_type of this FullReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this FullReportSchema.

        Document type.  # noqa: E501

        :param document_type: The document_type of this FullReportSchema.  # noqa: E501
        :type document_type: str
        """

        self._document_type = document_type

    @property
    def entities(self):
        """Gets the entities of this FullReportSchema.  # noqa: E501

        List of entities.  # noqa: E501

        :return: The entities of this FullReportSchema.  # noqa: E501
        :rtype: list[SimpleReportSchemaEntities]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this FullReportSchema.

        List of entities.  # noqa: E501

        :param entities: The entities of this FullReportSchema.  # noqa: E501
        :type entities: list[SimpleReportSchemaEntities]
        """

        self._entities = entities

    @property
    def last_updated(self):
        """Gets the last_updated of this FullReportSchema.  # noqa: E501

        Last modification date as Epoch Time.  # noqa: E501

        :return: The last_updated of this FullReportSchema.  # noqa: E501
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this FullReportSchema.

        Last modification date as Epoch Time.  # noqa: E501

        :param last_updated: The last_updated of this FullReportSchema.  # noqa: E501
        :type last_updated: int
        """

        self._last_updated = last_updated

    @property
    def locations(self):
        """Gets the locations of this FullReportSchema.  # noqa: E501

        Report `locations`.  # noqa: E501

        :return: The locations of this FullReportSchema.  # noqa: E501
        :rtype: list[SimpleReportSchemaLocations]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this FullReportSchema.

        Report `locations`.  # noqa: E501

        :param locations: The locations of this FullReportSchema.  # noqa: E501
        :type locations: list[SimpleReportSchemaLocations]
        """

        self._locations = locations

    @property
    def motivation(self):
        """Gets the motivation of this FullReportSchema.  # noqa: E501

        Actor's `motivation`. CC for Cyber Crime, CE for Cyber Espionage, HA for Hacktivism.  # noqa: E501

        :return: The motivation of this FullReportSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._motivation

    @motivation.setter
    def motivation(self, motivation):
        """Sets the motivation of this FullReportSchema.

        Actor's `motivation`. CC for Cyber Crime, CE for Cyber Espionage, HA for Hacktivism.  # noqa: E501

        :param motivation: The motivation of this FullReportSchema.  # noqa: E501
        :type motivation: list[str]
        """

        self._motivation = motivation

    @property
    def portal_report_url(self):
        """Gets the portal_report_url of this FullReportSchema.  # noqa: E501

        URL to the report on the portal.  # noqa: E501

        :return: The portal_report_url of this FullReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._portal_report_url

    @portal_report_url.setter
    def portal_report_url(self, portal_report_url):
        """Sets the portal_report_url of this FullReportSchema.

        URL to the report on the portal.  # noqa: E501

        :param portal_report_url: The portal_report_url of this FullReportSchema.  # noqa: E501
        :type portal_report_url: str
        """
        if self.local_vars_configuration.client_side_validation and portal_report_url is None:  # noqa: E501
            raise ValueError("Invalid value for `portal_report_url`, must not be `None`")  # noqa: E501

        self._portal_report_url = portal_report_url

    @property
    def related_reports(self):
        """Gets the related_reports of this FullReportSchema.  # noqa: E501

        List of related reports.  # noqa: E501

        :return: The related_reports of this FullReportSchema.  # noqa: E501
        :rtype: list[SimpleReportSchemaRelatedReports]
        """
        return self._related_reports

    @related_reports.setter
    def related_reports(self, related_reports):
        """Sets the related_reports of this FullReportSchema.

        List of related reports.  # noqa: E501

        :param related_reports: The related_reports of this FullReportSchema.  # noqa: E501
        :type related_reports: list[SimpleReportSchemaRelatedReports]
        """

        self._related_reports = related_reports

    @property
    def released(self):
        """Gets the released of this FullReportSchema.  # noqa: E501

        Date the report was `released` as Epoch Time.  # noqa: E501

        :return: The released of this FullReportSchema.  # noqa: E501
        :rtype: int
        """
        return self._released

    @released.setter
    def released(self, released):
        """Sets the released of this FullReportSchema.

        Date the report was `released` as Epoch Time.  # noqa: E501

        :param released: The released of this FullReportSchema.  # noqa: E501
        :type released: int
        """

        self._released = released

    @property
    def report_attachments(self):
        """Gets the report_attachments of this FullReportSchema.  # noqa: E501

        List of report attachments.  # noqa: E501

        :return: The report_attachments of this FullReportSchema.  # noqa: E501
        :rtype: list[SimpleReportSchemaReportAttachments]
        """
        return self._report_attachments

    @report_attachments.setter
    def report_attachments(self, report_attachments):
        """Sets the report_attachments of this FullReportSchema.

        List of report attachments.  # noqa: E501

        :param report_attachments: The report_attachments of this FullReportSchema.  # noqa: E501
        :type report_attachments: list[SimpleReportSchemaReportAttachments]
        """

        self._report_attachments = report_attachments

    @property
    def sensitive_source(self):
        """Gets the sensitive_source of this FullReportSchema.  # noqa: E501

        Indicates if the document contains sensitive source derived information.  # noqa: E501

        :return: The sensitive_source of this FullReportSchema.  # noqa: E501
        :rtype: bool
        """
        return self._sensitive_source

    @sensitive_source.setter
    def sensitive_source(self, sensitive_source):
        """Sets the sensitive_source of this FullReportSchema.

        Indicates if the document contains sensitive source derived information.  # noqa: E501

        :param sensitive_source: The sensitive_source of this FullReportSchema.  # noqa: E501
        :type sensitive_source: bool
        """

        self._sensitive_source = sensitive_source

    @property
    def source_characterization(self):
        """Gets the source_characterization of this FullReportSchema.  # noqa: E501

        Source characterization.  # noqa: E501

        :return: The source_characterization of this FullReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._source_characterization

    @source_characterization.setter
    def source_characterization(self, source_characterization):
        """Sets the source_characterization of this FullReportSchema.

        Source characterization.  # noqa: E501

        :param source_characterization: The source_characterization of this FullReportSchema.  # noqa: E501
        :type source_characterization: str
        """

        self._source_characterization = source_characterization

    @property
    def sources(self):
        """Gets the sources of this FullReportSchema.  # noqa: E501

        List of `sources`.  # noqa: E501

        :return: The sources of this FullReportSchema.  # noqa: E501
        :rtype: list[SimpleReportSchemaSources]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this FullReportSchema.

        List of `sources`.  # noqa: E501

        :param sources: The sources of this FullReportSchema.  # noqa: E501
        :type sources: list[SimpleReportSchemaSources]
        """

        self._sources = sources

    @property
    def subject(self):
        """Gets the subject of this FullReportSchema.  # noqa: E501

        Report's `subject`.  # noqa: E501

        :return: The subject of this FullReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this FullReportSchema.

        Report's `subject`.  # noqa: E501

        :param subject: The subject of this FullReportSchema.  # noqa: E501
        :type subject: str
        """
        if self.local_vars_configuration.client_side_validation and subject is None:  # noqa: E501
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def tags(self):
        """Gets the tags of this FullReportSchema.  # noqa: E501

        Report's assigned `tags`.  # noqa: E501

        :return: The tags of this FullReportSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FullReportSchema.

        Report's assigned `tags`.  # noqa: E501

        :param tags: The tags of this FullReportSchema.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def uid(self):
        """Gets the uid of this FullReportSchema.  # noqa: E501

        Unique report identifier.  # noqa: E501

        :return: The uid of this FullReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this FullReportSchema.

        Unique report identifier.  # noqa: E501

        :param uid: The uid of this FullReportSchema.  # noqa: E501
        :type uid: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def victims(self):
        """Gets the victims of this FullReportSchema.  # noqa: E501

        Purported victims list.  # noqa: E501

        :return: The victims of this FullReportSchema.  # noqa: E501
        :rtype: list[SimpleReportSchemaVictims]
        """
        return self._victims

    @victims.setter
    def victims(self, victims):
        """Sets the victims of this FullReportSchema.

        Purported victims list.  # noqa: E501

        :param victims: The victims of this FullReportSchema.  # noqa: E501
        :type victims: list[SimpleReportSchemaVictims]
        """

        self._victims = victims

    @property
    def executive_summary(self):
        """Gets the executive_summary of this FullReportSchema.  # noqa: E501

        Executive summary in HTML format.  # noqa: E501

        :return: The executive_summary of this FullReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._executive_summary

    @executive_summary.setter
    def executive_summary(self, executive_summary):
        """Sets the executive_summary of this FullReportSchema.

        Executive summary in HTML format.  # noqa: E501

        :param executive_summary: The executive_summary of this FullReportSchema.  # noqa: E501
        :type executive_summary: str
        """

        self._executive_summary = executive_summary

    @property
    def raw_text(self):
        """Gets the raw_text of this FullReportSchema.  # noqa: E501

        Raw text in HTML format.  # noqa: E501

        :return: The raw_text of this FullReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._raw_text

    @raw_text.setter
    def raw_text(self, raw_text):
        """Sets the raw_text of this FullReportSchema.

        Raw text in HTML format.  # noqa: E501

        :param raw_text: The raw_text of this FullReportSchema.  # noqa: E501
        :type raw_text: str
        """
        if self.local_vars_configuration.client_side_validation and raw_text is None:  # noqa: E501
            raise ValueError("Invalid value for `raw_text`, must not be `None`")  # noqa: E501

        self._raw_text = raw_text

    @property
    def raw_text_translated(self):
        """Gets the raw_text_translated of this FullReportSchema.  # noqa: E501

        Translated text in HTML format.  # noqa: E501

        :return: The raw_text_translated of this FullReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._raw_text_translated

    @raw_text_translated.setter
    def raw_text_translated(self, raw_text_translated):
        """Sets the raw_text_translated of this FullReportSchema.

        Translated text in HTML format.  # noqa: E501

        :param raw_text_translated: The raw_text_translated of this FullReportSchema.  # noqa: E501
        :type raw_text_translated: str
        """

        self._raw_text_translated = raw_text_translated

    @property
    def researcher_comments(self):
        """Gets the researcher_comments of this FullReportSchema.  # noqa: E501

        Researcher's comments in HTML format.  # noqa: E501

        :return: The researcher_comments of this FullReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._researcher_comments

    @researcher_comments.setter
    def researcher_comments(self, researcher_comments):
        """Sets the researcher_comments of this FullReportSchema.

        Researcher's comments in HTML format.  # noqa: E501

        :param researcher_comments: The researcher_comments of this FullReportSchema.  # noqa: E501
        :type researcher_comments: str
        """

        self._researcher_comments = researcher_comments

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
        if not isinstance(other, FullReportSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullReportSchema):
            return True

        return self.to_dict() != other.to_dict()
