# SimpleActorSchemaLinks

Linked data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forum_post_total_count** | **int** | Total count of linked posts. | 
**forum_private_message_total_count** | **int** | Total count of linked private messages. | 
**forum_total_count** | **int** | Total count of linked forums. | 
**forums** | [**List[SimpleActorSchemaLinksForumsInner]**](SimpleActorSchemaLinksForumsInner.md) | Linked forums. | [optional] 
**instant_message_channel_total_count** | **int** | Total count of instant messaging channels of particular server actor participated in. | 
**instant_message_server_total_count** | **int** | Total count of linked instant messaging servers. | 
**instant_message_servers** | [**List[SimpleActorSchemaLinksInstantMessageServersInner]**](SimpleActorSchemaLinksInstantMessageServersInner.md) | Linked instant messaging servers. | [optional] 
**instant_message_total_count** | **int** | Total count of instant messages actor has written on particular server. | 
**report_total_count** | **int** | Total count of linked reports. | 
**reports** | [**List[SimpleReportSchema]**](SimpleReportSchema.md) | Linked reports. Array of simplified version of one of the following: &#x60;Information Report&#x60;, &#x60;Fintel Report&#x60;, &#x60;Malware Report&#x60;, &#x60;Spot Report&#x60;, &#x60;Situation Report&#x60;, &#x60;Breach Alert&#x60;. | [optional] 

## Example

```python
from titan_client.models.simple_actor_schema_links import SimpleActorSchemaLinks

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleActorSchemaLinks from a JSON string
simple_actor_schema_links_instance = SimpleActorSchemaLinks.from_json(json)
# print the JSON string representation of the object
print(SimpleActorSchemaLinks.to_json())

# convert the object into a dict
simple_actor_schema_links_dict = simple_actor_schema_links_instance.to_dict()
# create an instance of SimpleActorSchemaLinks from a dict
simple_actor_schema_links_from_dict = SimpleActorSchemaLinks.from_dict(simple_actor_schema_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


