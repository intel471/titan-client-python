# CredentialOccurrencesStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_occurrences** | [**List[CredentialOccurrenceSchema]**](CredentialOccurrenceSchema.md) | List of &#x60;Credential occurrences&#x60;. | [optional] 
**credential_occurrences_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**credential_occurrences_total_count** | **int** | Total count of matched credential occurrences. | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 

## Example

```python
from titan_client.models.credential_occurrences_stream_response import CredentialOccurrencesStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialOccurrencesStreamResponse from a JSON string
credential_occurrences_stream_response_instance = CredentialOccurrencesStreamResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialOccurrencesStreamResponse.to_json())

# convert the object into a dict
credential_occurrences_stream_response_dict = credential_occurrences_stream_response_instance.to_dict()
# create an instance of CredentialOccurrencesStreamResponse from a dict
credential_occurrences_stream_response_from_dict = CredentialOccurrencesStreamResponse.from_dict(credential_occurrences_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


