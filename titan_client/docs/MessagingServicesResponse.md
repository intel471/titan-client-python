# MessagingServicesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instant_message_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**instant_message_total_count** | **int** | Total count of matched instant messages. | 
**instant_messages** | [**List[InstantMessageSchema]**](InstantMessageSchema.md) | List of &#x60;Instant messages&#x60;. | [optional] 

## Example

```python
from titan_client.models.messaging_services_response import MessagingServicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingServicesResponse from a JSON string
messaging_services_response_instance = MessagingServicesResponse.from_json(json)
# print the JSON string representation of the object
print(MessagingServicesResponse.to_json())

# convert the object into a dict
messaging_services_response_dict = messaging_services_response_instance.to_dict()
# create an instance of MessagingServicesResponse from a dict
messaging_services_response_from_dict = MessagingServicesResponse.from_dict(messaging_services_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


