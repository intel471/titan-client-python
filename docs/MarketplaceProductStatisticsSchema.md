# MarketplaceProductStatisticsSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials_total_count** | **int** | Total count of all credential products | 
**credit_cards_total_count** | **int** | Total count of all credit card products | 
**other_products_total_count** | **int** | Total count of all other products | 

## Example

```python
from titan_client.models.marketplace_product_statistics_schema import MarketplaceProductStatisticsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceProductStatisticsSchema from a JSON string
marketplace_product_statistics_schema_instance = MarketplaceProductStatisticsSchema.from_json(json)
# print the JSON string representation of the object
print(MarketplaceProductStatisticsSchema.to_json())

# convert the object into a dict
marketplace_product_statistics_schema_dict = marketplace_product_statistics_schema_instance.to_dict()
# create an instance of MarketplaceProductStatisticsSchema from a dict
marketplace_product_statistics_schema_from_dict = MarketplaceProductStatisticsSchema.from_dict(marketplace_product_statistics_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


