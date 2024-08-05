# CredentialSetAccessedUrlSchemaData

Credential set accessed URL with related objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessed_domain** | **str** | Accessed domain. | [optional] 
**accessed_url** | **str** | Accessed URL. | 
**credential_set** | [**CredentialSetAccessedUrlSchemaDataCredentialSet**](CredentialSetAccessedUrlSchemaDataCredentialSet.md) |  | [optional] 

## Example

```python
from titan_client.models.credential_set_accessed_url_schema_data import CredentialSetAccessedUrlSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetAccessedUrlSchemaData from a JSON string
credential_set_accessed_url_schema_data_instance = CredentialSetAccessedUrlSchemaData.from_json(json)
# print the JSON string representation of the object
print(CredentialSetAccessedUrlSchemaData.to_json())

# convert the object into a dict
credential_set_accessed_url_schema_data_dict = credential_set_accessed_url_schema_data_instance.to_dict()
# create an instance of CredentialSetAccessedUrlSchemaData from a dict
credential_set_accessed_url_schema_data_from_dict = CredentialSetAccessedUrlSchemaData.from_dict(credential_set_accessed_url_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


