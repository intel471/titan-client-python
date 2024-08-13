# MarketplaceProductSearchSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**MarketplaceProductSearchSchemaActivity**](MarketplaceProductSearchSchemaActivity.md) |  | 
**data** | [**MarketplaceProductSearchSchemaData**](MarketplaceProductSearchSchemaData.md) |  | 
**last_updated** | **int** | Last modification date. | 
**uid** | **str** | Unique credit card identifier. | 

## Example

```python
from titan_client.models.marketplace_product_search_schema import MarketplaceProductSearchSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceProductSearchSchema from a JSON string
marketplace_product_search_schema_instance = MarketplaceProductSearchSchema.from_json(json)
# print the JSON string representation of the object
print(MarketplaceProductSearchSchema.to_json())

# convert the object into a dict
marketplace_product_search_schema_dict = marketplace_product_search_schema_instance.to_dict()
# create an instance of MarketplaceProductSearchSchema from a dict
marketplace_product_search_schema_from_dict = MarketplaceProductSearchSchema.from_dict(marketplace_product_search_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


