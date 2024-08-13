# SimpleBreachAlertSchemaDataBreachAlertConfidence

`Confidence` of a breach: `high` — recommended to engage immediate countermeasures, `medium` — for potential threat alerting and double-checking systems, `low` — needs to be verified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description for the actual level. | 
**level** | **str** | Level of confidence | 

## Example

```python
from titan_client.models.simple_breach_alert_schema_data_breach_alert_confidence import SimpleBreachAlertSchemaDataBreachAlertConfidence

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleBreachAlertSchemaDataBreachAlertConfidence from a JSON string
simple_breach_alert_schema_data_breach_alert_confidence_instance = SimpleBreachAlertSchemaDataBreachAlertConfidence.from_json(json)
# print the JSON string representation of the object
print(SimpleBreachAlertSchemaDataBreachAlertConfidence.to_json())

# convert the object into a dict
simple_breach_alert_schema_data_breach_alert_confidence_dict = simple_breach_alert_schema_data_breach_alert_confidence_instance.to_dict()
# create an instance of SimpleBreachAlertSchemaDataBreachAlertConfidence from a dict
simple_breach_alert_schema_data_breach_alert_confidence_from_dict = SimpleBreachAlertSchemaDataBreachAlertConfidence.from_dict(simple_breach_alert_schema_data_breach_alert_confidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


