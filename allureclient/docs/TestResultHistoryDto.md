# TestResultHistoryDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**launch** | [**IdAndNameOnlyDto**](IdAndNameOnlyDto.md) |  | [optional] 
**start** | **int** |  | [optional] 
**stop** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**status** | [**TestStatus**](TestStatus.md) |  | [optional] 
**message** | **str** |  | [optional] 
**trace** | **str** |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**parameters** | [**List[TestResultParameterDto]**](TestResultParameterDto.md) |  | [optional] 
**environment** | [**List[EnvVarValueDto]**](EnvVarValueDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_result_history_dto import TestResultHistoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultHistoryDto from a JSON string
test_result_history_dto_instance = TestResultHistoryDto.from_json(json)
# print the JSON string representation of the object
print TestResultHistoryDto.to_json()

# convert the object into a dict
test_result_history_dto_dict = test_result_history_dto_instance.to_dict()
# create an instance of TestResultHistoryDto from a dict
test_result_history_dto_from_dict = TestResultHistoryDto.from_dict(test_result_history_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


