# SimpleCveSchemaDataCveReport

Sub-document containing report information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_location** | [**SimpleCveSchemaDataCveReportActivityLocation**](SimpleCveSchemaDataCveReportActivityLocation.md) |  | [optional] 
**counter_measure_links** | [**List[SimpleCveSchemaDataCveReportCounterMeasureLinksInner]**](SimpleCveSchemaDataCveReportCounterMeasureLinksInner.md) | Titled URLs to countermeasure information to protect against the CVE. | [optional] 
**counter_measures** | **str** | Summary of &#x60;countermeasures&#x60; to protect against the CVE. | [optional] 
**cpe** | **object** | &#x60;CPE&#x60; (Common Platform Enumeration) is the list of the software affected by the vulnerability. Raw data field. | [optional] 
**cve_status** | **str** | &#x60;status_new&#x60; for recently added CVE; &#x60;status_existing&#x60; for CVE being reported for a while; &#x60;status_historical&#x60; for phased out and not actual at the moment. Allowed values: &#x60;status_existing&#x60;, &#x60;status_new&#x60;, &#x60;status_historical&#x60;. | 
**cve_type** | **str** | Type of CVE, for example: &#x60;Buffer overflow&#x60;, &#x60;Privilege escalation&#x60;, &#x60;Memory corruption&#x60;, etc. | 
**cvss_score** | [**SimpleCveSchemaDataCveReportCvssScore**](SimpleCveSchemaDataCveReportCvssScore.md) |  | [optional] 
**detection** | **str** | Detection (signatures, definitions) exists for the CVE. Allowed values: &#x60;available&#x60;, &#x60;not_available&#x60;. | [optional] 
**exploit_status** | [**SimpleCveSchemaDataCveReportExploitStatus**](SimpleCveSchemaDataCveReportExploitStatus.md) |  | [optional] 
**interest_level** | [**SimpleCveSchemaDataCveReportInterestLevel**](SimpleCveSchemaDataCveReportInterestLevel.md) |  | [optional] 
**name** | **str** | CVE number. | 
**patch_links** | [**List[SimpleCveSchemaDataCveReportPatchLinksInner]**](SimpleCveSchemaDataCveReportPatchLinksInner.md) | Titled URLs to available CVE patch. | [optional] 
**patch_status** | **str** | Indicates availability of the CVE patch. Allowed values: &#x60;available&#x60;, &#x60;some_available&#x60;, &#x60;unavailable&#x60;. | [optional] 
**poc** | **str** | Proof of concept code or demonstration exists. Allowed values: &#x60;observed&#x60;, &#x60;not_observed&#x60;, &#x60;alleged_observed&#x60;. | 
**poc_links** | [**List[SimpleCveSchemaDataCveReportPocLinksInner]**](SimpleCveSchemaDataCveReportPocLinksInner.md) | Titled URLs to Proofs of Concept of the CVE. | [optional] 
**product_name** | **str** | &#x60;Product name&#x60; of the affected software. | [optional] 
**risk_level** | **str** | Intel471 &#x60;risk level&#x60; of the described CVE. Allowed values: &#x60;high&#x60;, &#x60;medium&#x60;, &#x60;low&#x60;. | 
**summary** | **str** | Intel471 &#x60;summary&#x60; of the CVE. | [optional] 
**titan_links** | [**List[SimpleCveSchemaDataCveReportTitanLinksInner]**](SimpleCveSchemaDataCveReportTitanLinksInner.md) | Links to the related titan items. | [optional] 
**underground_activity** | **str** | Describes whether &#x60;underground activity&#x60; is observed for given CVE. Allowed values: &#x60;observed&#x60;, &#x60;not_observed&#x60;. | [optional] 
**underground_activity_summary** | **str** | Describes CVE underground activity. | [optional] 
**vendor_name** | **str** | &#x60;Vendor name&#x60; of the affected software. | [optional] 

## Example

```python
from titan_client.models.simple_cve_schema_data_cve_report import SimpleCveSchemaDataCveReport

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCveSchemaDataCveReport from a JSON string
simple_cve_schema_data_cve_report_instance = SimpleCveSchemaDataCveReport.from_json(json)
# print the JSON string representation of the object
print(SimpleCveSchemaDataCveReport.to_json())

# convert the object into a dict
simple_cve_schema_data_cve_report_dict = simple_cve_schema_data_cve_report_instance.to_dict()
# create an instance of SimpleCveSchemaDataCveReport from a dict
simple_cve_schema_data_cve_report_from_dict = SimpleCveSchemaDataCveReport.from_dict(simple_cve_schema_data_cve_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


