# MarketplaceSearchSchemaStatistics

Marketplace statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products_total_count** | **int** | Total count of marketplace&#39;s products. | 
**vendors_total_count** | **int** | Total count of marketplace&#39;s vendors. | 

## Example

```python
from titan_client.models.marketplace_search_schema_statistics import MarketplaceSearchSchemaStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceSearchSchemaStatistics from a JSON string
marketplace_search_schema_statistics_instance = MarketplaceSearchSchemaStatistics.from_json(json)
# print the JSON string representation of the object
print(MarketplaceSearchSchemaStatistics.to_json())

# convert the object into a dict
marketplace_search_schema_statistics_dict = marketplace_search_schema_statistics_instance.to_dict()
# create an instance of MarketplaceSearchSchemaStatistics from a dict
marketplace_search_schema_statistics_from_dict = MarketplaceSearchSchemaStatistics.from_dict(marketplace_search_schema_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


