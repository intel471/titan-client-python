# PrivateMessageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | &#x60;Date&#x60; the message was sent. | 
**last_updated** | **int** | Event modification date. | [optional] 
**links** | [**PrivateMessageSchemaLinks**](PrivateMessageSchemaLinks.md) |  | 
**message** | **str** | HTML &#x60;message&#x60; content. If message is translated, this parameter contains translated text, if not — original. | 
**message_original** | **str** | Original HTML message content. This parameter is active if message is translated. | [optional] 
**subject** | **str** | Message &#x60;subject&#x60;. If message subject is translated, this parameter contains translated subject, if not — original. | [optional] 
**subject_original** | **str** | Original message subject. This parameter is active if message subject is translated. | [optional] 
**uid** | **str** | Unique message identifier. | 

## Example

```python
from titan_client.models.private_message_schema import PrivateMessageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessageSchema from a JSON string
private_message_schema_instance = PrivateMessageSchema.from_json(json)
# print the JSON string representation of the object
print(PrivateMessageSchema.to_json())

# convert the object into a dict
private_message_schema_dict = private_message_schema_instance.to_dict()
# create an instance of PrivateMessageSchema from a dict
private_message_schema_from_dict = PrivateMessageSchema.from_dict(private_message_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


