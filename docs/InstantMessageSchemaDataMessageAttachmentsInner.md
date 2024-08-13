# InstantMessageSchemaDataMessageAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **float** | Attachment &#x60;height&#x60;. | [optional] 
**original_url** | **str** | Attachment url. | 
**size** | **float** | Attachment &#x60;size&#x60; in bytes. | 
**type** | **str** | Attachment &#x60;type&#x60;. | 
**uid** | **str** | Unique attachment identifier. | 
**width** | **float** | Attachment &#x60;width&#x60;. | [optional] 

## Example

```python
from titan_client.models.instant_message_schema_data_message_attachments_inner import InstantMessageSchemaDataMessageAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMessageSchemaDataMessageAttachmentsInner from a JSON string
instant_message_schema_data_message_attachments_inner_instance = InstantMessageSchemaDataMessageAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(InstantMessageSchemaDataMessageAttachmentsInner.to_json())

# convert the object into a dict
instant_message_schema_data_message_attachments_inner_dict = instant_message_schema_data_message_attachments_inner_instance.to_dict()
# create an instance of InstantMessageSchemaDataMessageAttachmentsInner from a dict
instant_message_schema_data_message_attachments_inner_from_dict = InstantMessageSchemaDataMessageAttachmentsInner.from_dict(instant_message_schema_data_message_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


