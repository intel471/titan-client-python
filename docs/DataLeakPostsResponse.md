# DataLeakPostsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_leak_post_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**data_leak_post_total_count** | **int** | Total count of matched data leak posts. | 
**data_leak_posts** | [**list[DataLeakPostSchema]**](DataLeakPostSchema.md) | List of &#x60;Data Leak Posts&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


