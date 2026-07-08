# PageCustomFieldSchemaDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[CustomFieldSchemaDto]**](CustomFieldSchemaDto.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObject**](SortObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**Pageable**](Pageable.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.page_custom_field_schema_dto import PageCustomFieldSchemaDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageCustomFieldSchemaDto from a JSON string
page_custom_field_schema_dto_instance = PageCustomFieldSchemaDto.from_json(json)
# print the JSON string representation of the object
print PageCustomFieldSchemaDto.to_json()

# convert the object into a dict
page_custom_field_schema_dto_dict = page_custom_field_schema_dto_instance.to_dict()
# create an instance of PageCustomFieldSchemaDto from a dict
page_custom_field_schema_dto_from_dict = PageCustomFieldSchemaDto.from_dict(page_custom_field_schema_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


