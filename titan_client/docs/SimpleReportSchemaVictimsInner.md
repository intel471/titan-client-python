# SimpleReportSchemaVictimsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Purported victim &#x60;name&#x60;. | 
**urls** | **List[str]** | List of purported victim&#39;s &#x60;urls&#x60;. | [optional] 

## Example

```python
from titan_client.models.simple_report_schema_victims_inner import SimpleReportSchemaVictimsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleReportSchemaVictimsInner from a JSON string
simple_report_schema_victims_inner_instance = SimpleReportSchemaVictimsInner.from_json(json)
# print the JSON string representation of the object
print(SimpleReportSchemaVictimsInner.to_json())

# convert the object into a dict
simple_report_schema_victims_inner_dict = simple_report_schema_victims_inner_instance.to_dict()
# create an instance of SimpleReportSchemaVictimsInner from a dict
simple_report_schema_victims_inner_from_dict = SimpleReportSchemaVictimsInner.from_dict(simple_report_schema_victims_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


