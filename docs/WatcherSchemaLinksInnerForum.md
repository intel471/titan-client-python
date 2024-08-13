# WatcherSchemaLinksInnerForum

Forum object of a watched thread.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Forum &#x60;description&#x60;. | [optional] 
**name** | **str** | Forum &#x60;name&#x60;. | 
**uid** | **str** | Forum identifier. | 

## Example

```python
from titan_client.models.watcher_schema_links_inner_forum import WatcherSchemaLinksInnerForum

# TODO update the JSON string below
json = "{}"
# create an instance of WatcherSchemaLinksInnerForum from a JSON string
watcher_schema_links_inner_forum_instance = WatcherSchemaLinksInnerForum.from_json(json)
# print the JSON string representation of the object
print(WatcherSchemaLinksInnerForum.to_json())

# convert the object into a dict
watcher_schema_links_inner_forum_dict = watcher_schema_links_inner_forum_instance.to_dict()
# create an instance of WatcherSchemaLinksInnerForum from a dict
watcher_schema_links_inner_forum_from_dict = WatcherSchemaLinksInnerForum.from_dict(watcher_schema_links_inner_forum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


