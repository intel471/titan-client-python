# NewsSchemaData

Sub-document containing News data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[NewsSchemaDataAttachmentsInner]**](NewsSchemaDataAttachmentsInner.md) | News &#x60;attachments&#x60; list | [optional] 
**released** | **int** | News released date | [optional] 
**text** | **str** | Raw text with html tags | [optional] 
**topic** | **str** | &#x60;Topic&#x60; of the news | [optional] 
**type** | **str** | Type of News, for example: &#x60;BLOG&#x60;, &#x60;ANNOUNCEMENT&#x60; | 
**uid** | **str** | Unique news identifier | 

## Example

```python
from titan_client.models.news_schema_data import NewsSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of NewsSchemaData from a JSON string
news_schema_data_instance = NewsSchemaData.from_json(json)
# print the JSON string representation of the object
print(NewsSchemaData.to_json())

# convert the object into a dict
news_schema_data_dict = news_schema_data_instance.to_dict()
# create an instance of NewsSchemaData from a dict
news_schema_data_from_dict = NewsSchemaData.from_dict(news_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


