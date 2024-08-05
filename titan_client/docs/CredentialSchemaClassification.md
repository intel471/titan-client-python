# CredentialSchemaClassification

Classification of credential.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intel_requirements** | **List[str]** | General Intelligence Requirements that match the credential. | [optional] 

## Example

```python
from titan_client.models.credential_schema_classification import CredentialSchemaClassification

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSchemaClassification from a JSON string
credential_schema_classification_instance = CredentialSchemaClassification.from_json(json)
# print the JSON string representation of the object
print(CredentialSchemaClassification.to_json())

# convert the object into a dict
credential_schema_classification_dict = credential_schema_classification_instance.to_dict()
# create an instance of CredentialSchemaClassification from a dict
credential_schema_classification_from_dict = CredentialSchemaClassification.from_dict(credential_schema_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


