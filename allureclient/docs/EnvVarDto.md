# EnvVarDto



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
from openapi_client.models.env_var_dto import EnvVarDto

# TODO update the JSON string below
json = "{}"
# create an instance of EnvVarDto from a JSON string
env_var_dto_instance = EnvVarDto.from_json(json)
# print the JSON string representation of the object
print EnvVarDto.to_json()

# convert the object into a dict
env_var_dto_dict = env_var_dto_instance.to_dict()
# create an instance of EnvVarDto from a dict
env_var_dto_from_dict = EnvVarDto.from_dict(env_var_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


