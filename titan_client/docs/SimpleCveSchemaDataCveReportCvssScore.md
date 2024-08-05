# SimpleCveSchemaDataCveReportCvssScore

Numerical score reflecting CVE severity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v2** | **float** | CVSS score version 2. | [optional] 
**v3** | **float** | CVSS score version 3. | [optional] 

## Example

```python
from titan_client.models.simple_cve_schema_data_cve_report_cvss_score import SimpleCveSchemaDataCveReportCvssScore

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCveSchemaDataCveReportCvssScore from a JSON string
simple_cve_schema_data_cve_report_cvss_score_instance = SimpleCveSchemaDataCveReportCvssScore.from_json(json)
# print the JSON string representation of the object
print(SimpleCveSchemaDataCveReportCvssScore.to_json())

# convert the object into a dict
simple_cve_schema_data_cve_report_cvss_score_dict = simple_cve_schema_data_cve_report_cvss_score_instance.to_dict()
# create an instance of SimpleCveSchemaDataCveReportCvssScore from a dict
simple_cve_schema_data_cve_report_cvss_score_from_dict = SimpleCveSchemaDataCveReportCvssScore.from_dict(simple_cve_schema_data_cve_report_cvss_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


