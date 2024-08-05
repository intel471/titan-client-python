# MarketplaceProductOtherProductSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**MarketplaceProductAvailabilitySchema**](MarketplaceProductAvailabilitySchema.md) |  | [optional] 
**categories** | **List[str]** | Product categories. | [optional] 
**description** | **str** | Product description. | [optional] 
**marketplace** | [**MarketplaceProductMarketplaceSchema**](MarketplaceProductMarketplaceSchema.md) |  | [optional] 
**product_type** | **str** | Type of product | [optional] 
**title** | **str** | Product title. | [optional] 

## Example

```python
from titan_client.models.marketplace_product_other_product_schema import MarketplaceProductOtherProductSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceProductOtherProductSchema from a JSON string
marketplace_product_other_product_schema_instance = MarketplaceProductOtherProductSchema.from_json(json)
# print the JSON string representation of the object
print(MarketplaceProductOtherProductSchema.to_json())

# convert the object into a dict
marketplace_product_other_product_schema_dict = marketplace_product_other_product_schema_instance.to_dict()
# create an instance of MarketplaceProductOtherProductSchema from a dict
marketplace_product_other_product_schema_from_dict = MarketplaceProductOtherProductSchema.from_dict(marketplace_product_other_product_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


