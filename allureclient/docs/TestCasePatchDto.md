# TestCasePatchDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**precondition** | **str** |  | [optional] 
**expected_result** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**automated** | **bool** |  | [optional] 
**external** | **bool** |  | [optional] 
**test_layer_id** | **int** |  | [optional] 
**status_id** | **int** |  | [optional] 
**workflow_id** | **int** |  | [optional] 
**scenario** | [**TestCaseScenarioDto**](TestCaseScenarioDto.md) |  | [optional] 
**tags** | [**List[TestTagDto]**](TestTagDto.md) |  | [optional] 
**links** | [**List[ExternalLinkDto]**](ExternalLinkDto.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValueDto]**](CustomFieldValueDto.md) |  | [optional] 
**members** | [**List[MemberDto]**](MemberDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_case_patch_dto import TestCasePatchDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCasePatchDto from a JSON string
test_case_patch_dto_instance = TestCasePatchDto.from_json(json)
# print the JSON string representation of the object
print TestCasePatchDto.to_json()

# convert the object into a dict
test_case_patch_dto_dict = test_case_patch_dto_instance.to_dict()
# create an instance of TestCasePatchDto from a dict
test_case_patch_dto_from_dict = TestCasePatchDto.from_dict(test_case_patch_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


