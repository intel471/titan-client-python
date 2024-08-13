# NewsSchemaActivity

Period News was active

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **int** | Start of the news activity range | 
**last** | **int** | End of the news activity range | 

## Example

```python
from titan_client.models.news_schema_activity import NewsSchemaActivity

# TODO update the JSON string below
json = "{}"
# create an instance of NewsSchemaActivity from a JSON string
news_schema_activity_instance = NewsSchemaActivity.from_json(json)
# print the JSON string representation of the object
print(NewsSchemaActivity.to_json())

# convert the object into a dict
news_schema_activity_dict = news_schema_activity_instance.to_dict()
# create an instance of NewsSchemaActivity from a dict
news_schema_activity_from_dict = NewsSchemaActivity.from_dict(news_schema_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


