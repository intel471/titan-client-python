# AlertListSchema

Returns list of Alerts matching filter criteria excluding the following types: Malware reports, YARA

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**SimpleActorSchema**](SimpleActorSchema.md) |  | [optional] 
**breach_alert** | [**SimpleBreachAlertSchema**](SimpleBreachAlertSchema.md) |  | [optional] 
**credential** | [**CredentialSchema**](CredentialSchema.md) |  | [optional] 
**credential_occurrence** | [**CredentialOccurrenceSchema**](CredentialOccurrenceSchema.md) |  | [optional] 
**credential_set** | [**CredentialSetSchema**](CredentialSetSchema.md) |  | [optional] 
**cve_report** | [**SimpleCveSchema**](SimpleCveSchema.md) |  | [optional] 
**data_leak_post** | [**DataLeakPostSchema**](DataLeakPostSchema.md) |  | [optional] 
**entity** | [**EntitiesSchema**](EntitiesSchema.md) |  | [optional] 
**event** | [**EventSchema**](EventSchema.md) |  | [optional] 
**found_time** | **int** | Date when alert was created. | 
**highlights** | [**List[AlertListSchemaHighlightsInner]**](AlertListSchemaHighlightsInner.md) | Text snippets with &#x60;highlights&#x60; matching search terms. | [optional] 
**indicator** | [**IndicatorSearchSchema**](IndicatorSearchSchema.md) |  | [optional] 
**instant_message** | [**InstantMessageSchema**](InstantMessageSchema.md) |  | [optional] 
**post** | [**PostSchema**](PostSchema.md) |  | [optional] 
**private_message** | [**PrivateMessageSchema**](PrivateMessageSchema.md) |  | [optional] 
**report** | [**AlertListSchemaReport**](AlertListSchemaReport.md) |  | [optional] 
**status** | **str** | Read or unread. | 
**uid** | **str** | Unique alert identifier. | 
**watcher_group_uid** | **str** | Unique watcher group identifier. Displayed if user has access to this watcher group. | [optional] 
**watcher_uid** | **str** | Unique watcher identifier. Displayed if user has access to this watcher. | [optional] 

## Example

```python
from titan_client.models.alert_list_schema import AlertListSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AlertListSchema from a JSON string
alert_list_schema_instance = AlertListSchema.from_json(json)
# print the JSON string representation of the object
print(AlertListSchema.to_json())

# convert the object into a dict
alert_list_schema_dict = alert_list_schema_instance.to_dict()
# create an instance of AlertListSchema from a dict
alert_list_schema_from_dict = AlertListSchema.from_dict(alert_list_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


