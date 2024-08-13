# CredentialAccessedUrlStreamSchema


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
from titan_client.models.credential_accessed_url_stream_schema import CredentialAccessedUrlStreamSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialAccessedUrlStreamSchema from a JSON string
credential_accessed_url_stream_schema_instance = CredentialAccessedUrlStreamSchema.from_json(json)
# print the JSON string representation of the object
print(CredentialAccessedUrlStreamSchema.to_json())

# convert the object into a dict
credential_accessed_url_stream_schema_dict = credential_accessed_url_stream_schema_instance.to_dict()
# create an instance of CredentialAccessedUrlStreamSchema from a dict
credential_accessed_url_stream_schema_from_dict = CredentialAccessedUrlStreamSchema.from_dict(credential_accessed_url_stream_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


