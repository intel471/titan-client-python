# PostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**post_total_count** | **int** | Total count of matched posts. | 
**posts** | [**List[PostSchema]**](PostSchema.md) | List of &#x60;Posts&#x60;. | [optional] 

## Example

```python
from titan_client.models.posts_response import PostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostsResponse from a JSON string
posts_response_instance = PostsResponse.from_json(json)
# print the JSON string representation of the object
print(PostsResponse.to_json())

# convert the object into a dict
posts_response_dict = posts_response_instance.to_dict()
# create an instance of PostsResponse from a dict
posts_response_from_dict = PostsResponse.from_dict(posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


