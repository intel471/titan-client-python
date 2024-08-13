# CredentialOccurrenceSchemaDataCredentialSet

Sub-document containing credential set information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the credential set. | [optional] 
**uid** | **str** | Unique credential set identifier. | 

## Example

```python
from titan_client.models.credential_occurrence_schema_data_credential_set import CredentialOccurrenceSchemaDataCredentialSet

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialOccurrenceSchemaDataCredentialSet from a JSON string
credential_occurrence_schema_data_credential_set_instance = CredentialOccurrenceSchemaDataCredentialSet.from_json(json)
# print the JSON string representation of the object
print(CredentialOccurrenceSchemaDataCredentialSet.to_json())

# convert the object into a dict
credential_occurrence_schema_data_credential_set_dict = credential_occurrence_schema_data_credential_set_instance.to_dict()
# create an instance of CredentialOccurrenceSchemaDataCredentialSet from a dict
credential_occurrence_schema_data_credential_set_from_dict = CredentialOccurrenceSchemaDataCredentialSet.from_dict(credential_occurrence_schema_data_credential_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


