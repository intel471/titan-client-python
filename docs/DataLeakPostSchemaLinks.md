# DataLeakPostSchemaLinks

Linked data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blog** | [**DataLeakPostSchemaLinksBlog**](DataLeakPostSchemaLinksBlog.md) |  | [optional] 
**images** | [**List[ImageSnakeCaseSchema]**](ImageSnakeCaseSchema.md) | Array of images (if present). | [optional] 
**thread** | [**DataLeakPostSchemaLinksThread**](DataLeakPostSchemaLinksThread.md) |  | [optional] 

## Example

```python
from titan_client.models.data_leak_post_schema_links import DataLeakPostSchemaLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakPostSchemaLinks from a JSON string
data_leak_post_schema_links_instance = DataLeakPostSchemaLinks.from_json(json)
# print the JSON string representation of the object
print(DataLeakPostSchemaLinks.to_json())

# convert the object into a dict
data_leak_post_schema_links_dict = data_leak_post_schema_links_instance.to_dict()
# create an instance of DataLeakPostSchemaLinks from a dict
data_leak_post_schema_links_from_dict = DataLeakPostSchemaLinks.from_dict(data_leak_post_schema_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


