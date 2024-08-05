# FullWatcherGroupSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Type of watcher group ownership. | [optional] 
**muted** | **bool** | Watcher&#39;s mute status (a watcher group is muted if all of its watchers are muted) | 
**name** | **str** | Name of watcher group. | 
**owner** | **str** | Watcher group owner&#39;s name. | 
**type** | **str** | Type of watcher group ownership. | 
**uid** | **str** | Unique watcher group identifier. | 
**watchers** | [**List[FullWatcherGroupSchemaAllOfWatchers]**](FullWatcherGroupSchemaAllOfWatchers.md) | List of Watchers. Watchers are displayed only for alerts included in results. | 

## Example

```python
from titan_client.models.full_watcher_group_schema import FullWatcherGroupSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FullWatcherGroupSchema from a JSON string
full_watcher_group_schema_instance = FullWatcherGroupSchema.from_json(json)
# print the JSON string representation of the object
print(FullWatcherGroupSchema.to_json())

# convert the object into a dict
full_watcher_group_schema_dict = full_watcher_group_schema_instance.to_dict()
# create an instance of FullWatcherGroupSchema from a dict
full_watcher_group_schema_from_dict = FullWatcherGroupSchema.from_dict(full_watcher_group_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


