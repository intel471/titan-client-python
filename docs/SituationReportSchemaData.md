# SituationReportSchemaData

Sub-document containing Situation report and linked to in objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**situation_report** | [**SituationReportSchemaDataSituationReport**](SituationReportSchemaDataSituationReport.md) |  | [optional] 

## Example

```python
from titan_client.models.situation_report_schema_data import SituationReportSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of SituationReportSchemaData from a JSON string
situation_report_schema_data_instance = SituationReportSchemaData.from_json(json)
# print the JSON string representation of the object
print(SituationReportSchemaData.to_json())

# convert the object into a dict
situation_report_schema_data_dict = situation_report_schema_data_instance.to_dict()
# create an instance of SituationReportSchemaData from a dict
situation_report_schema_data_from_dict = SituationReportSchemaData.from_dict(situation_report_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


