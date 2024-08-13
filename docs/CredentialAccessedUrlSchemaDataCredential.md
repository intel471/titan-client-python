# CredentialAccessedUrlSchemaDataCredential

Sub-document containing credential information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliations** | **List[str]** | Affiliation of the credential. Allowed values: &#x60;my_employees&#x60;, &#x60;vip_emails&#x60;, &#x60;my_customers&#x60;, &#x60;third_parties&#x60;. | [optional] 
**credential_domain** | **str** | Domain of the credential. | [optional] 
**credential_login** | **str** | Login of the credential. | [optional] 
**detection_domain** | **str** | Detection domain of the credential. | [optional] 
**uid** | **str** | Unique credential identifier. | 

## Example

```python
from titan_client.models.credential_accessed_url_schema_data_credential import CredentialAccessedUrlSchemaDataCredential

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialAccessedUrlSchemaDataCredential from a JSON string
credential_accessed_url_schema_data_credential_instance = CredentialAccessedUrlSchemaDataCredential.from_json(json)
# print the JSON string representation of the object
print(CredentialAccessedUrlSchemaDataCredential.to_json())

# convert the object into a dict
credential_accessed_url_schema_data_credential_dict = credential_accessed_url_schema_data_credential_instance.to_dict()
# create an instance of CredentialAccessedUrlSchemaDataCredential from a dict
credential_accessed_url_schema_data_credential_from_dict = CredentialAccessedUrlSchemaDataCredential.from_dict(credential_accessed_url_schema_data_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


