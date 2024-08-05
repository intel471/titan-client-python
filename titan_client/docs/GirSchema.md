# GirSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GirSchemaData**](GirSchemaData.md) |  | 
**uid** | **str** | Unique GIR identifier. | 

## Example

```python
from titan_client.models.gir_schema import GirSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GirSchema from a JSON string
gir_schema_instance = GirSchema.from_json(json)
# print the JSON string representation of the object
print(GirSchema.to_json())

# convert the object into a dict
gir_schema_dict = gir_schema_instance.to_dict()
# create an instance of GirSchema from a dict
gir_schema_from_dict = GirSchema.from_dict(gir_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


