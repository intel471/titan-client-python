# CredentialSetsAccessedUrlsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_sets_accessed_urls** | [**List[CredentialSetAccessedUrlSchema]**](CredentialSetAccessedUrlSchema.md) | List of &#x60;Credential set accessed urls&#x60;. | [optional] 
**credential_sets_accessed_urls_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**credential_sets_accessed_urls_total_count** | **int** | Total count of matched credential set accessed urls. | 

## Example

```python
from titan_client.models.credential_sets_accessed_urls_response import CredentialSetsAccessedUrlsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetsAccessedUrlsResponse from a JSON string
credential_sets_accessed_urls_response_instance = CredentialSetsAccessedUrlsResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialSetsAccessedUrlsResponse.to_json())

# convert the object into a dict
credential_sets_accessed_urls_response_dict = credential_sets_accessed_urls_response_instance.to_dict()
# create an instance of CredentialSetsAccessedUrlsResponse from a dict
credential_sets_accessed_urls_response_from_dict = CredentialSetsAccessedUrlsResponse.from_dict(credential_sets_accessed_urls_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


