# DataLeakPostSchemaLinksThread

Data leak thread in which the post was found.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | &#x60;Count&#x60; of posts in thread. | 
**topic** | **str** | Data leak thread &#x60;topic&#x60;. If post topic is translated, this parameter contains translated topic, if not — original. | [optional] 
**uid** | **str** | Unique data leak thread identifier. | 

## Example

```python
from titan_client.models.data_leak_post_schema_links_thread import DataLeakPostSchemaLinksThread

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakPostSchemaLinksThread from a JSON string
data_leak_post_schema_links_thread_instance = DataLeakPostSchemaLinksThread.from_json(json)
# print the JSON string representation of the object
print(DataLeakPostSchemaLinksThread.to_json())

# convert the object into a dict
data_leak_post_schema_links_thread_dict = data_leak_post_schema_links_thread_instance.to_dict()
# create an instance of DataLeakPostSchemaLinksThread from a dict
data_leak_post_schema_links_thread_from_dict = DataLeakPostSchemaLinksThread.from_dict(data_leak_post_schema_links_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


