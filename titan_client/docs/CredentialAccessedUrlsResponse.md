# CredentialAccessedUrlsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_accessed_urls** | [**List[CredentialAccessedUrlSchema]**](CredentialAccessedUrlSchema.md) | List of &#x60;Credential accessed urls&#x60;. | [optional] 
**credential_accessed_urls_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**credential_accessed_urls_total_count** | **int** | Total count of matched credential accessed urls. | 

## Example

```python
from titan_client.models.credential_accessed_urls_response import CredentialAccessedUrlsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialAccessedUrlsResponse from a JSON string
credential_accessed_urls_response_instance = CredentialAccessedUrlsResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialAccessedUrlsResponse.to_json())

# convert the object into a dict
credential_accessed_urls_response_dict = credential_accessed_urls_response_instance.to_dict()
# create an instance of CredentialAccessedUrlsResponse from a dict
credential_accessed_urls_response_from_dict = CredentialAccessedUrlsResponse.from_dict(credential_accessed_urls_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


