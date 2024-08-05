# MarketplaceResourceSearchSchemaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | **str** | Internet browser. | 
**contains** | **List[str]** | Datasets of resource. | [optional] 
**grabbed_at** | **int** | Timestamp when resource was grabbed. | 
**name** | **str** | Name (url) of resource. | 
**package** | **str** | Package name of resource. | 
**source** | **str** | Source of resource. | 
**url** | **str** | Url of resource. | 

## Example

```python
from titan_client.models.marketplace_resource_search_schema_data import MarketplaceResourceSearchSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceResourceSearchSchemaData from a JSON string
marketplace_resource_search_schema_data_instance = MarketplaceResourceSearchSchemaData.from_json(json)
# print the JSON string representation of the object
print(MarketplaceResourceSearchSchemaData.to_json())

# convert the object into a dict
marketplace_resource_search_schema_data_dict = marketplace_resource_search_schema_data_instance.to_dict()
# create an instance of MarketplaceResourceSearchSchemaData from a dict
marketplace_resource_search_schema_data_from_dict = MarketplaceResourceSearchSchemaData.from_dict(marketplace_resource_search_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


