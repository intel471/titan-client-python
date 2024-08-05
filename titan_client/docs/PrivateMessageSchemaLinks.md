# PrivateMessageSchemaLinks

Linked data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_actor** | [**PrivateMessageSchemaLinksAuthorActor**](PrivateMessageSchemaLinksAuthorActor.md) |  | 
**forum** | [**PrivateMessageSchemaLinksForum**](PrivateMessageSchemaLinksForum.md) |  | 
**images** | [**List[ImageSchema]**](ImageSchema.md) | Array of images (if present). | [optional] 
**recipient_actor** | [**PrivateMessageSchemaLinksRecipientActor**](PrivateMessageSchemaLinksRecipientActor.md) |  | [optional] 
**thread** | [**PrivateMessageSchemaLinksThread**](PrivateMessageSchemaLinksThread.md) |  | 

## Example

```python
from titan_client.models.private_message_schema_links import PrivateMessageSchemaLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessageSchemaLinks from a JSON string
private_message_schema_links_instance = PrivateMessageSchemaLinks.from_json(json)
# print the JSON string representation of the object
print(PrivateMessageSchemaLinks.to_json())

# convert the object into a dict
private_message_schema_links_dict = private_message_schema_links_instance.to_dict()
# create an instance of PrivateMessageSchemaLinks from a dict
private_message_schema_links_from_dict = PrivateMessageSchemaLinks.from_dict(private_message_schema_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


