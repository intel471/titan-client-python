# InstantMessageSchemaData

Sub-document containing instant message and linked to it information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**InstantMessageSchemaDataActor**](InstantMessageSchemaDataActor.md) |  | 
**channel** | [**InstantMessageSchemaDataChannel**](InstantMessageSchemaDataChannel.md) |  | 
**message** | [**InstantMessageSchemaDataMessage**](InstantMessageSchemaDataMessage.md) |  | 
**server** | [**InstantMessageSchemaDataServer**](InstantMessageSchemaDataServer.md) |  | 

## Example

```python
from titan_client.models.instant_message_schema_data import InstantMessageSchemaData

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMessageSchemaData from a JSON string
instant_message_schema_data_instance = InstantMessageSchemaData.from_json(json)
# print the JSON string representation of the object
print(InstantMessageSchemaData.to_json())

# convert the object into a dict
instant_message_schema_data_dict = instant_message_schema_data_instance.to_dict()
# create an instance of InstantMessageSchemaData from a dict
instant_message_schema_data_from_dict = InstantMessageSchemaData.from_dict(instant_message_schema_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


