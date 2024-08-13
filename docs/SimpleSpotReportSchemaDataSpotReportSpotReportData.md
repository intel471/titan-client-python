# SimpleSpotReportSchemaDataSpotReportSpotReportData

Sub-document containing Spot report data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_of_information** | **int** | Spot report date of information. | 
**intel_requirements** | **List[str]** | General Intel Requirements (GIR). | [optional] 
**links** | [**List[SimpleSpotReportSchemaDataSpotReportSpotReportDataLinksInner]**](SimpleSpotReportSchemaDataSpotReportSpotReportDataLinksInner.md) | Links to any other entity in portal, like Post, Thread or external &#x60;resource&#x60;. | [optional] 
**related_reports** | **List[str]** | Spot report links to related reports like \&quot;Information Report\&quot; or \&quot;Malware Report\&quot;. | [optional] 
**released_at** | **int** | Spot report released date. | 
**sensitive_source** | **bool** | Indicates if the document contains sensitive source derived information. | [optional] 
**text** | **str** | Spot report text. | 
**title** | **str** | Spot report title. | [optional] 
**version** | **str** | Spot report release &#x60;version&#x60;. | 
**victims** | [**List[SimpleSpotReportSchemaDataSpotReportSpotReportDataVictimsInner]**](SimpleSpotReportSchemaDataSpotReportSpotReportDataVictimsInner.md) | List of purported &#x60;victims&#x60;. | [optional] 

## Example

```python
from titan_client.models.simple_spot_report_schema_data_spot_report_spot_report_data import SimpleSpotReportSchemaDataSpotReportSpotReportData

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleSpotReportSchemaDataSpotReportSpotReportData from a JSON string
simple_spot_report_schema_data_spot_report_spot_report_data_instance = SimpleSpotReportSchemaDataSpotReportSpotReportData.from_json(json)
# print the JSON string representation of the object
print(SimpleSpotReportSchemaDataSpotReportSpotReportData.to_json())

# convert the object into a dict
simple_spot_report_schema_data_spot_report_spot_report_data_dict = simple_spot_report_schema_data_spot_report_spot_report_data_instance.to_dict()
# create an instance of SimpleSpotReportSchemaDataSpotReportSpotReportData from a dict
simple_spot_report_schema_data_spot_report_spot_report_data_from_dict = SimpleSpotReportSchemaDataSpotReportSpotReportData.from_dict(simple_spot_report_schema_data_spot_report_spot_report_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


