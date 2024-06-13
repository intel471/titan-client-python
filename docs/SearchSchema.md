# SearchSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_total_count** | **int** | Total count of matched actors. | 
**actors** | [**list[SimpleActorSchema]**](SimpleActorSchema.md) | List of [Actors](#tag/Actors/paths/~1actors/get). | [optional] 
**breach_alerts** | [**list[SimpleBreachAlertSchema]**](SimpleBreachAlertSchema.md) | List of [Breach Alerts](#tag/Reports/paths/~1breachAlerts/get). | [optional] 
**breach_alerts_total_count** | **int** | Total count of matched breach alerts. | 
**credential_occurrences** | [**list[CredentialOccurrenceSchema]**](CredentialOccurrenceSchema.md) | List of [Credential occurrences](#tag/Credentials/paths/~1credentials~1occurrences/get). | [optional] 
**credential_occurrences_total_count** | **int** | Total count of matched credentials occurrences. | 
**credential_sets** | [**list[CredentialSetSchema]**](CredentialSetSchema.md) | List of [Credential sets](#tag/Credentials/paths/~1credentialSets/get). | [optional] 
**credential_sets_total_count** | **int** | Total count of matched credential sets. | 
**credentials** | [**list[CredentialSchema]**](CredentialSchema.md) | List of [Credentials](#tag/Credentials/paths/~1credentials/get). | [optional] 
**credentials_total_count** | **int** | Total count of matched credentials. | 
**cve_reports** | [**list[SimpleCveSchema]**](SimpleCveSchema.md) | List of [Cve Reports](#tag/Vulnerabilities/paths/~1cve~1reports/get). | [optional] 
**cve_reports_total_count** | **int** | Total count of matched vulnerability reports. | 
**data_leak_post_total_count** | **int** | Total count of matched data leak posts. | 
**data_leak_posts** | [**list[DataLeakPostSchema]**](DataLeakPostSchema.md) | List of [Data Leak Blogs](#tag/Data-Leak-Blogs/paths/~1dataleak~1posts/get). | [optional] 
**entities** | [**list[EntitiesSchema]**](EntitiesSchema.md) | List of [Entities](#tag/Entities/paths/~1entities/get). | [optional] 
**entity_total_count** | **int** | Total count of matched entities. | 
**event_total_count** | **int** | Total count of matched events. | 
**events** | [**list[EventSchema]**](EventSchema.md) | List of [Events](#tag/Events/paths/~1events/get). | [optional] 
**indicator_total_count** | **int** | Total count of matched indicators. | 
**indicators** | [**list[IndicatorSearchSchema]**](IndicatorSearchSchema.md) | List of [Indicators](#tag/Indicators/paths/~1indicators/get). | [optional] 
**instant_message_total_count** | **int** | Total count of matched instant messages. | 
**instant_messages** | [**list[InstantMessageSchema]**](InstantMessageSchema.md) | List of [Instant Messages](#tag/Messaging-Services/paths/~1messagingServices~1instantMessages/get). | [optional] 
**ioc_total_count** | **int** | Total count of matched IOCs. | 
**iocs** | [**list[IocSchema]**](IocSchema.md) | List of [Indicators of compromise](#tag/Indicators/paths/~1indicators/get). | [optional] 
**malware_report_total_count** | **int** | Total count of matched malware reports. | 
**malware_reports** | [**list[MalwareReportsSearchSchema]**](MalwareReportsSearchSchema.md) | List of [Malware Reports](#tag/Malware/paths/~1malwareReports/get). | [optional] 
**news** | [**list[NewsSchema]**](NewsSchema.md) | List of [News](#tag/News/paths/~1news/get). | [optional] 
**news_total_count** | **int** | Total count of matched news. | 
**post_total_count** | **int** | Total count of matched posts. | 
**posts** | [**list[PostSchema]**](PostSchema.md) | List of [Posts](#tag/Forums/paths/~1posts/get). | [optional] 
**private_message_total_count** | **int** | Total count of matched private messages. | 
**private_messages** | [**list[PrivateMessageSchema]**](PrivateMessageSchema.md) | List of [PrivateMessages](#tag/Forums/paths/~1privateMessages/get). | [optional] 
**report_total_count** | **int** | Total count of matched information or fintel reports. | 
**reports** | [**list[SimpleReportSchema]**](SimpleReportSchema.md) | List of [Information Reports] or [Fintel Reports]() ordered by creation time descending.  In version 1.3.0 reports also include new field &#x60;actorSubjectOfReport&#x60; with actors, mentioned in report subject. | [optional] 
**situation_reports** | [**list[SituationReportSchema]**](SituationReportSchema.md) | List of [Situation Reports](#tag/Global-Search/paths/~1search/get). | [optional] 
**situation_reports_total_count** | **int** | Total count of matched situation reports. | 
**spot_reports** | [**list[SimpleSpotReportSchema]**](SimpleSpotReportSchema.md) | List of [Spot Reports](#tag/Reports/paths/~1spotReports/get). | [optional] 
**spot_reports_total_count** | **int** | Total count of matched spot reports. | 
**yara_total_count** | **int** | Total count of matched yaras. | 
**yaras** | [**list[YARASearchSchema]**](YARASearchSchema.md) | List of [YARA](#tag/YARA/paths/~1yara/get). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


