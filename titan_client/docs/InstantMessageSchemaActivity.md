# InstantMessageSchemaActivity

Period an instant message was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the instant message activity range. | 
**last** | **int** | End of the instant message activity range. | 

## Example

```python
from titan_client.models.instant_message_schema_activity import InstantMessageSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMessageSchemaActivity from a JSON string
instant_message_schema_activity_instance = InstantMessageSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(InstantMessageSchemaActivity.to_json())

# convert the object into a dict
instant_message_schema_activity_dict = instant_message_schema_activity_instance.to_dict()
# create an instance of InstantMessageSchemaActivity from a dict
instant_message_schema_activity_from_dict = InstantMessageSchemaActivity.from_dict(instant_message_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


