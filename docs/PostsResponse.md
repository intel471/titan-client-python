# PostsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**post_total_count** | **int** | Total count of matched posts. | 
**posts** | [**list[PostSchema]**](PostSchema.md) | List of &#x60;Posts&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


