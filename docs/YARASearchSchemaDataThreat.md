# YARASearchSchemaDataThreat

Detailed information about a `threat`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**YARASearchSchemaDataThreatData**](YARASearchSchemaDataThreatData.md) |  | 
**type** | **str** | &#x60;Type&#x60; of threat: &#x60;malware&#x60;, &#x60;proxy_service&#x60; etc. | 
**uid** | **str** | Unique threat identifier. | 

## Example

```python
from titan_client.models.yara_search_schema_data_threat import YARASearchSchemaDataThreat

# TODO update the JSON string below
json = "{}"
# create an instance of YARASearchSchemaDataThreat from a JSON string
yara_search_schema_data_threat_instance = YARASearchSchemaDataThreat.from_json(json)
# print the JSON string representation of the object
print(YARASearchSchemaDataThreat.to_json())

# convert the object into a dict
yara_search_schema_data_threat_dict = yara_search_schema_data_threat_instance.to_dict()
# create an instance of YARASearchSchemaDataThreat from a dict
yara_search_schema_data_threat_from_dict = YARASearchSchemaDataThreat.from_dict(yara_search_schema_data_threat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


