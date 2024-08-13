# EventSchemaMeta

Meta data used to describe document version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Document schema version. | 

## Example

```python
from titan_client.models.event_schema_meta import EventSchemaMeta

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchemaMeta from a JSON string
event_schema_meta_instance = EventSchemaMeta.from_json(json)
# print the JSON string representation of the object
print(EventSchemaMeta.to_json())

# convert the object into a dict
event_schema_meta_dict = event_schema_meta_instance.to_dict()
# create an instance of EventSchemaMeta from a dict
event_schema_meta_from_dict = EventSchemaMeta.from_dict(event_schema_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


