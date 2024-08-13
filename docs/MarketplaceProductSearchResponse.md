# MarketplaceProductSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[MarketplaceProductSearchSchema]**](MarketplaceProductSearchSchema.md) | List of products. | [optional] 
**products_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**products_count** | **int** | Count of matched results. | 
**statistics** | [**MarketplaceProductStatisticsSchema**](MarketplaceProductStatisticsSchema.md) |  | [optional] 

## Example

```python
from titan_client.models.marketplace_product_search_response import MarketplaceProductSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceProductSearchResponse from a JSON string
marketplace_product_search_response_instance = MarketplaceProductSearchResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceProductSearchResponse.to_json())

# convert the object into a dict
marketplace_product_search_response_dict = marketplace_product_search_response_instance.to_dict()
# create an instance of MarketplaceProductSearchResponse from a dict
marketplace_product_search_response_from_dict = MarketplaceProductSearchResponse.from_dict(marketplace_product_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


