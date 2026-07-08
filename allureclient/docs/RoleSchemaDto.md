# RoleSchemaDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**role** | [**RoleDto**](RoleDto.md) |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.role_schema_dto import RoleSchemaDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoleSchemaDto from a JSON string
role_schema_dto_instance = RoleSchemaDto.from_json(json)
# print the JSON string representation of the object
print RoleSchemaDto.to_json()

# convert the object into a dict
role_schema_dto_dict = role_schema_dto_instance.to_dict()
# create an instance of RoleSchemaDto from a dict
role_schema_dto_from_dict = RoleSchemaDto.from_dict(role_schema_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


