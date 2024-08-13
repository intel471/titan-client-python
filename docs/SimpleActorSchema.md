# SimpleActorSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_from** | **int** | Date first seen. | [optional] 
**active_until** | **int** | Date last seen. | [optional] 
**handles** | **List[str]** | List of actor&#39;s &#x60;handles&#x60;. | [optional] 
**last_updated** | **int** | Last modification date. | [optional] 
**links** | [**SimpleActorSchemaLinks**](SimpleActorSchemaLinks.md) |  | 
**uid** | **str** | Unique actor identifier. | 

## Example

```python
from titan_client.models.simple_actor_schema import SimpleActorSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleActorSchema from a JSON string
simple_actor_schema_instance = SimpleActorSchema.from_json(json)
# print the JSON string representation of the object
print(SimpleActorSchema.to_json())

# convert the object into a dict
simple_actor_schema_dict = simple_actor_schema_instance.to_dict()
# create an instance of SimpleActorSchema from a dict
simple_actor_schema_from_dict = SimpleActorSchema.from_dict(simple_actor_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


