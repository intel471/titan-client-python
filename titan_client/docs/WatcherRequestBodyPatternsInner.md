# WatcherRequestBodyPatternsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **str** | Search pattern. | [optional] 
**types** | **str** | Search pattern type. Any mismatch will result to &#x60;FreeText&#x60; value in this field. | [optional] 

## Example

```python
from titan_client.models.watcher_request_body_patterns_inner import WatcherRequestBodyPatternsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WatcherRequestBodyPatternsInner from a JSON string
watcher_request_body_patterns_inner_instance = WatcherRequestBodyPatternsInner.from_json(json)
# print the JSON string representation of the object
print(WatcherRequestBodyPatternsInner.to_json())

# convert the object into a dict
watcher_request_body_patterns_inner_dict = watcher_request_body_patterns_inner_instance.to_dict()
# create an instance of WatcherRequestBodyPatternsInner from a dict
watcher_request_body_patterns_inner_from_dict = WatcherRequestBodyPatternsInner.from_dict(watcher_request_body_patterns_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


