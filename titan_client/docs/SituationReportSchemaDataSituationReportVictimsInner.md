# SituationReportSchemaDataSituationReportVictimsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Purported victim name. | 
**urls** | **List[str]** | Purported victim url list. | [optional] 

## Example

```python
from titan_client.models.situation_report_schema_data_situation_report_victims_inner import SituationReportSchemaDataSituationReportVictimsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SituationReportSchemaDataSituationReportVictimsInner from a JSON string
situation_report_schema_data_situation_report_victims_inner_instance = SituationReportSchemaDataSituationReportVictimsInner.from_json(json)
# print the JSON string representation of the object
print(SituationReportSchemaDataSituationReportVictimsInner.to_json())

# convert the object into a dict
situation_report_schema_data_situation_report_victims_inner_dict = situation_report_schema_data_situation_report_victims_inner_instance.to_dict()
# create an instance of SituationReportSchemaDataSituationReportVictimsInner from a dict
situation_report_schema_data_situation_report_victims_inner_from_dict = SituationReportSchemaDataSituationReportVictimsInner.from_dict(situation_report_schema_data_situation_report_victims_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


