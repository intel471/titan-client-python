# CredentialSetStreamSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**CredentialSetSchemaActivity**](CredentialSetSchemaActivity.md) |  | 
**classification** | [**CredentialSetSchemaClassification**](CredentialSetSchemaClassification.md) |  | [optional] 
**data** | [**CredentialSetStreamSchemaData**](CredentialSetStreamSchemaData.md) |  | 
**last_updated** | **int** | Credential set last modification date. | 
**statistics** | [**CredentialSetSchemaStatistics**](CredentialSetSchemaStatistics.md) |  | [optional] 
**uid** | **str** | Unique credential set identifier. | 

## Example

```python
from titan_client.models.credential_set_stream_schema import CredentialSetStreamSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetStreamSchema from a JSON string
credential_set_stream_schema_instance = CredentialSetStreamSchema.from_json(json)
# print the JSON string representation of the object
print(CredentialSetStreamSchema.to_json())

# convert the object into a dict
credential_set_stream_schema_dict = credential_set_stream_schema_instance.to_dict()
# create an instance of CredentialSetStreamSchema from a dict
credential_set_stream_schema_from_dict = CredentialSetStreamSchema.from_dict(credential_set_stream_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


