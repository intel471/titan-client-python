# SimpleSpotReportSchemaData

Sub-document containing Spot report and linked to in objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[SimpleSpotReportSchemaDataEntitiesInner]**](SimpleSpotReportSchemaDataEntitiesInner.md) | List of &#x60;entities&#x60;. | [optional] 
**spot_report** | [**SimpleSpotReportSchemaDataSpotReport**](SimpleSpotReportSchemaDataSpotReport.md) |  | 

## Example

```python
from titan_client.models.simple_spot_report_schema_data import SimpleSpotReportSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleSpotReportSchemaData from a JSON string
simple_spot_report_schema_data_instance = SimpleSpotReportSchemaData.from_json(json)
# print the JSON string representation of the object
print(SimpleSpotReportSchemaData.to_json())

# convert the object into a dict
simple_spot_report_schema_data_dict = simple_spot_report_schema_data_instance.to_dict()
# create an instance of SimpleSpotReportSchemaData from a dict
simple_spot_report_schema_data_from_dict = SimpleSpotReportSchemaData.from_dict(simple_spot_report_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


