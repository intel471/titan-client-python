# SimpleActorSchemaLinksForumsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_handle** | **str** | Actor handle. | [optional] 
**contact_info** | [**List[SimpleActorSchemaLinksForumsInnerContactInfoInner]**](SimpleActorSchemaLinksForumsInnerContactInfoInner.md) | &#x60;Contact Info&#x60; objects. | [optional] 
**name** | **str** | Forum &#x60;name&#x60;. | 
**time_zone** | **str** | &#x60;Timezone&#x60;. | [optional] 
**uid** | **str** | Unique forum identifier. | 

## Example

```python
from titan_client.models.simple_actor_schema_links_forums_inner import SimpleActorSchemaLinksForumsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleActorSchemaLinksForumsInner from a JSON string
simple_actor_schema_links_forums_inner_instance = SimpleActorSchemaLinksForumsInner.from_json(json)
# print the JSON string representation of the object
print(SimpleActorSchemaLinksForumsInner.to_json())

# convert the object into a dict
simple_actor_schema_links_forums_inner_dict = simple_actor_schema_links_forums_inner_instance.to_dict()
# create an instance of SimpleActorSchemaLinksForumsInner from a dict
simple_actor_schema_links_forums_inner_from_dict = SimpleActorSchemaLinksForumsInner.from_dict(simple_actor_schema_links_forums_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


