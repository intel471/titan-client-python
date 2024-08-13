# EventSchemaDataThreatData

Additional details about a threat such as `service provider`, `malware family`, `malware family version`, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** | Malware &#x60;family&#x60;: &#x60;gozi_isfb&#x60;, &#x60;smokeloader&#x60;, &#x60;trickbot&#x60;, etc. (for &#x60;malware&#x60; threat type). | [optional] 
**malware_family_profile_uid** | **str** | Malware family profile UID. | [optional] 
**variant** | **str** | &#x60;Variant&#x60; of the threat. | [optional] 
**version** | **str** | &#x60;Version&#x60; of the threat. | [optional] 

## Example

```python
from titan_client.models.event_schema_data_threat_data import EventSchemaDataThreatData

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaDataThreatData from a JSON string
event_schema_data_threat_data_instance = EventSchemaDataThreatData.from_json(json)
# print the JSON string representation of the object
print(EventSchemaDataThreatData.to_json())

# convert the object into a dict
event_schema_data_threat_data_dict = event_schema_data_threat_data_instance.to_dict()
# create an instance of EventSchemaDataThreatData from a dict
event_schema_data_threat_data_from_dict = EventSchemaDataThreatData.from_dict(event_schema_data_threat_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


