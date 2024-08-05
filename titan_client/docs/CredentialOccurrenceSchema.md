# CredentialOccurrenceSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**CredentialOccurrenceSchemaActivity**](CredentialOccurrenceSchemaActivity.md) |  | 
**classification** | [**CredentialOccurrenceSchemaClassification**](CredentialOccurrenceSchemaClassification.md) |  | [optional] 
**data** | [**CredentialOccurrenceSchemaData**](CredentialOccurrenceSchemaData.md) |  | 
**last_updated** | **int** | Credential occurrence last modification date. | 
**uid** | **str** | Unique credential occurrence identifier. | 

## Example

```python
from titan_client.models.credential_occurrence_schema import CredentialOccurrenceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialOccurrenceSchema from a JSON string
credential_occurrence_schema_instance = CredentialOccurrenceSchema.from_json(json)
# print the JSON string representation of the object
print(CredentialOccurrenceSchema.to_json())

# convert the object into a dict
credential_occurrence_schema_dict = credential_occurrence_schema_instance.to_dict()
# create an instance of CredentialOccurrenceSchema from a dict
credential_occurrence_schema_from_dict = CredentialOccurrenceSchema.from_dict(credential_occurrence_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


