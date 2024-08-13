# CredentialSchemaActivity

Period credential was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the credential activity range. | 
**last** | **int** | End of the credential activity range. | 

## Example

```python
from titan_client.models.credential_schema_activity import CredentialSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSchemaActivity from a JSON string
credential_schema_activity_instance = CredentialSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(CredentialSchemaActivity.to_json())

# convert the object into a dict
credential_schema_activity_dict = credential_schema_activity_instance.to_dict()
# create an instance of CredentialSchemaActivity from a dict
credential_schema_activity_from_dict = CredentialSchemaActivity.from_dict(credential_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


