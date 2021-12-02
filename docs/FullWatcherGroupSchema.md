# FullWatcherGroupSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Type of watcher group ownership. | [optional] 
**muted** | **bool** | Watcher&#39;s mute status (a watcher group is muted if all of its watchers are muted) | 
**name** | **str** | Name of watcher group. | 
**owner** | **str** | Watcher group owner&#39;s name. | 
**type** | **str** | Type of watcher group ownership. | 
**uid** | **str** | Unique watcher group identifier. | 
**watchers** | [**list[FullWatcherGroupSchemaAllOfWatchers]**](FullWatcherGroupSchemaAllOfWatchers.md) | List of Watchers. Watchers are displayed only for alerts included in results. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


