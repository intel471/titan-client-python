# DataLeakPostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_leak_post_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**data_leak_post_total_count** | **int** | Total count of matched data leak posts. | 
**data_leak_posts** | [**List[DataLeakPostSchema]**](DataLeakPostSchema.md) | List of &#x60;Data Leak Posts&#x60;. | [optional] 

## Example

```python
from titan_client.models.data_leak_posts_response import DataLeakPostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakPostsResponse from a JSON string
data_leak_posts_response_instance = DataLeakPostsResponse.from_json(json)
# print the JSON string representation of the object
print(DataLeakPostsResponse.to_json())

# convert the object into a dict
data_leak_posts_response_dict = data_leak_posts_response_instance.to_dict()
# create an instance of DataLeakPostsResponse from a dict
data_leak_posts_response_from_dict = DataLeakPostsResponse.from_dict(data_leak_posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


