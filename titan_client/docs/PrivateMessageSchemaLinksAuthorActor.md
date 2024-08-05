# PrivateMessageSchemaLinksAuthorActor

Message author.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle** | **str** | Author &#x60;handle&#x60;. | [optional] 
**uid** | **str** | Unique author identifier. | 

## Example

```python
from titan_client.models.private_message_schema_links_author_actor import PrivateMessageSchemaLinksAuthorActor

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessageSchemaLinksAuthorActor from a JSON string
private_message_schema_links_author_actor_instance = PrivateMessageSchemaLinksAuthorActor.from_json(json)
# print the JSON string representation of the object
print(PrivateMessageSchemaLinksAuthorActor.to_json())

# convert the object into a dict
private_message_schema_links_author_actor_dict = private_message_schema_links_author_actor_instance.to_dict()
# create an instance of PrivateMessageSchemaLinksAuthorActor from a dict
private_message_schema_links_author_actor_from_dict = PrivateMessageSchemaLinksAuthorActor.from_dict(private_message_schema_links_author_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


