# FullReportSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_handle** | **str** | Actor&#39;s handle | [optional] 
**actor_subject_of_report** | [**List[SimpleReportSchemaActorSubjectOfReportInner]**](SimpleReportSchemaActorSubjectOfReportInner.md) | List of actors mentioned in report subject. | [optional] 
**admiralty_code** | **str** | Code as described [here](http://en.wikipedia.org/wiki/Admiralty_code). All Fintel reports have admiraltyCode&#x3D;&#x60;A1&#x60;. | [optional] 
**classification** | [**SimpleReportSchemaClassification**](SimpleReportSchemaClassification.md) |  | [optional] 
**created** | **int** | Date the report was &#x60;created&#x60; as Epoch Time. | [optional] 
**date_of_information** | **int** | Date of information as Epoch Time. | [optional] 
**document_family** | **str** | Document family. | [optional] 
**document_type** | **str** | Document type. | [optional] 
**entities** | [**List[SimpleReportSchemaEntitiesInner]**](SimpleReportSchemaEntitiesInner.md) | List of entities. | [optional] 
**last_updated** | **int** | Last modification date as Epoch Time. | [optional] 
**locations** | [**List[SimpleReportSchemaLocationsInner]**](SimpleReportSchemaLocationsInner.md) | Report &#x60;locations&#x60;. | [optional] 
**motivation** | **List[str]** | Actor&#39;s &#x60;motivation&#x60;. CC for Cyber Crime, CE for Cyber Espionage, HA for Hacktivism. | [optional] 
**portal_report_url** | **str** | URL to the report on the portal. | 
**related_reports** | [**List[SimpleReportSchemaRelatedReportsInner]**](SimpleReportSchemaRelatedReportsInner.md) | List of related reports. | [optional] 
**released** | **int** | Date the report was &#x60;released&#x60; as Epoch Time. | [optional] 
**report_attachments** | [**List[SimpleReportSchemaReportAttachmentsInner]**](SimpleReportSchemaReportAttachmentsInner.md) | List of report attachments. | [optional] 
**sensitive_source** | **bool** | Indicates if the document contains sensitive source derived information. | [optional] 
**source_characterization** | **str** | Source characterization. | [optional] 
**sources** | [**List[SimpleReportSchemaSourcesInner]**](SimpleReportSchemaSourcesInner.md) | List of &#x60;sources&#x60;. | [optional] 
**subject** | **str** | Report&#39;s &#x60;subject&#x60;. | 
**tags** | **List[str]** | Report&#39;s assigned &#x60;tags&#x60;. | [optional] 
**uid** | **str** | Unique report identifier. | 
**victims** | [**List[SimpleReportSchemaVictimsInner]**](SimpleReportSchemaVictimsInner.md) | Purported victims list. | [optional] 
**executive_summary** | **str** | Executive summary in HTML format. | [optional] 
**raw_text** | **str** | Raw text in HTML format. | 
**raw_text_translated** | **str** | Translated text in HTML format. | [optional] 
**researcher_comments** | **str** | Researcher&#39;s comments in HTML format. | [optional] 

## Example

```python
from titan_client.models.full_report_schema import FullReportSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FullReportSchema from a JSON string
full_report_schema_instance = FullReportSchema.from_json(json)
# print the JSON string representation of the object
print(FullReportSchema.to_json())

# convert the object into a dict
full_report_schema_dict = full_report_schema_instance.to_dict()
# create an instance of FullReportSchema from a dict
full_report_schema_from_dict = FullReportSchema.from_dict(full_report_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


