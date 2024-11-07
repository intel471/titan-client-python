# EventSchemaDataEventData

Sub-document containing event data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack_targets** | **list[object]** |  | [optional] 
**attack_type** | **str** |  | [optional] 
**bot_settings** | **object** | An object containing varying data types showing malware bot settings data. Contains any of but not limited the following fields: &#x60;exit_country&#x60;, &#x60;config&#x60;, &#x60;encryption&#x60;. | [optional] 
**command** | **str** | Command. | [optional] 
**component_type** | **str** | Type of component i.e. &#x60;CORE&#x60;. | [optional] 
**config_file** | **str** | Config file. | [optional] 
**controller** | [**EventSchemaDataEventDataController**](EventSchemaDataEventDataController.md) |  | [optional] 
**controllers** | [**list[EventSchemaDataEventDataControllersInner]**](EventSchemaDataEventDataControllersInner.md) | An array of objects, each containing an individual controller&#39;s url. | [optional] 
**encryption** | [**list[EventSchemaDataEventDataEncryptionInner]**](EventSchemaDataEventDataEncryptionInner.md) | An array of &#x60;encryption&#x60; meta data. | [optional] 
**exfil_location** | **str** | Contains the url location of the exfiltration event. | [optional] 
**file** | [**EventSchemaDataEventDataFile**](EventSchemaDataEventDataFile.md) |  | [optional] 
**inject_type** | **str** | Inject type. | [optional] 
**location** | [**EventSchemaDataEventDataLocation**](EventSchemaDataEventDataLocation.md) |  | [optional] 
**parameters** | **list[object]** |  | [optional] 
**plugin_name** | **str** | Plugin&#39;s name. | [optional] 
**plugin_type** | **str** | Type of plugin. i.e. &#x60;REMOTE_ACCESS&#x60;, &#x60;CREDENTIAL_STEALER&#x60;, &#x60;OTHER&#x60;. | [optional] 
**recipient_domains** | [**list[EventSchemaDataEventDataRecipientDomainsInner]**](EventSchemaDataEventDataRecipientDomainsInner.md) | Recipient domains. | [optional] 
**senders** | **list[str]** | Senders. | [optional] 
**settings** | **list[object]** | An array of event related &#x60;settings&#x60; objects containing any of but not limited the following fields: &#x60;plugin_location&#x60;, &#x60;bot_version&#x60;, &#x60;compaign_id&#x60;, etc. | [optional] 
**target_type** | **str** | Type of target. | [optional] 
**triggers** | [**list[EventSchemaDataEventDataTriggersInner]**](EventSchemaDataEventDataTriggersInner.md) | An array of objects, each containing the field &#x60;trigger&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


