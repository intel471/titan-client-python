# IndicatorSearchSchemaDataIndicatorDataFile

File details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | File&#39;s download URL | [optional] 
**md5** | **str** | File&#39;s MD5 sum | [optional] 
**sha1** | **str** | File&#39;s SHA1 sum | [optional] 
**sha256** | **str** | File&#39;s SHA256 sum | [optional] 
**size** | **int** | File&#39;s size | [optional] 
**ssdeep** | **str** | File&#39;s ssdeep hash (fuzzy hash) | [optional] 
**type** | **str** | File&#39;s type | [optional] 

## Example

```python
from titan_client.models.indicator_search_schema_data_indicator_data_file import IndicatorSearchSchemaDataIndicatorDataFile

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorSearchSchemaDataIndicatorDataFile from a JSON string
indicator_search_schema_data_indicator_data_file_instance = IndicatorSearchSchemaDataIndicatorDataFile.from_json(json)
# print the JSON string representation of the object
print(IndicatorSearchSchemaDataIndicatorDataFile.to_json())

# convert the object into a dict
indicator_search_schema_data_indicator_data_file_dict = indicator_search_schema_data_indicator_data_file_instance.to_dict()
# create an instance of IndicatorSearchSchemaDataIndicatorDataFile from a dict
indicator_search_schema_data_indicator_data_file_from_dict = IndicatorSearchSchemaDataIndicatorDataFile.from_dict(indicator_search_schema_data_indicator_data_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


