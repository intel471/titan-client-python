# CredentialSetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_sets** | [**List[CredentialSetSchema]**](CredentialSetSchema.md) | List of &#x60;Credential sets&#x60;. | [optional] 
**credential_sets_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**credential_sets_total_count** | **int** | Total count of matched credential sets. | 

## Example

```python
from titan_client.models.credential_sets_response import CredentialSetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetsResponse from a JSON string
credential_sets_response_instance = CredentialSetsResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialSetsResponse.to_json())

# convert the object into a dict
credential_sets_response_dict = credential_sets_response_instance.to_dict()
# create an instance of CredentialSetsResponse from a dict
credential_sets_response_from_dict = CredentialSetsResponse.from_dict(credential_sets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


