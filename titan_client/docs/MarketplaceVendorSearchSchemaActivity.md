# MarketplaceVendorSearchSchemaActivity

Period when vendor was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the vendor activity range. | 
**last** | **int** | End of the vendor activity range. | 

## Example

```python
from titan_client.models.marketplace_vendor_search_schema_activity import MarketplaceVendorSearchSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceVendorSearchSchemaActivity from a JSON string
marketplace_vendor_search_schema_activity_instance = MarketplaceVendorSearchSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(MarketplaceVendorSearchSchemaActivity.to_json())

# convert the object into a dict
marketplace_vendor_search_schema_activity_dict = marketplace_vendor_search_schema_activity_instance.to_dict()
# create an instance of MarketplaceVendorSearchSchemaActivity from a dict
marketplace_vendor_search_schema_activity_from_dict = MarketplaceVendorSearchSchemaActivity.from_dict(marketplace_vendor_search_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


