# CredentialOccurrenceSchemaActivity

Period credential occurrence was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the credential occurrence activity range. | 
**last** | **int** | End of the credential occurrence activity range. | 

## Example

```python
from titan_client.models.credential_occurrence_schema_activity import CredentialOccurrenceSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialOccurrenceSchemaActivity from a JSON string
credential_occurrence_schema_activity_instance = CredentialOccurrenceSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(CredentialOccurrenceSchemaActivity.to_json())

# convert the object into a dict
credential_occurrence_schema_activity_dict = credential_occurrence_schema_activity_instance.to_dict()
# create an instance of CredentialOccurrenceSchemaActivity from a dict
credential_occurrence_schema_activity_from_dict = CredentialOccurrenceSchemaActivity.from_dict(credential_occurrence_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


