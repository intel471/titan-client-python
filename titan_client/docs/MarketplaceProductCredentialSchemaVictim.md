# MarketplaceProductCredentialSchemaVictim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | ISO code of country. | [optional] 
**ip_address** | **str** | Ip address. | [optional] 
**os** | **str** | Operating system. | [optional] 

## Example

```python
from titan_client.models.marketplace_product_credential_schema_victim import MarketplaceProductCredentialSchemaVictim

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceProductCredentialSchemaVictim from a JSON string
marketplace_product_credential_schema_victim_instance = MarketplaceProductCredentialSchemaVictim.from_json(json)
# print the JSON string representation of the object
print(MarketplaceProductCredentialSchemaVictim.to_json())

# convert the object into a dict
marketplace_product_credential_schema_victim_dict = marketplace_product_credential_schema_victim_instance.to_dict()
# create an instance of MarketplaceProductCredentialSchemaVictim from a dict
marketplace_product_credential_schema_victim_from_dict = MarketplaceProductCredentialSchemaVictim.from_dict(marketplace_product_credential_schema_victim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


