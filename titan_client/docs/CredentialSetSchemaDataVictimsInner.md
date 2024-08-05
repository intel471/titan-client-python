# CredentialSetSchemaDataVictimsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Purported victim name. | 
**urls** | **List[str]** | List of purported victim URLs. | [optional] 

## Example

```python
from titan_client.models.credential_set_schema_data_victims_inner import CredentialSetSchemaDataVictimsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetSchemaDataVictimsInner from a JSON string
credential_set_schema_data_victims_inner_instance = CredentialSetSchemaDataVictimsInner.from_json(json)
# print the JSON string representation of the object
print(CredentialSetSchemaDataVictimsInner.to_json())

# convert the object into a dict
credential_set_schema_data_victims_inner_dict = credential_set_schema_data_victims_inner_instance.to_dict()
# create an instance of CredentialSetSchemaDataVictimsInner from a dict
credential_set_schema_data_victims_inner_from_dict = CredentialSetSchemaDataVictimsInner.from_dict(credential_set_schema_data_victims_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


