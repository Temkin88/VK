# TreeDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**fields** | [**List[CustomFieldDto]**](CustomFieldDto.md) |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tree_dto import TreeDto

# TODO update the JSON string below
json = "{}"
# create an instance of TreeDto from a JSON string
tree_dto_instance = TreeDto.from_json(json)
# print the JSON string representation of the object
print TreeDto.to_json()

# convert the object into a dict
tree_dto_dict = tree_dto_instance.to_dict()
# create an instance of TreeDto from a dict
tree_dto_from_dict = TreeDto.from_dict(tree_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


