# CredentialSchemaStatistics

Statistics regarding returned objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessed_urls_total_count** | **int** | Number of accessed URLs. | [optional] 

## Example

```python
from titan_client.models.credential_schema_statistics import CredentialSchemaStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSchemaStatistics from a JSON string
credential_schema_statistics_instance = CredentialSchemaStatistics.from_json(json)
# print the JSON string representation of the object
print(CredentialSchemaStatistics.to_json())

# convert the object into a dict
credential_schema_statistics_dict = credential_schema_statistics_instance.to_dict()
# create an instance of CredentialSchemaStatistics from a dict
credential_schema_statistics_from_dict = CredentialSchemaStatistics.from_dict(credential_schema_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


