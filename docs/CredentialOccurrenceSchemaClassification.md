# CredentialOccurrenceSchemaClassification

Classification of credential occurrence.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intel_requirements** | **List[str]** | General Intelligence Requirements that match the credential occurrence. | [optional] 

## Example

```python
from titan_client.models.credential_occurrence_schema_classification import CredentialOccurrenceSchemaClassification

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialOccurrenceSchemaClassification from a JSON string
credential_occurrence_schema_classification_instance = CredentialOccurrenceSchemaClassification.from_json(json)
# print the JSON string representation of the object
print(CredentialOccurrenceSchemaClassification.to_json())

# convert the object into a dict
credential_occurrence_schema_classification_dict = credential_occurrence_schema_classification_instance.to_dict()
# create an instance of CredentialOccurrenceSchemaClassification from a dict
credential_occurrence_schema_classification_from_dict = CredentialOccurrenceSchemaClassification.from_dict(credential_occurrence_schema_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


