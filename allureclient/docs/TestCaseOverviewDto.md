# TestCaseOverviewDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_html** | **str** |  | [optional] 
**precondition** | **str** |  | [optional] 
**precondition_html** | **str** |  | [optional] 
**expected_result** | **str** |  | [optional] 
**expected_result_html** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**editable** | **bool** |  | [optional] 
**automated** | **bool** |  | [optional] 
**external** | **bool** |  | [optional] 
**style** | [**TestCaseStyle**](TestCaseStyle.md) |  | [optional] 
**scenario** | [**TestCaseScenarioDto**](TestCaseScenarioDto.md) |  | [optional] 
**status** | [**StatusDto**](StatusDto.md) |  | [optional] 
**workflow** | [**WorkflowDto**](WorkflowDto.md) |  | [optional] 
**layer** | [**TestLayerDto**](TestLayerDto.md) |  | [optional] 
**tags** | [**List[TestTagDto]**](TestTagDto.md) |  | [optional] 
**links** | [**List[ExternalLinkDto]**](ExternalLinkDto.md) |  | [optional] 
**issues** | [**List[IssueDto]**](IssueDto.md) |  | [optional] 
**test_keys** | [**List[TestKeyDto]**](TestKeyDto.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValueDto]**](CustomFieldValueDto.md) |  | [optional] 
**members** | [**List[MemberDto]**](MemberDto.md) |  | [optional] 
**parameters** | [**List[TestCaseParameterDto]**](TestCaseParameterDto.md) |  | [optional] 
**examples** | [**List[TestCaseExampleDto]**](TestCaseExampleDto.md) |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.test_case_overview_dto import TestCaseOverviewDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseOverviewDto from a JSON string
test_case_overview_dto_instance = TestCaseOverviewDto.from_json(json)
# print the JSON string representation of the object
print TestCaseOverviewDto.to_json()

# convert the object into a dict
test_case_overview_dto_dict = test_case_overview_dto_instance.to_dict()
# create an instance of TestCaseOverviewDto from a dict
test_case_overview_dto_from_dict = TestCaseOverviewDto.from_dict(test_case_overview_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


