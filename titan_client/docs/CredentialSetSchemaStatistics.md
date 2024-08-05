# CredentialSetSchemaStatistics

Statistics regarding returned objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessed_urls_total_count** | **int** | Number of accessed URLs. | [optional] 
**credential_occurrences_total_count** | **int** | Number of credential occurrences. | [optional] 
**credentials_total_count** | **int** | Number of credentials. | [optional] 

## Example

```python
from titan_client.models.credential_set_schema_statistics import CredentialSetSchemaStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSetSchemaStatistics from a JSON string
credential_set_schema_statistics_instance = CredentialSetSchemaStatistics.from_json(json)
# print the JSON string representation of the object
print(CredentialSetSchemaStatistics.to_json())

# convert the object into a dict
credential_set_schema_statistics_dict = credential_set_schema_statistics_instance.to_dict()
# create an instance of CredentialSetSchemaStatistics from a dict
credential_set_schema_statistics_from_dict = CredentialSetSchemaStatistics.from_dict(credential_set_schema_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


