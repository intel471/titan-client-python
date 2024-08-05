# CredentialAccessedUrlsStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_accessed_urls** | [**List[CredentialAccessedUrlStreamSchema]**](CredentialAccessedUrlStreamSchema.md) | List of &#x60;Credential accessed urls&#x60;. | [optional] 
**credential_accessed_urls_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**credential_accessed_urls_total_count** | **int** | Total count of matched credential accessed urls. | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 

## Example

```python
from titan_client.models.credential_accessed_urls_stream_response import CredentialAccessedUrlsStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialAccessedUrlsStreamResponse from a JSON string
credential_accessed_urls_stream_response_instance = CredentialAccessedUrlsStreamResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialAccessedUrlsStreamResponse.to_json())

# convert the object into a dict
credential_accessed_urls_stream_response_dict = credential_accessed_urls_stream_response_instance.to_dict()
# create an instance of CredentialAccessedUrlsStreamResponse from a dict
credential_accessed_urls_stream_response_from_dict = CredentialAccessedUrlsStreamResponse.from_dict(credential_accessed_urls_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


