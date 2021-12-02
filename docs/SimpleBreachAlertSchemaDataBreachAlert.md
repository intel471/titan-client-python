# SimpleBreachAlertSchemaDataBreachAlert

Sub-document containing Breach Alert information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_or_group** | **str** | Name of the actor or the actor group behind the breach. | 
**confidence** | [**SimpleBreachAlertSchemaDataBreachAlertConfidence**](SimpleBreachAlertSchemaDataBreachAlertConfidence.md) |  | 
**date_of_information** | **int** | Breach Alert&#39;s date of information. | 
**intel_requirements** | **list[str]** | General Intel Requirements (GIR). | [optional] 
**released_at** | **int** | Breach Alert&#39;s release date. | 
**sensitive_source** | **bool** | Indicates if the document contains sensitive source derived information. | [optional] 
**sources** | [**list[SimpleBreachAlertSchemaDataBreachAlertSources]**](SimpleBreachAlertSchemaDataBreachAlertSources.md) | Sources for this alert, either from Titan or external &#x60;resources&#x60;. | [optional] 
**title** | **str** | Breach Alert&#39;s title. | 
**victim** | [**SimpleBreachAlertSchemaDataBreachAlertVictim**](SimpleBreachAlertSchemaDataBreachAlertVictim.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


