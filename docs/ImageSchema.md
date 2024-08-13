# ImageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **str** | Dimension of the image. | [optional] 
**hash** | **str** | Hash value of the image. | 
**hash_type** | **str** | Type of hash function to produce hash. | 
**image_original** | **str** | Original image download url. Note: It&#39;s just an example. The actual path depends on specific API endpoint like posts, instant messages, etc. | [optional] 
**image_sanitized** | **str** | Sanitised image download url. Note: It&#39;s just an example. The actual path depends on specific API endpoint like posts, instant messages, etc. | [optional] 
**ocr** | **str** | Recognized text from image. | [optional] 
**original_url** | **str** | Image original url. | 
**size** | **str** | Size of the image in bytes. | 
**status** | **str** | Image status. If image has no status this field will not be displayed. | [optional] 

## Example

```python
from titan_client.models.image_schema import ImageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImageSchema from a JSON string
image_schema_instance = ImageSchema.from_json(json)
# print the JSON string representation of the object
print(ImageSchema.to_json())

# convert the object into a dict
image_schema_dict = image_schema_instance.to_dict()
# create an instance of ImageSchema from a dict
image_schema_from_dict = ImageSchema.from_dict(image_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


