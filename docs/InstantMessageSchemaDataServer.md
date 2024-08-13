# InstantMessageSchemaDataServer

Sub-document containing `server` information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Server &#x60;name&#x60;. | [optional] 
**service_type** | **str** | Server&#39;s service type. | 
**uid** | **str** | Unique server identifier. | 

## Example

```python
from titan_client.models.instant_message_schema_data_server import InstantMessageSchemaDataServer

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMessageSchemaDataServer from a JSON string
instant_message_schema_data_server_instance = InstantMessageSchemaDataServer.from_json(json)
# print the JSON string representation of the object
print(InstantMessageSchemaDataServer.to_json())

# convert the object into a dict
instant_message_schema_data_server_dict = instant_message_schema_data_server_instance.to_dict()
# create an instance of InstantMessageSchemaDataServer from a dict
instant_message_schema_data_server_from_dict = InstantMessageSchemaDataServer.from_dict(instant_message_schema_data_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


