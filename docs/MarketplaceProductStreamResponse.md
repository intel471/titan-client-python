# MarketplaceProductStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 
**products** | [**List[MarketplaceProductSearchSchema]**](MarketplaceProductSearchSchema.md) | List of &#x60;Products&#x60;. | [optional] 
**products_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**products_count** | **int** | Count of matched resources. | 
**statistics** | [**MarketplaceProductStatisticsSchema**](MarketplaceProductStatisticsSchema.md) |  | [optional] 

## Example

```python
from titan_client.models.marketplace_product_stream_response import MarketplaceProductStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceProductStreamResponse from a JSON string
marketplace_product_stream_response_instance = MarketplaceProductStreamResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceProductStreamResponse.to_json())

# convert the object into a dict
marketplace_product_stream_response_dict = marketplace_product_stream_response_instance.to_dict()
# create an instance of MarketplaceProductStreamResponse from a dict
marketplace_product_stream_response_from_dict = MarketplaceProductStreamResponse.from_dict(marketplace_product_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


