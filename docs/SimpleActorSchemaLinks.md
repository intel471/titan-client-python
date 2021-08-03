# SimpleActorSchemaLinks

Linked data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forum_post_total_count** | **int** | Total count of linked posts. | 
**forum_private_message_total_count** | **int** | Total count of linked private messages. | 
**forum_total_count** | **int** | Total count of linked forums. | 
**forums** | [**list[SimpleActorSchemaLinksForums]**](SimpleActorSchemaLinksForums.md) | Linked forums. | [optional] 
**instant_message_channel_total_count** | **int** | Total count of instant messaging channels of particular server actor participated in. | 
**instant_message_server_total_count** | **int** | Total count of linked instant messaging servers. | 
**instant_message_servers** | [**list[SimpleActorSchemaLinksInstantMessageServers]**](SimpleActorSchemaLinksInstantMessageServers.md) | Linked instant messaging servers. | [optional] 
**instant_message_total_count** | **int** | Total count of instant messages actor has written on particular server. | 
**report_total_count** | **int** | Total count of linked reports. | 
**reports** | [**list[SimpleReportSchema]**](SimpleReportSchema.md) | Linked reports. Array of simplified version of one of the following: &#x60;Information Report&#x60;, &#x60;Fintel Report&#x60;, &#x60;Malware Report&#x60;, &#x60;Spot Report&#x60;, &#x60;Situation Report&#x60;, &#x60;Breach Alert&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


