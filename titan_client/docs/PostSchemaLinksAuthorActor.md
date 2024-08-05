# PostSchemaLinksAuthorActor

Post author.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle** | **str** | Author name. | 
**uid** | **str** | Unique author identifier. | 

## Example

```python
from titan_client.models.post_schema_links_author_actor import PostSchemaLinksAuthorActor

# TODO update the JSON string below
json = "{}"
# create an instance of PostSchemaLinksAuthorActor from a JSON string
post_schema_links_author_actor_instance = PostSchemaLinksAuthorActor.from_json(json)
# print the JSON string representation of the object
print(PostSchemaLinksAuthorActor.to_json())

# convert the object into a dict
post_schema_links_author_actor_dict = post_schema_links_author_actor_instance.to_dict()
# create an instance of PostSchemaLinksAuthorActor from a dict
post_schema_links_author_actor_from_dict = PostSchemaLinksAuthorActor.from_dict(post_schema_links_author_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


