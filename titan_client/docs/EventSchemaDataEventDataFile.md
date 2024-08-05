# EventSchemaDataEventDataFile

Object containing fields of the `file`'s hashes (`md5`, `sha1`, `sha256`) and file `type`, `size` and `download_url`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | The url where the file can be downloaded. | 
**md5** | **str** | An &#x60;md5&#x60; hash of the file. | 
**sha1** | **str** | An &#x60;sha1&#x60; hash of the file. | 
**sha256** | **str** | An &#x60;sha256&#x60; hash of the file. | 
**size** | **float** | &#x60;Size&#x60; of the file. | [optional] 
**type** | **str** | &#x60;Type&#x60; of the file. | [optional] 

## Example

```python
from titan_client.models.event_schema_data_event_data_file import EventSchemaDataEventDataFile

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaDataEventDataFile from a JSON string
event_schema_data_event_data_file_instance = EventSchemaDataEventDataFile.from_json(json)
# print the JSON string representation of the object
print(EventSchemaDataEventDataFile.to_json())

# convert the object into a dict
event_schema_data_event_data_file_dict = event_schema_data_event_data_file_instance.to_dict()
# create an instance of EventSchemaDataEventDataFile from a dict
event_schema_data_event_data_file_from_dict = EventSchemaDataEventDataFile.from_dict(event_schema_data_event_data_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


