# TestCaseScenarioStepDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**keyword** | **str** |  | [optional] 
**expected_result** | **str** |  | [optional] 
**attachments** | [**List[TestCaseAttachmentRowDto]**](TestCaseAttachmentRowDto.md) |  | [optional] 
**steps** | [**List[TestCaseScenarioStepDto]**](TestCaseScenarioStepDto.md) |  | [optional] 
**leaf** | **bool** |  | [optional] [readonly] 
**steps_count** | **int** |  | [optional] [readonly] 
**has_content** | **bool** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.test_case_scenario_step_dto import TestCaseScenarioStepDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseScenarioStepDto from a JSON string
test_case_scenario_step_dto_instance = TestCaseScenarioStepDto.from_json(json)
# print the JSON string representation of the object
print TestCaseScenarioStepDto.to_json()

# convert the object into a dict
test_case_scenario_step_dto_dict = test_case_scenario_step_dto_instance.to_dict()
# create an instance of TestCaseScenarioStepDto from a dict
test_case_scenario_step_dto_from_dict = TestCaseScenarioStepDto.from_dict(test_case_scenario_step_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


