# CredentialSchemaData

Credential with related objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliations** | **list[str]** | Affiliation of the credential. Allowed values: &#x60;my_employees&#x60;, &#x60;vip_emails&#x60;, &#x60;my_customers&#x60;, &#x60;third_parties&#x60;. | [optional] 
**credential_domain** | **str** | Domain of the credential. | [optional] 
**credential_login** | **str** | Login of the credential. | [optional] 
**credential_sets** | [**list[CredentialSchemaDataCredentialSetsInner]**](CredentialSchemaDataCredentialSetsInner.md) | Credential sets associated with the credential. | [optional] 
**detected_malware** | [**list[Malware]**](Malware.md) | Array of malware family objects. | [optional] 
**detection_domain** | **str** | Detection domain of the credential. | [optional] 
**password** | [**CredentialSchemaDataPassword**](CredentialSchemaDataPassword.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


