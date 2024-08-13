# MarketplaceProductCredentialSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**MarketplaceProductAvailabilitySchema**](MarketplaceProductAvailabilitySchema.md) |  | [optional] 
**installed_at** | **int** | Timestamp when bot was installed. | [optional] 
**marketplace** | [**MarketplaceProductMarketplaceSchema**](MarketplaceProductMarketplaceSchema.md) |  | [optional] 
**product_type** | **str** | Type of product | [optional] 
**stolen_by_form_stealers** | **int** | Count of stolen credentials in this package. | [optional] 
**title** | **str** | Credential title. | [optional] 
**victim** | [**MarketplaceProductCredentialSchemaVictim**](MarketplaceProductCredentialSchemaVictim.md) |  | [optional] 

## Example

```python
from titan_client.models.marketplace_product_credential_schema import MarketplaceProductCredentialSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceProductCredentialSchema from a JSON string
marketplace_product_credential_schema_instance = MarketplaceProductCredentialSchema.from_json(json)
# print the JSON string representation of the object
print(MarketplaceProductCredentialSchema.to_json())

# convert the object into a dict
marketplace_product_credential_schema_dict = marketplace_product_credential_schema_instance.to_dict()
# create an instance of MarketplaceProductCredentialSchema from a dict
marketplace_product_credential_schema_from_dict = MarketplaceProductCredentialSchema.from_dict(marketplace_product_credential_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


