# LaunchCreateAndUploadDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**project_id** | **int** |  | 
**tags** | [**List[LaunchTagDto]**](LaunchTagDto.md) |  | [optional] 
**links** | [**List[ExternalLinkDto]**](ExternalLinkDto.md) |  | [optional] 
**issues** | [**List[IssueDto]**](IssueDto.md) |  | [optional] 
**env_var_values** | [**List[EnvVarValueDto]**](EnvVarValueDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.launch_create_and_upload_dto import LaunchCreateAndUploadDto

# TODO update the JSON string below
json = "{}"
# create an instance of LaunchCreateAndUploadDto from a JSON string
launch_create_and_upload_dto_instance = LaunchCreateAndUploadDto.from_json(json)
# print the JSON string representation of the object
print LaunchCreateAndUploadDto.to_json()

# convert the object into a dict
launch_create_and_upload_dto_dict = launch_create_and_upload_dto_instance.to_dict()
# create an instance of LaunchCreateAndUploadDto from a dict
launch_create_and_upload_dto_from_dict = LaunchCreateAndUploadDto.from_dict(launch_create_and_upload_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


