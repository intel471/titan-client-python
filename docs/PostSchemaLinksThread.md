# PostSchemaLinksThread

Thread in which the post was found.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | &#x60;Count&#x60; of posts in thread. | 
**topic** | **str** | Thread &#x60;topic&#x60;. If post topic is translated, this parameter contains translated topic, if not — original. | [optional] 
**topic_original** | **str** | Original thread topic. This parameter is active if post topic is translated. | [optional] 
**uid** | **str** | Unique thread identifier. | 

## Example

```python
from titan_client.models.post_schema_links_thread import PostSchemaLinksThread

# TODO update the JSON string below
json = "{}"
# create an instance of PostSchemaLinksThread from a JSON string
post_schema_links_thread_instance = PostSchemaLinksThread.from_json(json)
# print the JSON string representation of the object
print(PostSchemaLinksThread.to_json())

# convert the object into a dict
post_schema_links_thread_dict = post_schema_links_thread_instance.to_dict()
# create an instance of PostSchemaLinksThread from a dict
post_schema_links_thread_from_dict = PostSchemaLinksThread.from_dict(post_schema_links_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


