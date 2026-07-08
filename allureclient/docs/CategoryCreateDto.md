# CategoryCreateDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | 
**color** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.category_create_dto import CategoryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryCreateDto from a JSON string
category_create_dto_instance = CategoryCreateDto.from_json(json)
# print the JSON string representation of the object
print CategoryCreateDto.to_json()

# convert the object into a dict
category_create_dto_dict = category_create_dto_instance.to_dict()
# create an instance of CategoryCreateDto from a dict
category_create_dto_from_dict = CategoryCreateDto.from_dict(category_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


