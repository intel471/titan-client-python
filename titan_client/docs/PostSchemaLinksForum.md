# PostSchemaLinksForum

Forum on which the post was found.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Forum &#x60;description&#x60;. | [optional] 
**name** | **str** | Forum &#x60;name&#x60;. | 
**uid** | **str** | Unique forum identifier. | 

## Example

```python
from titan_client.models.post_schema_links_forum import PostSchemaLinksForum

# TODO update the JSON string below
json = "{}"
# create an instance of PostSchemaLinksForum from a JSON string
post_schema_links_forum_instance = PostSchemaLinksForum.from_json(json)
# print the JSON string representation of the object
print(PostSchemaLinksForum.to_json())

# convert the object into a dict
post_schema_links_forum_dict = post_schema_links_forum_instance.to_dict()
# create an instance of PostSchemaLinksForum from a dict
post_schema_links_forum_from_dict = PostSchemaLinksForum.from_dict(post_schema_links_forum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


