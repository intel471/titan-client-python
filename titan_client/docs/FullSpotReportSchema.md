# FullSpotReportSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**SimpleSpotReportSchemaActivity**](SimpleSpotReportSchemaActivity.md) |  | 
**data** | [**SimpleSpotReportSchemaData**](SimpleSpotReportSchemaData.md) |  | 
**last_updated** | **int** | Spot report last modification date. | 
**uid** | **str** | Unique Spot report identifier. | 

## Example

```python
from titan_client.models.full_spot_report_schema import FullSpotReportSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FullSpotReportSchema from a JSON string
full_spot_report_schema_instance = FullSpotReportSchema.from_json(json)
# print the JSON string representation of the object
print(FullSpotReportSchema.to_json())

# convert the object into a dict
full_spot_report_schema_dict = full_spot_report_schema_instance.to_dict()
# create an instance of FullSpotReportSchema from a dict
full_spot_report_schema_from_dict = FullSpotReportSchema.from_dict(full_spot_report_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


