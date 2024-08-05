# YARASearchSchemaDataYaraData

Sub-document containing YARA type and value(s).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | **str** | &#x60;Signature&#x60; of YARA rule. | [optional] 
**title** | **str** | &#x60;Title&#x60; of YARA rule. | [optional] 

## Example

```python
from titan_client.models.yara_search_schema_data_yara_data import YARASearchSchemaDataYaraData

# TODO update the JSON string below
json = "{}"
# create an instance of YARASearchSchemaDataYaraData from a JSON string
yara_search_schema_data_yara_data_instance = YARASearchSchemaDataYaraData.from_json(json)
# print the JSON string representation of the object
print(YARASearchSchemaDataYaraData.to_json())

# convert the object into a dict
yara_search_schema_data_yara_data_dict = yara_search_schema_data_yara_data_instance.to_dict()
# create an instance of YARASearchSchemaDataYaraData from a dict
yara_search_schema_data_yara_data_from_dict = YARASearchSchemaDataYaraData.from_dict(yara_search_schema_data_yara_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


