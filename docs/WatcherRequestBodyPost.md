# WatcherRequestBodyPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_sets** | **list[str]** | Limiting watcher by data sets. Defaults to all accessible data sets if empty. Please pay attention, that &#x60;Malware Reports&#x60; belongs to &#x60;malware&#x60; data set and &#x60;Vulnerability Reports&#x60; belong to cve data set. | [optional] 
**description** | **str** | Watcher description. | [optional] 
**filter_by_gir_set** | **str** | GIR set filter. | [optional] 
**filters** | [**list[WatcherRequestBodyFiltersInner]**](WatcherRequestBodyFiltersInner.md) | Search filters. Can be used with &#x60;search&#x60; watchers for narrowing results. More information about search filter types and their compatibility with search pattern types is [here](https://titan.intel471.com/api/docs/#api-_footer). | [optional] 
**free_text_pattern** | **str** | Simplified form of adding search pattern. Search type will be automatically set to &#x60;FreeText&#x60; and pattern will be filled with a given value. | [optional] 
**girs** | **list[str]** | GIR paths selected by user. Ignored if &#x60;filterByGirSet&#x60; isn&#39;t &#x60;custom&#x60;. | [optional] 
**notification_channel** | **str** | Notifications channel. email channel will send &#x60;email&#x60; notifications either &#x60;immediately&#x60; or &#x60;daily&#x60; (frequency has to be specified in another field). &#x60;website&#x60; channel doesn&#39;t send emails and keeps all notifications in the website. Regardless of the field value alerts are always accessible via API. | [optional] 
**notification_frequency** | **str** | Notification frequency. Applicable to &#x60;email&#x60; channel only. | [optional] 
**patterns** | [**list[WatcherRequestBodyPatternsInner]**](WatcherRequestBodyPatternsInner.md) | Extended form of adding search patterns to a &#x60;search&#x60; type watcher. Used to specify search pattern type (handle, IP address, hash, etc.). | [optional] 
**thread_uid** | **str** | Forum thread identifier. Applicable only for &#x60;thread&#x60; watcher type. | [optional] 
**type** | **str** | Watcher type.&lt;br /&gt;&#x60;search&#x60; type watcher queries search engine with a pattern provided,&lt;br /&gt;&#x60;thread&#x60; watcher monitors given forum thread for a new posts. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


