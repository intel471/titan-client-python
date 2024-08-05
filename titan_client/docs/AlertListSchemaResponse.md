# AlertListSchemaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_total_count** | **int** | Total count of alerts. | 
**alerts** | [**List[AlertListSchema]**](AlertListSchema.md) | List of Alerts. | [optional] 
**watcher_groups** | [**List[FullWatcherGroupSchema]**](FullWatcherGroupSchema.md) | List of Watcher groups. Groups are displayed only for alerts included in results. | [optional] 

## Example

```python
from titan_client.models.alert_list_schema_response import AlertListSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlertListSchemaResponse from a JSON string
alert_list_schema_response_instance = AlertListSchemaResponse.from_json(json)
# print the JSON string representation of the object
print(AlertListSchemaResponse.to_json())

# convert the object into a dict
alert_list_schema_response_dict = alert_list_schema_response_instance.to_dict()
# create an instance of AlertListSchemaResponse from a dict
alert_list_schema_response_from_dict = AlertListSchemaResponse.from_dict(alert_list_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


