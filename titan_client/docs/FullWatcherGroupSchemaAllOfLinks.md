# FullWatcherGroupSchemaAllOfLinks

Watcher linked data. Only for thread watchers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forum** | [**FullWatcherGroupSchemaAllOfLinksForum**](FullWatcherGroupSchemaAllOfLinksForum.md) |  | [optional] 
**thread** | [**FullWatcherGroupSchemaAllOfLinksThread**](FullWatcherGroupSchemaAllOfLinksThread.md) |  | [optional] 

## Example

```python
from titan_client.models.full_watcher_group_schema_all_of_links import FullWatcherGroupSchemaAllOfLinks

# TODO update the JSON string below
json = "{}"
# create an instance of FullWatcherGroupSchemaAllOfLinks from a JSON string
full_watcher_group_schema_all_of_links_instance = FullWatcherGroupSchemaAllOfLinks.from_json(json)
# print the JSON string representation of the object
print(FullWatcherGroupSchemaAllOfLinks.to_json())

# convert the object into a dict
full_watcher_group_schema_all_of_links_dict = full_watcher_group_schema_all_of_links_instance.to_dict()
# create an instance of FullWatcherGroupSchemaAllOfLinks from a dict
full_watcher_group_schema_all_of_links_from_dict = FullWatcherGroupSchemaAllOfLinks.from_dict(full_watcher_group_schema_all_of_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


