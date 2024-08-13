# SimpleReportSchemaReportAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A &#x60;description&#x60; of attachment. | [optional] 
**file_name** | **str** | Attachment file&#39;s name. | 
**file_size** | **int** | Attachment file size in bytes. | 
**malicious** | **bool** | Indicates if attachment is &#x60;malicious&#x60;. If malicious&#x3D;&#x60;true&#x60;, attachment will be an archive with password &#x60;infected&#x60;. | [optional] 
**mime_type** | **str** | Mime type. | 
**url** | **str** | &#x60;Url&#x60; to download attachment. | 

## Example

```python
from titan_client.models.simple_report_schema_report_attachments_inner import SimpleReportSchemaReportAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleReportSchemaReportAttachmentsInner from a JSON string
simple_report_schema_report_attachments_inner_instance = SimpleReportSchemaReportAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(SimpleReportSchemaReportAttachmentsInner.to_json())

# convert the object into a dict
simple_report_schema_report_attachments_inner_dict = simple_report_schema_report_attachments_inner_instance.to_dict()
# create an instance of SimpleReportSchemaReportAttachmentsInner from a dict
simple_report_schema_report_attachments_inner_from_dict = SimpleReportSchemaReportAttachmentsInner.from_dict(simple_report_schema_report_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


