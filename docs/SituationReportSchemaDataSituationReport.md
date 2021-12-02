# SituationReportSchemaDataSituationReport

Sub-document containing Situation report information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**list[SituationReportSchemaDataSituationReportEntities]**](SituationReportSchemaDataSituationReportEntities.md) | List of entities. Contains the type and value fields of an &#x60;entity&#x60; object from the entities endpoint. | [optional] 
**link** | [**SituationReportSchemaDataSituationReportLink**](SituationReportSchemaDataSituationReportLink.md) |  | 
**related_reports** | **list[str]** | Situation report links to related reports like \&quot;Information Report\&quot; or \&quot;Malware Report\&quot;. | [optional] 
**released_at** | **int** | Situation report released date. | 
**sensitive_source** | **bool** | Indicates if the document contains sensitive source derived information. | [optional] 
**text** | **str** | Situation report text. | 
**title** | **str** | Situation report title. | [optional] 
**victims** | [**list[SituationReportSchemaDataSituationReportVictims]**](SituationReportSchemaDataSituationReportVictims.md) | Purported victims list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


