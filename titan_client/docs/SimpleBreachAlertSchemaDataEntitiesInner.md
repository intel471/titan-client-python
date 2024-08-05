# SimpleBreachAlertSchemaDataEntitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Elaboration on the entity&#39;s value | [optional] 
**geo_info** | [**SimpleBreachAlertSchemaDataEntitiesInnerGeoInfo**](SimpleBreachAlertSchemaDataEntitiesInnerGeoInfo.md) |  | [optional] 
**type** | **str** | Entity &#x60;type&#x60;. | 
**value** | **str** | Entity &#x60;value&#x60;. | 

## Example

```python
from titan_client.models.simple_breach_alert_schema_data_entities_inner import SimpleBreachAlertSchemaDataEntitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleBreachAlertSchemaDataEntitiesInner from a JSON string
simple_breach_alert_schema_data_entities_inner_instance = SimpleBreachAlertSchemaDataEntitiesInner.from_json(json)
# print the JSON string representation of the object
print(SimpleBreachAlertSchemaDataEntitiesInner.to_json())

# convert the object into a dict
simple_breach_alert_schema_data_entities_inner_dict = simple_breach_alert_schema_data_entities_inner_instance.to_dict()
# create an instance of SimpleBreachAlertSchemaDataEntitiesInner from a dict
simple_breach_alert_schema_data_entities_inner_from_dict = SimpleBreachAlertSchemaDataEntitiesInner.from_dict(simple_breach_alert_schema_data_entities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


