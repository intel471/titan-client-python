# SituationReportSchemaActivity

Period Situation report was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the Situation report activity range. | [optional] 
**last** | **int** | End of the Situation report activity range. | [optional] 

## Example

```python
from titan_client.models.situation_report_schema_activity import SituationReportSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of SituationReportSchemaActivity from a JSON string
situation_report_schema_activity_instance = SituationReportSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(SituationReportSchemaActivity.to_json())

# convert the object into a dict
situation_report_schema_activity_dict = situation_report_schema_activity_instance.to_dict()
# create an instance of SituationReportSchemaActivity from a dict
situation_report_schema_activity_from_dict = SituationReportSchemaActivity.from_dict(situation_report_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


