# FullWatcherGroupSchemaAllOfLinksThread

Watched forum thread data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Posts count. | [optional] 
**topic** | **str** | Subject of forum thread. | [optional] 
**uid** | **str** | Unique forum thread indentifier. | [optional] 

## Example

```python
from titan_client.models.full_watcher_group_schema_all_of_links_thread import FullWatcherGroupSchemaAllOfLinksThread

# TODO update the JSON string below
json = "{}"
# create an instance of FullWatcherGroupSchemaAllOfLinksThread from a JSON string
full_watcher_group_schema_all_of_links_thread_instance = FullWatcherGroupSchemaAllOfLinksThread.from_json(json)
# print the JSON string representation of the object
print(FullWatcherGroupSchemaAllOfLinksThread.to_json())

# convert the object into a dict
full_watcher_group_schema_all_of_links_thread_dict = full_watcher_group_schema_all_of_links_thread_instance.to_dict()
# create an instance of FullWatcherGroupSchemaAllOfLinksThread from a dict
full_watcher_group_schema_all_of_links_thread_from_dict = FullWatcherGroupSchemaAllOfLinksThread.from_dict(full_watcher_group_schema_all_of_links_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


