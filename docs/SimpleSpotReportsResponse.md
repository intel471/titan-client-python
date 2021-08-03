# SimpleSpotReportsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**spot_reports** | [**list[SimpleSpotReportSchema]**](SimpleSpotReportSchema.md) | List of &#x60;Spot reports&#x60;. | [optional] 
**spot_reports_total_count** | **int** | Total count of matched results. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


