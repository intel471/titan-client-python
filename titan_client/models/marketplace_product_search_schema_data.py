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


class MarketplaceProductSearchSchemaData(object):
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
        'availability': 'MarketplaceProductAvailabilitySchema',
        'base': 'str',
        'card_holder': 'str',
        'card_number': 'str',
        'card_type': 'str',
        'categories': 'list[str]',
        'cvv': 'str',
        'description': 'str',
        'expiration': 'str',
        'installed_at': 'int',
        'issuer': 'str',
        'marketplace': 'MarketplaceProductMarketplaceSchema',
        'obfuscated_number': 'str',
        'product_type': 'str',
        'stolen_by_form_stealers': 'int',
        'title': 'str',
        'victim': 'MarketplaceProductSearchSchemaDataVictim'
    }

    attribute_map = {
        'availability': 'availability',
        'base': 'base',
        'card_holder': 'card_holder',
        'card_number': 'card_number',
        'card_type': 'card_type',
        'categories': 'categories',
        'cvv': 'cvv',
        'description': 'description',
        'expiration': 'expiration',
        'installed_at': 'installed_at',
        'issuer': 'issuer',
        'marketplace': 'marketplace',
        'obfuscated_number': 'obfuscated_number',
        'product_type': 'product_type',
        'stolen_by_form_stealers': 'stolen_by_form_stealers',
        'title': 'title',
        'victim': 'victim'
    }

    def __init__(self, availability=None, base=None, card_holder=None, card_number=None, card_type=None, categories=None, cvv=None, description=None, expiration=None, installed_at=None, issuer=None, marketplace=None, obfuscated_number=None, product_type=None, stolen_by_form_stealers=None, title=None, victim=None, local_vars_configuration=None):  # noqa: E501
        """MarketplaceProductSearchSchemaData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._availability = None
        self._base = None
        self._card_holder = None
        self._card_number = None
        self._card_type = None
        self._categories = None
        self._cvv = None
        self._description = None
        self._expiration = None
        self._installed_at = None
        self._issuer = None
        self._marketplace = None
        self._obfuscated_number = None
        self._product_type = None
        self._stolen_by_form_stealers = None
        self._title = None
        self._victim = None
        self.discriminator = None

        if availability is not None:
            self.availability = availability
        if base is not None:
            self.base = base
        if card_holder is not None:
            self.card_holder = card_holder
        if card_number is not None:
            self.card_number = card_number
        if card_type is not None:
            self.card_type = card_type
        if categories is not None:
            self.categories = categories
        if cvv is not None:
            self.cvv = cvv
        if description is not None:
            self.description = description
        if expiration is not None:
            self.expiration = expiration
        if installed_at is not None:
            self.installed_at = installed_at
        if issuer is not None:
            self.issuer = issuer
        if marketplace is not None:
            self.marketplace = marketplace
        if obfuscated_number is not None:
            self.obfuscated_number = obfuscated_number
        if product_type is not None:
            self.product_type = product_type
        if stolen_by_form_stealers is not None:
            self.stolen_by_form_stealers = stolen_by_form_stealers
        if title is not None:
            self.title = title
        if victim is not None:
            self.victim = victim

    @property
    def availability(self):
        """Gets the availability of this MarketplaceProductSearchSchemaData.  # noqa: E501


        :return: The availability of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: MarketplaceProductAvailabilitySchema
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this MarketplaceProductSearchSchemaData.


        :param availability: The availability of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type availability: MarketplaceProductAvailabilitySchema
        """

        self._availability = availability

    @property
    def base(self):
        """Gets the base of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Base dump name.  # noqa: E501

        :return: The base of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this MarketplaceProductSearchSchemaData.

        Base dump name.  # noqa: E501

        :param base: The base of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type base: str
        """

        self._base = base

    @property
    def card_holder(self):
        """Gets the card_holder of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Credit card holder.  # noqa: E501

        :return: The card_holder of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._card_holder

    @card_holder.setter
    def card_holder(self, card_holder):
        """Sets the card_holder of this MarketplaceProductSearchSchemaData.

        Credit card holder.  # noqa: E501

        :param card_holder: The card_holder of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type card_holder: str
        """

        self._card_holder = card_holder

    @property
    def card_number(self):
        """Gets the card_number of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Credit card number.  # noqa: E501

        :return: The card_number of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this MarketplaceProductSearchSchemaData.

        Credit card number.  # noqa: E501

        :param card_number: The card_number of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type card_number: str
        """

        self._card_number = card_number

    @property
    def card_type(self):
        """Gets the card_type of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Credit card type.  # noqa: E501

        :return: The card_type of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this MarketplaceProductSearchSchemaData.

        Credit card type.  # noqa: E501

        :param card_type: The card_type of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type card_type: str
        """

        self._card_type = card_type

    @property
    def categories(self):
        """Gets the categories of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Product categories.  # noqa: E501

        :return: The categories of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this MarketplaceProductSearchSchemaData.

        Product categories.  # noqa: E501

        :param categories: The categories of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type categories: list[str]
        """

        self._categories = categories

    @property
    def cvv(self):
        """Gets the cvv of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Credit card cvv.  # noqa: E501

        :return: The cvv of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        """Sets the cvv of this MarketplaceProductSearchSchemaData.

        Credit card cvv.  # noqa: E501

        :param cvv: The cvv of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type cvv: str
        """

        self._cvv = cvv

    @property
    def description(self):
        """Gets the description of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Product description.  # noqa: E501

        :return: The description of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MarketplaceProductSearchSchemaData.

        Product description.  # noqa: E501

        :param description: The description of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def expiration(self):
        """Gets the expiration of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Credit card expiration date.  # noqa: E501

        :return: The expiration of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this MarketplaceProductSearchSchemaData.

        Credit card expiration date.  # noqa: E501

        :param expiration: The expiration of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type expiration: str
        """

        self._expiration = expiration

    @property
    def installed_at(self):
        """Gets the installed_at of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Timestamp when bot was installed.  # noqa: E501

        :return: The installed_at of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: int
        """
        return self._installed_at

    @installed_at.setter
    def installed_at(self, installed_at):
        """Sets the installed_at of this MarketplaceProductSearchSchemaData.

        Timestamp when bot was installed.  # noqa: E501

        :param installed_at: The installed_at of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type installed_at: int
        """

        self._installed_at = installed_at

    @property
    def issuer(self):
        """Gets the issuer of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Credit card issuer.  # noqa: E501

        :return: The issuer of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this MarketplaceProductSearchSchemaData.

        Credit card issuer.  # noqa: E501

        :param issuer: The issuer of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type issuer: str
        """

        self._issuer = issuer

    @property
    def marketplace(self):
        """Gets the marketplace of this MarketplaceProductSearchSchemaData.  # noqa: E501


        :return: The marketplace of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: MarketplaceProductMarketplaceSchema
        """
        return self._marketplace

    @marketplace.setter
    def marketplace(self, marketplace):
        """Sets the marketplace of this MarketplaceProductSearchSchemaData.


        :param marketplace: The marketplace of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type marketplace: MarketplaceProductMarketplaceSchema
        """

        self._marketplace = marketplace

    @property
    def obfuscated_number(self):
        """Gets the obfuscated_number of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Obfuscated credit card number.  # noqa: E501

        :return: The obfuscated_number of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._obfuscated_number

    @obfuscated_number.setter
    def obfuscated_number(self, obfuscated_number):
        """Sets the obfuscated_number of this MarketplaceProductSearchSchemaData.

        Obfuscated credit card number.  # noqa: E501

        :param obfuscated_number: The obfuscated_number of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type obfuscated_number: str
        """

        self._obfuscated_number = obfuscated_number

    @property
    def product_type(self):
        """Gets the product_type of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Type of product  # noqa: E501

        :return: The product_type of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this MarketplaceProductSearchSchemaData.

        Type of product  # noqa: E501

        :param product_type: The product_type of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type product_type: str
        """
        allowed_values = ["Other product", "Credential", "Credit card"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and product_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `product_type` ({0}), must be one of {1}"  # noqa: E501
                .format(product_type, allowed_values)
            )

        self._product_type = product_type

    @property
    def stolen_by_form_stealers(self):
        """Gets the stolen_by_form_stealers of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Count of stolen credentials in this package.  # noqa: E501

        :return: The stolen_by_form_stealers of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: int
        """
        return self._stolen_by_form_stealers

    @stolen_by_form_stealers.setter
    def stolen_by_form_stealers(self, stolen_by_form_stealers):
        """Sets the stolen_by_form_stealers of this MarketplaceProductSearchSchemaData.

        Count of stolen credentials in this package.  # noqa: E501

        :param stolen_by_form_stealers: The stolen_by_form_stealers of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type stolen_by_form_stealers: int
        """

        self._stolen_by_form_stealers = stolen_by_form_stealers

    @property
    def title(self):
        """Gets the title of this MarketplaceProductSearchSchemaData.  # noqa: E501

        Product title.  # noqa: E501

        :return: The title of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MarketplaceProductSearchSchemaData.

        Product title.  # noqa: E501

        :param title: The title of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def victim(self):
        """Gets the victim of this MarketplaceProductSearchSchemaData.  # noqa: E501


        :return: The victim of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :rtype: MarketplaceProductSearchSchemaDataVictim
        """
        return self._victim

    @victim.setter
    def victim(self, victim):
        """Sets the victim of this MarketplaceProductSearchSchemaData.


        :param victim: The victim of this MarketplaceProductSearchSchemaData.  # noqa: E501
        :type victim: MarketplaceProductSearchSchemaDataVictim
        """

        self._victim = victim

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
        if not isinstance(other, MarketplaceProductSearchSchemaData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarketplaceProductSearchSchemaData):
            return True

        return self.to_dict() != other.to_dict()
