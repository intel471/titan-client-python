# coding: utf-8

"""
    Titan API v1

    # Introduction The Intel 471 API is organized around the principles of REST. Our API lets you gather results from our platform using anything that can send a HTTP request, including cURL and modern internet browsers. Access to this API requires an API token which is managed from your account settings.  Intel 471 reserves the right to add fields to our API however we will provide backwards compatibility and older version support so that it will be possible to choose exact versions that provide a response with an older structure.  # Authentication Authentication to the API occurs by providing your email address as the login and API key as a password in the authorization header via HTTP Basic Auth. Your API key can be found in the [API](https://portal.intel471.com/api) section on the portal. It carries many privileges so please do not expose it on public web resources.  # Accessing the API  Following examples demonstrate different methods to get the reports from `/reports` endpoint.  ## Internet browser  Just open URL: https://api.intel471.com/v1/reports  Browser will ask you for credentials, provide your email as login and API key as password.  ## cURL command line utility  Execute following command in your terminal:  ``` curl -u <YOU EMAIL>:<YOUR API KEY> https://api.intel471.com/v1/reports ```  ## Python client  We provide a [Python client](https://github.com/intel471/titan-client-python) for Intel 471's Titan API, which aims at providing common ground for all the endpoints. Please note that all the call parameters and response body fields' names are normalized to camel_case, so for example when you search reports by document type using Python client use `document_type` instead of `documentType`.  Install the client using pip (python >= 3.6 required):  ``` pip install titan-client ```  Run following script  ```python import titan_client  configuration = titan_client.Configuration(     username=\"<YOU EMAIL>\",     password=\"<YOUR API KEY>\")  with titan_client.ApiClient(configuration) as api_client:     api_instance = titan_client.ReportsApi(api_client)     api_response = api_instance.reports_get() print(api_response) ```  # Use cases  Below we present several commonly used scenarios in both raw HTTP request format and as a script using Python client. Examples are simplified so that they do not contain the authentication part and for Python client they do not contain configuration and API client object creation portion. For full example please refer to **Accessing the API** section of this document.   ## Paging  One page of the results can carry up to 100 records and you can display up to 11 pages for one query (max offset is 1000) in non-stream API endpoints. Use `count` parameter to set the number of items per page. Use `offset` parameter to shift the window by given number of results.  **HTTP**  ``` # Get 20 reports, sorted by the default field GET https://api.intel471.com/v1/reports?count=20  # Get next 20 reports GET https://api.intel471.com/v1/reports?count=20&offset=20  # Get 40 reports in one go to save API calls GET https://api.intel471.com/v1/reports?count=40 ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(count=20, offset=20) ```  ## Paging beyond the max allowed offset  Paging described in the previous use case is generally sufficient for most needs. If there are more than 1100 objects to be obtained for a given time period and set of filter criteria, then it is possible to move the filter timestamps along and then restart the offset sequencing. There is a very small number of situations where this may cause issues, where there is multiple objects with the same timestamp adjacent to the last object in the response.  For the higher volume or fast changing data (such as malware indicators, malware events, creds) there are stream API endpoints available where cursors may be used in order to acquire data easily and to avoid the need to shift timestamp ranges.  ``` # Get first 11 pages, 100 objects each GET https://api.intel471.com/v1/reports?sort=latest&count=100 GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&count=100&offset=1000 ... > {\"reports\": [{..., \"created\": 1661867086000}, {..., \"created\": 1661864268000}]} ```  Then the `created` time value from the last response will be used as an upper limit in the next series of calls:  ```  GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&count=100 GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=100 ... GET https://api.intel471.com/v1/reports?sort=latest&until=1661864268000&offset=1000 ```  And so on, until the results are available or until the desired number of objects has been fetched.  ## Paging /alerts endpoint  Alerts endpoint differs from all the other non-stream API endpoints in that the `offset` parameter needs to be set to the uid of the most recent acquired alert instead of an integer indicating the shift.  **HTTP**  ``` GET https://api.intel471.com/v1/alerts?count=100 > {\"alerts\": [{..., \"uid\": \"abc123\"}, {..., \"uid\": \"abc234\"}]}  GET https://api.intel471.com/v1/alerts?count=100&offset=abc234 > {\"alerts\": [{..., \"uid\": \"abc345\"}, {..., \"uid\": \"abc456\"}]} ```  **Python**  ``` response = titan_client.AlertsApi(api_client).alerts_get(count=100, offset=\"abc456\") ```  ## Stream endpoints paging  Stream endpoints provide the same data as their regular counterparts but they differ in a way of paging. When working with a stream endpoint, the response always contains `cursorNext` field, which should be provided to the next subsequent call to fetch potential next page of the results. All the subsequent calls should have the same set of query parameters as the first one, except the cursor value. Keep calling the endpoint with a new cursor value until it stops yielding results. When new data appear after that, another call will fetch it.  **HTTP**  ``` GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT1\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT1 > {\"indicators\": [...], \"cursorNext\": \"MTY1NT2\"}  GET https://api.intel471.com/v1/indicators/stream?lastUpdatedFrom=1655809200000&cursor=MTY1NT2 > {\"cursorNext\": \"MTY1NT3\"} ```  **Python**  ``` response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000) print(response.cursor_next, response.indicators) # MTY1NT1, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT1\")) print(response.cursor_next, response.indicators) # MTY1NT2, [...]  response = titan_client.IndicatorsApi(api_client).indicators_stream_get(last_updated_from=1656809200000, cursor=\"MTY1NT2\")) print(response.cursor_next, response.indicators) # MTY1NT3, None ```  ## Querying using logical operators  ### Array parameters  Any query parameter can be singular or array, if multiple parameters with the same name were provided. All parameters with the same name are internally combined into a query with `AND` operator.  So following query:  ``` GET https://api.intel471.com/v1/reports?report=sources&report=abba ```  Means \"find me reports with `source` AND `abba` in their body\".  This approach is not supported in the Python client. Instead use query string method discussed below.  ### Query string parameters  Query parameters accept Elastic's query string syntax, which allows for even better flexibility.  For example above query can be rephrased as:  **HTTP**  ``` GET https://api.intel471.com/v1/reports?report=sources OR abba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"sources OR abba\") ```  More advanced combination would include both `OR` and `AND` operators and a negation:  **HTTP**  ``` GET https://api.intel471.com/v1/reports?report=(sources OR abba) AND -creaba ```  **Python**  ``` response = titan_client.ReportsApi(api_client).reports_get(report=\"(sources OR abba) AND -creaba\") ```  Means \"find me reports with `source` or `abba` in their body which at the same time do not contain `creaba`\".  The query string \"mini-language\" reference and examples can be found on [Elastic's query string syntax](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/query-dsl-query-string-query.html#query-dsl-query-string-query) page.  ## Get CVEs using multiple filtering criteria  Get all CVE reports for Chrome product where the risk is high and the patch is not available yet.  **HTTP**  ``` GET https://api.intel471.com/v1/cve/reports?productName=Chrome&riskLevel=high&patchStatus=unavailable ```  **Python**  ``` response = titan_client.VulnerabilitiesApi(api_client).cve_reports_get(     product_name=\"Chrome\",     risk_level=\"high\",     patch_status=\"unavailable\" ) ```  ## List watcher groups  **HTTP**  ``` GET https://api.intel471.com/v1/watcherGroups ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_get() ```  ## Create watcher group  To create a watcher group you need to pass a body along with the request.  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups {   \"name\": \"my_group_name\",   \"description\": \"My description\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_post(   {\"name\": \"my_group_name\", \"description\": \"My description\"} ) ```  ## Create free text search watcher  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"freeTextPattern\": \"text to search\",   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"freeTextPattern\": \"text to search\",     \"notificationChannel\": \"website\"   } ) ```  ## Create specific search watcher  **HTTP**  ``` POST https://api.intel471.com/v1/watcherGroups/<GROUP UID>/watchers {   \"type\": \"search\",   \"patterns\": [     {\"types\": \"Actor\" , \"pattern\": \"swisman\"}   ],   \"notificationChannel\": \"website\" } ```  **Python**  ``` response = titan_client.WatchersApi(api_client).watcher_groups_group_uid_watchers_post(   group_uid=\"<GROUP UID>\",   watcher_request_body_post={     \"type\": \"search\",     \"patterns\": [       {\"types\": \"Actor\" , \"pattern\": \"swisman\"}     ],     \"notificationChannel\": \"website\"   } ) ```  # API integration best practice with your application CORS requests to the API are not allowed due to security concerns, so please avoid AJAX calls directly from the browser. Instead consider setting up a server side proxy in your application to handle API requests.  Please consider not storing information provided by the API locally as we are constantly improving our data set and want you to have the most updated information.  # Versioning support We consistently improve our API and occasionally introduce the changes based on the customer feedback. The current API version is provided in this documentation's header. We provide API backwards compatibility whenever possible.  All requests are prefixed with the major version number, for example `/v1`:  ``` https://api.intel471.com/v1/reports ```  Different major versions are not compatible and imply significant response structure changes. Minor versions differences might include extra fields in response or provide new request parameter support. To stick to the specific version, just add `v` parameter to the request, for example: `?v=1.19.2`. If you specify a non existing version, it will be brought down to the nearest existing one.  Omitting the version parameter in the request will call the latest version of the API.  We consistently phase out the outdated versions of the API, keeping only several most recent versions. Specific version is getting disabled only when we do not record any requests using it, so it's guaranteed that calls to the outdated ones will work, though we recommend switching to the latest one as soon as possible.  We recommend to always add the version parameter to the request to be safe on API updates in your integrations.  Python client always adds the version parameter in the underlying request. API version matches the Python client's package version. 

    The version of the OpenAPI document: 1.20.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from titan_client.models.alert_list_schema import AlertListSchema

class TestAlertListSchema(unittest.TestCase):
    """AlertListSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertListSchema:
        """Test AlertListSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertListSchema`
        """
        model = AlertListSchema()
        if include_optional:
            return AlertListSchema(
                actor = titan_client.models.simple_actor_schema.SimpleActorSchema(
                    active_from = 56, 
                    active_until = 56, 
                    handles = [
                        ''
                        ], 
                    last_updated = 56, 
                    links = titan_client.models.simple_actor_schema_links.SimpleActorSchema_links(
                        forum_post_total_count = 56, 
                        forum_private_message_total_count = 56, 
                        forum_total_count = 56, 
                        forums = [
                            titan_client.models.simple_actor_schema_links_forums_inner.SimpleActorSchema_links_forums_inner(
                                actor_handle = '', 
                                contact_info = [
                                    titan_client.models.simple_actor_schema_links_forums_inner_contact_info_inner.SimpleActorSchema_links_forums_inner_contactInfo_inner(
                                        type = '', 
                                        value = '', )
                                    ], 
                                name = '', 
                                time_zone = '', 
                                uid = '', )
                            ], 
                        instant_message_channel_total_count = 56, 
                        instant_message_server_total_count = 56, 
                        instant_message_servers = [
                            titan_client.models.simple_actor_schema_links_instant_message_servers_inner.SimpleActorSchema_links_instantMessageServers_inner(
                                name = '', 
                                service_type = '', 
                                uid = '', )
                            ], 
                        instant_message_total_count = 56, 
                        report_total_count = 56, 
                        reports = [
                            titan_client.models.simple_report_schema.SimpleReportSchema(
                                actor_handle = '', 
                                actor_subject_of_report = [
                                    titan_client.models.simple_report_schema_actor_subject_of_report_inner.SimpleReportSchema_actorSubjectOfReport_inner(
                                        aliases = [
                                            ''
                                            ], 
                                        handle = '', )
                                    ], 
                                admiralty_code = 'C3', 
                                classification = titan_client.models.simple_report_schema_classification.SimpleReportSchema_classification(
                                    intel_requirements = [
                                        ''
                                        ], ), 
                                created = 56, 
                                date_of_information = 56, 
                                document_family = '', 
                                document_type = '', 
                                entities = [
                                    titan_client.models.simple_report_schema_entities_inner.SimpleReportSchema_entities_inner(
                                        type = '', 
                                        value = '', )
                                    ], 
                                last_updated = 56, 
                                locations = [
                                    titan_client.models.simple_report_schema_locations_inner.SimpleReportSchema_locations_inner(
                                        country = '', 
                                        link = '', 
                                        region = '', )
                                    ], 
                                motivation = [
                                    ''
                                    ], 
                                portal_report_url = '', 
                                related_reports = [
                                    titan_client.models.simple_report_schema_related_reports_inner.SimpleReportSchema_relatedReports_inner(
                                        document_family = '', 
                                        uid = '', )
                                    ], 
                                released = 56, 
                                report_attachments = [
                                    titan_client.models.simple_report_schema_report_attachments_inner.SimpleReportSchema_reportAttachments_inner(
                                        description = '', 
                                        file_name = '', 
                                        file_size = 56, 
                                        malicious = True, 
                                        mime_type = '', 
                                        url = '', )
                                    ], 
                                sensitive_source = True, 
                                source_characterization = '', 
                                sources = [
                                    titan_client.models.simple_report_schema_sources_inner.SimpleReportSchema_sources_inner(
                                        index = 56, 
                                        title = '', 
                                        type = '', 
                                        url = '', )
                                    ], 
                                subject = '', 
                                tags = [
                                    ''
                                    ], 
                                uid = '', 
                                victims = [
                                    titan_client.models.simple_report_schema_victims_inner.SimpleReportSchema_victims_inner(
                                        name = '', 
                                        urls = [
                                            ''
                                            ], )
                                    ], )
                            ], ), 
                    uid = '', ),
                breach_alert = titan_client.models.simple_breach_alert_schema.SimpleBreachAlertSchema(
                    activity = titan_client.models.simple_breach_alert_schema_activity.SimpleBreachAlertSchema_activity(
                        first = 56, 
                        last = 56, ), 
                    data = titan_client.models.simple_breach_alert_schema_data.SimpleBreachAlertSchema_data(
                        breach_alert = titan_client.models.simple_breach_alert_schema_data_breach_alert.SimpleBreachAlertSchema_data_breach_alert(
                            actor_or_group = '', 
                            confidence = titan_client.models.simple_breach_alert_schema_data_breach_alert_confidence.SimpleBreachAlertSchema_data_breach_alert_confidence(
                                description = '', 
                                level = 'low', ), 
                            date_of_information = 56, 
                            intel_requirements = [
                                ''
                                ], 
                            released_at = 56, 
                            sensitive_source = True, 
                            sources = [
                                titan_client.models.simple_breach_alert_schema_data_breach_alert_sources_inner.SimpleBreachAlertSchema_data_breach_alert_sources_inner(
                                    date = 56, 
                                    source_type = '', 
                                    title = '', 
                                    type = 'internal', 
                                    url = '', )
                                ], 
                            summary = '', 
                            title = '', 
                            victim = titan_client.models.simple_breach_alert_schema_data_breach_alert_victim.SimpleBreachAlertSchema_data_breach_alert_victim(
                                country = '', 
                                industries = [
                                    titan_client.models.simple_breach_alert_schema_data_breach_alert_victim_industries_inner.SimpleBreachAlertSchema_data_breach_alert_victim_industries_inner(
                                        industry = '', 
                                        sector = '', )
                                    ], 
                                name = '', 
                                region = '', 
                                revenue = '', 
                                urls = [
                                    ''
                                    ], ), ), 
                        entities = [
                            titan_client.models.simple_breach_alert_schema_data_entities_inner.SimpleBreachAlertSchema_data_entities_inner(
                                description = '', 
                                geo_info = titan_client.models.simple_breach_alert_schema_data_entities_inner_geo_info.SimpleBreachAlertSchema_data_entities_inner_geo_info(
                                    country = '', 
                                    provider = '', ), 
                                type = '', 
                                value = '', )
                            ], ), 
                    last_updated = 56, 
                    uid = '', ),
                credential = titan_client.models.credential_schema.CredentialSchema(
                    activity = titan_client.models.credential_schema_activity.CredentialSchema_activity(
                        first = 56, 
                        last = 56, ), 
                    classification = titan_client.models.credential_schema_classification.CredentialSchema_classification(
                        intel_requirements = [
                            ''
                            ], ), 
                    data = titan_client.models.credential_schema_data.CredentialSchema_data(
                        affiliations = [
                            ''
                            ], 
                        credential_domain = '', 
                        credential_login = '', 
                        credential_sets = [
                            titan_client.models.credential_schema_data_credential_sets_inner.CredentialSchema_data_credential_sets_inner(
                                name = '', 
                                uid = '', )
                            ], 
                        detected_malware = [
                            titan_client.models.malware.malware(
                                family = '', )
                            ], 
                        detection_domain = '', 
                        password = titan_client.models.credential_schema_data_password.CredentialSchema_data_password(
                            complexity = titan_client.models.credential_schema_data_password_complexity.CredentialSchema_data_password_complexity(
                                entropy = 1.337, 
                                length = 56, 
                                lowercase = 56, 
                                numbers = 56, 
                                other = 56, 
                                punctuation_marks = 56, 
                                score = 1.337, 
                                separators = 56, 
                                symbols = 56, 
                                uppercase = 56, 
                                weakness = 1.337, ), 
                            id = '', 
                            password_plain = '', 
                            strength = '', ), ), 
                    last_updated = 56, 
                    statistics = titan_client.models.credential_schema_statistics.CredentialSchema_statistics(
                        accessed_urls_total_count = 56, ), 
                    uid = '', ),
                credential_occurrence = titan_client.models.credential_occurrence_schema.CredentialOccurrenceSchema(
                    activity = titan_client.models.credential_occurrence_schema_activity.CredentialOccurrenceSchema_activity(
                        first = 56, 
                        last = 56, ), 
                    classification = titan_client.models.credential_occurrence_schema_classification.CredentialOccurrenceSchema_classification(
                        intel_requirements = [
                            ''
                            ], ), 
                    data = titan_client.models.credential_occurrence_schema_data.CredentialOccurrenceSchema_data(
                        accessed_url = '', 
                        credential = titan_client.models.credential_occurrence_schema_data_credential.CredentialOccurrenceSchema_data_credential(
                            affiliations = [
                                ''
                                ], 
                            credential_domain = '', 
                            credential_login = '', 
                            detection_domain = '', 
                            password = titan_client.models.credential_schema_data_password.CredentialSchema_data_password(
                                complexity = titan_client.models.credential_schema_data_password_complexity.CredentialSchema_data_password_complexity(
                                    entropy = 1.337, 
                                    length = 56, 
                                    lowercase = 56, 
                                    numbers = 56, 
                                    other = 56, 
                                    punctuation_marks = 56, 
                                    score = 1.337, 
                                    separators = 56, 
                                    symbols = 56, 
                                    uppercase = 56, 
                                    weakness = 1.337, ), 
                                id = '', 
                                password_plain = '', 
                                strength = '', ), 
                            uid = '', ), 
                        credential_set = titan_client.models.credential_occurrence_schema_data_credential_set.CredentialOccurrenceSchema_data_credential_set(
                            name = '', 
                            uid = '', ), 
                        detected_malware = titan_client.models.malware.malware(
                            family = '', ), 
                        file_path = '', ), 
                    last_updated = 56, 
                    uid = '', ),
                credential_set = titan_client.models.credential_set_schema.CredentialSetSchema(
                    activity = titan_client.models.credential_set_schema_activity.CredentialSetSchema_activity(
                        first = 56, 
                        last = 56, ), 
                    classification = titan_client.models.credential_set_schema_classification.CredentialSetSchema_classification(
                        intel_requirements = [
                            ''
                            ], ), 
                    data = titan_client.models.credential_set_schema_data.CredentialSetSchema_data(
                        breach_date = 56, 
                        collection_date = 56, 
                        description = '', 
                        disclosure_date = 56, 
                        external_sources = [
                            titan_client.models.credential_set_schema_data_external_sources_inner.CredentialSetSchema_data_external_sources_inner(
                                title = '', 
                                url = '', )
                            ], 
                        internal_sources = [
                            titan_client.models.credential_set_schema_data_internal_sources_inner.CredentialSetSchema_data_internal_sources_inner(
                                title = '', 
                                url = '', )
                            ], 
                        name = '', 
                        record_count = 56, 
                        victims = [
                            titan_client.models.credential_set_schema_data_victims_inner.CredentialSetSchema_data_victims_inner(
                                name = '', 
                                urls = [
                                    ''
                                    ], )
                            ], ), 
                    last_updated = 56, 
                    statistics = titan_client.models.credential_set_schema_statistics.CredentialSetSchema_statistics(
                        accessed_urls_total_count = 56, 
                        credential_occurrences_total_count = 56, 
                        credentials_total_count = 56, ), 
                    uid = '', ),
                cve_report = titan_client.models.simple_cve_schema.SimpleCveSchema(
                    activity = titan_client.models.simple_cve_schema_activity.SimpleCveSchema_activity(
                        first = 56, 
                        last = 56, ), 
                    classification = titan_client.models.simple_cve_schema_classification.SimpleCveSchema_classification(
                        intel_requirements = [
                            ''
                            ], ), 
                    data = titan_client.models.simple_cve_schema_data.SimpleCveSchema_data(
                        cve_report = titan_client.models.simple_cve_schema_data_cve_report.SimpleCveSchema_data_cve_report(
                            activity_location = titan_client.models.simple_cve_schema_data_cve_report_activity_location.SimpleCveSchema_data_cve_report_activity_location(
                                location_opensource = True, 
                                location_private = True, 
                                location_underground = True, ), 
                            counter_measure_links = [
                                titan_client.models.simple_cve_schema_data_cve_report_counter_measure_links_inner.SimpleCveSchema_data_cve_report_counter_measure_links_inner(
                                    title = '', 
                                    url = '', )
                                ], 
                            counter_measures = '', 
                            cpe = titan_client.models.cpe.cpe(), 
                            cve_status = '', 
                            cve_type = '', 
                            cvss_score = titan_client.models.simple_cve_schema_data_cve_report_cvss_score.SimpleCveSchema_data_cve_report_cvss_score(
                                v2 = 1.337, 
                                v3 = 1.337, ), 
                            detection = '', 
                            exploit_status = titan_client.models.simple_cve_schema_data_cve_report_exploit_status.SimpleCveSchema_data_cve_report_exploit_status(
                                available = True, 
                                not_observed = True, 
                                productized = True, 
                                weaponized = True, ), 
                            interest_level = titan_client.models.simple_cve_schema_data_cve_report_interest_level.SimpleCveSchema_data_cve_report_interest_level(
                                disclosed_publicly = True, 
                                exploit_sought = True, 
                                researched_publicly = True, ), 
                            name = '', 
                            patch_links = [
                                titan_client.models.simple_cve_schema_data_cve_report_patch_links_inner.SimpleCveSchema_data_cve_report_patch_links_inner(
                                    title = '', 
                                    url = '', )
                                ], 
                            patch_status = '', 
                            poc = '', 
                            poc_links = [
                                titan_client.models.simple_cve_schema_data_cve_report_poc_links_inner.SimpleCveSchema_data_cve_report_poc_links_inner(
                                    title = '', 
                                    url = '', )
                                ], 
                            product_name = '', 
                            risk_level = '', 
                            summary = '', 
                            titan_links = [
                                titan_client.models.simple_cve_schema_data_cve_report_titan_links_inner.SimpleCveSchema_data_cve_report_titan_links_inner(
                                    title = '', 
                                    url = '', )
                                ], 
                            underground_activity = '', 
                            underground_activity_summary = '', 
                            vendor_name = '', ), ), 
                    last_updated = 56, 
                    uid = '', ),
                data_leak_post = titan_client.models.data_leak_post_schema.DataLeakPostSchema(
                    chunk_number = 56, 
                    date = 56, 
                    file_listing = titan_client.models.data_leak_post_schema_file_listing.DataLeakPostSchema_file_listing(
                        download_url = '', ), 
                    last_updated = 56, 
                    links = titan_client.models.data_leak_post_schema_links.DataLeakPostSchema_links(
                        blog = titan_client.models.data_leak_post_schema_links_blog.DataLeakPostSchema_links_blog(
                            description = '', 
                            name = '', 
                            uid = '', ), 
                        images = [
                            titan_client.models.image_snake_case_schema.ImageSnakeCaseSchema(
                                dimension = '800x580', 
                                hash = '36af534f2504fd7f9cc4a7096fa2988fec018f8997086eed803cc9e53052b3ad', 
                                hash_type = 'SHA256', 
                                image_original = 'https://api.intel471.com/v1/messagingServices/images/original/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f', 
                                image_sanitized = 'https://api.intel471.com/v1/messagingServices/images/large/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f.webp', 
                                ocr = '', 
                                original_url = 'https://www.securitylab.ru/upload/iblock/487/4n6p9w4n9z84g24ok36gq6od2rnoikuh.jpg', 
                                size = '145763', 
                                status = 'validated', )
                            ], 
                        thread = titan_client.models.data_leak_post_schema_links_thread.DataLeakPostSchema_links_thread(
                            count = 56, 
                            topic = '', 
                            uid = '', ), ), 
                    message = '', 
                    uid = '', ),
                entity = titan_client.models.entities_schema.EntitiesSchema(
                    active_from = 56, 
                    active_till = 56, 
                    last_updated = 56, 
                    links = titan_client.models.entities_schema_links.EntitiesSchema_links(
                        actor_total_count = 56, 
                        actors = [
                            titan_client.models.entities_schema_links_actors_inner.EntitiesSchema_links_actors_inner(
                                handles = [
                                    ''
                                    ], 
                                uid = '', )
                            ], 
                        report_total_count = 56, 
                        reports = [
                            titan_client.models.entities_schema_links_reports_inner.EntitiesSchema_links_reports_inner(
                                admiralty_code = 'C3', 
                                date_of_information = 56, 
                                motivation = [
                                    ''
                                    ], 
                                portal_report_url = '', 
                                released = 56, 
                                source_characterization = '', 
                                subject = '', 
                                uid = '', )
                            ], ), 
                    type = '', 
                    uid = '', 
                    value = '', ),
                event = titan_client.models.event_schema.EventSchema(
                    activity = titan_client.models.event_schema_activity.EventSchema_activity(
                        first = 56, 
                        last = 56, ), 
                    data = titan_client.models.event_schema_data.EventSchema_data(
                        event_data = titan_client.models.event_schema_data_event_data.EventSchema_data_event_data(
                            bot_settings = titan_client.models.bot_settings.bot_settings(), 
                            command = '', 
                            component_type = '', 
                            config_file = '', 
                            controller = titan_client.models.event_schema_data_event_data_controller.EventSchema_data_event_data_controller(
                                geo_ip = titan_client.models.event_schema_data_event_data_controller_geo_ip.EventSchema_data_event_data_controller_geo_ip(
                                    city = '', 
                                    country = '', 
                                    country_code = '', 
                                    isp = titan_client.models.event_schema_data_event_data_controller_geo_ip_isp.EventSchema_data_event_data_controller_geo_ip_isp(
                                        autonomous_system = '', 
                                        network = '', 
                                        organization = '', ), 
                                    subdivision = [
                                        ''
                                        ], ), 
                                ipv4 = '', 
                                url = '', ), 
                            controllers = [
                                titan_client.models.event_schema_data_event_data_controllers_inner.EventSchema_data_event_data_controllers_inner(
                                    url = '', )
                                ], 
                            encryption = [
                                titan_client.models.event_schema_data_event_data_encryption_inner.EventSchema_data_event_data_encryption_inner(
                                    algorithm = '', 
                                    context = '', 
                                    key = '', )
                                ], 
                            exfil_location = '', 
                            file = titan_client.models.event_schema_data_event_data_file.EventSchema_data_event_data_file(
                                download_url = '', 
                                md5 = '', 
                                sha1 = '', 
                                sha256 = '', 
                                size = 1.337, 
                                type = '', ), 
                            inject_type = '', 
                            location = titan_client.models.event_schema_data_event_data_location.EventSchema_data_event_data_location(
                                ipv4 = '', 
                                url = '', ), 
                            plugin_name = '', 
                            plugin_type = '', 
                            recipient_domains = [
                                titan_client.models.event_schema_data_event_data_recipient_domains_inner.EventSchema_data_event_data_recipient_domains_inner(
                                    count = 56, 
                                    domain = '', )
                                ], 
                            senders = [
                                ''
                                ], 
                            settings = [
                                None
                                ], 
                            target_type = '', 
                            triggers = [
                                titan_client.models.event_schema_data_event_data_triggers_inner.EventSchema_data_event_data_triggers_inner(
                                    trigger = '', )
                                ], ), 
                        event_type = '', 
                        intel_requirements = [
                            ''
                            ], 
                        mitre_tactics = '', 
                        threat = titan_client.models.event_schema_data_threat.EventSchema_data_threat(
                            data = titan_client.models.event_schema_data_threat_data.EventSchema_data_threat_data(
                                family = '', 
                                malware_family_profile_uid = '', 
                                variant = '', 
                                version = '', ), 
                            type = '', 
                            uid = '', ), ), 
                    last_updated = 56, 
                    meta = titan_client.models.event_schema_meta.EventSchema_meta(
                        version = '', ), 
                    uid = '', ),
                found_time = 56,
                highlights = [
                    titan_client.models.alert_list_schema_highlights_inner.AlertListSchema_highlights_inner(
                        chunks = [
                            titan_client.models.alert_list_schema_highlights_inner_chunks_inner.AlertListSchema_highlights_inner_chunks_inner(
                                hl = '', 
                                text = '', )
                            ], 
                        field = '', )
                    ],
                indicator = titan_client.models.indicator_search_schema.IndicatorSearchSchema(
                    activity = titan_client.models.indicator_search_schema_activity.IndicatorSearchSchema_activity(
                        first = 56, 
                        last = 56, ), 
                    data = titan_client.models.indicator_search_schema_data.IndicatorSearchSchema_data(
                        confidence = '', 
                        context = titan_client.models.indicator_search_schema_data_context.IndicatorSearchSchema_data_context(
                            description = '', ), 
                        expiration = 56, 
                        indicator_data = titan_client.models.indicator_search_schema_data_indicator_data.IndicatorSearchSchema_data_indicator_data(
                            address = '', 
                            file = titan_client.models.indicator_search_schema_data_indicator_data_file.IndicatorSearchSchema_data_indicator_data_file(
                                download_url = '', 
                                md5 = '', 
                                sha1 = '', 
                                sha256 = '', 
                                size = 56, 
                                ssdeep = '', 
                                type = '', ), 
                            geo_ip = titan_client.models.event_schema_data_event_data_controller_geo_ip.EventSchema_data_event_data_controller_geo_ip(
                                city = '', 
                                country = '', 
                                country_code = '', 
                                isp = titan_client.models.event_schema_data_event_data_controller_geo_ip_isp.EventSchema_data_event_data_controller_geo_ip_isp(
                                    autonomous_system = '', 
                                    network = '', 
                                    organization = '', ), 
                                subdivision = [
                                    ''
                                    ], ), 
                            url = '', ), 
                        indicator_type = '', 
                        intel_requirements = [
                            ''
                            ], 
                        mitre_tactics = '', 
                        threat = titan_client.models.indicator_search_schema_data_threat.IndicatorSearchSchema_data_threat(
                            data = titan_client.models.indicator_search_schema_data_threat_data.IndicatorSearchSchema_data_threat_data(
                                family = '', 
                                malware_family_profile_uid = '', 
                                variant = '', 
                                version = '', ), 
                            type = '', 
                            uid = '', ), 
                        uid = '', ), 
                    last_updated = 56, 
                    meta = titan_client.models.indicator_search_schema_meta.IndicatorSearchSchema_meta(
                        version = '', ), 
                    uid = '', ),
                instant_message = titan_client.models.instant_message_schema.InstantMessageSchema(
                    activity = titan_client.models.instant_message_schema_activity.InstantMessageSchema_activity(
                        first = 56, 
                        last = 56, ), 
                    data = titan_client.models.instant_message_schema_data.InstantMessageSchema_data(
                        actor = titan_client.models.instant_message_schema_data_actor.InstantMessageSchema_data_actor(
                            handle = '', 
                            uid = '', ), 
                        channel = titan_client.models.instant_message_schema_data_channel.InstantMessageSchema_data_channel(
                            name = '', 
                            registration_date = 56, 
                            topic = '', 
                            uid = '', 
                            url = '', ), 
                        message = titan_client.models.instant_message_schema_data_message.InstantMessageSchema_data_message(
                            attachments = [
                                titan_client.models.instant_message_schema_data_message_attachments_inner.InstantMessageSchema_data_message_attachments_inner(
                                    height = 1.337, 
                                    original_url = '', 
                                    size = 1.337, 
                                    type = '', 
                                    uid = '', 
                                    width = 1.337, )
                                ], 
                            images = [
                                titan_client.models.image_schema.ImageSchema(
                                    dimension = '800x580', 
                                    hash = '36af534f2504fd7f9cc4a7096fa2988fec018f8997086eed803cc9e53052b3ad', 
                                    hash_type = 'SHA256', 
                                    image_original = 'https://api.intel471.com/v1/messagingServices/images/original/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f', 
                                    image_sanitized = 'https://api.intel471.com/v1/messagingServices/images/large/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f.webp', 
                                    ocr = '', 
                                    original_url = 'https://www.securitylab.ru/upload/iblock/487/4n6p9w4n9z84g24ok36gq6od2rnoikuh.jpg', 
                                    size = '145763', 
                                    status = 'validated', )
                                ], 
                            reply_uid = '', 
                            text = '', 
                            uid = '', ), 
                        server = titan_client.models.instant_message_schema_data_server.InstantMessageSchema_data_server(
                            name = '', 
                            service_type = '', 
                            uid = '', ), ), 
                    last_updated = 56, ),
                post = titan_client.models.post_schema.PostSchema(
                    date = 56, 
                    last_updated = 56, 
                    links = titan_client.models.post_schema_links.PostSchema_links(
                        author_actor = titan_client.models.post_schema_links_author_actor.PostSchema_links_authorActor(
                            handle = '', 
                            uid = '', ), 
                        forum = titan_client.models.post_schema_links_forum.PostSchema_links_forum(
                            description = '', 
                            name = '', 
                            uid = '', ), 
                        images = [
                            titan_client.models.image_schema.ImageSchema(
                                dimension = '800x580', 
                                hash = '36af534f2504fd7f9cc4a7096fa2988fec018f8997086eed803cc9e53052b3ad', 
                                hash_type = 'SHA256', 
                                image_original = 'https://api.intel471.com/v1/messagingServices/images/original/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f', 
                                image_sanitized = 'https://api.intel471.com/v1/messagingServices/images/large/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f.webp', 
                                ocr = '', 
                                original_url = 'https://www.securitylab.ru/upload/iblock/487/4n6p9w4n9z84g24ok36gq6od2rnoikuh.jpg', 
                                size = '145763', 
                                status = 'validated', )
                            ], 
                        thread = titan_client.models.post_schema_links_thread.PostSchema_links_thread(
                            count = 56, 
                            topic = '', 
                            topic_original = '', 
                            uid = '', ), ), 
                    message = '', 
                    message_original = '', 
                    uid = '', ),
                private_message = titan_client.models.private_message_schema.PrivateMessageSchema(
                    date = 56, 
                    last_updated = 56, 
                    links = titan_client.models.private_message_schema_links.PrivateMessageSchema_links(
                        author_actor = titan_client.models.private_message_schema_links_author_actor.PrivateMessageSchema_links_authorActor(
                            handle = '', 
                            uid = '', ), 
                        forum = titan_client.models.private_message_schema_links_forum.PrivateMessageSchema_links_forum(
                            description = '', 
                            name = '', 
                            uid = '', ), 
                        images = [
                            titan_client.models.image_schema.ImageSchema(
                                dimension = '800x580', 
                                hash = '36af534f2504fd7f9cc4a7096fa2988fec018f8997086eed803cc9e53052b3ad', 
                                hash_type = 'SHA256', 
                                image_original = 'https://api.intel471.com/v1/messagingServices/images/original/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f', 
                                image_sanitized = 'https://api.intel471.com/v1/messagingServices/images/large/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f/701c4587cfac817c12901b3244f628054a8a1791f3238f4920f258f0d86ce94f.webp', 
                                ocr = '', 
                                original_url = 'https://www.securitylab.ru/upload/iblock/487/4n6p9w4n9z84g24ok36gq6od2rnoikuh.jpg', 
                                size = '145763', 
                                status = 'validated', )
                            ], 
                        recipient_actor = titan_client.models.private_message_schema_links_recipient_actor.PrivateMessageSchema_links_recipientActor(
                            handle = '', 
                            uid = '', ), 
                        thread = titan_client.models.private_message_schema_links_thread.PrivateMessageSchema_links_thread(
                            uid = '', ), ), 
                    message = '', 
                    message_original = '', 
                    subject = '', 
                    subject_original = '', 
                    uid = '', ),
                report = titan_client.models.alert_list_schema_report.AlertListSchema_report(
                    admiralty_code = 'C3', 
                    date_of_information = 56, 
                    motivation = [
                        ''
                        ], 
                    portal_report_url = '', 
                    source_characterization = '', 
                    subject = '', 
                    uid = '', ),
                status = '',
                uid = '',
                watcher_group_uid = '',
                watcher_uid = ''
            )
        else:
            return AlertListSchema(
                found_time = 56,
                status = '',
                uid = '',
        )
        """

    def testAlertListSchema(self):
        """Test AlertListSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
