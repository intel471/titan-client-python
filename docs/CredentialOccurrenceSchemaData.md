# CredentialOccurrenceSchemaData

Credential occurrence with related objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessed_url** | **str** | Accessed URL. | [optional] 
**credential** | [**CredentialOccurrenceSchemaDataCredential**](CredentialOccurrenceSchemaDataCredential.md) |  | [optional] 
**credential_set** | [**CredentialOccurrenceSchemaDataCredentialSet**](CredentialOccurrenceSchemaDataCredentialSet.md) |  | [optional] 
**detected_malware** | [**Malware**](Malware.md) |  | [optional] 
**file_path** | **str** | Credential occurrence file path. | [optional] 

## Example

```python
from titan_client.models.credential_occurrence_schema_data import CredentialOccurrenceSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialOccurrenceSchemaData from a JSON string
credential_occurrence_schema_data_instance = CredentialOccurrenceSchemaData.from_json(json)
# print the JSON string representation of the object
print(CredentialOccurrenceSchemaData.to_json())

# convert the object into a dict
credential_occurrence_schema_data_dict = credential_occurrence_schema_data_instance.to_dict()
# create an instance of CredentialOccurrenceSchemaData from a dict
credential_occurrence_schema_data_from_dict = CredentialOccurrenceSchemaData.from_dict(credential_occurrence_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


