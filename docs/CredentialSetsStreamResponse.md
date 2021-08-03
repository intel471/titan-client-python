# CredentialSetsStreamResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_sets** | [**list[CredentialSetStreamSchema]**](CredentialSetStreamSchema.md) | List of &#x60;Credential sets&#x60;. | [optional] 
**credential_sets_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**credential_sets_total_count** | **int** | Total count of matched credential sets. | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


