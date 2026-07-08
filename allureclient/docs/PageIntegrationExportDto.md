# PageIntegrationExportDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[IntegrationExportDto]**](IntegrationExportDto.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObject**](SortObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**Pageable**](Pageable.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.page_integration_export_dto import PageIntegrationExportDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageIntegrationExportDto from a JSON string
page_integration_export_dto_instance = PageIntegrationExportDto.from_json(json)
# print the JSON string representation of the object
print PageIntegrationExportDto.to_json()

# convert the object into a dict
page_integration_export_dto_dict = page_integration_export_dto_instance.to_dict()
# create an instance of PageIntegrationExportDto from a dict
page_integration_export_dto_from_dict = PageIntegrationExportDto.from_dict(page_integration_export_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


