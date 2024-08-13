# CredentialSetAccessedUrlStreamSchemaData

Credential set accessed URL with related objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessed_domain** | **str** | Accessed domain. | 
**accessed_url** | **str** | Accessed URL. | 
**credential_set** | [**CredentialSetAccessedUrlSchemaDataCredentialSet**](CredentialSetAccessedUrlSchemaDataCredentialSet.md) |  | [optional] 

## Example

```python
from titan_client.models.credential_set_accessed_url_stream_schema_data import CredentialSetAccessedUrlStreamSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetAccessedUrlStreamSchemaData from a JSON string
credential_set_accessed_url_stream_schema_data_instance = CredentialSetAccessedUrlStreamSchemaData.from_json(json)
# print the JSON string representation of the object
print(CredentialSetAccessedUrlStreamSchemaData.to_json())

# convert the object into a dict
credential_set_accessed_url_stream_schema_data_dict = credential_set_accessed_url_stream_schema_data_instance.to_dict()
# create an instance of CredentialSetAccessedUrlStreamSchemaData from a dict
credential_set_accessed_url_stream_schema_data_from_dict = CredentialSetAccessedUrlStreamSchemaData.from_dict(credential_set_accessed_url_stream_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


