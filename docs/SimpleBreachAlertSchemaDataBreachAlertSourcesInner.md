# SimpleBreachAlertSchemaDataBreachAlertSourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | Date of source publication or information acquisition. | 
**source_type** | **str** | Description of source information&#39;s type. | 
**title** | **str** | The &#x60;title&#x60; of the source. | 
**type** | **str** | Source &#x60;type&#x60;, external or internal. | 
**url** | **str** | Source link, an absolute &#x60;url&#x60;. | 

## Example

```python
from titan_client.models.simple_breach_alert_schema_data_breach_alert_sources_inner import SimpleBreachAlertSchemaDataBreachAlertSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleBreachAlertSchemaDataBreachAlertSourcesInner from a JSON string
simple_breach_alert_schema_data_breach_alert_sources_inner_instance = SimpleBreachAlertSchemaDataBreachAlertSourcesInner.from_json(json)
# print the JSON string representation of the object
print(SimpleBreachAlertSchemaDataBreachAlertSourcesInner.to_json())

# convert the object into a dict
simple_breach_alert_schema_data_breach_alert_sources_inner_dict = simple_breach_alert_schema_data_breach_alert_sources_inner_instance.to_dict()
# create an instance of SimpleBreachAlertSchemaDataBreachAlertSourcesInner from a dict
simple_breach_alert_schema_data_breach_alert_sources_inner_from_dict = SimpleBreachAlertSchemaDataBreachAlertSourcesInner.from_dict(simple_breach_alert_schema_data_breach_alert_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


