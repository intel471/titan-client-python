# PrivateMessageSchemaLinksRecipientActor

Message recipient.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle** | **str** | Recipient &#x60;handle&#x60;. | [optional] 
**uid** | **str** | Unique recipient identifier. | 

## Example

```python
from titan_client.models.private_message_schema_links_recipient_actor import PrivateMessageSchemaLinksRecipientActor

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessageSchemaLinksRecipientActor from a JSON string
private_message_schema_links_recipient_actor_instance = PrivateMessageSchemaLinksRecipientActor.from_json(json)
# print the JSON string representation of the object
print(PrivateMessageSchemaLinksRecipientActor.to_json())

# convert the object into a dict
private_message_schema_links_recipient_actor_dict = private_message_schema_links_recipient_actor_instance.to_dict()
# create an instance of PrivateMessageSchemaLinksRecipientActor from a dict
private_message_schema_links_recipient_actor_from_dict = PrivateMessageSchemaLinksRecipientActor.from_dict(private_message_schema_links_recipient_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


