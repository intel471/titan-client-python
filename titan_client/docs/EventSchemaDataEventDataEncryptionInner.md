# EventSchemaDataEventDataEncryptionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Type of &#x60;algorithm&#x60; used in the encryption. | [optional] 
**context** | **str** | The &#x60;context&#39; of the event. | [optional] 
**key** | **str** | The encryption &#x60;key&#x60;. | [optional] 

## Example

```python
from titan_client.models.event_schema_data_event_data_encryption_inner import EventSchemaDataEventDataEncryptionInner

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaDataEventDataEncryptionInner from a JSON string
event_schema_data_event_data_encryption_inner_instance = EventSchemaDataEventDataEncryptionInner.from_json(json)
# print the JSON string representation of the object
print(EventSchemaDataEventDataEncryptionInner.to_json())

# convert the object into a dict
event_schema_data_event_data_encryption_inner_dict = event_schema_data_event_data_encryption_inner_instance.to_dict()
# create an instance of EventSchemaDataEventDataEncryptionInner from a dict
event_schema_data_event_data_encryption_inner_from_dict = EventSchemaDataEventDataEncryptionInner.from_dict(event_schema_data_event_data_encryption_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


