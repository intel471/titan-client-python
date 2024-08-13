# SimpleCveSchemaDataCveReportInterestLevel

Level of interest for the CVE.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disclosed_publicly** | **bool** | The CVE has been &#x60;disclosed publicly&#x60;. | [optional] 
**exploit_sought** | **bool** | An actor is seeking an exploit of the CVE. | [optional] 
**researched_publicly** | **bool** | The CVE has been documented &#x60;researched publicly&#x60;. | [optional] 

## Example

```python
from titan_client.models.simple_cve_schema_data_cve_report_interest_level import SimpleCveSchemaDataCveReportInterestLevel

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCveSchemaDataCveReportInterestLevel from a JSON string
simple_cve_schema_data_cve_report_interest_level_instance = SimpleCveSchemaDataCveReportInterestLevel.from_json(json)
# print the JSON string representation of the object
print(SimpleCveSchemaDataCveReportInterestLevel.to_json())

# convert the object into a dict
simple_cve_schema_data_cve_report_interest_level_dict = simple_cve_schema_data_cve_report_interest_level_instance.to_dict()
# create an instance of SimpleCveSchemaDataCveReportInterestLevel from a dict
simple_cve_schema_data_cve_report_interest_level_from_dict = SimpleCveSchemaDataCveReportInterestLevel.from_dict(simple_cve_schema_data_cve_report_interest_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


