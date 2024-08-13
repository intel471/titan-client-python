# SimpleReportSchemaSourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Numerical value that the source is denoted by in the text of the report. | 
**title** | **str** | Source &#x60;title&#x60;. | 
**type** | **str** | &#x60;Type&#x60; of source such as Thread Post, Information Report, etc. | [optional] 
**url** | **str** | &#x60;Url&#x60; to resource where the report information came from. | 

## Example

```python
from titan_client.models.simple_report_schema_sources_inner import SimpleReportSchemaSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleReportSchemaSourcesInner from a JSON string
simple_report_schema_sources_inner_instance = SimpleReportSchemaSourcesInner.from_json(json)
# print the JSON string representation of the object
print(SimpleReportSchemaSourcesInner.to_json())

# convert the object into a dict
simple_report_schema_sources_inner_dict = simple_report_schema_sources_inner_instance.to_dict()
# create an instance of SimpleReportSchemaSourcesInner from a dict
simple_report_schema_sources_inner_from_dict = SimpleReportSchemaSourcesInner.from_dict(simple_report_schema_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


