# TestCaseLastResultDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**test_result_id** | **int** |  | [optional] 
**status** | [**TestStatus**](TestStatus.md) |  | [optional] 
**var_date** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.test_case_last_result_dto import TestCaseLastResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseLastResultDto from a JSON string
test_case_last_result_dto_instance = TestCaseLastResultDto.from_json(json)
# print the JSON string representation of the object
print TestCaseLastResultDto.to_json()

# convert the object into a dict
test_case_last_result_dto_dict = test_case_last_result_dto_instance.to_dict()
# create an instance of TestCaseLastResultDto from a dict
test_case_last_result_dto_from_dict = TestCaseLastResultDto.from_dict(test_case_last_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


