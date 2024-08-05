# FullWatcherGroupSchemaAllOfWatchers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Watcher description. | [optional] 
**links** | [**FullWatcherGroupSchemaAllOfLinks**](FullWatcherGroupSchemaAllOfLinks.md) |  | [optional] 
**patterns** | [**List[FullWatcherGroupSchemaAllOfPatterns]**](FullWatcherGroupSchemaAllOfPatterns.md) | List of Search patterns. Applicable for watchers of search type only. | [optional] 
**type** | **str** | Watcher type — search or thread. | 
**uid** | **str** | Unique watcher identifier. | 

## Example

```python
from titan_client.models.full_watcher_group_schema_all_of_watchers import FullWatcherGroupSchemaAllOfWatchers

# TODO update the JSON string below
json = "{}"
# create an instance of FullWatcherGroupSchemaAllOfWatchers from a JSON string
full_watcher_group_schema_all_of_watchers_instance = FullWatcherGroupSchemaAllOfWatchers.from_json(json)
# print the JSON string representation of the object
print(FullWatcherGroupSchemaAllOfWatchers.to_json())

# convert the object into a dict
full_watcher_group_schema_all_of_watchers_dict = full_watcher_group_schema_all_of_watchers_instance.to_dict()
# create an instance of FullWatcherGroupSchemaAllOfWatchers from a dict
full_watcher_group_schema_all_of_watchers_from_dict = FullWatcherGroupSchemaAllOfWatchers.from_dict(full_watcher_group_schema_all_of_watchers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


