# SituationReportSchemaClassification

Classification of Situation report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intel_requirements** | **List[str]** | List of General Intel Requirements (GIR) linked to Situation report. | [optional] 

## Example

```python
from titan_client.models.situation_report_schema_classification import SituationReportSchemaClassification

# TODO update the JSON string below
json = "{}"
# create an instance of SituationReportSchemaClassification from a JSON string
situation_report_schema_classification_instance = SituationReportSchemaClassification.from_json(json)
# print the JSON string representation of the object
print(SituationReportSchemaClassification.to_json())

# convert the object into a dict
situation_report_schema_classification_dict = situation_report_schema_classification_instance.to_dict()
# create an instance of SituationReportSchemaClassification from a dict
situation_report_schema_classification_from_dict = SituationReportSchemaClassification.from_dict(situation_report_schema_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


