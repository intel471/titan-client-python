# IndicatorSearchSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**IndicatorSearchSchemaActivity**](IndicatorSearchSchemaActivity.md) |  | [optional] 
**data** | [**IndicatorSearchSchemaData**](IndicatorSearchSchemaData.md) |  | 
**last_updated** | **int** | Indicator last modification date. | 
**meta** | [**IndicatorSearchSchemaMeta**](IndicatorSearchSchemaMeta.md) |  | [optional] 
**uid** | **str** | Unique indicator identifier. | [optional] 

## Example

```python
from titan_client.models.indicator_search_schema import IndicatorSearchSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorSearchSchema from a JSON string
indicator_search_schema_instance = IndicatorSearchSchema.from_json(json)
# print the JSON string representation of the object
print(IndicatorSearchSchema.to_json())

# convert the object into a dict
indicator_search_schema_dict = indicator_search_schema_instance.to_dict()
# create an instance of IndicatorSearchSchema from a dict
indicator_search_schema_from_dict = IndicatorSearchSchema.from_dict(indicator_search_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


