# MarketplaceResourceSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[MarketplaceResourceSearchSchema]**](MarketplaceResourceSearchSchema.md) | List of resources. | [optional] 
**resources_count** | **int** | Count of matched results. | 
**resources_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 

## Example

```python
from titan_client.models.marketplace_resource_search_response import MarketplaceResourceSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceResourceSearchResponse from a JSON string
marketplace_resource_search_response_instance = MarketplaceResourceSearchResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceResourceSearchResponse.to_json())

# convert the object into a dict
marketplace_resource_search_response_dict = marketplace_resource_search_response_instance.to_dict()
# create an instance of MarketplaceResourceSearchResponse from a dict
marketplace_resource_search_response_from_dict = MarketplaceResourceSearchResponse.from_dict(marketplace_resource_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


