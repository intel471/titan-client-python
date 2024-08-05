# CredentialSetAccessedUrlStreamSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**CredentialSetAccessedUrlSchemaActivity**](CredentialSetAccessedUrlSchemaActivity.md) |  | 
**classification** | [**CredentialSetAccessedUrlSchemaClassification**](CredentialSetAccessedUrlSchemaClassification.md) |  | [optional] 
**data** | [**CredentialSetAccessedUrlStreamSchemaData**](CredentialSetAccessedUrlStreamSchemaData.md) |  | 
**last_updated** | **int** | Credential set accessed url last modification date. | 
**uid** | **str** | Unique credential set accessed url identifier. | 

## Example

```python
from titan_client.models.credential_set_accessed_url_stream_schema import CredentialSetAccessedUrlStreamSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetAccessedUrlStreamSchema from a JSON string
credential_set_accessed_url_stream_schema_instance = CredentialSetAccessedUrlStreamSchema.from_json(json)
# print the JSON string representation of the object
print(CredentialSetAccessedUrlStreamSchema.to_json())

# convert the object into a dict
credential_set_accessed_url_stream_schema_dict = credential_set_accessed_url_stream_schema_instance.to_dict()
# create an instance of CredentialSetAccessedUrlStreamSchema from a dict
credential_set_accessed_url_stream_schema_from_dict = CredentialSetAccessedUrlStreamSchema.from_dict(credential_set_accessed_url_stream_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


