# IndicatorSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indicator_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**indicator_total_count** | **int** | Total count of matched indicators. | 
**indicators** | [**List[IndicatorSearchSchema]**](IndicatorSearchSchema.md) | List of &#x60;Indicators&#x60; | [optional] 

## Example

```python
from titan_client.models.indicator_search_response import IndicatorSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorSearchResponse from a JSON string
indicator_search_response_instance = IndicatorSearchResponse.from_json(json)
# print the JSON string representation of the object
print(IndicatorSearchResponse.to_json())

# convert the object into a dict
indicator_search_response_dict = indicator_search_response_instance.to_dict()
# create an instance of IndicatorSearchResponse from a dict
indicator_search_response_from_dict = IndicatorSearchResponse.from_dict(indicator_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


