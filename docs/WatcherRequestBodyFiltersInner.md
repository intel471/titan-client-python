# WatcherRequestBodyFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Search filter. | [optional] 
**type** | **str** | Search filter type. Any mismatch with search pattern type will remove filters. | [optional] 

## Example

```python
from titan_client.models.watcher_request_body_filters_inner import WatcherRequestBodyFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of WatcherRequestBodyFiltersInner from a JSON string
watcher_request_body_filters_inner_instance = WatcherRequestBodyFiltersInner.from_json(json)
# print the JSON string representation of the object
print(WatcherRequestBodyFiltersInner.to_json())

# convert the object into a dict
watcher_request_body_filters_inner_dict = watcher_request_body_filters_inner_instance.to_dict()
# create an instance of WatcherRequestBodyFiltersInner from a dict
watcher_request_body_filters_inner_from_dict = WatcherRequestBodyFiltersInner.from_dict(watcher_request_body_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


