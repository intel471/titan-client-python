# CredentialSetAccessedUrlSchemaDataCredentialSet

Sub-document containing credential set information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the credential set. | 
**uid** | **str** | Unique credential set identifier. | 

## Example

```python
from titan_client.models.credential_set_accessed_url_schema_data_credential_set import CredentialSetAccessedUrlSchemaDataCredentialSet

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetAccessedUrlSchemaDataCredentialSet from a JSON string
credential_set_accessed_url_schema_data_credential_set_instance = CredentialSetAccessedUrlSchemaDataCredentialSet.from_json(json)
# print the JSON string representation of the object
print(CredentialSetAccessedUrlSchemaDataCredentialSet.to_json())

# convert the object into a dict
credential_set_accessed_url_schema_data_credential_set_dict = credential_set_accessed_url_schema_data_credential_set_instance.to_dict()
# create an instance of CredentialSetAccessedUrlSchemaDataCredentialSet from a dict
credential_set_accessed_url_schema_data_credential_set_from_dict = CredentialSetAccessedUrlSchemaDataCredentialSet.from_dict(credential_set_accessed_url_schema_data_credential_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


