# NewsSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**NewsSchemaActivity**](NewsSchemaActivity.md) |  | 
**data** | [**NewsSchemaData**](NewsSchemaData.md) |  | 
**last_updated** | **int** | News last modification date | 

## Example

```python
from titan_client.models.news_schema import NewsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NewsSchema from a JSON string
news_schema_instance = NewsSchema.from_json(json)
# print the JSON string representation of the object
print(NewsSchema.to_json())

# convert the object into a dict
news_schema_dict = news_schema_instance.to_dict()
# create an instance of NewsSchema from a dict
news_schema_from_dict = NewsSchema.from_dict(news_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


