# SimpleBreachAlertSchemaDataBreachAlertVictim

Purported victim information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Purported victim&#39;s &#x60;country&#x60;. | [optional] 
**industries** | [**List[SimpleBreachAlertSchemaDataBreachAlertVictimIndustriesInner]**](SimpleBreachAlertSchemaDataBreachAlertVictimIndustriesInner.md) | Purported victim&#39;s &#x60;industries&#x60;. | 
**name** | **str** | Purported victim&#39;s &#x60;name&#x60;. | 
**region** | **str** | Purported victim&#39;s &#x60;region&#x60;. | 
**revenue** | **str** | Purported victim&#39;s &#x60;revenue&#x60;. | 
**urls** | **List[str]** | List of purported victim&#39;s &#x60;urls&#x60;. | 

## Example

```python
from titan_client.models.simple_breach_alert_schema_data_breach_alert_victim import SimpleBreachAlertSchemaDataBreachAlertVictim

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleBreachAlertSchemaDataBreachAlertVictim from a JSON string
simple_breach_alert_schema_data_breach_alert_victim_instance = SimpleBreachAlertSchemaDataBreachAlertVictim.from_json(json)
# print the JSON string representation of the object
print(SimpleBreachAlertSchemaDataBreachAlertVictim.to_json())

# convert the object into a dict
simple_breach_alert_schema_data_breach_alert_victim_dict = simple_breach_alert_schema_data_breach_alert_victim_instance.to_dict()
# create an instance of SimpleBreachAlertSchemaDataBreachAlertVictim from a dict
simple_breach_alert_schema_data_breach_alert_victim_from_dict = SimpleBreachAlertSchemaDataBreachAlertVictim.from_dict(simple_breach_alert_schema_data_breach_alert_victim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


