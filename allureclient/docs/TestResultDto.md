# TestResultDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**launch_id** | **int** |  | [optional] 
**test_case_id** | **int** |  | [optional] 
**history_key** | **str** |  | [optional] 
**scenario_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_html** | **str** |  | [optional] 
**precondition** | **str** |  | [optional] 
**precondition_html** | **str** |  | [optional] 
**expected_result** | **str** |  | [optional] 
**expected_result_html** | **str** |  | [optional] 
**start** | **int** |  | [optional] 
**stop** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**status** | [**TestStatus**](TestStatus.md) |  | [optional] 
**layer** | [**TestLayerDto**](TestLayerDto.md) |  | [optional] 
**category** | [**CategoryDto**](CategoryDto.md) |  | [optional] 
**message** | **str** |  | [optional] 
**trace** | **str** |  | [optional] 
**external** | **bool** |  | [optional] 
**manual** | **bool** |  | [optional] 
**assignee** | **str** |  | [optional] 
**tested_by** | **str** |  | [optional] 
**job_run** | [**JobRunDto**](JobRunDto.md) |  | [optional] 
**host_id** | **str** |  | [optional] 
**thread_id** | **str** |  | [optional] 
**flaky** | **bool** |  | [optional] 
**muted** | **bool** |  | [optional] 
**known** | **bool** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**retried_by** | [**IdAndNameOnlyDto**](IdAndNameOnlyDto.md) |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**parameters** | [**List[TestResultParameterDto]**](TestResultParameterDto.md) |  | [optional] 
**tags** | [**List[TestTagDto]**](TestTagDto.md) |  | [optional] 
**links** | [**List[ExternalLinkDto]**](ExternalLinkDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_result_dto import TestResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultDto from a JSON string
test_result_dto_instance = TestResultDto.from_json(json)
# print the JSON string representation of the object
print TestResultDto.to_json()

# convert the object into a dict
test_result_dto_dict = test_result_dto_instance.to_dict()
# create an instance of TestResultDto from a dict
test_result_dto_from_dict = TestResultDto.from_dict(test_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


