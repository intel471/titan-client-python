# PrivateMessageSchemaLinksThread

Thread in which private message was found.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique thread identifier. | 

## Example

```python
from titan_client.models.private_message_schema_links_thread import PrivateMessageSchemaLinksThread

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessageSchemaLinksThread from a JSON string
private_message_schema_links_thread_instance = PrivateMessageSchemaLinksThread.from_json(json)
# print the JSON string representation of the object
print(PrivateMessageSchemaLinksThread.to_json())

# convert the object into a dict
private_message_schema_links_thread_dict = private_message_schema_links_thread_instance.to_dict()
# create an instance of PrivateMessageSchemaLinksThread from a dict
private_message_schema_links_thread_from_dict = PrivateMessageSchemaLinksThread.from_dict(private_message_schema_links_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


