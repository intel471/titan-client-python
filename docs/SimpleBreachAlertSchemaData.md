# SimpleBreachAlertSchemaData

Sub-document containing Breach Alert and linked to it `entities`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breach_alert** | [**SimpleBreachAlertSchemaDataBreachAlert**](SimpleBreachAlertSchemaDataBreachAlert.md) |  | 
**entities** | [**List[SimpleBreachAlertSchemaDataEntitiesInner]**](SimpleBreachAlertSchemaDataEntitiesInner.md) | List of &#x60;entities&#x60;. | [optional] 

## Example

```python
from titan_client.models.simple_breach_alert_schema_data import SimpleBreachAlertSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleBreachAlertSchemaData from a JSON string
simple_breach_alert_schema_data_instance = SimpleBreachAlertSchemaData.from_json(json)
# print the JSON string representation of the object
print(SimpleBreachAlertSchemaData.to_json())

# convert the object into a dict
simple_breach_alert_schema_data_dict = simple_breach_alert_schema_data_instance.to_dict()
# create an instance of SimpleBreachAlertSchemaData from a dict
simple_breach_alert_schema_data_from_dict = SimpleBreachAlertSchemaData.from_dict(simple_breach_alert_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


