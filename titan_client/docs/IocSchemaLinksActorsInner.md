# IocSchemaLinksActorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handles** | **List[str]** | List of actor&#39;s &#x60;handles&#x60;. | [optional] 
**uid** | **str** | Unique indentifier of linked actor. | 

## Example

```python
from titan_client.models.ioc_schema_links_actors_inner import IocSchemaLinksActorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IocSchemaLinksActorsInner from a JSON string
ioc_schema_links_actors_inner_instance = IocSchemaLinksActorsInner.from_json(json)
# print the JSON string representation of the object
print(IocSchemaLinksActorsInner.to_json())

# convert the object into a dict
ioc_schema_links_actors_inner_dict = ioc_schema_links_actors_inner_instance.to_dict()
# create an instance of IocSchemaLinksActorsInner from a dict
ioc_schema_links_actors_inner_from_dict = IocSchemaLinksActorsInner.from_dict(ioc_schema_links_actors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


