# JobRunDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**stage** | [**JobRunStageDto**](JobRunStageDto.md) |  | [optional] 
**status** | [**JobRunStatusDto**](JobRunStatusDto.md) |  | [optional] 
**error_message** | **str** |  | [optional] 
**job** | [**JobInfoDto**](JobInfoDto.md) |  | [optional] 
**launch_id** | **int** |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.job_run_dto import JobRunDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobRunDto from a JSON string
job_run_dto_instance = JobRunDto.from_json(json)
# print the JSON string representation of the object
print JobRunDto.to_json()

# convert the object into a dict
job_run_dto_dict = job_run_dto_instance.to_dict()
# create an instance of JobRunDto from a dict
job_run_dto_from_dict = JobRunDto.from_dict(job_run_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


