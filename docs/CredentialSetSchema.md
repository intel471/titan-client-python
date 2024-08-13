# CredentialSetSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**CredentialSetSchemaActivity**](CredentialSetSchemaActivity.md) |  | 
**classification** | [**CredentialSetSchemaClassification**](CredentialSetSchemaClassification.md) |  | [optional] 
**data** | [**CredentialSetSchemaData**](CredentialSetSchemaData.md) |  | 
**last_updated** | **int** | Credential set last modification date. | 
**statistics** | [**CredentialSetSchemaStatistics**](CredentialSetSchemaStatistics.md) |  | [optional] 
**uid** | **str** | Unique credential set identifier. | 

## Example

```python
from titan_client.models.credential_set_schema import CredentialSetSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetSchema from a JSON string
credential_set_schema_instance = CredentialSetSchema.from_json(json)
# print the JSON string representation of the object
print(CredentialSetSchema.to_json())

# convert the object into a dict
credential_set_schema_dict = credential_set_schema_instance.to_dict()
# create an instance of CredentialSetSchema from a dict
credential_set_schema_from_dict = CredentialSetSchema.from_dict(credential_set_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


