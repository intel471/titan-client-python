# YARASearchSchemaDataThreatData

Additional details about a threat such as service `provider`, `malware family`, `malware family version` etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** | &#x60;Family&#x60; of malware &#x60;gozi_isfb&#x60;, &#x60;smokeloader&#x60;, &#x60;trickbot&#x60; etc (for &#x60;malware&#x60; threat type). | [optional] 
**malware_family_profile_uid** | **str** | Malware family profile UID. | [optional] 
**version** | **str** | &#x60;Version&#x60; of threat. | [optional] 

## Example

```python
from titan_client.models.yara_search_schema_data_threat_data import YARASearchSchemaDataThreatData

# TODO update the JSON string below
json = "{}"
# create an instance of YARASearchSchemaDataThreatData from a JSON string
yara_search_schema_data_threat_data_instance = YARASearchSchemaDataThreatData.from_json(json)
# print the JSON string representation of the object
print(YARASearchSchemaDataThreatData.to_json())

# convert the object into a dict
yara_search_schema_data_threat_data_dict = yara_search_schema_data_threat_data_instance.to_dict()
# create an instance of YARASearchSchemaDataThreatData from a dict
yara_search_schema_data_threat_data_from_dict = YARASearchSchemaDataThreatData.from_dict(yara_search_schema_data_threat_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


