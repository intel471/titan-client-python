# IndicatorSearchSchemaDataContext

Sub-document containing contextual information to describe the observed malicious activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Free form text describing the indicator context. | 

## Example

```python
from titan_client.models.indicator_search_schema_data_context import IndicatorSearchSchemaDataContext

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorSearchSchemaDataContext from a JSON string
indicator_search_schema_data_context_instance = IndicatorSearchSchemaDataContext.from_json(json)
# print the JSON string representation of the object
print(IndicatorSearchSchemaDataContext.to_json())

# convert the object into a dict
indicator_search_schema_data_context_dict = indicator_search_schema_data_context_instance.to_dict()
# create an instance of IndicatorSearchSchemaDataContext from a dict
indicator_search_schema_data_context_from_dict = IndicatorSearchSchemaDataContext.from_dict(indicator_search_schema_data_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


