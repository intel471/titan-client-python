# MarketplaceVendorStreamResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 
**vendors** | [**list[MarketplaceVendorSearchSchema]**](MarketplaceVendorSearchSchema.md) | List of &#x60;Vendors&#x60;. | [optional] 
**vendors_count** | **int** | Count of matched vendors. | 
**vendors_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


