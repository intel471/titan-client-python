# IndicatorSearchSchemaActivity

Period an indicator was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the indicator activity range. | 
**last** | **int** | End of the indicator activity range. | 

## Example

```python
from titan_client.models.indicator_search_schema_activity import IndicatorSearchSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorSearchSchemaActivity from a JSON string
indicator_search_schema_activity_instance = IndicatorSearchSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(IndicatorSearchSchemaActivity.to_json())

# convert the object into a dict
indicator_search_schema_activity_dict = indicator_search_schema_activity_instance.to_dict()
# create an instance of IndicatorSearchSchemaActivity from a dict
indicator_search_schema_activity_from_dict = IndicatorSearchSchemaActivity.from_dict(indicator_search_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


