# SimpleCvesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_reports** | [**List[SimpleCveSchema]**](SimpleCveSchema.md) | List of &#x60;Reports&#x60;. | [optional] 
**cve_reports_total_count** | **int** | Total count of matched reports. | 
**post_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 

## Example

```python
from titan_client.models.simple_cves_response import SimpleCvesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCvesResponse from a JSON string
simple_cves_response_instance = SimpleCvesResponse.from_json(json)
# print the JSON string representation of the object
print(SimpleCvesResponse.to_json())

# convert the object into a dict
simple_cves_response_dict = simple_cves_response_instance.to_dict()
# create an instance of SimpleCvesResponse from a dict
simple_cves_response_from_dict = SimpleCvesResponse.from_dict(simple_cves_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


