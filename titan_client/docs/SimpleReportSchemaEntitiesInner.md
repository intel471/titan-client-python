# SimpleReportSchemaEntitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Entity &#x60;type&#x60;. | 
**value** | **str** | Entity &#x60;value&#x60;. | [optional] 

## Example

```python
from titan_client.models.simple_report_schema_entities_inner import SimpleReportSchemaEntitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleReportSchemaEntitiesInner from a JSON string
simple_report_schema_entities_inner_instance = SimpleReportSchemaEntitiesInner.from_json(json)
# print the JSON string representation of the object
print(SimpleReportSchemaEntitiesInner.to_json())

# convert the object into a dict
simple_report_schema_entities_inner_dict = simple_report_schema_entities_inner_instance.to_dict()
# create an instance of SimpleReportSchemaEntitiesInner from a dict
simple_report_schema_entities_inner_from_dict = SimpleReportSchemaEntitiesInner.from_dict(simple_report_schema_entities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


