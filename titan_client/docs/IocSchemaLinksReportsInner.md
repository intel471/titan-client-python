# IocSchemaLinksReportsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admiralty_code** | **str** | Code as described [here](http://en.wikipedia.org/wiki/Admiralty_code). All Fintel reports have admiraltyCode&#x3D;&#x60;A1&#x60;. | [optional] 
**date_of_information** | **int** | Date of information as Epoch Time. | [optional] 
**motivation** | **List[str]** | Actor&#39;s &#x60;motivation&#x60;. &#x60;CC&#x60; for Cyber Crime, &#x60;CE&#x60; for Cyber Espionage, &#x60;HA&#x60; for Hacktivism. | [optional] 
**portal_report_url** | **str** | URL to the report on the portal. | 
**released** | **int** | Date of report was &#x60;released&#x60;. | 
**source_characterization** | **str** | Source characterization. | [optional] 
**subject** | **str** | Report&#39;s &#x60;subject&#x60;. | 
**uid** | **str** | Unique report identifier. | 

## Example

```python
from titan_client.models.ioc_schema_links_reports_inner import IocSchemaLinksReportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IocSchemaLinksReportsInner from a JSON string
ioc_schema_links_reports_inner_instance = IocSchemaLinksReportsInner.from_json(json)
# print the JSON string representation of the object
print(IocSchemaLinksReportsInner.to_json())

# convert the object into a dict
ioc_schema_links_reports_inner_dict = ioc_schema_links_reports_inner_instance.to_dict()
# create an instance of IocSchemaLinksReportsInner from a dict
ioc_schema_links_reports_inner_from_dict = IocSchemaLinksReportsInner.from_dict(ioc_schema_links_reports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


