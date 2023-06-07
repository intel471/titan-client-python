# MarketplaceProductStreamResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 
**products** | [**list[MarketplaceProductSearchSchema]**](MarketplaceProductSearchSchema.md) | List of &#x60;Products&#x60;. | [optional] 
**products_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**products_count** | **int** | Count of matched resources. | 
**statistics** | [**MarketplaceProductStatisticsSchema**](MarketplaceProductStatisticsSchema.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


