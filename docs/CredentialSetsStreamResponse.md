# CredentialSetsStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_sets** | [**List[CredentialSetStreamSchema]**](CredentialSetStreamSchema.md) | List of &#x60;Credential sets&#x60;. | [optional] 
**credential_sets_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**credential_sets_total_count** | **int** | Total count of matched credential sets. | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 

## Example

```python
from titan_client.models.credential_sets_stream_response import CredentialSetsStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetsStreamResponse from a JSON string
credential_sets_stream_response_instance = CredentialSetsStreamResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialSetsStreamResponse.to_json())

# convert the object into a dict
credential_sets_stream_response_dict = credential_sets_stream_response_instance.to_dict()
# create an instance of CredentialSetsStreamResponse from a dict
credential_sets_stream_response_from_dict = CredentialSetsStreamResponse.from_dict(credential_sets_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


