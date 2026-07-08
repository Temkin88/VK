# TestCaseScenarioDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_result_id** | **int** |  | [optional] 
**attachments** | [**List[TestCaseAttachmentRowDto]**](TestCaseAttachmentRowDto.md) |  | [optional] 
**steps** | [**List[TestCaseScenarioStepDto]**](TestCaseScenarioStepDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_case_scenario_dto import TestCaseScenarioDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseScenarioDto from a JSON string
test_case_scenario_dto_instance = TestCaseScenarioDto.from_json(json)
# print the JSON string representation of the object
print TestCaseScenarioDto.to_json()

# convert the object into a dict
test_case_scenario_dto_dict = test_case_scenario_dto_instance.to_dict()
# create an instance of TestCaseScenarioDto from a dict
test_case_scenario_dto_from_dict = TestCaseScenarioDto.from_dict(test_case_scenario_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


