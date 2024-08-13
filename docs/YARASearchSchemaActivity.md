# YARASearchSchemaActivity

Period YARA was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the YARA activity range. | 
**last** | **int** | End of the YARA activity range. | 

## Example

```python
from titan_client.models.yara_search_schema_activity import YARASearchSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of YARASearchSchemaActivity from a JSON string
yara_search_schema_activity_instance = YARASearchSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(YARASearchSchemaActivity.to_json())

# convert the object into a dict
yara_search_schema_activity_dict = yara_search_schema_activity_instance.to_dict()
# create an instance of YARASearchSchemaActivity from a dict
yara_search_schema_activity_from_dict = YARASearchSchemaActivity.from_dict(yara_search_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


