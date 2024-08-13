# MarketplaceSearchSchemaActivity

Period when marketplace was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the marketplace activity range. | 
**last** | **int** | End of the marketplace activity range. | 

## Example

```python
from titan_client.models.marketplace_search_schema_activity import MarketplaceSearchSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceSearchSchemaActivity from a JSON string
marketplace_search_schema_activity_instance = MarketplaceSearchSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(MarketplaceSearchSchemaActivity.to_json())

# convert the object into a dict
marketplace_search_schema_activity_dict = marketplace_search_schema_activity_instance.to_dict()
# create an instance of MarketplaceSearchSchemaActivity from a dict
marketplace_search_schema_activity_from_dict = MarketplaceSearchSchemaActivity.from_dict(marketplace_search_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


