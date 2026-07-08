# PageDefectCountRowDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[DefectCountRowDto]**](DefectCountRowDto.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObject**](SortObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**Pageable**](Pageable.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.page_defect_count_row_dto import PageDefectCountRowDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageDefectCountRowDto from a JSON string
page_defect_count_row_dto_instance = PageDefectCountRowDto.from_json(json)
# print the JSON string representation of the object
print PageDefectCountRowDto.to_json()

# convert the object into a dict
page_defect_count_row_dto_dict = page_defect_count_row_dto_instance.to_dict()
# create an instance of PageDefectCountRowDto from a dict
page_defect_count_row_dto_from_dict = PageDefectCountRowDto.from_dict(page_defect_count_row_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


