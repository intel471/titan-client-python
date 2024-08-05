# SimpleCveSchemaDataCveReportActivityLocation

Location of activity/discussion for the CVE.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_opensource** | **bool** | The CVE is being discussed in open source. | [optional] 
**location_private** | **bool** | The CVE is being discussed in private/direct communications. | [optional] 
**location_underground** | **bool** | The CVE is being discussed in the underground. | [optional] 

## Example

```python
from titan_client.models.simple_cve_schema_data_cve_report_activity_location import SimpleCveSchemaDataCveReportActivityLocation

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCveSchemaDataCveReportActivityLocation from a JSON string
simple_cve_schema_data_cve_report_activity_location_instance = SimpleCveSchemaDataCveReportActivityLocation.from_json(json)
# print the JSON string representation of the object
print(SimpleCveSchemaDataCveReportActivityLocation.to_json())

# convert the object into a dict
simple_cve_schema_data_cve_report_activity_location_dict = simple_cve_schema_data_cve_report_activity_location_instance.to_dict()
# create an instance of SimpleCveSchemaDataCveReportActivityLocation from a dict
simple_cve_schema_data_cve_report_activity_location_from_dict = SimpleCveSchemaDataCveReportActivityLocation.from_dict(simple_cve_schema_data_cve_report_activity_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


