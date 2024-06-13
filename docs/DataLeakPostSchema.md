# DataLeakPostSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_number** | **int** | Data leak post file listing search terms chunk number in which search term was found. File listing search terms related to specific post are stored as chunks. | [optional] 
**date** | **int** | The &#x60;date&#x60; of the data leak post. | 
**file_listing** | [**DataLeakPostSchemaFileListing**](DataLeakPostSchemaFileListing.md) |  | [optional] 
**last_updated** | **int** | Last modification date. | [optional] 
**links** | [**DataLeakPostSchemaLinks**](DataLeakPostSchemaLinks.md) |  | 
**message** | **str** | HTML data leak post content. | 
**uid** | **str** | Unique data leak post identifier. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


