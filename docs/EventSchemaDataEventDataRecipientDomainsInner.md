# EventSchemaDataEventDataRecipientDomainsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Cout of recipient domains. | [optional] 
**domain** | **str** | Recipient domain. | [optional] 

## Example

```python
from titan_client.models.event_schema_data_event_data_recipient_domains_inner import EventSchemaDataEventDataRecipientDomainsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaDataEventDataRecipientDomainsInner from a JSON string
event_schema_data_event_data_recipient_domains_inner_instance = EventSchemaDataEventDataRecipientDomainsInner.from_json(json)
# print the JSON string representation of the object
print(EventSchemaDataEventDataRecipientDomainsInner.to_json())

# convert the object into a dict
event_schema_data_event_data_recipient_domains_inner_dict = event_schema_data_event_data_recipient_domains_inner_instance.to_dict()
# create an instance of EventSchemaDataEventDataRecipientDomainsInner from a dict
event_schema_data_event_data_recipient_domains_inner_from_dict = EventSchemaDataEventDataRecipientDomainsInner.from_dict(event_schema_data_event_data_recipient_domains_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


