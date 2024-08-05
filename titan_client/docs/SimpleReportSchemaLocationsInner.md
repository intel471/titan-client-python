# SimpleReportSchemaLocationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Name of &#x60;country&#x60;. | [optional] 
**link** | **str** | Linkage type. | 
**region** | **str** | Name of &#x60;region&#x60;. | 

## Example

```python
from titan_client.models.simple_report_schema_locations_inner import SimpleReportSchemaLocationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleReportSchemaLocationsInner from a JSON string
simple_report_schema_locations_inner_instance = SimpleReportSchemaLocationsInner.from_json(json)
# print the JSON string representation of the object
print(SimpleReportSchemaLocationsInner.to_json())

# convert the object into a dict
simple_report_schema_locations_inner_dict = simple_report_schema_locations_inner_instance.to_dict()
# create an instance of SimpleReportSchemaLocationsInner from a dict
simple_report_schema_locations_inner_from_dict = SimpleReportSchemaLocationsInner.from_dict(simple_report_schema_locations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


