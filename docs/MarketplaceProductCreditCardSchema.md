# MarketplaceProductCreditCardSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**MarketplaceProductAvailabilitySchema**](MarketplaceProductAvailabilitySchema.md) |  | [optional] 
**base** | **str** | Base dump name. | [optional] 
**card_holder** | **str** | Credit card holder. | [optional] 
**card_number** | **str** | Credit card number. | [optional] 
**card_type** | **str** | Credit card type. | [optional] 
**cvv** | **str** | Credit card cvv. | [optional] 
**expiration** | **str** | Credit card expiration date. | [optional] 
**issuer** | **str** | Credit card issuer. | [optional] 
**marketplace** | [**MarketplaceProductMarketplaceSchema**](MarketplaceProductMarketplaceSchema.md) |  | [optional] 
**obfuscated_number** | **str** | Obfuscated credit card number. | [optional] 
**product_type** | **str** | Type of product | [optional] 
**victim** | [**MarketplaceProductCreditCardSchemaVictim**](MarketplaceProductCreditCardSchemaVictim.md) |  | [optional] 

## Example

```python
from titan_client.models.marketplace_product_credit_card_schema import MarketplaceProductCreditCardSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceProductCreditCardSchema from a JSON string
marketplace_product_credit_card_schema_instance = MarketplaceProductCreditCardSchema.from_json(json)
# print the JSON string representation of the object
print(MarketplaceProductCreditCardSchema.to_json())

# convert the object into a dict
marketplace_product_credit_card_schema_dict = marketplace_product_credit_card_schema_instance.to_dict()
# create an instance of MarketplaceProductCreditCardSchema from a dict
marketplace_product_credit_card_schema_from_dict = MarketplaceProductCreditCardSchema.from_dict(marketplace_product_credit_card_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


