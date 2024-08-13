# GirsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gir_total_count** | **int** | Total count of matched results. | 
**girs** | [**List[GirSchema]**](GirSchema.md) | The array of GIRs. | [optional] 
**partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 

## Example

```python
from titan_client.models.girs_response import GirsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GirsResponse from a JSON string
girs_response_instance = GirsResponse.from_json(json)
# print the JSON string representation of the object
print(GirsResponse.to_json())

# convert the object into a dict
girs_response_dict = girs_response_instance.to_dict()
# create an instance of GirsResponse from a dict
girs_response_from_dict = GirsResponse.from_dict(girs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


