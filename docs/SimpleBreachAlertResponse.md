# SimpleBreachAlertResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breach_alerts** | [**List[SimpleBreachAlertSchema]**](SimpleBreachAlertSchema.md) | List of &#x60;Breach Alerts&#x60;. | [optional] 
**breach_alerts_total_count** | **int** | Total count of matched results. | 
**partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 

## Example

```python
from titan_client.models.simple_breach_alert_response import SimpleBreachAlertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleBreachAlertResponse from a JSON string
simple_breach_alert_response_instance = SimpleBreachAlertResponse.from_json(json)
# print the JSON string representation of the object
print(SimpleBreachAlertResponse.to_json())

# convert the object into a dict
simple_breach_alert_response_dict = simple_breach_alert_response_instance.to_dict()
# create an instance of SimpleBreachAlertResponse from a dict
simple_breach_alert_response_from_dict = SimpleBreachAlertResponse.from_dict(simple_breach_alert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


