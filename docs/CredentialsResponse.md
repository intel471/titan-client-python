# CredentialsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**List[CredentialSchema]**](CredentialSchema.md) | List of &#x60;Credentials&#x60;. | [optional] 
**credentials_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**credentials_total_count** | **int** | Total count of matched credentials. | 

## Example

```python
from titan_client.models.credentials_response import CredentialsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsResponse from a JSON string
credentials_response_instance = CredentialsResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialsResponse.to_json())

# convert the object into a dict
credentials_response_dict = credentials_response_instance.to_dict()
# create an instance of CredentialsResponse from a dict
credentials_response_from_dict = CredentialsResponse.from_dict(credentials_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


