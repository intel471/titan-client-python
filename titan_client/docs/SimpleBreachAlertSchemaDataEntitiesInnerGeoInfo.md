# SimpleBreachAlertSchemaDataEntitiesInnerGeoInfo

Optional field, present only for `IP Address` entities contains the registered geolocation for the IP from `value` field, if any available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Country of the IP&#39;s registration | 
**provider** | **str** | Registrant for the IP address | 

## Example

```python
from titan_client.models.simple_breach_alert_schema_data_entities_inner_geo_info import SimpleBreachAlertSchemaDataEntitiesInnerGeoInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleBreachAlertSchemaDataEntitiesInnerGeoInfo from a JSON string
simple_breach_alert_schema_data_entities_inner_geo_info_instance = SimpleBreachAlertSchemaDataEntitiesInnerGeoInfo.from_json(json)
# print the JSON string representation of the object
print(SimpleBreachAlertSchemaDataEntitiesInnerGeoInfo.to_json())

# convert the object into a dict
simple_breach_alert_schema_data_entities_inner_geo_info_dict = simple_breach_alert_schema_data_entities_inner_geo_info_instance.to_dict()
# create an instance of SimpleBreachAlertSchemaDataEntitiesInnerGeoInfo from a dict
simple_breach_alert_schema_data_entities_inner_geo_info_from_dict = SimpleBreachAlertSchemaDataEntitiesInnerGeoInfo.from_dict(simple_breach_alert_schema_data_entities_inner_geo_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


