# MarketplaceResourceStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 
**resources** | [**List[MarketplaceResourceSearchSchema]**](MarketplaceResourceSearchSchema.md) | List of &#x60;Resources&#x60;. | [optional] 
**resources_count** | **int** | Count of matched resources. | 
**resources_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 

## Example

```python
from titan_client.models.marketplace_resource_stream_response import MarketplaceResourceStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceResourceStreamResponse from a JSON string
marketplace_resource_stream_response_instance = MarketplaceResourceStreamResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceResourceStreamResponse.to_json())

# convert the object into a dict
marketplace_resource_stream_response_dict = marketplace_resource_stream_response_instance.to_dict()
# create an instance of MarketplaceResourceStreamResponse from a dict
marketplace_resource_stream_response_from_dict = MarketplaceResourceStreamResponse.from_dict(marketplace_resource_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


