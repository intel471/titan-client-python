# WatcherSchema

Returns list of Watchers of a given Watcher group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_sets** | **list[str]** | Data sets the watcher is limited by. | [optional] 
**description** | **str** | Watcher &#x60;description&#x60;. | [optional] 
**filter_by_gir_set** | **str** | GIR set filter. | [optional] 
**filters** | [**list[WatcherSchemaFilters]**](WatcherSchemaFilters.md) | Search filter of &#x60;search&#x60; watcher. | [optional] 
**girs** | **list[str]** | GIR set paths defined by &#x60;filterByGirSet&#x60; param. | [optional] 
**links** | [**list[WatcherSchemaLinks]**](WatcherSchemaLinks.md) | Links to the Forum and Thread of the &#x60;thread&#x60; type watcher. | [optional] 
**notification_channel** | **str** | Notification chanel. | 
**notification_frequency** | **str** | Notification frequency. | 
**patterns** | [**list[WatcherSchemaPatterns]**](WatcherSchemaPatterns.md) | Search query patterns applicable to a watcher of the &#x60;search&#x60; type. | [optional] 
**type** | **str** | Watcher &#x60;type&#x60;. | 
**uid** | **str** | Watcher identifier. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


