# EventSchemaDataEventDataControllerGeoIp

Geo IP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City | [optional] 
**country** | **str** | Country | [optional] 
**country_code** | **str** | Country code | [optional] 
**isp** | [**EventSchemaDataEventDataControllerGeoIpIsp**](EventSchemaDataEventDataControllerGeoIpIsp.md) |  | [optional] 
**subdivision** | **List[str]** | Subdivision | [optional] 

## Example

```python
from titan_client.models.event_schema_data_event_data_controller_geo_ip import EventSchemaDataEventDataControllerGeoIp

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaDataEventDataControllerGeoIp from a JSON string
event_schema_data_event_data_controller_geo_ip_instance = EventSchemaDataEventDataControllerGeoIp.from_json(json)
# print the JSON string representation of the object
print(EventSchemaDataEventDataControllerGeoIp.to_json())

# convert the object into a dict
event_schema_data_event_data_controller_geo_ip_dict = event_schema_data_event_data_controller_geo_ip_instance.to_dict()
# create an instance of EventSchemaDataEventDataControllerGeoIp from a dict
event_schema_data_event_data_controller_geo_ip_from_dict = EventSchemaDataEventDataControllerGeoIp.from_dict(event_schema_data_event_data_controller_geo_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


