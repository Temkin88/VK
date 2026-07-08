# RoleDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.role_dto import RoleDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoleDto from a JSON string
role_dto_instance = RoleDto.from_json(json)
# print the JSON string representation of the object
print RoleDto.to_json()

# convert the object into a dict
role_dto_dict = role_dto_instance.to_dict()
# create an instance of RoleDto from a dict
role_dto_from_dict = RoleDto.from_dict(role_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


