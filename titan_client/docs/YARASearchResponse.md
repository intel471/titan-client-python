# YARASearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yara_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**yara_total_count** | **int** | Total count of matched results. | 
**yaras** | [**List[YARASearchSchema]**](YARASearchSchema.md) | List of &#x60;YARA&#x60;. | [optional] 

## Example

```python
from titan_client.models.yara_search_response import YARASearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of YARASearchResponse from a JSON string
yara_search_response_instance = YARASearchResponse.from_json(json)
# print the JSON string representation of the object
print(YARASearchResponse.to_json())

# convert the object into a dict
yara_search_response_dict = yara_search_response_instance.to_dict()
# create an instance of YARASearchResponse from a dict
yara_search_response_from_dict = YARASearchResponse.from_dict(yara_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


