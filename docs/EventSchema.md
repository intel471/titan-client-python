# EventSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**EventSchemaActivity**](EventSchemaActivity.md) |  | 
**data** | [**EventSchemaData**](EventSchemaData.md) |  | 
**last_updated** | **int** | Event last modification date. | 
**meta** | [**EventSchemaMeta**](EventSchemaMeta.md) |  | 
**uid** | **str** | Unique event identifier. | 

## Example

```python
from titan_client.models.event_schema import EventSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchema from a JSON string
event_schema_instance = EventSchema.from_json(json)
# print the JSON string representation of the object
print(EventSchema.to_json())

# convert the object into a dict
event_schema_dict = event_schema_instance.to_dict()
# create an instance of EventSchema from a dict
event_schema_from_dict = EventSchema.from_dict(event_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


