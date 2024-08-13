# MarketplaceVendorSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendors** | [**List[MarketplaceVendorSearchSchema]**](MarketplaceVendorSearchSchema.md) | List of vendors. | [optional] 
**vendors_count** | **int** | Count of matched results. | 
**vendors_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 

## Example

```python
from titan_client.models.marketplace_vendor_search_response import MarketplaceVendorSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceVendorSearchResponse from a JSON string
marketplace_vendor_search_response_instance = MarketplaceVendorSearchResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceVendorSearchResponse.to_json())

# convert the object into a dict
marketplace_vendor_search_response_dict = marketplace_vendor_search_response_instance.to_dict()
# create an instance of MarketplaceVendorSearchResponse from a dict
marketplace_vendor_search_response_from_dict = MarketplaceVendorSearchResponse.from_dict(marketplace_vendor_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


