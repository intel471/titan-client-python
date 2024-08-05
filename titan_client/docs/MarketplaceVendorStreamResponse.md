# MarketplaceVendorStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 
**vendors** | [**List[MarketplaceVendorSearchSchema]**](MarketplaceVendorSearchSchema.md) | List of &#x60;Vendors&#x60;. | [optional] 
**vendors_count** | **int** | Count of matched vendors. | 
**vendors_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 

## Example

```python
from titan_client.models.marketplace_vendor_stream_response import MarketplaceVendorStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceVendorStreamResponse from a JSON string
marketplace_vendor_stream_response_instance = MarketplaceVendorStreamResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceVendorStreamResponse.to_json())

# convert the object into a dict
marketplace_vendor_stream_response_dict = marketplace_vendor_stream_response_instance.to_dict()
# create an instance of MarketplaceVendorStreamResponse from a dict
marketplace_vendor_stream_response_from_dict = MarketplaceVendorStreamResponse.from_dict(marketplace_vendor_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


