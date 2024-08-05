# EventSchemaDataEventDataControllerGeoIpIsp

ISP details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autonomous_system** | **str** | Autonomous System | [optional] 
**isp** | **str** | ISP name | [optional] 
**network** | **str** | Network | [optional] 
**organization** | **str** | Organization | [optional] 

## Example

```python
from titan_client.models.event_schema_data_event_data_controller_geo_ip_isp import EventSchemaDataEventDataControllerGeoIpIsp

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaDataEventDataControllerGeoIpIsp from a JSON string
event_schema_data_event_data_controller_geo_ip_isp_instance = EventSchemaDataEventDataControllerGeoIpIsp.from_json(json)
# print the JSON string representation of the object
print(EventSchemaDataEventDataControllerGeoIpIsp.to_json())

# convert the object into a dict
event_schema_data_event_data_controller_geo_ip_isp_dict = event_schema_data_event_data_controller_geo_ip_isp_instance.to_dict()
# create an instance of EventSchemaDataEventDataControllerGeoIpIsp from a dict
event_schema_data_event_data_controller_geo_ip_isp_from_dict = EventSchemaDataEventDataControllerGeoIpIsp.from_dict(event_schema_data_event_data_controller_geo_ip_isp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


