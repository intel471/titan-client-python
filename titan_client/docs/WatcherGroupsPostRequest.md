# WatcherGroupsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | &#x60;Description&#x60; of Watcher Group to be created | [optional] 
**name** | **str** | &#x60;Name&#x60; of Watcher Group to be created | [optional] 

## Example

```python
from titan_client.models.watcher_groups_post_request import WatcherGroupsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WatcherGroupsPostRequest from a JSON string
watcher_groups_post_request_instance = WatcherGroupsPostRequest.from_json(json)
# print the JSON string representation of the object
print(WatcherGroupsPostRequest.to_json())

# convert the object into a dict
watcher_groups_post_request_dict = watcher_groups_post_request_instance.to_dict()
# create an instance of WatcherGroupsPostRequest from a dict
watcher_groups_post_request_from_dict = WatcherGroupsPostRequest.from_dict(watcher_groups_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


