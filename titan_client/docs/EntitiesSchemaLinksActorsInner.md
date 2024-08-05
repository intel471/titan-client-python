# EntitiesSchemaLinksActorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handles** | **List[str]** | The actor&#39;s &#x60;handles&#x60;. | [optional] 
**uid** | **str** | Unique indentifier of linked actor. | 

## Example

```python
from titan_client.models.entities_schema_links_actors_inner import EntitiesSchemaLinksActorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EntitiesSchemaLinksActorsInner from a JSON string
entities_schema_links_actors_inner_instance = EntitiesSchemaLinksActorsInner.from_json(json)
# print the JSON string representation of the object
print(EntitiesSchemaLinksActorsInner.to_json())

# convert the object into a dict
entities_schema_links_actors_inner_dict = entities_schema_links_actors_inner_instance.to_dict()
# create an instance of EntitiesSchemaLinksActorsInner from a dict
entities_schema_links_actors_inner_from_dict = EntitiesSchemaLinksActorsInner.from_dict(entities_schema_links_actors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


