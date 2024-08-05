# SituationReportSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**SituationReportSchemaActivity**](SituationReportSchemaActivity.md) |  | 
**classification** | [**SituationReportSchemaClassification**](SituationReportSchemaClassification.md) |  | 
**data** | [**SituationReportSchemaData**](SituationReportSchemaData.md) |  | 
**last_updated** | **int** | Situation report last modification date. | 
**uid** | **str** | Unique Situation report identifier. | 

## Example

```python
from titan_client.models.situation_report_schema import SituationReportSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SituationReportSchema from a JSON string
situation_report_schema_instance = SituationReportSchema.from_json(json)
# print the JSON string representation of the object
print(SituationReportSchema.to_json())

# convert the object into a dict
situation_report_schema_dict = situation_report_schema_instance.to_dict()
# create an instance of SituationReportSchema from a dict
situation_report_schema_from_dict = SituationReportSchema.from_dict(situation_report_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


