# MarketplaceSearchSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**MarketplaceSearchSchemaActivity**](MarketplaceSearchSchemaActivity.md) |  | 
**data** | [**MarketplaceSearchSchemaData**](MarketplaceSearchSchemaData.md) |  | 
**last_updated** | **int** | Last modification date. | 
**statistics** | [**MarketplaceSearchSchemaStatistics**](MarketplaceSearchSchemaStatistics.md) |  | 
**uid** | **str** | Unique marketplace identifier. | 

## Example

```python
from titan_client.models.marketplace_search_schema import MarketplaceSearchSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceSearchSchema from a JSON string
marketplace_search_schema_instance = MarketplaceSearchSchema.from_json(json)
# print the JSON string representation of the object
print(MarketplaceSearchSchema.to_json())

# convert the object into a dict
marketplace_search_schema_dict = marketplace_search_schema_instance.to_dict()
# create an instance of MarketplaceSearchSchema from a dict
marketplace_search_schema_from_dict = MarketplaceSearchSchema.from_dict(marketplace_search_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


