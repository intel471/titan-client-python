# CredentialAccessedUrlSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**CredentialAccessedUrlSchemaActivity**](CredentialAccessedUrlSchemaActivity.md) |  | 
**classification** | [**CredentialAccessedUrlSchemaClassification**](CredentialAccessedUrlSchemaClassification.md) |  | [optional] 
**data** | [**CredentialAccessedUrlSchemaData**](CredentialAccessedUrlSchemaData.md) |  | 
**last_updated** | **int** | Credential accessed url last modification date. | 
**uid** | **str** | Unique credential accessed url identifier. | 

## Example

```python
from titan_client.models.credential_accessed_url_schema import CredentialAccessedUrlSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialAccessedUrlSchema from a JSON string
credential_accessed_url_schema_instance = CredentialAccessedUrlSchema.from_json(json)
# print the JSON string representation of the object
print(CredentialAccessedUrlSchema.to_json())

# convert the object into a dict
credential_accessed_url_schema_dict = credential_accessed_url_schema_instance.to_dict()
# create an instance of CredentialAccessedUrlSchema from a dict
credential_accessed_url_schema_from_dict = CredentialAccessedUrlSchema.from_dict(credential_accessed_url_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


