# LaunchCreateDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**name** | **str** |  | 
**external** | **bool** |  | [optional] 
**autoclose** | **bool** |  | [optional] 
**tags** | [**List[LaunchTagDto]**](LaunchTagDto.md) |  | [optional] 
**links** | [**List[ExternalLinkDto]**](ExternalLinkDto.md) |  | [optional] 
**issues** | [**List[IssueDto]**](IssueDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.launch_create_dto import LaunchCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LaunchCreateDto from a JSON string
launch_create_dto_instance = LaunchCreateDto.from_json(json)
# print the JSON string representation of the object
print LaunchCreateDto.to_json()

# convert the object into a dict
launch_create_dto_dict = launch_create_dto_instance.to_dict()
# create an instance of LaunchCreateDto from a dict
launch_create_dto_from_dict = LaunchCreateDto.from_dict(launch_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


