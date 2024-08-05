# SimpleBreachAlertSchemaActivity

Period Breach Alert was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the Breach Alert activity range. | 
**last** | **int** | End of the Breach Alert activity range. | 

## Example

```python
from titan_client.models.simple_breach_alert_schema_activity import SimpleBreachAlertSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleBreachAlertSchemaActivity from a JSON string
simple_breach_alert_schema_activity_instance = SimpleBreachAlertSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(SimpleBreachAlertSchemaActivity.to_json())

# convert the object into a dict
simple_breach_alert_schema_activity_dict = simple_breach_alert_schema_activity_instance.to_dict()
# create an instance of SimpleBreachAlertSchemaActivity from a dict
simple_breach_alert_schema_activity_from_dict = SimpleBreachAlertSchemaActivity.from_dict(simple_breach_alert_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


