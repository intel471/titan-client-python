# CredentialSetSchemaDataExternalSourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | External source title. | [optional] 
**url** | **str** | External source URL. | [optional] 

## Example

```python
from titan_client.models.credential_set_schema_data_external_sources_inner import CredentialSetSchemaDataExternalSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetSchemaDataExternalSourcesInner from a JSON string
credential_set_schema_data_external_sources_inner_instance = CredentialSetSchemaDataExternalSourcesInner.from_json(json)
# print the JSON string representation of the object
print(CredentialSetSchemaDataExternalSourcesInner.to_json())

# convert the object into a dict
credential_set_schema_data_external_sources_inner_dict = credential_set_schema_data_external_sources_inner_instance.to_dict()
# create an instance of CredentialSetSchemaDataExternalSourcesInner from a dict
credential_set_schema_data_external_sources_inner_from_dict = CredentialSetSchemaDataExternalSourcesInner.from_dict(credential_set_schema_data_external_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


