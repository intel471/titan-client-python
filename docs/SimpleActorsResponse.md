# SimpleActorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**actor_total_count** | **int** | Total count of matched actors. | 
**actors** | [**List[SimpleActorSchema]**](SimpleActorSchema.md) | List of &#x60;Actors&#x60;. | [optional] 

## Example

```python
from titan_client.models.simple_actors_response import SimpleActorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleActorsResponse from a JSON string
simple_actors_response_instance = SimpleActorsResponse.from_json(json)
# print the JSON string representation of the object
print(SimpleActorsResponse.to_json())

# convert the object into a dict
simple_actors_response_dict = simple_actors_response_instance.to_dict()
# create an instance of SimpleActorsResponse from a dict
simple_actors_response_from_dict = SimpleActorsResponse.from_dict(simple_actors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


