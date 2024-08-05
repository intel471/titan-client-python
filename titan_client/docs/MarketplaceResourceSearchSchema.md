# MarketplaceResourceSearchSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**MarketplaceResourceSearchSchemaActivity**](MarketplaceResourceSearchSchemaActivity.md) |  | 
**data** | [**MarketplaceResourceSearchSchemaData**](MarketplaceResourceSearchSchemaData.md) |  | 
**last_updated** | **int** | Last modification date. | 
**uid** | **str** | Unique resource identifier. | 

## Example

```python
from titan_client.models.marketplace_resource_search_schema import MarketplaceResourceSearchSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceResourceSearchSchema from a JSON string
marketplace_resource_search_schema_instance = MarketplaceResourceSearchSchema.from_json(json)
# print the JSON string representation of the object
print(MarketplaceResourceSearchSchema.to_json())

# convert the object into a dict
marketplace_resource_search_schema_dict = marketplace_resource_search_schema_instance.to_dict()
# create an instance of MarketplaceResourceSearchSchema from a dict
marketplace_resource_search_schema_from_dict = MarketplaceResourceSearchSchema.from_dict(marketplace_resource_search_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


