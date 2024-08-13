# EventSchemaDataEventDataController

Object containing the `url` and `ipv4` of a `controller`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_ip** | [**EventSchemaDataEventDataControllerGeoIp**](EventSchemaDataEventDataControllerGeoIp.md) |  | [optional] 
**ipv4** | **str** | The &#x60;ipv4&#x60; of a controller | [optional] 
**url** | **str** | The &#x60;url&#x60; of a controller. | [optional] 

## Example

```python
from titan_client.models.event_schema_data_event_data_controller import EventSchemaDataEventDataController

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaDataEventDataController from a JSON string
event_schema_data_event_data_controller_instance = EventSchemaDataEventDataController.from_json(json)
# print the JSON string representation of the object
print(EventSchemaDataEventDataController.to_json())

# convert the object into a dict
event_schema_data_event_data_controller_dict = event_schema_data_event_data_controller_instance.to_dict()
# create an instance of EventSchemaDataEventDataController from a dict
event_schema_data_event_data_controller_from_dict = EventSchemaDataEventDataController.from_dict(event_schema_data_event_data_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


