# SimpleReportSchemaRelatedReportsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_family** | **str** | Related report document family. | 
**uid** | **str** | Related report unique identifier. | 

## Example

```python
from titan_client.models.simple_report_schema_related_reports_inner import SimpleReportSchemaRelatedReportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleReportSchemaRelatedReportsInner from a JSON string
simple_report_schema_related_reports_inner_instance = SimpleReportSchemaRelatedReportsInner.from_json(json)
# print the JSON string representation of the object
print(SimpleReportSchemaRelatedReportsInner.to_json())

# convert the object into a dict
simple_report_schema_related_reports_inner_dict = simple_report_schema_related_reports_inner_instance.to_dict()
# create an instance of SimpleReportSchemaRelatedReportsInner from a dict
simple_report_schema_related_reports_inner_from_dict = SimpleReportSchemaRelatedReportsInner.from_dict(simple_report_schema_related_reports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


