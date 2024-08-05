# DataLeakPostSchemaLinksBlog

Data leak blog on which the post was found.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Data leak blog &#x60;description&#x60;. | [optional] 
**name** | **str** | Data leak blog &#x60;name&#x60;. | 
**uid** | **str** | Unique data leak blog identifier. | 

## Example

```python
from titan_client.models.data_leak_post_schema_links_blog import DataLeakPostSchemaLinksBlog

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakPostSchemaLinksBlog from a JSON string
data_leak_post_schema_links_blog_instance = DataLeakPostSchemaLinksBlog.from_json(json)
# print the JSON string representation of the object
print(DataLeakPostSchemaLinksBlog.to_json())

# convert the object into a dict
data_leak_post_schema_links_blog_dict = data_leak_post_schema_links_blog_instance.to_dict()
# create an instance of DataLeakPostSchemaLinksBlog from a dict
data_leak_post_schema_links_blog_from_dict = DataLeakPostSchemaLinksBlog.from_dict(data_leak_post_schema_links_blog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


