# EventSchemaData

Sub-document containing event information. The fields returned in the API response vary based on available information and type of event. All the possible fields are listed here. For a typical response see the example for this endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_data** | [**EventSchemaDataEventData**](EventSchemaDataEventData.md) |  | 
**event_type** | **str** | Describes the type of event: &#x60;download_execute&#x60;, &#x60;start_ddos&#x60;, &#x60;execute_command&#x60;, &#x60;keylog&#x60;, &#x60;screenshot&#x60;, etc. | 
**intel_requirements** | **List[str]** | General Intelligence Requirements that match this observed event. | [optional] 
**mitre_tactics** | **str** | &#x60;MITRE ATT&amp;CK&#x60; tactic classification. | [optional] 
**threat** | [**EventSchemaDataThreat**](EventSchemaDataThreat.md) |  | 

## Example

```python
from titan_client.models.event_schema_data import EventSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaData from a JSON string
event_schema_data_instance = EventSchemaData.from_json(json)
# print the JSON string representation of the object
print(EventSchemaData.to_json())

# convert the object into a dict
event_schema_data_dict = event_schema_data_instance.to_dict()
# create an instance of EventSchemaData from a dict
event_schema_data_from_dict = EventSchemaData.from_dict(event_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


