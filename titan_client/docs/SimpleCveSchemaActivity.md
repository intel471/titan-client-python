# SimpleCveSchemaActivity

Period an event message was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the event activity range. | 
**last** | **int** | End of the event activity range. | 

## Example

```python
from titan_client.models.simple_cve_schema_activity import SimpleCveSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCveSchemaActivity from a JSON string
simple_cve_schema_activity_instance = SimpleCveSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(SimpleCveSchemaActivity.to_json())

# convert the object into a dict
simple_cve_schema_activity_dict = simple_cve_schema_activity_instance.to_dict()
# create an instance of SimpleCveSchemaActivity from a dict
simple_cve_schema_activity_from_dict = SimpleCveSchemaActivity.from_dict(simple_cve_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


