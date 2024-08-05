# SimpleSpotReportsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**spot_reports** | [**List[SimpleSpotReportSchema]**](SimpleSpotReportSchema.md) | List of &#x60;Spot reports&#x60;. | [optional] 
**spot_reports_total_count** | **int** | Total count of matched results. | 

## Example

```python
from titan_client.models.simple_spot_reports_response import SimpleSpotReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleSpotReportsResponse from a JSON string
simple_spot_reports_response_instance = SimpleSpotReportsResponse.from_json(json)
# print the JSON string representation of the object
print(SimpleSpotReportsResponse.to_json())

# convert the object into a dict
simple_spot_reports_response_dict = simple_spot_reports_response_instance.to_dict()
# create an instance of SimpleSpotReportsResponse from a dict
simple_spot_reports_response_from_dict = SimpleSpotReportsResponse.from_dict(simple_spot_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


