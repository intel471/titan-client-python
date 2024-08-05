# CredentialSetAccessedUrlSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**CredentialSetAccessedUrlSchemaActivity**](CredentialSetAccessedUrlSchemaActivity.md) |  | 
**classification** | [**CredentialSetAccessedUrlSchemaClassification**](CredentialSetAccessedUrlSchemaClassification.md) |  | [optional] 
**data** | [**CredentialSetAccessedUrlSchemaData**](CredentialSetAccessedUrlSchemaData.md) |  | 
**last_updated** | **int** | Credential set accessed url last modification date. | 
**uid** | **str** | Unique credential set accessed url identifier. | 

## Example

```python
from titan_client.models.credential_set_accessed_url_schema import CredentialSetAccessedUrlSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetAccessedUrlSchema from a JSON string
credential_set_accessed_url_schema_instance = CredentialSetAccessedUrlSchema.from_json(json)
# print the JSON string representation of the object
print(CredentialSetAccessedUrlSchema.to_json())

# convert the object into a dict
credential_set_accessed_url_schema_dict = credential_set_accessed_url_schema_instance.to_dict()
# create an instance of CredentialSetAccessedUrlSchema from a dict
credential_set_accessed_url_schema_from_dict = CredentialSetAccessedUrlSchema.from_dict(credential_set_accessed_url_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


