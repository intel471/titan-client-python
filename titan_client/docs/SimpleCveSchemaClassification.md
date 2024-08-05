# SimpleCveSchemaClassification

`Classification` of reports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intel_requirements** | **List[str]** | General Intel Requirements (GIR). | [optional] 

## Example

```python
from titan_client.models.simple_cve_schema_classification import SimpleCveSchemaClassification

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCveSchemaClassification from a JSON string
simple_cve_schema_classification_instance = SimpleCveSchemaClassification.from_json(json)
# print the JSON string representation of the object
print(SimpleCveSchemaClassification.to_json())

# convert the object into a dict
simple_cve_schema_classification_dict = simple_cve_schema_classification_instance.to_dict()
# create an instance of SimpleCveSchemaClassification from a dict
simple_cve_schema_classification_from_dict = SimpleCveSchemaClassification.from_dict(simple_cve_schema_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


