# AlertListSchemaHighlightsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunks** | [**List[AlertListSchemaHighlightsInnerChunksInner]**](AlertListSchemaHighlightsInnerChunksInner.md) | Text snippet &#x60;chunks&#x60; with highlights. | 
**var_field** | **str** | Document &#x60;field&#x60; which was highlighted. | 

## Example

```python
from titan_client.models.alert_list_schema_highlights_inner import AlertListSchemaHighlightsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AlertListSchemaHighlightsInner from a JSON string
alert_list_schema_highlights_inner_instance = AlertListSchemaHighlightsInner.from_json(json)
# print the JSON string representation of the object
print(AlertListSchemaHighlightsInner.to_json())

# convert the object into a dict
alert_list_schema_highlights_inner_dict = alert_list_schema_highlights_inner_instance.to_dict()
# create an instance of AlertListSchemaHighlightsInner from a dict
alert_list_schema_highlights_inner_from_dict = AlertListSchemaHighlightsInner.from_dict(alert_list_schema_highlights_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


