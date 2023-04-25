# MarketplaceResourceStreamResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 
**resources** | [**list[MarketplaceResourceSearchSchema]**](MarketplaceResourceSearchSchema.md) | List of &#x60;Resources&#x60;. | [optional] 
**resources_count** | **int** | Count of matched resources. | 
**resources_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


