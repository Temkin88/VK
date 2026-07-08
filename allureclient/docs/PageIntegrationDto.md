# PageIntegrationDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[IntegrationDto]**](IntegrationDto.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObject**](SortObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**Pageable**](Pageable.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.page_integration_dto import PageIntegrationDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageIntegrationDto from a JSON string
page_integration_dto_instance = PageIntegrationDto.from_json(json)
# print the JSON string representation of the object
print PageIntegrationDto.to_json()

# convert the object into a dict
page_integration_dto_dict = page_integration_dto_instance.to_dict()
# create an instance of PageIntegrationDto from a dict
page_integration_dto_from_dict = PageIntegrationDto.from_dict(page_integration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


