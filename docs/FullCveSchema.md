# FullCveSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**SimpleCveSchemaActivity**](SimpleCveSchemaActivity.md) |  | 
**classification** | [**SimpleCveSchemaClassification**](SimpleCveSchemaClassification.md) |  | [optional] 
**data** | [**SimpleCveSchemaData**](SimpleCveSchemaData.md) |  | 
**last_updated** | **int** | CVE report last modification date. | 
**uid** | **str** | Unique report identifier. | 

## Example

```python
from titan_client.models.full_cve_schema import FullCveSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FullCveSchema from a JSON string
full_cve_schema_instance = FullCveSchema.from_json(json)
# print the JSON string representation of the object
print(FullCveSchema.to_json())

# convert the object into a dict
full_cve_schema_dict = full_cve_schema_instance.to_dict()
# create an instance of FullCveSchema from a dict
full_cve_schema_from_dict = FullCveSchema.from_dict(full_cve_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


