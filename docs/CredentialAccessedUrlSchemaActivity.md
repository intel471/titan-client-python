# CredentialAccessedUrlSchemaActivity

Period credential accessed url was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the credential accessed url activity range. | 
**last** | **int** | End of the credential accessed url activity range. | 

## Example

```python
from titan_client.models.credential_accessed_url_schema_activity import CredentialAccessedUrlSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialAccessedUrlSchemaActivity from a JSON string
credential_accessed_url_schema_activity_instance = CredentialAccessedUrlSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(CredentialAccessedUrlSchemaActivity.to_json())

# convert the object into a dict
credential_accessed_url_schema_activity_dict = credential_accessed_url_schema_activity_instance.to_dict()
# create an instance of CredentialAccessedUrlSchemaActivity from a dict
credential_accessed_url_schema_activity_from_dict = CredentialAccessedUrlSchemaActivity.from_dict(credential_accessed_url_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


