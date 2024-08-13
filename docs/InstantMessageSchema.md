# InstantMessageSchema

Sub-document containing instant message and linked to it information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**InstantMessageSchemaActivity**](InstantMessageSchemaActivity.md) |  | 
**data** | [**InstantMessageSchemaData**](InstantMessageSchemaData.md) |  | 
**last_updated** | **int** | Instant message last modification date. | 

## Example

```python
from titan_client.models.instant_message_schema import InstantMessageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMessageSchema from a JSON string
instant_message_schema_instance = InstantMessageSchema.from_json(json)
# print the JSON string representation of the object
print(InstantMessageSchema.to_json())

# convert the object into a dict
instant_message_schema_dict = instant_message_schema_instance.to_dict()
# create an instance of InstantMessageSchema from a dict
instant_message_schema_from_dict = InstantMessageSchema.from_dict(instant_message_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


