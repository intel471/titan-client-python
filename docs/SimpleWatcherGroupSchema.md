# SimpleWatcherGroupSchema

Returns list of Watcher groups matching filter criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Type of watcher group ownership. | [optional] 
**muted** | **bool** | Watcher&#39;s mute status (a watcher group is muted if all of its watchers are muted) | 
**name** | **str** | Name of watcher group. | 
**owner** | **str** | Watcher group owner&#39;s name. | 
**type** | **str** | Type of watcher group ownership. | 
**uid** | **str** | Unique watcher group identifier. | 

## Example

```python
from titan_client.models.simple_watcher_group_schema import SimpleWatcherGroupSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleWatcherGroupSchema from a JSON string
simple_watcher_group_schema_instance = SimpleWatcherGroupSchema.from_json(json)
# print the JSON string representation of the object
print(SimpleWatcherGroupSchema.to_json())

# convert the object into a dict
simple_watcher_group_schema_dict = simple_watcher_group_schema_instance.to_dict()
# create an instance of SimpleWatcherGroupSchema from a dict
simple_watcher_group_schema_from_dict = SimpleWatcherGroupSchema.from_dict(simple_watcher_group_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


