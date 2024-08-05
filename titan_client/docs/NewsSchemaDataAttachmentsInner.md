# NewsSchemaDataAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**malicious** | **bool** | Indicates if attachment is malicious. If &#x60;malicious&#x3D;true&#x60;, attachment will be an archive with password &#x60;infected&#x60; | [optional] 
**mime_type** | **str** | Mimetype | 
**name** | **str** | Attachment file &#x60;name&#x60; | 
**size** | **int** | Attachment fie &#x60;size&#x60; in bytes | 
**url** | **str** | &#x60;Url&#x60; to download attachment | 

## Example

```python
from titan_client.models.news_schema_data_attachments_inner import NewsSchemaDataAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NewsSchemaDataAttachmentsInner from a JSON string
news_schema_data_attachments_inner_instance = NewsSchemaDataAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(NewsSchemaDataAttachmentsInner.to_json())

# convert the object into a dict
news_schema_data_attachments_inner_dict = news_schema_data_attachments_inner_instance.to_dict()
# create an instance of NewsSchemaDataAttachmentsInner from a dict
news_schema_data_attachments_inner_from_dict = NewsSchemaDataAttachmentsInner.from_dict(news_schema_data_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


