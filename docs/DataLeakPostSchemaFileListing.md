# DataLeakPostSchemaFileListing

File listing information/meta data (if present).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | Url for downloading file listing archive. | 

## Example

```python
from titan_client.models.data_leak_post_schema_file_listing import DataLeakPostSchemaFileListing

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakPostSchemaFileListing from a JSON string
data_leak_post_schema_file_listing_instance = DataLeakPostSchemaFileListing.from_json(json)
# print the JSON string representation of the object
print(DataLeakPostSchemaFileListing.to_json())

# convert the object into a dict
data_leak_post_schema_file_listing_dict = data_leak_post_schema_file_listing_instance.to_dict()
# create an instance of DataLeakPostSchemaFileListing from a dict
data_leak_post_schema_file_listing_from_dict = DataLeakPostSchemaFileListing.from_dict(data_leak_post_schema_file_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


