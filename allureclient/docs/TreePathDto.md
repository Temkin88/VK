# TreePathDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**tree_id** | **int** |  | [optional] 
**items** | [**List[TreePathItemDto]**](TreePathItemDto.md) |  | [optional] 
**favorite** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.tree_path_dto import TreePathDto

# TODO update the JSON string below
json = "{}"
# create an instance of TreePathDto from a JSON string
tree_path_dto_instance = TreePathDto.from_json(json)
# print the JSON string representation of the object
print TreePathDto.to_json()

# convert the object into a dict
tree_path_dto_dict = tree_path_dto_instance.to_dict()
# create an instance of TreePathDto from a dict
tree_path_dto_from_dict = TreePathDto.from_dict(tree_path_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


