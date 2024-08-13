# MarketplaceVendorSearchSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**MarketplaceVendorSearchSchemaActivity**](MarketplaceVendorSearchSchemaActivity.md) |  | 
**data** | [**MarketplaceVendorSearchSchemaData**](MarketplaceVendorSearchSchemaData.md) |  | 
**last_updated** | **int** | Last modification date. | 
**statistics** | [**MarketplaceVendorSearchSchemaStatistics**](MarketplaceVendorSearchSchemaStatistics.md) |  | 
**uid** | **str** | Unique vendor identifier. | 

## Example

```python
from titan_client.models.marketplace_vendor_search_schema import MarketplaceVendorSearchSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceVendorSearchSchema from a JSON string
marketplace_vendor_search_schema_instance = MarketplaceVendorSearchSchema.from_json(json)
# print the JSON string representation of the object
print(MarketplaceVendorSearchSchema.to_json())

# convert the object into a dict
marketplace_vendor_search_schema_dict = marketplace_vendor_search_schema_instance.to_dict()
# create an instance of MarketplaceVendorSearchSchema from a dict
marketplace_vendor_search_schema_from_dict = MarketplaceVendorSearchSchema.from_dict(marketplace_vendor_search_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


