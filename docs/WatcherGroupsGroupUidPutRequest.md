# WatcherGroupsGroupUidPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | &#x60;Description&#x60; of Watcher Group to be created | [optional] 
**muted** | **bool** | Watcher&#39;s mute status | [optional] 
**name** | **str** | &#x60;Name&#x60; of Watcher Group to be created | [optional] 

## Example

```python
from titan_client.models.watcher_groups_group_uid_put_request import WatcherGroupsGroupUidPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WatcherGroupsGroupUidPutRequest from a JSON string
watcher_groups_group_uid_put_request_instance = WatcherGroupsGroupUidPutRequest.from_json(json)
# print the JSON string representation of the object
print(WatcherGroupsGroupUidPutRequest.to_json())

# convert the object into a dict
watcher_groups_group_uid_put_request_dict = watcher_groups_group_uid_put_request_instance.to_dict()
# create an instance of WatcherGroupsGroupUidPutRequest from a dict
watcher_groups_group_uid_put_request_from_dict = WatcherGroupsGroupUidPutRequest.from_dict(watcher_groups_group_uid_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


