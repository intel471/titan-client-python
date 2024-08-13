# FullNewsSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**NewsSchemaActivity**](NewsSchemaActivity.md) |  | 
**data** | [**NewsSchemaData**](NewsSchemaData.md) |  | 
**last_updated** | **int** | News last modification date | 

## Example

```python
from titan_client.models.full_news_schema import FullNewsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FullNewsSchema from a JSON string
full_news_schema_instance = FullNewsSchema.from_json(json)
# print the JSON string representation of the object
print(FullNewsSchema.to_json())

# convert the object into a dict
full_news_schema_dict = full_news_schema_instance.to_dict()
# create an instance of FullNewsSchema from a dict
full_news_schema_from_dict = FullNewsSchema.from_dict(full_news_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


