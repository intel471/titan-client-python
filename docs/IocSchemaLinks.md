# IocSchemaLinks

Linked data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_total_count** | **int** | Total count of linked actors. | 
**actors** | [**List[IocSchemaLinksActorsInner]**](IocSchemaLinksActorsInner.md) | List of &#x60;Actors&#x60; &lt;br /&gt;&#x60;Array&#x60; of simple &#x60;Actor&#x60;. Contains only &#x60;uid&#x60;, &#x60;handles&#x60; from [Actors](). | [optional] 
**report_total_count** | **int** | Total count of linked reports. | 
**reports** | [**List[IocSchemaLinksReportsInner]**](IocSchemaLinksReportsInner.md) | Linked &#x60;reports&#x60; Array of simplified version of one of the following: &#x60;Information Report&#x60;, &#x60;Fintel Report&#x60;, &#x60;Malware Report&#x60;, &#x60;Spot Report&#x60;, &#x60;Situation Report&#x60;, &#x60;Breach Alert&#x60;. | [optional] 

## Example

```python
from titan_client.models.ioc_schema_links import IocSchemaLinks

# TODO update the JSON string below
json = "{}"
# create an instance of IocSchemaLinks from a JSON string
ioc_schema_links_instance = IocSchemaLinks.from_json(json)
# print the JSON string representation of the object
print(IocSchemaLinks.to_json())

# convert the object into a dict
ioc_schema_links_dict = ioc_schema_links_instance.to_dict()
# create an instance of IocSchemaLinks from a dict
ioc_schema_links_from_dict = IocSchemaLinks.from_dict(ioc_schema_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


