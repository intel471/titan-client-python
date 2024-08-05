# EventStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_next** | **str** | Stream position identifier to continue scrolling from. | [optional] 
**event_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**event_total_count** | **int** | Total count of matched events. | 
**events** | [**List[EventSchema]**](EventSchema.md) | List of &#x60;Events&#x60;. | [optional] 

## Example

```python
from titan_client.models.event_stream_response import EventStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventStreamResponse from a JSON string
event_stream_response_instance = EventStreamResponse.from_json(json)
# print the JSON string representation of the object
print(EventStreamResponse.to_json())

# convert the object into a dict
event_stream_response_dict = event_stream_response_instance.to_dict()
# create an instance of EventStreamResponse from a dict
event_stream_response_from_dict = EventStreamResponse.from_dict(event_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


