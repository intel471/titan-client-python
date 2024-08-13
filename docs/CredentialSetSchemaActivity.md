# CredentialSetSchemaActivity

Period credential set was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the credential set activity range. | 
**last** | **int** | End of the credential set activity range. | 

## Example

```python
from titan_client.models.credential_set_schema_activity import CredentialSetSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetSchemaActivity from a JSON string
credential_set_schema_activity_instance = CredentialSetSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(CredentialSetSchemaActivity.to_json())

# convert the object into a dict
credential_set_schema_activity_dict = credential_set_schema_activity_instance.to_dict()
# create an instance of CredentialSetSchemaActivity from a dict
credential_set_schema_activity_from_dict = CredentialSetSchemaActivity.from_dict(credential_set_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


