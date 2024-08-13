# EntitiesSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_from** | **int** | Date first seen. | [optional] 
**active_till** | **int** | Date last seen. | [optional] 
**last_updated** | **int** | Last modification date. | [optional] 
**links** | [**EntitiesSchemaLinks**](EntitiesSchemaLinks.md) |  | 
**type** | **str** | Entity &#x60;type&#x60;. | 
**uid** | **str** | Unique entity identifier. | 
**value** | **str** | Entity &#x60;value&#x60;. | 

## Example

```python
from titan_client.models.entities_schema import EntitiesSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EntitiesSchema from a JSON string
entities_schema_instance = EntitiesSchema.from_json(json)
# print the JSON string representation of the object
print(EntitiesSchema.to_json())

# convert the object into a dict
entities_schema_dict = entities_schema_instance.to_dict()
# create an instance of EntitiesSchema from a dict
entities_schema_from_dict = EntitiesSchema.from_dict(entities_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


