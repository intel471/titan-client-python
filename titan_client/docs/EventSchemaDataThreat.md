# EventSchemaDataThreat

Detailed information about a `threat`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventSchemaDataThreatData**](EventSchemaDataThreatData.md) |  | 
**type** | **str** | Threat &#x60;type&#x60;: &#x60;malware&#x60;, &#x60;proxy_service&#x60; etc. | [optional] 
**uid** | **str** | Unique threat identifier. | 

## Example

```python
from titan_client.models.event_schema_data_threat import EventSchemaDataThreat

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaDataThreat from a JSON string
event_schema_data_threat_instance = EventSchemaDataThreat.from_json(json)
# print the JSON string representation of the object
print(EventSchemaDataThreat.to_json())

# convert the object into a dict
event_schema_data_threat_dict = event_schema_data_threat_instance.to_dict()
# create an instance of EventSchemaDataThreat from a dict
event_schema_data_threat_from_dict = EventSchemaDataThreat.from_dict(event_schema_data_threat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


