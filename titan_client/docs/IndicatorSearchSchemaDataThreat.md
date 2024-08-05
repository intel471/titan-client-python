# IndicatorSearchSchemaDataThreat

Detailed information about a threat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IndicatorSearchSchemaDataThreatData**](IndicatorSearchSchemaDataThreatData.md) |  | 
**type** | **str** | Threat type: &#x60;malware&#x60;, &#x60;proxy_service&#x60; etc. | 
**uid** | **str** | Unique threat identifier. | 

## Example

```python
from titan_client.models.indicator_search_schema_data_threat import IndicatorSearchSchemaDataThreat

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorSearchSchemaDataThreat from a JSON string
indicator_search_schema_data_threat_instance = IndicatorSearchSchemaDataThreat.from_json(json)
# print the JSON string representation of the object
print(IndicatorSearchSchemaDataThreat.to_json())

# convert the object into a dict
indicator_search_schema_data_threat_dict = indicator_search_schema_data_threat_instance.to_dict()
# create an instance of IndicatorSearchSchemaDataThreat from a dict
indicator_search_schema_data_threat_from_dict = IndicatorSearchSchemaDataThreat.from_dict(indicator_search_schema_data_threat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


