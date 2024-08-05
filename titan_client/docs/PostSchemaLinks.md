# PostSchemaLinks

Linked data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_actor** | [**PostSchemaLinksAuthorActor**](PostSchemaLinksAuthorActor.md) |  | [optional] 
**forum** | [**PostSchemaLinksForum**](PostSchemaLinksForum.md) |  | [optional] 
**images** | [**List[ImageSchema]**](ImageSchema.md) | Array of images (if present). | [optional] 
**thread** | [**PostSchemaLinksThread**](PostSchemaLinksThread.md) |  | [optional] 

## Example

```python
from titan_client.models.post_schema_links import PostSchemaLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PostSchemaLinks from a JSON string
post_schema_links_instance = PostSchemaLinks.from_json(json)
# print the JSON string representation of the object
print(PostSchemaLinks.to_json())

# convert the object into a dict
post_schema_links_dict = post_schema_links_instance.to_dict()
# create an instance of PostSchemaLinks from a dict
post_schema_links_from_dict = PostSchemaLinks.from_dict(post_schema_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


