# GirSchemaDataGir

Sub-document containing GIR information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | GIR &#x60;description&#x60;. | [optional] 
**name** | **str** | GIR &#x60;name&#x60;. | 
**parent** | **object** | &#x60;GIR&#x60; that is &#x60;parent&#x60; of the current one. Has the same structure as described above and may also contain &#x60;parent&#x60; &#x60;GIR&#x60;s. &lt;br /&gt;If GIR has a &#x60;parent&#x60; object, &#x60;parent&#x60; will contain a &#x60;path&#x60; and &#x60;name&#x60; field and optionally description and another &#x60;parent&#x60; object. | [optional] 
**path** | **str** | GIR &#x60;path&#x60;. | 

## Example

```python
from titan_client.models.gir_schema_data_gir import GirSchemaDataGir

# TODO update the JSON string below
json = "{}"
# create an instance of GirSchemaDataGir from a JSON string
gir_schema_data_gir_instance = GirSchemaDataGir.from_json(json)
# print the JSON string representation of the object
print(GirSchemaDataGir.to_json())

# convert the object into a dict
gir_schema_data_gir_dict = gir_schema_data_gir_instance.to_dict()
# create an instance of GirSchemaDataGir from a dict
gir_schema_data_gir_from_dict = GirSchemaDataGir.from_dict(gir_schema_data_gir_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


