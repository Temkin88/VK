# ExternalRunStopRequestDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**job_uid** | **str** |  | 
**job_run_uid** | **str** |  | 
**status** | [**Status**](Status.md) |  | [optional] 

## Example

```python
from openapi_client.models.external_run_stop_request_dto import ExternalRunStopRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalRunStopRequestDto from a JSON string
external_run_stop_request_dto_instance = ExternalRunStopRequestDto.from_json(json)
# print the JSON string representation of the object
print ExternalRunStopRequestDto.to_json()

# convert the object into a dict
external_run_stop_request_dto_dict = external_run_stop_request_dto_instance.to_dict()
# create an instance of ExternalRunStopRequestDto from a dict
external_run_stop_request_dto_from_dict = ExternalRunStopRequestDto.from_dict(external_run_stop_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


