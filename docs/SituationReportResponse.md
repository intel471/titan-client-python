# SituationReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**situation_reports** | [**List[SituationReportSchema]**](SituationReportSchema.md) | List of Situation reports. | [optional] 
**situation_reports_total_count** | **int** | Total count of matched results. | 

## Example

```python
from titan_client.models.situation_report_response import SituationReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SituationReportResponse from a JSON string
situation_report_response_instance = SituationReportResponse.from_json(json)
# print the JSON string representation of the object
print(SituationReportResponse.to_json())

# convert the object into a dict
situation_report_response_dict = situation_report_response_instance.to_dict()
# create an instance of SituationReportResponse from a dict
situation_report_response_from_dict = SituationReportResponse.from_dict(situation_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


