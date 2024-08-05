# InstantMessageSchemaDataChannel

Sub-document containing channel information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Channel &#x60;name&#x60;. | 
**registration_date** | **int** | Channel registration date. | [optional] 
**topic** | **str** | Description of channel &#x60;topic&#x60;. | [optional] 
**uid** | **str** | Unique channel identifier. | 
**url** | **str** | Channel &#x60;url&#x60;. | [optional] 

## Example

```python
from titan_client.models.instant_message_schema_data_channel import InstantMessageSchemaDataChannel

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMessageSchemaDataChannel from a JSON string
instant_message_schema_data_channel_instance = InstantMessageSchemaDataChannel.from_json(json)
# print the JSON string representation of the object
print(InstantMessageSchemaDataChannel.to_json())

# convert the object into a dict
instant_message_schema_data_channel_dict = instant_message_schema_data_channel_instance.to_dict()
# create an instance of InstantMessageSchemaDataChannel from a dict
instant_message_schema_data_channel_from_dict = InstantMessageSchemaDataChannel.from_dict(instant_message_schema_data_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


