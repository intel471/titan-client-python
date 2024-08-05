# IndicatorSearchSchemaDataThreatData

Additional details about a threat such as service `provider`, `malware family`, `malware family version`, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** | Malware family: &#x60;gozi_isfb&#x60;, &#x60;smokeloader&#x60;, &#x60;trickbot&#x60; etc (for &#x60;malware&#x60; threat type). | [optional] 
**malware_family_profile_uid** | **str** | Malware family profile UID. | [optional] 
**variant** | **str** | Variant of the threat. | [optional] 
**version** | **str** | Version of the threat. | [optional] 

## Example

```python
from titan_client.models.indicator_search_schema_data_threat_data import IndicatorSearchSchemaDataThreatData

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorSearchSchemaDataThreatData from a JSON string
indicator_search_schema_data_threat_data_instance = IndicatorSearchSchemaDataThreatData.from_json(json)
# print the JSON string representation of the object
print(IndicatorSearchSchemaDataThreatData.to_json())

# convert the object into a dict
indicator_search_schema_data_threat_data_dict = indicator_search_schema_data_threat_data_instance.to_dict()
# create an instance of IndicatorSearchSchemaDataThreatData from a dict
indicator_search_schema_data_threat_data_from_dict = IndicatorSearchSchemaDataThreatData.from_dict(indicator_search_schema_data_threat_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


