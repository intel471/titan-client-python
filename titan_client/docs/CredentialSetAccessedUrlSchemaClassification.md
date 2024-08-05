# CredentialSetAccessedUrlSchemaClassification

Classification of credential set accessed url.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intel_requirements** | **List[str]** | General Intelligence Requirements that match the credential set accessed url. | [optional] 

## Example

```python
from titan_client.models.credential_set_accessed_url_schema_classification import CredentialSetAccessedUrlSchemaClassification

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetAccessedUrlSchemaClassification from a JSON string
credential_set_accessed_url_schema_classification_instance = CredentialSetAccessedUrlSchemaClassification.from_json(json)
# print the JSON string representation of the object
print(CredentialSetAccessedUrlSchemaClassification.to_json())

# convert the object into a dict
credential_set_accessed_url_schema_classification_dict = credential_set_accessed_url_schema_classification_instance.to_dict()
# create an instance of CredentialSetAccessedUrlSchemaClassification from a dict
credential_set_accessed_url_schema_classification_from_dict = CredentialSetAccessedUrlSchemaClassification.from_dict(credential_set_accessed_url_schema_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


