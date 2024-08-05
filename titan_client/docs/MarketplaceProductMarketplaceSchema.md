# MarketplaceProductMarketplaceSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of marketplace. | 
**price** | **str** | Value and currency. | [optional] 
**uid** | **str** | Unique marketplace identifier. | 

## Example

```python
from titan_client.models.marketplace_product_marketplace_schema import MarketplaceProductMarketplaceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceProductMarketplaceSchema from a JSON string
marketplace_product_marketplace_schema_instance = MarketplaceProductMarketplaceSchema.from_json(json)
# print the JSON string representation of the object
print(MarketplaceProductMarketplaceSchema.to_json())

# convert the object into a dict
marketplace_product_marketplace_schema_dict = marketplace_product_marketplace_schema_instance.to_dict()
# create an instance of MarketplaceProductMarketplaceSchema from a dict
marketplace_product_marketplace_schema_from_dict = MarketplaceProductMarketplaceSchema.from_dict(marketplace_product_marketplace_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


