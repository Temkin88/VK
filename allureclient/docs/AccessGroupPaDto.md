# AccessGroupPaDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**abbr** | **str** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**permission_set_id** | **int** |  | 

## Example

```python
from openapi_client.models.access_group_pa_dto import AccessGroupPaDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccessGroupPaDto from a JSON string
access_group_pa_dto_instance = AccessGroupPaDto.from_json(json)
# print the JSON string representation of the object
print AccessGroupPaDto.to_json()

# convert the object into a dict
access_group_pa_dto_dict = access_group_pa_dto_instance.to_dict()
# create an instance of AccessGroupPaDto from a dict
access_group_pa_dto_from_dict = AccessGroupPaDto.from_dict(access_group_pa_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


