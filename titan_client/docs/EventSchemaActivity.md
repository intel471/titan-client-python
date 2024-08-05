# EventSchemaActivity

Period an event message was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the event activity range. | 
**last** | **int** | End of the event activity range. | 

## Example

```python
from titan_client.models.event_schema_activity import EventSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaActivity from a JSON string
event_schema_activity_instance = EventSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(EventSchemaActivity.to_json())

# convert the object into a dict
event_schema_activity_dict = event_schema_activity_instance.to_dict()
# create an instance of EventSchemaActivity from a dict
event_schema_activity_from_dict = EventSchemaActivity.from_dict(event_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


