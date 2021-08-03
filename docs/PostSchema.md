# PostSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **int** | The &#x60;date&#x60; of the post. | 
**last_updated** | **int** | Last modification date. | [optional] 
**links** | [**PostSchemaLinks**](PostSchemaLinks.md) |  | 
**message** | **str** | HTML post content. If post message is translated, this parameter contains translated text, if not — original. [Markup explained](#forum-post-or-pm-markup). | 
**message_original** | **str** | Original HTML post content. This parameter is active if post message is translated. [Markup explained](#forum-post-or-pm-markup). | [optional] 
**uid** | **str** | Unique post identifier. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


