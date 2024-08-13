# SimpleSpotReportSchemaActivity

Period Spot report was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the Spot report activity range. | 
**last** | **int** | End of the Spot report activity range. | 

## Example

```python
from titan_client.models.simple_spot_report_schema_activity import SimpleSpotReportSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleSpotReportSchemaActivity from a JSON string
simple_spot_report_schema_activity_instance = SimpleSpotReportSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(SimpleSpotReportSchemaActivity.to_json())

# convert the object into a dict
simple_spot_report_schema_activity_dict = simple_spot_report_schema_activity_instance.to_dict()
# create an instance of SimpleSpotReportSchemaActivity from a dict
simple_spot_report_schema_activity_from_dict = SimpleSpotReportSchemaActivity.from_dict(simple_spot_report_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


