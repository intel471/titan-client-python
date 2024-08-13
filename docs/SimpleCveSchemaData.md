# SimpleCveSchemaData

Sub-document containing CVE data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_report** | [**SimpleCveSchemaDataCveReport**](SimpleCveSchemaDataCveReport.md) |  | 

## Example

```python
from titan_client.models.simple_cve_schema_data import SimpleCveSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCveSchemaData from a JSON string
simple_cve_schema_data_instance = SimpleCveSchemaData.from_json(json)
# print the JSON string representation of the object
print(SimpleCveSchemaData.to_json())

# convert the object into a dict
simple_cve_schema_data_dict = simple_cve_schema_data_instance.to_dict()
# create an instance of SimpleCveSchemaData from a dict
simple_cve_schema_data_from_dict = SimpleCveSchemaData.from_dict(simple_cve_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


