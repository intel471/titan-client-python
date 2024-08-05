# CredentialsStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**List[CredentialSchema]**](CredentialSchema.md) | List of &#x60;Credentials&#x60;. | [optional] 
**credentials_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**credentials_total_count** | **int** | Total count of matched credentials. | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 

## Example

```python
from titan_client.models.credentials_stream_response import CredentialsStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsStreamResponse from a JSON string
credentials_stream_response_instance = CredentialsStreamResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialsStreamResponse.to_json())

# convert the object into a dict
credentials_stream_response_dict = credentials_stream_response_instance.to_dict()
# create an instance of CredentialsStreamResponse from a dict
credentials_stream_response_from_dict = CredentialsStreamResponse.from_dict(credentials_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


