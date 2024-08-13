# SimpleNewsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**news** | [**List[NewsSchema]**](NewsSchema.md) | List of &#x60;News&#x60;. | [optional] 
**news_total_count** | **int** | Total count of matched news. | 

## Example

```python
from titan_client.models.simple_news_response import SimpleNewsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleNewsResponse from a JSON string
simple_news_response_instance = SimpleNewsResponse.from_json(json)
# print the JSON string representation of the object
print(SimpleNewsResponse.to_json())

# convert the object into a dict
simple_news_response_dict = simple_news_response_instance.to_dict()
# create an instance of SimpleNewsResponse from a dict
simple_news_response_from_dict = SimpleNewsResponse.from_dict(simple_news_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


