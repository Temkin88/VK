# TestResultCreateDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**launch_id** | **int** |  | 
**test_case_id** | **int** |  | [optional] 
**name** | **str** |  | 
**full_name** | **str** |  | [optional] 
**status** | [**TestStatus**](TestStatus.md) |  | 
**message** | **str** |  | [optional] 
**trace** | **str** |  | [optional] 
**start** | **int** |  | [optional] 
**stop** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**precondition** | **str** |  | [optional] 
**expected_result** | **str** |  | [optional] 
**manual** | **bool** |  | [optional] 
**external** | **bool** |  | [optional] 
**test_layer_id** | **int** |  | [optional] 
**scenario** | [**TestResultScenarioDto**](TestResultScenarioDto.md) |  | [optional] 
**tags** | [**List[TestTagDto]**](TestTagDto.md) |  | [optional] 
**links** | [**List[ExternalLinkDto]**](ExternalLinkDto.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValueDto]**](CustomFieldValueDto.md) |  | [optional] 
**members** | [**List[MemberDto]**](MemberDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_result_create_dto import TestResultCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultCreateDto from a JSON string
test_result_create_dto_instance = TestResultCreateDto.from_json(json)
# print the JSON string representation of the object
print TestResultCreateDto.to_json()

# convert the object into a dict
test_result_create_dto_dict = test_result_create_dto_instance.to_dict()
# create an instance of TestResultCreateDto from a dict
test_result_create_dto_from_dict = TestResultCreateDto.from_dict(test_result_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


