# YARASearchSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**YARASearchSchemaActivity**](YARASearchSchemaActivity.md) |  | 
**data** | [**YARASearchSchemaData**](YARASearchSchemaData.md) |  | 
**last_updated** | **int** | YARA last modification date. | 
**meta** | [**YARASearchSchemaMeta**](YARASearchSchemaMeta.md) |  | 
**uid** | **str** | Unique YARA identifier. | 

## Example

```python
from titan_client.models.yara_search_schema import YARASearchSchema

# TODO update the JSON string below
json = "{}"
# create an instance of YARASearchSchema from a JSON string
yara_search_schema_instance = YARASearchSchema.from_json(json)
# print the JSON string representation of the object
print(YARASearchSchema.to_json())

# convert the object into a dict
yara_search_schema_dict = yara_search_schema_instance.to_dict()
# create an instance of YARASearchSchema from a dict
yara_search_schema_from_dict = YARASearchSchema.from_dict(yara_search_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


