# ProjectStatsDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_test_cases** | **int** |  | [optional] 
**automated_test_cases** | **int** |  | [optional] 
**launches** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.project_stats_dto import ProjectStatsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatsDto from a JSON string
project_stats_dto_instance = ProjectStatsDto.from_json(json)
# print the JSON string representation of the object
print ProjectStatsDto.to_json()

# convert the object into a dict
project_stats_dto_dict = project_stats_dto_instance.to_dict()
# create an instance of ProjectStatsDto from a dict
project_stats_dto_from_dict = ProjectStatsDto.from_dict(project_stats_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


