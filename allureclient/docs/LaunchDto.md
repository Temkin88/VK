# LaunchDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**closed** | **bool** |  | [optional] 
**external** | **bool** |  | [optional] 
**autoclose** | **bool** |  | [optional] 
**project_id** | **int** |  | [optional] 
**tags** | [**List[LaunchTagDto]**](LaunchTagDto.md) |  | [optional] 
**links** | [**List[ExternalLinkDto]**](ExternalLinkDto.md) |  | [optional] 
**issues** | [**List[IssueDto]**](IssueDto.md) |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.launch_dto import LaunchDto

# TODO update the JSON string below
json = "{}"
# create an instance of LaunchDto from a JSON string
launch_dto_instance = LaunchDto.from_json(json)
# print the JSON string representation of the object
print LaunchDto.to_json()

# convert the object into a dict
launch_dto_dict = launch_dto_instance.to_dict()
# create an instance of LaunchDto from a dict
launch_dto_from_dict = LaunchDto.from_dict(launch_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


