# TagSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_count** | **int** | Count of reports with this tag. | [optional] 
**tag** | **str** | List of &#x60;Tags&#x60;. | 
**use_count** | **int** | Total usage count. Right now this number is equal to the &#x60;report_count&#x60; field as only [Information Reports](#../paths/reports.yaml) are tagged.  In future might include other tagged entries. | 

## Example

```python
from titan_client.models.tag_schema import TagSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TagSchema from a JSON string
tag_schema_instance = TagSchema.from_json(json)
# print the JSON string representation of the object
print(TagSchema.to_json())

# convert the object into a dict
tag_schema_dict = tag_schema_instance.to_dict()
# create an instance of TagSchema from a dict
tag_schema_from_dict = TagSchema.from_dict(tag_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


