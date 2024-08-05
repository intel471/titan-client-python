# CredentialSetAccessedUrlSchemaActivity

Period credential set accessed url was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the credential set accessed url activity range. | 
**last** | **int** | End of the credential set accessed url activity range. | 

## Example

```python
from titan_client.models.credential_set_accessed_url_schema_activity import CredentialSetAccessedUrlSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetAccessedUrlSchemaActivity from a JSON string
credential_set_accessed_url_schema_activity_instance = CredentialSetAccessedUrlSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(CredentialSetAccessedUrlSchemaActivity.to_json())

# convert the object into a dict
credential_set_accessed_url_schema_activity_dict = credential_set_accessed_url_schema_activity_instance.to_dict()
# create an instance of CredentialSetAccessedUrlSchemaActivity from a dict
credential_set_accessed_url_schema_activity_from_dict = CredentialSetAccessedUrlSchemaActivity.from_dict(credential_set_accessed_url_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


