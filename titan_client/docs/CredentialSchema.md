# CredentialSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**CredentialSchemaActivity**](CredentialSchemaActivity.md) |  | 
**classification** | [**CredentialSchemaClassification**](CredentialSchemaClassification.md) |  | [optional] 
**data** | [**CredentialSchemaData**](CredentialSchemaData.md) |  | 
**last_updated** | **int** | Credential last modification date. | 
**statistics** | [**CredentialSchemaStatistics**](CredentialSchemaStatistics.md) |  | [optional] 
**uid** | **str** | Unique credential identifier. | 

## Example

```python
from titan_client.models.credential_schema import CredentialSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSchema from a JSON string
credential_schema_instance = CredentialSchema.from_json(json)
# print the JSON string representation of the object
print(CredentialSchema.to_json())

# convert the object into a dict
credential_schema_dict = credential_schema_instance.to_dict()
# create an instance of CredentialSchema from a dict
credential_schema_from_dict = CredentialSchema.from_dict(credential_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


