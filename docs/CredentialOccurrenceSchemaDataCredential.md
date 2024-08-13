# CredentialOccurrenceSchemaDataCredential

Sub-document containing credential information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliations** | **List[str]** | Affiliation of the credential. Allowed values: &#x60;my_employees&#x60;, &#x60;vip_emails&#x60;, &#x60;my_customers&#x60;, &#x60;third_parties&#x60;. | [optional] 
**credential_domain** | **str** | Domain of the credential. | [optional] 
**credential_login** | **str** | Login of the credential. | [optional] 
**detection_domain** | **str** | Detection domain of the credential. | [optional] 
**password** | [**CredentialSchemaDataPassword**](CredentialSchemaDataPassword.md) |  | [optional] 
**uid** | **str** | Unique credential identifier. | 

## Example

```python
from titan_client.models.credential_occurrence_schema_data_credential import CredentialOccurrenceSchemaDataCredential

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialOccurrenceSchemaDataCredential from a JSON string
credential_occurrence_schema_data_credential_instance = CredentialOccurrenceSchemaDataCredential.from_json(json)
# print the JSON string representation of the object
print(CredentialOccurrenceSchemaDataCredential.to_json())

# convert the object into a dict
credential_occurrence_schema_data_credential_dict = credential_occurrence_schema_data_credential_instance.to_dict()
# create an instance of CredentialOccurrenceSchemaDataCredential from a dict
credential_occurrence_schema_data_credential_from_dict = CredentialOccurrenceSchemaDataCredential.from_dict(credential_occurrence_schema_data_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


