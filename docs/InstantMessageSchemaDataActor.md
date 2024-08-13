# InstantMessageSchemaDataActor

Sub-document containing actor information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle** | **str** | Actor&#39;s &#x60;handle&#x60;. Actual for the moment message was written. | [optional] 
**uid** | **str** | Unique actor identifier. | 

## Example

```python
from titan_client.models.instant_message_schema_data_actor import InstantMessageSchemaDataActor

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMessageSchemaDataActor from a JSON string
instant_message_schema_data_actor_instance = InstantMessageSchemaDataActor.from_json(json)
# print the JSON string representation of the object
print(InstantMessageSchemaDataActor.to_json())

# convert the object into a dict
instant_message_schema_data_actor_dict = instant_message_schema_data_actor_instance.to_dict()
# create an instance of InstantMessageSchemaDataActor from a dict
instant_message_schema_data_actor_from_dict = InstantMessageSchemaDataActor.from_dict(instant_message_schema_data_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


