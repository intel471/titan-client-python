# PrivateMessageSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **int** | &#x60;Date&#x60; the message was sent. | 
**last_updated** | **int** | Event modification date. | [optional] 
**links** | [**PrivateMessageSchemaLinks**](PrivateMessageSchemaLinks.md) |  | 
**message** | **str** | HTML &#x60;message&#x60; content. If message is translated, this parameter contains translated text, if not — original. | 
**message_original** | **str** | Original HTML message content. This parameter is active if message is translated. | [optional] 
**subject** | **str** | Message &#x60;subject&#x60;. If message subject is translated, this parameter contains translated subject, if not — original. | [optional] 
**subject_original** | **str** | Original message subject. This parameter is active if message subject is translated. | [optional] 
**uid** | **str** | Unique message identifier. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


