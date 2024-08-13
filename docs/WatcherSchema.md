# WatcherSchema

Returns list of Watchers of a given Watcher group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_sets** | **List[str]** | Data sets the watcher is limited by. | [optional] 
**description** | **str** | Watcher &#x60;description&#x60;. | [optional] 
**filter_by_gir_set** | **str** | GIR set filter. | [optional] 
**filters** | [**List[WatcherSchemaFiltersInner]**](WatcherSchemaFiltersInner.md) | Search filter of &#x60;search&#x60; watcher. | [optional] 
**girs** | **List[str]** | GIR set paths defined by &#x60;filterByGirSet&#x60; param. | [optional] 
**links** | [**List[WatcherSchemaLinksInner]**](WatcherSchemaLinksInner.md) | Links to the Forum and Thread of the &#x60;thread&#x60; type watcher. | [optional] 
**muted** | **bool** | Watcher&#39;s mute status (if a watcher is muted, no alerts are received during its mute period) | 
**notification_channel** | **str** | Notification chanel. | 
**notification_frequency** | **str** | Notification frequency. | 
**patterns** | [**List[WatcherSchemaPatternsInner]**](WatcherSchemaPatternsInner.md) | Search query patterns applicable to a watcher of the &#x60;search&#x60; type. | [optional] 
**thread_type** | **str** | In case watcher &#x60;type&#x60; is &#x60;thread&#x60; the &#x60;threadType&#x60; must be specified. | [optional] 
**type** | **str** | Watcher &#x60;type&#x60;. | 
**uid** | **str** | Watcher identifier. | 

## Example

```python
from titan_client.models.watcher_schema import WatcherSchema

# TODO update the JSON string below
json = "{}"
# create an instance of WatcherSchema from a JSON string
watcher_schema_instance = WatcherSchema.from_json(json)
# print the JSON string representation of the object
print(WatcherSchema.to_json())

# convert the object into a dict
watcher_schema_dict = watcher_schema_instance.to_dict()
# create an instance of WatcherSchema from a dict
watcher_schema_from_dict = WatcherSchema.from_dict(watcher_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


