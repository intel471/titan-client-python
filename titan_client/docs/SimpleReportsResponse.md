# SimpleReportsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**report_total_count** | **int** | Total count of matched reports. | 
**reports** | [**List[SimpleReportSchema]**](SimpleReportSchema.md) | List of Information Reports or Fintel Reports excluding researcherComments, rawText, rawTextTranslated fields. | [optional] 

## Example

```python
from titan_client.models.simple_reports_response import SimpleReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleReportsResponse from a JSON string
simple_reports_response_instance = SimpleReportsResponse.from_json(json)
# print the JSON string representation of the object
print(SimpleReportsResponse.to_json())

# convert the object into a dict
simple_reports_response_dict = simple_reports_response_instance.to_dict()
# create an instance of SimpleReportsResponse from a dict
simple_reports_response_from_dict = SimpleReportsResponse.from_dict(simple_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


