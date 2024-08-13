# CredentialAccessedUrlSchemaData

Credential accessed URL with related objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessed_domain** | **str** | Accessed domain. | [optional] 
**accessed_url** | **str** | Accessed URL. | 
**credential** | [**CredentialAccessedUrlSchemaDataCredential**](CredentialAccessedUrlSchemaDataCredential.md) |  | [optional] 

## Example

```python
from titan_client.models.credential_accessed_url_schema_data import CredentialAccessedUrlSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialAccessedUrlSchemaData from a JSON string
credential_accessed_url_schema_data_instance = CredentialAccessedUrlSchemaData.from_json(json)
# print the JSON string representation of the object
print(CredentialAccessedUrlSchemaData.to_json())

# convert the object into a dict
credential_accessed_url_schema_data_dict = credential_accessed_url_schema_data_instance.to_dict()
# create an instance of CredentialAccessedUrlSchemaData from a dict
credential_accessed_url_schema_data_from_dict = CredentialAccessedUrlSchemaData.from_dict(credential_accessed_url_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


