# SimpleBreachAlertSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**SimpleBreachAlertSchemaActivity**](SimpleBreachAlertSchemaActivity.md) |  | 
**data** | [**SimpleBreachAlertSchemaData**](SimpleBreachAlertSchemaData.md) |  | 
**last_updated** | **int** | Breach Alert last modification date. | 
**uid** | **str** | Unique Breach Alert identifier. | 

## Example

```python
from titan_client.models.simple_breach_alert_schema import SimpleBreachAlertSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleBreachAlertSchema from a JSON string
simple_breach_alert_schema_instance = SimpleBreachAlertSchema.from_json(json)
# print the JSON string representation of the object
print(SimpleBreachAlertSchema.to_json())

# convert the object into a dict
simple_breach_alert_schema_dict = simple_breach_alert_schema_instance.to_dict()
# create an instance of SimpleBreachAlertSchema from a dict
simple_breach_alert_schema_from_dict = SimpleBreachAlertSchema.from_dict(simple_breach_alert_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


