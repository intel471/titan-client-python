# IndicatorSearchSchemaMeta

Meta data used to describe document version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Document &#x60;version&#x60;. | 

## Example

```python
from titan_client.models.indicator_search_schema_meta import IndicatorSearchSchemaMeta

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorSearchSchemaMeta from a JSON string
indicator_search_schema_meta_instance = IndicatorSearchSchemaMeta.from_json(json)
# print the JSON string representation of the object
print(IndicatorSearchSchemaMeta.to_json())

# convert the object into a dict
indicator_search_schema_meta_dict = indicator_search_schema_meta_instance.to_dict()
# create an instance of IndicatorSearchSchemaMeta from a dict
indicator_search_schema_meta_from_dict = IndicatorSearchSchemaMeta.from_dict(indicator_search_schema_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


