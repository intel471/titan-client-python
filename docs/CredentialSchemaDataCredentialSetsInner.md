# CredentialSchemaDataCredentialSetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the credential set. | [optional] 
**uid** | **str** | Unique credential set identifier. | [optional] 

## Example

```python
from titan_client.models.credential_schema_data_credential_sets_inner import CredentialSchemaDataCredentialSetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSchemaDataCredentialSetsInner from a JSON string
credential_schema_data_credential_sets_inner_instance = CredentialSchemaDataCredentialSetsInner.from_json(json)
# print the JSON string representation of the object
print(CredentialSchemaDataCredentialSetsInner.to_json())

# convert the object into a dict
credential_schema_data_credential_sets_inner_dict = credential_schema_data_credential_sets_inner_instance.to_dict()
# create an instance of CredentialSchemaDataCredentialSetsInner from a dict
credential_schema_data_credential_sets_inner_from_dict = CredentialSchemaDataCredentialSetsInner.from_dict(credential_schema_data_credential_sets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


