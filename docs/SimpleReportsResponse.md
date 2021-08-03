# SimpleReportsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_partial_result** | **bool** | Indicates whether response contains partial result. It could be in case when request took too long and was terminated by timeout. | [optional] 
**report_total_count** | **int** | Total count of matched reports. | 
**reports** | [**list[SimpleReportSchema]**](SimpleReportSchema.md) | List of Information Reports or Fintel Reports excluding researcherComments, rawText, rawTextTranslated fields. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


