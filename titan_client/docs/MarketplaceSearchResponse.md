# MarketplaceSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketplaces** | [**List[MarketplaceSearchSchema]**](MarketplaceSearchSchema.md) | List of marketplaces. | [optional] 
**marketplaces_count** | **int** | Count of matched results. | 
**marketplaces_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 

## Example

```python
from titan_client.models.marketplace_search_response import MarketplaceSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceSearchResponse from a JSON string
marketplace_search_response_instance = MarketplaceSearchResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceSearchResponse.to_json())

# convert the object into a dict
marketplace_search_response_dict = marketplace_search_response_instance.to_dict()
# create an instance of MarketplaceSearchResponse from a dict
marketplace_search_response_from_dict = MarketplaceSearchResponse.from_dict(marketplace_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


