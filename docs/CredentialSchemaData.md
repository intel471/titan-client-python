# CredentialSchemaData

Credential with related objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliations** | **List[str]** | Affiliation of the credential. Allowed values: &#x60;my_employees&#x60;, &#x60;vip_emails&#x60;, &#x60;my_customers&#x60;, &#x60;third_parties&#x60;. | [optional] 
**credential_domain** | **str** | Domain of the credential. | [optional] 
**credential_login** | **str** | Login of the credential. | [optional] 
**credential_sets** | [**List[CredentialSchemaDataCredentialSetsInner]**](CredentialSchemaDataCredentialSetsInner.md) | Credential sets associated with the credential. | [optional] 
**detected_malware** | [**List[Malware]**](Malware.md) | Array of malware family objects. | [optional] 
**detection_domain** | **str** | Detection domain of the credential. | [optional] 
**password** | [**CredentialSchemaDataPassword**](CredentialSchemaDataPassword.md) |  | [optional] 

## Example

```python
from titan_client.models.credential_schema_data import CredentialSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSchemaData from a JSON string
credential_schema_data_instance = CredentialSchemaData.from_json(json)
# print the JSON string representation of the object
print(CredentialSchemaData.to_json())

# convert the object into a dict
credential_schema_data_dict = credential_schema_data_instance.to_dict()
# create an instance of CredentialSchemaData from a dict
credential_schema_data_from_dict = CredentialSchemaData.from_dict(credential_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


