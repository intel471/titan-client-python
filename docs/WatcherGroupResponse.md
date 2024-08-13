# WatcherGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**watcher_group_total_count** | **int** | Total count of watcher groups. | 
**watcher_groups** | [**List[SimpleWatcherGroupSchema]**](SimpleWatcherGroupSchema.md) | List of watcher groups. | [optional] 

## Example

```python
from titan_client.models.watcher_group_response import WatcherGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WatcherGroupResponse from a JSON string
watcher_group_response_instance = WatcherGroupResponse.from_json(json)
# print the JSON string representation of the object
print(WatcherGroupResponse.to_json())

# convert the object into a dict
watcher_group_response_dict = watcher_group_response_instance.to_dict()
# create an instance of WatcherGroupResponse from a dict
watcher_group_response_from_dict = WatcherGroupResponse.from_dict(watcher_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


