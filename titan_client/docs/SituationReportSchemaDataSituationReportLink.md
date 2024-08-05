# SituationReportSchemaDataSituationReportLink

Links to malware family and malware report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**malware_family** | [**SituationReportSchemaDataSituationReportLinkMalwareFamily**](SituationReportSchemaDataSituationReportLinkMalwareFamily.md) |  | [optional] 
**malware_report** | [**SituationReportSchemaDataSituationReportLinkMalwareReport**](SituationReportSchemaDataSituationReportLinkMalwareReport.md) |  | [optional] 

## Example

```python
from titan_client.models.situation_report_schema_data_situation_report_link import SituationReportSchemaDataSituationReportLink

# TODO update the JSON string below
json = "{}"
# create an instance of SituationReportSchemaDataSituationReportLink from a JSON string
situation_report_schema_data_situation_report_link_instance = SituationReportSchemaDataSituationReportLink.from_json(json)
# print the JSON string representation of the object
print(SituationReportSchemaDataSituationReportLink.to_json())

# convert the object into a dict
situation_report_schema_data_situation_report_link_dict = situation_report_schema_data_situation_report_link_instance.to_dict()
# create an instance of SituationReportSchemaDataSituationReportLink from a dict
situation_report_schema_data_situation_report_link_from_dict = SituationReportSchemaDataSituationReportLink.from_dict(situation_report_schema_data_situation_report_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


