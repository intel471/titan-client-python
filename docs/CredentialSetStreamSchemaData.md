# CredentialSetStreamSchemaData

Credential set with related objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breach_date** | **int** | Date of breach. | [optional] 
**collection_date** | **int** | Date of collection. | [optional] 
**description** | **str** | Description of the credential set. | [optional] 
**disclosure_date** | **int** | Date of disclosure. | [optional] 
**external_sources** | [**list[CredentialSetSchemaDataExternalSourcesInner]**](CredentialSetSchemaDataExternalSourcesInner.md) | List of external sources. | [optional] 
**internal_sources** | [**list[CredentialSetSchemaDataInternalSourcesInner]**](CredentialSetSchemaDataInternalSourcesInner.md) | List of internal sources. | [optional] 
**name** | **str** | Name of the credential set. | 
**record_count** | **int** | Number of records. | [optional] 
**victims** | [**list[CredentialSetSchemaDataVictimsInner]**](CredentialSetSchemaDataVictimsInner.md) | List of purported victims. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


