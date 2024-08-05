# IocsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ioc_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**ioc_total_count** | **int** | Total count of matched entities. | 
**iocs** | [**List[IocSchema]**](IocSchema.md) | List of &#x60;Indicators of compromise&#x60;. | [optional] 

## Example

```python
from titan_client.models.iocs_response import IocsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IocsResponse from a JSON string
iocs_response_instance = IocsResponse.from_json(json)
# print the JSON string representation of the object
print(IocsResponse.to_json())

# convert the object into a dict
iocs_response_dict = iocs_response_instance.to_dict()
# create an instance of IocsResponse from a dict
iocs_response_from_dict = IocsResponse.from_dict(iocs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


