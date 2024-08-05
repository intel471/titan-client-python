# PostSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | The &#x60;date&#x60; of the post. | 
**last_updated** | **int** | Last modification date. | [optional] 
**links** | [**PostSchemaLinks**](PostSchemaLinks.md) |  | 
**message** | **str** | HTML post content. If post message is translated, this parameter contains translated text, if not — original. [Markup explained](#forum-post-or-pm-markup). | 
**message_original** | **str** | Original HTML post content. This parameter is active if post message is translated. [Markup explained](#forum-post-or-pm-markup). | [optional] 
**uid** | **str** | Unique post identifier. | 

## Example

```python
from titan_client.models.post_schema import PostSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PostSchema from a JSON string
post_schema_instance = PostSchema.from_json(json)
# print the JSON string representation of the object
print(PostSchema.to_json())

# convert the object into a dict
post_schema_dict = post_schema_instance.to_dict()
# create an instance of PostSchema from a dict
post_schema_from_dict = PostSchema.from_dict(post_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


