# CategoryMatcherDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**category** | [**CategoryDto**](CategoryDto.md) |  | [optional] 
**message_regex** | **str** |  | [optional] 
**trace_regex** | **str** |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.category_matcher_dto import CategoryMatcherDto

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryMatcherDto from a JSON string
category_matcher_dto_instance = CategoryMatcherDto.from_json(json)
# print the JSON string representation of the object
print CategoryMatcherDto.to_json()

# convert the object into a dict
category_matcher_dto_dict = category_matcher_dto_instance.to_dict()
# create an instance of CategoryMatcherDto from a dict
category_matcher_dto_from_dict = CategoryMatcherDto.from_dict(category_matcher_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


