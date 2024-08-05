# SimpleActorSchemaLinksInstantMessageServersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | IM server name. | [optional] 
**service_type** | **str** | Type of IM service (Telegram, Discord, IRC etc.). | 
**uid** | **str** | Unique IM server identifier. | 

## Example

```python
from titan_client.models.simple_actor_schema_links_instant_message_servers_inner import SimpleActorSchemaLinksInstantMessageServersInner

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleActorSchemaLinksInstantMessageServersInner from a JSON string
simple_actor_schema_links_instant_message_servers_inner_instance = SimpleActorSchemaLinksInstantMessageServersInner.from_json(json)
# print the JSON string representation of the object
print(SimpleActorSchemaLinksInstantMessageServersInner.to_json())

# convert the object into a dict
simple_actor_schema_links_instant_message_servers_inner_dict = simple_actor_schema_links_instant_message_servers_inner_instance.to_dict()
# create an instance of SimpleActorSchemaLinksInstantMessageServersInner from a dict
simple_actor_schema_links_instant_message_servers_inner_from_dict = SimpleActorSchemaLinksInstantMessageServersInner.from_dict(simple_actor_schema_links_instant_message_servers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


