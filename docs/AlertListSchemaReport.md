# AlertListSchemaReport

`Report` object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admiralty_code** | **str** | Code as described [here](http://en.wikipedia.org/wiki/Admiralty_code). All Fintel reports have admiraltyCode&#x3D;&#x60;A1&#x60;. | 
**date_of_information** | **int** | &#x60;Date of information&#x60; as Epoch Time. | 
**motivation** | **List[str]** | &#x60;Actor&#x60;&#39;s &#x60;motivation&#x60;. CC for Cyber Crime, CE for Cyber Espionage, HA for Hacktivism. | 
**portal_report_url** | **str** | URL to the report on the portal. | 
**source_characterization** | **str** | &#x60;Source characterization&#x60;. | 
**subject** | **str** | Report&#39;s subject. | 
**uid** | **str** | Unique report identifier. | 

## Example

```python
from titan_client.models.alert_list_schema_report import AlertListSchemaReport

# TODO update the JSON string below
json = "{}"
# create an instance of AlertListSchemaReport from a JSON string
alert_list_schema_report_instance = AlertListSchemaReport.from_json(json)
# print the JSON string representation of the object
print(AlertListSchemaReport.to_json())

# convert the object into a dict
alert_list_schema_report_dict = alert_list_schema_report_instance.to_dict()
# create an instance of AlertListSchemaReport from a dict
alert_list_schema_report_from_dict = AlertListSchemaReport.from_dict(alert_list_schema_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


