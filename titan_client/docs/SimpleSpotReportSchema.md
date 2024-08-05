# SimpleSpotReportSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**SimpleSpotReportSchemaActivity**](SimpleSpotReportSchemaActivity.md) |  | 
**data** | [**SimpleSpotReportSchemaData**](SimpleSpotReportSchemaData.md) |  | 
**last_updated** | **int** | Spot report last modification date. | 
**uid** | **str** | Unique Spot report identifier. | 

## Example

```python
from titan_client.models.simple_spot_report_schema import SimpleSpotReportSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleSpotReportSchema from a JSON string
simple_spot_report_schema_instance = SimpleSpotReportSchema.from_json(json)
# print the JSON string representation of the object
print(SimpleSpotReportSchema.to_json())

# convert the object into a dict
simple_spot_report_schema_dict = simple_spot_report_schema_instance.to_dict()
# create an instance of SimpleSpotReportSchema from a dict
simple_spot_report_schema_from_dict = SimpleSpotReportSchema.from_dict(simple_spot_report_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


