# WatcherSchemaLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forum** | [**WatcherSchemaLinksInnerForum**](WatcherSchemaLinksInnerForum.md) |  | 
**thread** | [**WatcherSchemaLinksInnerThread**](WatcherSchemaLinksInnerThread.md) |  | 

## Example

```python
from titan_client.models.watcher_schema_links_inner import WatcherSchemaLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of WatcherSchemaLinksInner from a JSON string
watcher_schema_links_inner_instance = WatcherSchemaLinksInner.from_json(json)
# print the JSON string representation of the object
print(WatcherSchemaLinksInner.to_json())

# convert the object into a dict
watcher_schema_links_inner_dict = watcher_schema_links_inner_instance.to_dict()
# create an instance of WatcherSchemaLinksInner from a dict
watcher_schema_links_inner_from_dict = WatcherSchemaLinksInner.from_dict(watcher_schema_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


