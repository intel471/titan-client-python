# PrivateMessagesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_message_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**private_message_total_count** | **int** | Total count of matched messages. | 
**private_messages** | [**list[PrivateMessageSchema]**](PrivateMessageSchema.md) | List of &#x60;Private messages&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


