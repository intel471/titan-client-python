# CredentialSetStreamSchemaData

Credential set with related objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breach_date** | **int** | Date of breach. | [optional] 
**collection_date** | **int** | Date of collection. | [optional] 
**description** | **str** | Description of the credential set. | [optional] 
**disclosure_date** | **int** | Date of disclosure. | [optional] 
**external_sources** | [**List[CredentialSetSchemaDataExternalSourcesInner]**](CredentialSetSchemaDataExternalSourcesInner.md) | List of external sources. | [optional] 
**internal_sources** | [**List[CredentialSetSchemaDataInternalSourcesInner]**](CredentialSetSchemaDataInternalSourcesInner.md) | List of internal sources. | [optional] 
**name** | **str** | Name of the credential set. | 
**record_count** | **int** | Number of records. | [optional] 
**victims** | [**List[CredentialSetSchemaDataVictimsInner]**](CredentialSetSchemaDataVictimsInner.md) | List of purported victims. | [optional] 

## Example

```python
from titan_client.models.credential_set_stream_schema_data import CredentialSetStreamSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetStreamSchemaData from a JSON string
credential_set_stream_schema_data_instance = CredentialSetStreamSchemaData.from_json(json)
# print the JSON string representation of the object
print(CredentialSetStreamSchemaData.to_json())

# convert the object into a dict
credential_set_stream_schema_data_dict = credential_set_stream_schema_data_instance.to_dict()
# create an instance of CredentialSetStreamSchemaData from a dict
credential_set_stream_schema_data_from_dict = CredentialSetStreamSchemaData.from_dict(credential_set_stream_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


