# WatcherSchemaFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Search &#x60;filter&#x60;. | 
**type** | **str** | Type of search filter. | 

## Example

```python
from titan_client.models.watcher_schema_filters_inner import WatcherSchemaFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of WatcherSchemaFiltersInner from a JSON string
watcher_schema_filters_inner_instance = WatcherSchemaFiltersInner.from_json(json)
# print the JSON string representation of the object
print(WatcherSchemaFiltersInner.to_json())

# convert the object into a dict
watcher_schema_filters_inner_dict = watcher_schema_filters_inner_instance.to_dict()
# create an instance of WatcherSchemaFiltersInner from a dict
watcher_schema_filters_inner_from_dict = WatcherSchemaFiltersInner.from_dict(watcher_schema_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


