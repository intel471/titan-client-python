# EntitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[EntitiesSchema]**](EntitiesSchema.md) | List of &#x60;Enitites&#x60;. | [optional] 
**entity_partial_result** | **bool** | Indicates whether response contains partial result. That could be in case when request took to long and was terminated. | [optional] 
**entity_total_count** | **int** | Total count of matched entities. | 

## Example

```python
from titan_client.models.entities_response import EntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntitiesResponse from a JSON string
entities_response_instance = EntitiesResponse.from_json(json)
# print the JSON string representation of the object
print(EntitiesResponse.to_json())

# convert the object into a dict
entities_response_dict = entities_response_instance.to_dict()
# create an instance of EntitiesResponse from a dict
entities_response_from_dict = EntitiesResponse.from_dict(entities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


