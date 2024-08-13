# MarketplaceProductSearchSchemaActivity

Period when credit card was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the credit card activity range. | 
**last** | **int** | End of the credit card activity range. | 

## Example

```python
from titan_client.models.marketplace_product_search_schema_activity import MarketplaceProductSearchSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceProductSearchSchemaActivity from a JSON string
marketplace_product_search_schema_activity_instance = MarketplaceProductSearchSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(MarketplaceProductSearchSchemaActivity.to_json())

# convert the object into a dict
marketplace_product_search_schema_activity_dict = marketplace_product_search_schema_activity_instance.to_dict()
# create an instance of MarketplaceProductSearchSchemaActivity from a dict
marketplace_product_search_schema_activity_from_dict = MarketplaceProductSearchSchemaActivity.from_dict(marketplace_product_search_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


