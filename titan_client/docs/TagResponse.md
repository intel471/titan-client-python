# TagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_total_count** | **int** | Total count of all tags including unused. | 
**tags** | [**List[TagSchema]**](TagSchema.md) | List of &#x60;Tags&#x60;. | [optional] 
**used_tag_count** | **int** | Count of used tags with &#x60;use_count&#x60; &gt; 0. | 

## Example

```python
from titan_client.models.tag_response import TagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TagResponse from a JSON string
tag_response_instance = TagResponse.from_json(json)
# print the JSON string representation of the object
print(TagResponse.to_json())

# convert the object into a dict
tag_response_dict = tag_response_instance.to_dict()
# create an instance of TagResponse from a dict
tag_response_from_dict = TagResponse.from_dict(tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


