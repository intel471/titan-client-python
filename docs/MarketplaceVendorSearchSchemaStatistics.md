# MarketplaceVendorSearchSchemaStatistics

Detailed statistics about vendor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products_total_count** | **int** | Total count of products related to vendor. | 

## Example

```python
from titan_client.models.marketplace_vendor_search_schema_statistics import MarketplaceVendorSearchSchemaStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceVendorSearchSchemaStatistics from a JSON string
marketplace_vendor_search_schema_statistics_instance = MarketplaceVendorSearchSchemaStatistics.from_json(json)
# print the JSON string representation of the object
print(MarketplaceVendorSearchSchemaStatistics.to_json())

# convert the object into a dict
marketplace_vendor_search_schema_statistics_dict = marketplace_vendor_search_schema_statistics_instance.to_dict()
# create an instance of MarketplaceVendorSearchSchemaStatistics from a dict
marketplace_vendor_search_schema_statistics_from_dict = MarketplaceVendorSearchSchemaStatistics.from_dict(marketplace_vendor_search_schema_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


