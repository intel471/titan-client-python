# SimpleSpotReportSchemaDataSpotReport

Sub-document containing Spot report information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spot_report_data** | [**SimpleSpotReportSchemaDataSpotReportSpotReportData**](SimpleSpotReportSchemaDataSpotReportSpotReportData.md) |  | 
**uid** | **str** | Spot report&#39;s IDw. | [optional] 

## Example

```python
from titan_client.models.simple_spot_report_schema_data_spot_report import SimpleSpotReportSchemaDataSpotReport

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleSpotReportSchemaDataSpotReport from a JSON string
simple_spot_report_schema_data_spot_report_instance = SimpleSpotReportSchemaDataSpotReport.from_json(json)
# print the JSON string representation of the object
print(SimpleSpotReportSchemaDataSpotReport.to_json())

# convert the object into a dict
simple_spot_report_schema_data_spot_report_dict = simple_spot_report_schema_data_spot_report_instance.to_dict()
# create an instance of SimpleSpotReportSchemaDataSpotReport from a dict
simple_spot_report_schema_data_spot_report_from_dict = SimpleSpotReportSchemaDataSpotReport.from_dict(simple_spot_report_schema_data_spot_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


