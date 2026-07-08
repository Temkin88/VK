# LaunchPreviewDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**statistic** | [**List[TestStatusCount]**](TestStatusCount.md) |  | [optional] 
**tags** | [**List[LaunchTagDto]**](LaunchTagDto.md) |  | [optional] 
**issues** | [**List[IssueDto]**](IssueDto.md) |  | [optional] 
**links** | [**List[ExternalLinkDto]**](ExternalLinkDto.md) |  | [optional] 
**environment** | [**List[EnvVarValueDto]**](EnvVarValueDto.md) |  | [optional] 
**jobs** | [**List[JobRunDto]**](JobRunDto.md) |  | [optional] 
**closed** | **bool** |  | [optional] 
**external** | **bool** |  | [optional] 
**new_defects_count** | **int** |  | [optional] 
**known_defects_count** | **int** |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.launch_preview_dto import LaunchPreviewDto

# TODO update the JSON string below
json = "{}"
# create an instance of LaunchPreviewDto from a JSON string
launch_preview_dto_instance = LaunchPreviewDto.from_json(json)
# print the JSON string representation of the object
print LaunchPreviewDto.to_json()

# convert the object into a dict
launch_preview_dto_dict = launch_preview_dto_instance.to_dict()
# create an instance of LaunchPreviewDto from a dict
launch_preview_dto_from_dict = LaunchPreviewDto.from_dict(launch_preview_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


