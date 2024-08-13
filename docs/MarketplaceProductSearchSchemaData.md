# MarketplaceProductSearchSchemaData


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
**victim** | [**MarketplaceProductCredentialSchemaVictim**](MarketplaceProductCredentialSchemaVictim.md) |  | [optional] 
**installed_at** | **int** | Timestamp when bot was installed. | [optional] 
**stolen_by_form_stealers** | **int** | Count of stolen credentials in this package. | [optional] 
**title** | **str** | Product title. | [optional] 
**categories** | **List[str]** | Product categories. | [optional] 
**description** | **str** | Product description. | [optional] 

## Example

```python
from titan_client.models.marketplace_product_search_schema_data import MarketplaceProductSearchSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceProductSearchSchemaData from a JSON string
marketplace_product_search_schema_data_instance = MarketplaceProductSearchSchemaData.from_json(json)
# print the JSON string representation of the object
print(MarketplaceProductSearchSchemaData.to_json())

# convert the object into a dict
marketplace_product_search_schema_data_dict = marketplace_product_search_schema_data_instance.to_dict()
# create an instance of MarketplaceProductSearchSchemaData from a dict
marketplace_product_search_schema_data_from_dict = MarketplaceProductSearchSchemaData.from_dict(marketplace_product_search_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


