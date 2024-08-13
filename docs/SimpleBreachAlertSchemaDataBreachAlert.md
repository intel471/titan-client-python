# SimpleBreachAlertSchemaDataBreachAlert

Sub-document containing Breach Alert information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_or_group** | **str** | Name of the actor or the actor group behind the breach. | 
**confidence** | [**SimpleBreachAlertSchemaDataBreachAlertConfidence**](SimpleBreachAlertSchemaDataBreachAlertConfidence.md) |  | 
**date_of_information** | **int** | Breach Alert&#39;s date of information. | 
**intel_requirements** | **List[str]** | General Intel Requirements (GIR). | [optional] 
**released_at** | **int** | Breach Alert&#39;s release date. | 
**sensitive_source** | **bool** | Indicates if the document contains sensitive source derived information. | [optional] 
**sources** | [**List[SimpleBreachAlertSchemaDataBreachAlertSourcesInner]**](SimpleBreachAlertSchemaDataBreachAlertSourcesInner.md) | Sources for this alert, either from Titan or external &#x60;resources&#x60;. | [optional] 
**summary** | **str** | Breach Alert&#39;s summary - raw text in HTML format. | [optional] 
**title** | **str** | Breach Alert&#39;s title. | 
**victim** | [**SimpleBreachAlertSchemaDataBreachAlertVictim**](SimpleBreachAlertSchemaDataBreachAlertVictim.md) |  | 

## Example

```python
from titan_client.models.simple_breach_alert_schema_data_breach_alert import SimpleBreachAlertSchemaDataBreachAlert

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleBreachAlertSchemaDataBreachAlert from a JSON string
simple_breach_alert_schema_data_breach_alert_instance = SimpleBreachAlertSchemaDataBreachAlert.from_json(json)
# print the JSON string representation of the object
print(SimpleBreachAlertSchemaDataBreachAlert.to_json())

# convert the object into a dict
simple_breach_alert_schema_data_breach_alert_dict = simple_breach_alert_schema_data_breach_alert_instance.to_dict()
# create an instance of SimpleBreachAlertSchemaDataBreachAlert from a dict
simple_breach_alert_schema_data_breach_alert_from_dict = SimpleBreachAlertSchemaDataBreachAlert.from_dict(simple_breach_alert_schema_data_breach_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


