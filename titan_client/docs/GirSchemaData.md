# GirSchemaData

Sub-document containing GIR data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gir** | [**GirSchemaDataGir**](GirSchemaDataGir.md) |  | 

## Example

```python
from titan_client.models.gir_schema_data import GirSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of GirSchemaData from a JSON string
gir_schema_data_instance = GirSchemaData.from_json(json)
# print the JSON string representation of the object
print(GirSchemaData.to_json())

# convert the object into a dict
gir_schema_data_dict = gir_schema_data_instance.to_dict()
# create an instance of GirSchemaData from a dict
gir_schema_data_from_dict = GirSchemaData.from_dict(gir_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


