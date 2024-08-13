# CredentialSetSchemaClassification

Classification of credential set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intel_requirements** | **List[str]** | General Intelligence Requirements that match the credential set. | [optional] 

## Example

```python
from titan_client.models.credential_set_schema_classification import CredentialSetSchemaClassification

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetSchemaClassification from a JSON string
credential_set_schema_classification_instance = CredentialSetSchemaClassification.from_json(json)
# print the JSON string representation of the object
print(CredentialSetSchemaClassification.to_json())

# convert the object into a dict
credential_set_schema_classification_dict = credential_set_schema_classification_instance.to_dict()
# create an instance of CredentialSetSchemaClassification from a dict
credential_set_schema_classification_from_dict = CredentialSetSchemaClassification.from_dict(credential_set_schema_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


