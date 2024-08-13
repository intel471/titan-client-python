# IndicatorSearchSchemaDataIndicatorData

Sub-document containing indicator type and value(s).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address | [optional] 
**file** | [**IndicatorSearchSchemaDataIndicatorDataFile**](IndicatorSearchSchemaDataIndicatorDataFile.md) |  | [optional] 
**geo_ip** | [**EventSchemaDataEventDataControllerGeoIp**](EventSchemaDataEventDataControllerGeoIp.md) |  | [optional] 
**url** | **str** | The &#x60;url&#x60; of the indicator. | [optional] 

## Example

```python
from titan_client.models.indicator_search_schema_data_indicator_data import IndicatorSearchSchemaDataIndicatorData

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorSearchSchemaDataIndicatorData from a JSON string
indicator_search_schema_data_indicator_data_instance = IndicatorSearchSchemaDataIndicatorData.from_json(json)
# print the JSON string representation of the object
print(IndicatorSearchSchemaDataIndicatorData.to_json())

# convert the object into a dict
indicator_search_schema_data_indicator_data_dict = indicator_search_schema_data_indicator_data_instance.to_dict()
# create an instance of IndicatorSearchSchemaDataIndicatorData from a dict
indicator_search_schema_data_indicator_data_from_dict = IndicatorSearchSchemaDataIndicatorData.from_dict(indicator_search_schema_data_indicator_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


