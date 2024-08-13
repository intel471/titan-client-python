# WatcherSchemaLinksInnerThread

Forum `thread` object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Thread &#x60;topic&#x60;. | 
**uid** | **str** | Thread identifier. | 

## Example

```python
from titan_client.models.watcher_schema_links_inner_thread import WatcherSchemaLinksInnerThread

# TODO update the JSON string below
json = "{}"
# create an instance of WatcherSchemaLinksInnerThread from a JSON string
watcher_schema_links_inner_thread_instance = WatcherSchemaLinksInnerThread.from_json(json)
# print the JSON string representation of the object
print(WatcherSchemaLinksInnerThread.to_json())

# convert the object into a dict
watcher_schema_links_inner_thread_dict = watcher_schema_links_inner_thread_instance.to_dict()
# create an instance of WatcherSchemaLinksInnerThread from a dict
watcher_schema_links_inner_thread_from_dict = WatcherSchemaLinksInnerThread.from_dict(watcher_schema_links_inner_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


