# DataLeakPostSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_number** | **int** | Data leak post file listing search terms chunk number in which search term was found. File listing search terms related to specific post are stored as chunks. | [optional] 
**var_date** | **int** | The &#x60;date&#x60; of the data leak post. | 
**file_listing** | [**DataLeakPostSchemaFileListing**](DataLeakPostSchemaFileListing.md) |  | [optional] 
**last_updated** | **int** | Last modification date. | [optional] 
**links** | [**DataLeakPostSchemaLinks**](DataLeakPostSchemaLinks.md) |  | 
**message** | **str** | HTML data leak post content. | 
**uid** | **str** | Unique data leak post identifier. | 

## Example

```python
from titan_client.models.data_leak_post_schema import DataLeakPostSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakPostSchema from a JSON string
data_leak_post_schema_instance = DataLeakPostSchema.from_json(json)
# print the JSON string representation of the object
print(DataLeakPostSchema.to_json())

# convert the object into a dict
data_leak_post_schema_dict = data_leak_post_schema_instance.to_dict()
# create an instance of DataLeakPostSchema from a dict
data_leak_post_schema_from_dict = DataLeakPostSchema.from_dict(data_leak_post_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


