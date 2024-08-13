# MarketplaceResourceSearchSchemaActivity

Period when resource was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the resource activity range. | 
**last** | **int** | End of the resource activity range. | 

## Example

```python
from titan_client.models.marketplace_resource_search_schema_activity import MarketplaceResourceSearchSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceResourceSearchSchemaActivity from a JSON string
marketplace_resource_search_schema_activity_instance = MarketplaceResourceSearchSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(MarketplaceResourceSearchSchemaActivity.to_json())

# convert the object into a dict
marketplace_resource_search_schema_activity_dict = marketplace_resource_search_schema_activity_instance.to_dict()
# create an instance of MarketplaceResourceSearchSchemaActivity from a dict
marketplace_resource_search_schema_activity_from_dict = MarketplaceResourceSearchSchemaActivity.from_dict(marketplace_resource_search_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


