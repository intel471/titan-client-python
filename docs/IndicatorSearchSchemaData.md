# IndicatorSearchSchemaData

Sub-document containing indicator information. Might contain fields specific for different indicator types which are not described in current documentation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **str** | Indicators with &#x60;high&#x60; confidence are derived from a primary source and are verified. They can safely be used for blocking. If indicators are from a primary source, but they have not been verified, then the confidence rating is reduced to &#x60;medium&#x60;. We recommend them for alerting or threat hunting. An example of this is a controller URL extracted from a malware configuration file. The file is verified (high), but the controller URLs inside it’s configuration are not (medium). Indicators that are derived from a third party source via pivoting are marked as &#x60;low&#x60; confidence unless they have been verified. We don’t publish many low confidence indicators. | 
**context** | [**IndicatorSearchSchemaDataContext**](IndicatorSearchSchemaDataContext.md) |  | [optional] 
**expiration** | **int** | Indicator should be removed from block lists at this date. | 
**indicator_data** | [**IndicatorSearchSchemaDataIndicatorData**](IndicatorSearchSchemaDataIndicatorData.md) |  | 
**indicator_type** | **str** | Describes the type of indicator: (e.g. file, ipv4, url). | 
**intel_requirements** | **list[str]** | List of General Intelligence Requirements matching this indicator. | [optional] 
**mitre_tactics** | **str** | The MITRE ATT&amp;CK tactic classification. | [optional] 
**threat** | [**IndicatorSearchSchemaDataThreat**](IndicatorSearchSchemaDataThreat.md) |  | 
**uid** | **str** | Indicator&#39;s UID | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


