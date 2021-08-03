# YARASearchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yara_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**yara_total_count** | **int** | Total count of matched results. | 
**yaras** | [**list[YARASearchSchema]**](YARASearchSchema.md) | List of &#x60;YARA&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


