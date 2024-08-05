# PrivateMessageSchemaLinksForum

Forum.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Forum &#x60;description&#x60;. | [optional] 
**name** | **str** | Forum &#x60;name&#x60;. | 
**uid** | **str** | Unique forum identifier. | 

## Example

```python
from titan_client.models.private_message_schema_links_forum import PrivateMessageSchemaLinksForum

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessageSchemaLinksForum from a JSON string
private_message_schema_links_forum_instance = PrivateMessageSchemaLinksForum.from_json(json)
# print the JSON string representation of the object
print(PrivateMessageSchemaLinksForum.to_json())

# convert the object into a dict
private_message_schema_links_forum_dict = private_message_schema_links_forum_instance.to_dict()
# create an instance of PrivateMessageSchemaLinksForum from a dict
private_message_schema_links_forum_from_dict = PrivateMessageSchemaLinksForum.from_dict(private_message_schema_links_forum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


