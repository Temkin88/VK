# TestCaseCloneRqDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_project_id** | **int** |  | [optional] 
**workflow_id** | **int** |  | [optional] 
**status_id** | **int** |  | [optional] 
**name_suffix** | **str** |  | [optional] 
**ignore_links** | **bool** |  | [optional] 
**ignore_cfv** | **bool** |  | [optional] 
**ignore_members** | **bool** |  | [optional] 
**ignore_tags** | **bool** |  | [optional] 
**ignore_test_keys** | **bool** |  | [optional] 
**ignore_issue_links** | **bool** |  | [optional] 
**ignore_parameters** | **bool** |  | [optional] 
**ignore_relations** | **bool** |  | [optional] 
**ignore_attachments** | **bool** |  | [optional] 
**ignore_scenario** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.test_case_clone_rq_dto import TestCaseCloneRqDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseCloneRqDto from a JSON string
test_case_clone_rq_dto_instance = TestCaseCloneRqDto.from_json(json)
# print the JSON string representation of the object
print TestCaseCloneRqDto.to_json()

# convert the object into a dict
test_case_clone_rq_dto_dict = test_case_clone_rq_dto_instance.to_dict()
# create an instance of TestCaseCloneRqDto from a dict
test_case_clone_rq_dto_from_dict = TestCaseCloneRqDto.from_dict(test_case_clone_rq_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


