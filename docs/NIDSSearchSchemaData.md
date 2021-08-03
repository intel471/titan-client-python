# NIDSSearchSchemaData

Sub-document containing NIDS information. Might contain fields specific for different NIDS types which are not described in current documentation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **str** | NIDS &#x60;confidence&#x60; level: &#x60;high&#x60; — recommended for blocking, &#x60;medium&#x60; — for alerting, &#x60;low&#x60; — needs to be verified. | 
**intel_requirements** | **list[str]** | List of General Intelligence Requirements matching this NIDS. | [optional] 
**nids_data** | **object** | Sub-document containing NIDS type and value(s). | 
**nids_type** | **str** | Describes the type of NIDS. | 
**threat** | [**NIDSSearchSchemaDataThreat**](NIDSSearchSchemaDataThreat.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


