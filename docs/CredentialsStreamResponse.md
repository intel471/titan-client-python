# CredentialsStreamResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**list[CredentialSchema]**](CredentialSchema.md) | List of &#x60;Credentials&#x60;. | [optional] 
**credentials_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**credentials_total_count** | **int** | Total count of matched credentials. | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


