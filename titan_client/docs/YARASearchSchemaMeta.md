# YARASearchSchemaMeta

`Meta` data used to describe document version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Document version. | 

## Example

```python
from titan_client.models.yara_search_schema_meta import YARASearchSchemaMeta

# TODO update the JSON string below
json = "{}"
# create an instance of YARASearchSchemaMeta from a JSON string
yara_search_schema_meta_instance = YARASearchSchemaMeta.from_json(json)
# print the JSON string representation of the object
print(YARASearchSchemaMeta.to_json())

# convert the object into a dict
yara_search_schema_meta_dict = yara_search_schema_meta_instance.to_dict()
# create an instance of YARASearchSchemaMeta from a dict
yara_search_schema_meta_from_dict = YARASearchSchemaMeta.from_dict(yara_search_schema_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


