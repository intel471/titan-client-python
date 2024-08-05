# MarketplaceProductCreditCardSchemaVictim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**dob** | **bool** | Availability of dob info. | [optional] 
**full** | **bool** | Availability of full info. | [optional] 
**pin** | **bool** | Availability of pin info. | [optional] 
**ssn** | **bool** | Availability of ssn info. | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 

## Example

```python
from titan_client.models.marketplace_product_credit_card_schema_victim import MarketplaceProductCreditCardSchemaVictim

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceProductCreditCardSchemaVictim from a JSON string
marketplace_product_credit_card_schema_victim_instance = MarketplaceProductCreditCardSchemaVictim.from_json(json)
# print the JSON string representation of the object
print(MarketplaceProductCreditCardSchemaVictim.to_json())

# convert the object into a dict
marketplace_product_credit_card_schema_victim_dict = marketplace_product_credit_card_schema_victim_instance.to_dict()
# create an instance of MarketplaceProductCreditCardSchemaVictim from a dict
marketplace_product_credit_card_schema_victim_from_dict = MarketplaceProductCreditCardSchemaVictim.from_dict(marketplace_product_credit_card_schema_victim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


