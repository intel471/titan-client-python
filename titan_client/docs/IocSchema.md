# IocSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_from** | **int** | Date first seen. | [optional] 
**active_till** | **int** | Date last seen. | [optional] 
**isp_country_code** | **str** | Internet Service Provider country code. | [optional] 
**isp_name** | **str** | Internet Service Provider name. | [optional] 
**last_updated** | **int** | Last modification date. | [optional] 
**links** | [**IocSchemaLinks**](IocSchemaLinks.md) |  | 
**type** | **str** | IOC &#x60;type&#x60;, one of &#x60;MaliciousDomain&#x60;, &#x60;IPAddress&#x60;, &#x60;IPv4Prefix&#x60;, &#x60;IPv6Prefix&#x60;, &#x60;AutonomousSystem&#x60;, &#x60;MaliciousURL&#x60;, &#x60;MD5&#x60;, &#x60;SHA1&#x60;, &#x60;SHA256&#x60;, &#x60;FileType&#x60;, &#x60;FileSize&#x60;, &#x60;FileName&#x60;, &#x60;SSLCertificate&#x60;, &#x60;SSLCertificateID&#x60;, &#x60;SSLCertificateFingerprint&#x60;. | 
**uid** | **str** | Unique IOC identifier. | 
**value** | **str** | &#x60;Value&#x60; of the indicator. | 

## Example

```python
from titan_client.models.ioc_schema import IocSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IocSchema from a JSON string
ioc_schema_instance = IocSchema.from_json(json)
# print the JSON string representation of the object
print(IocSchema.to_json())

# convert the object into a dict
ioc_schema_dict = ioc_schema_instance.to_dict()
# create an instance of IocSchema from a dict
ioc_schema_from_dict = IocSchema.from_dict(ioc_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


