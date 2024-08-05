# CredentialSchemaDataPasswordComplexity

Details of the password's complexity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entropy** | **float** | The password entropy. | [optional] 
**length** | **int** | The length of the password. | [optional] 
**lowercase** | **int** | The number of lowercase letters in the password. | [optional] 
**numbers** | **int** | The number of digits in the password. | [optional] 
**other** | **int** | The number of other characters in the password. | [optional] 
**punctuation_marks** | **int** | The number of punctuation marks in the password. | [optional] 
**score** | **float** | The password score. | [optional] 
**separators** | **int** | The number of separators in the password. | [optional] 
**symbols** | **int** | The number of symbols in the password. | [optional] 
**uppercase** | **int** | The number of uppercase characters in the password. | [optional] 
**weakness** | **float** | The password weakness. | [optional] 

## Example

```python
from titan_client.models.credential_schema_data_password_complexity import CredentialSchemaDataPasswordComplexity

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSchemaDataPasswordComplexity from a JSON string
credential_schema_data_password_complexity_instance = CredentialSchemaDataPasswordComplexity.from_json(json)
# print the JSON string representation of the object
print(CredentialSchemaDataPasswordComplexity.to_json())

# convert the object into a dict
credential_schema_data_password_complexity_dict = credential_schema_data_password_complexity_instance.to_dict()
# create an instance of CredentialSchemaDataPasswordComplexity from a dict
credential_schema_data_password_complexity_from_dict = CredentialSchemaDataPasswordComplexity.from_dict(credential_schema_data_password_complexity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


