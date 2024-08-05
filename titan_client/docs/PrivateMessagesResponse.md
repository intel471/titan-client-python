# PrivateMessagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_message_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**private_message_total_count** | **int** | Total count of matched messages. | 
**private_messages** | [**List[PrivateMessageSchema]**](PrivateMessageSchema.md) | List of &#x60;Private messages&#x60;. | [optional] 

## Example

```python
from titan_client.models.private_messages_response import PrivateMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessagesResponse from a JSON string
private_messages_response_instance = PrivateMessagesResponse.from_json(json)
# print the JSON string representation of the object
print(PrivateMessagesResponse.to_json())

# convert the object into a dict
private_messages_response_dict = private_messages_response_instance.to_dict()
# create an instance of PrivateMessagesResponse from a dict
private_messages_response_from_dict = PrivateMessagesResponse.from_dict(private_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


