# EventSchemaDataEventDataLocation

The `url` object of the location of the event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | **str** | IPv4 address. | [optional] 
**url** | **str** | Url string. | [optional] 

## Example

```python
from titan_client.models.event_schema_data_event_data_location import EventSchemaDataEventDataLocation

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaDataEventDataLocation from a JSON string
event_schema_data_event_data_location_instance = EventSchemaDataEventDataLocation.from_json(json)
# print the JSON string representation of the object
print(EventSchemaDataEventDataLocation.to_json())

# convert the object into a dict
event_schema_data_event_data_location_dict = event_schema_data_event_data_location_instance.to_dict()
# create an instance of EventSchemaDataEventDataLocation from a dict
event_schema_data_event_data_location_from_dict = EventSchemaDataEventDataLocation.from_dict(event_schema_data_event_data_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


