# MarketplaceProductSearchSchemaData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**MarketplaceProductAvailabilitySchema**](MarketplaceProductAvailabilitySchema.md) |  | 
**base** | **str** | Base dump name. | [optional] 
**card_holder** | **str** | Credit card holder. | [optional] 
**card_number** | **str** | Credit card number. | [optional] 
**card_type** | **str** | Credit card type. | [optional] 
**cvv** | **str** | Credit card cvv. | [optional] 
**expiration** | **str** | Credit card expiration date. | [optional] 
**issuer** | **str** | Credit card issuer. | [optional] 
**marketplace** | [**MarketplaceProductMarketplaceSchema**](MarketplaceProductMarketplaceSchema.md) |  | 
**obfuscated_number** | **str** | Obfuscated credit card number. | [optional] 
**product_type** | [**MarketplaceProductTypeSchema**](MarketplaceProductTypeSchema.md) |  | 
**victim** | [**MarketplaceProductCredentialSchemaVictim**](MarketplaceProductCredentialSchemaVictim.md) |  | 
**installed_at** | **int** | Timestamp when bot was installed. | 
**stolen_by_form_stealers** | **int** | Count of stolen credentials in this package. | 
**title** | **str** | Product title. | 
**categories** | **list[str]** | Product categories. | 
**description** | **str** | Product description. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


