# InstantMessageSchemaDataMessage

Sub-document containing instant message information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[InstantMessageSchemaDataMessageAttachmentsInner]**](InstantMessageSchemaDataMessageAttachmentsInner.md) | Message attachment. | [optional] 
**images** | [**List[ImageSchema]**](ImageSchema.md) | Array of images (if present). | [optional] 
**reply_uid** | **str** | Unique identifier of message this message is replying to. | [optional] 
**text** | **str** | HTML message content. | 
**uid** | **str** | Unique message identifier. | 

## Example

```python
from titan_client.models.instant_message_schema_data_message import InstantMessageSchemaDataMessage

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMessageSchemaDataMessage from a JSON string
instant_message_schema_data_message_instance = InstantMessageSchemaDataMessage.from_json(json)
# print the JSON string representation of the object
print(InstantMessageSchemaDataMessage.to_json())

# convert the object into a dict
instant_message_schema_data_message_dict = instant_message_schema_data_message_instance.to_dict()
# create an instance of InstantMessageSchemaDataMessage from a dict
instant_message_schema_data_message_from_dict = InstantMessageSchemaDataMessage.from_dict(instant_message_schema_data_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


