# WatcherSchemaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**watcher_total_count** | **int** | Watcher count. | 
**watchers** | [**List[WatcherSchema]**](WatcherSchema.md) | List of &#x60;watchers&#x60;. | [optional] 

## Example

```python
from titan_client.models.watcher_schema_response import WatcherSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WatcherSchemaResponse from a JSON string
watcher_schema_response_instance = WatcherSchemaResponse.from_json(json)
# print the JSON string representation of the object
print(WatcherSchemaResponse.to_json())

# convert the object into a dict
watcher_schema_response_dict = watcher_schema_response_instance.to_dict()
# create an instance of WatcherSchemaResponse from a dict
watcher_schema_response_from_dict = WatcherSchemaResponse.from_dict(watcher_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


