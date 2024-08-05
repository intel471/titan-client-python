# SituationReportSchemaDataSituationReport

Sub-document containing Situation report information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[SituationReportSchemaDataSituationReportEntitiesInner]**](SituationReportSchemaDataSituationReportEntitiesInner.md) | List of entities. Contains the type and value fields of an &#x60;entity&#x60; object from the entities endpoint. | [optional] 
**link** | [**SituationReportSchemaDataSituationReportLink**](SituationReportSchemaDataSituationReportLink.md) |  | 
**related_reports** | **List[str]** | Situation report links to related reports like \&quot;Information Report\&quot; or \&quot;Malware Report\&quot;. | [optional] 
**released_at** | **int** | Situation report released date. | 
**sensitive_source** | **bool** | Indicates if the document contains sensitive source derived information. | [optional] 
**text** | **str** | Situation report text. | 
**title** | **str** | Situation report title. | [optional] 
**victims** | [**List[SituationReportSchemaDataSituationReportVictimsInner]**](SituationReportSchemaDataSituationReportVictimsInner.md) | Purported victims list. | [optional] 

## Example

```python
from titan_client.models.situation_report_schema_data_situation_report import SituationReportSchemaDataSituationReport

# TODO update the JSON string below
json = "{}"
# create an instance of SituationReportSchemaDataSituationReport from a JSON string
situation_report_schema_data_situation_report_instance = SituationReportSchemaDataSituationReport.from_json(json)
# print the JSON string representation of the object
print(SituationReportSchemaDataSituationReport.to_json())

# convert the object into a dict
situation_report_schema_data_situation_report_dict = situation_report_schema_data_situation_report_instance.to_dict()
# create an instance of SituationReportSchemaDataSituationReport from a dict
situation_report_schema_data_situation_report_from_dict = SituationReportSchemaDataSituationReport.from_dict(situation_report_schema_data_situation_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


