# MarketplaceSearchSchemaData

Marketplace detailed data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of marketplace | 
**name** | **str** | Name of marketplace. | 
**tier** | **str** | Marketplace&#39;s tier. | 
**url** | **str** | URL of marketplace. | 

## Example

```python
from titan_client.models.marketplace_search_schema_data import MarketplaceSearchSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceSearchSchemaData from a JSON string
marketplace_search_schema_data_instance = MarketplaceSearchSchemaData.from_json(json)
# print the JSON string representation of the object
print(MarketplaceSearchSchemaData.to_json())

# convert the object into a dict
marketplace_search_schema_data_dict = marketplace_search_schema_data_instance.to_dict()
# create an instance of MarketplaceSearchSchemaData from a dict
marketplace_search_schema_data_from_dict = MarketplaceSearchSchemaData.from_dict(marketplace_search_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


