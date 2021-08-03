# YARASearchSchemaData

Sub-document containing YARA information. Might contain fields specific for different YARA types which are not described in current documentation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **str** | &#x60;Confidence&#x60; of YARA: &#x60;high&#x60; — recommended for blocking, &#x60;medium&#x60; — for alerting, &#x60;low&#x60; — needs to be verified. | 
**intel_requirements** | **list[str]** | List of General Intelligence Requirements matching this YARA. | [optional] 
**threat** | [**YARASearchSchemaDataThreat**](YARASearchSchemaDataThreat.md) |  | 
**yara_data** | [**YARASearchSchemaDataYaraData**](YARASearchSchemaDataYaraData.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


