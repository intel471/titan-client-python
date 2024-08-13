# CredentialSchemaDataPassword

Credential password details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complexity** | [**CredentialSchemaDataPasswordComplexity**](CredentialSchemaDataPasswordComplexity.md) |  | [optional] 
**id** | **str** | ID of the password. | [optional] 
**password_plain** | **str** | Password plain text. | [optional] 
**strength** | **str** | Password strength. Allowed values: &#x60;excellent&#x60;, &#x60;strong&#x60;, &#x60;medium&#x60;, &#x60;weak&#x60;, &#x60;poor&#x60;, &#x60;not_provided&#x60;. | [optional] 

## Example

```python
from titan_client.models.credential_schema_data_password import CredentialSchemaDataPassword

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSchemaDataPassword from a JSON string
credential_schema_data_password_instance = CredentialSchemaDataPassword.from_json(json)
# print the JSON string representation of the object
print(CredentialSchemaDataPassword.to_json())

# convert the object into a dict
credential_schema_data_password_dict = credential_schema_data_password_instance.to_dict()
# create an instance of CredentialSchemaDataPassword from a dict
credential_schema_data_password_from_dict = CredentialSchemaDataPassword.from_dict(credential_schema_data_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


