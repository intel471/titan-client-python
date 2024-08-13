# YARASearchSchemaData

Sub-document containing YARA information. Might contain fields specific for different YARA types which are not described in current documentation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **str** | &#x60;Confidence&#x60; of YARA: &#x60;high&#x60; — recommended for blocking, &#x60;medium&#x60; — for alerting, &#x60;low&#x60; — needs to be verified. | 
**intel_requirements** | **List[str]** | List of General Intelligence Requirements matching this YARA. | [optional] 
**threat** | [**YARASearchSchemaDataThreat**](YARASearchSchemaDataThreat.md) |  | 
**yara_data** | [**YARASearchSchemaDataYaraData**](YARASearchSchemaDataYaraData.md) |  | 

## Example

```python
from titan_client.models.yara_search_schema_data import YARASearchSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of YARASearchSchemaData from a JSON string
yara_search_schema_data_instance = YARASearchSchemaData.from_json(json)
# print the JSON string representation of the object
print(YARASearchSchemaData.to_json())

# convert the object into a dict
yara_search_schema_data_dict = yara_search_schema_data_instance.to_dict()
# create an instance of YARASearchSchemaData from a dict
yara_search_schema_data_from_dict = YARASearchSchemaData.from_dict(yara_search_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


