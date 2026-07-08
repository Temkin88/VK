# PageJobDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[JobDto]**](JobDto.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObject**](SortObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**Pageable**](Pageable.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.page_job_dto import PageJobDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageJobDto from a JSON string
page_job_dto_instance = PageJobDto.from_json(json)
# print the JSON string representation of the object
print PageJobDto.to_json()

# convert the object into a dict
page_job_dto_dict = page_job_dto_instance.to_dict()
# create an instance of PageJobDto from a dict
page_job_dto_from_dict = PageJobDto.from_dict(page_job_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


