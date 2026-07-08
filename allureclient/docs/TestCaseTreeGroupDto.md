# TestCaseTreeGroupDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**custom_field_id** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.test_case_tree_group_dto import TestCaseTreeGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseTreeGroupDto from a JSON string
test_case_tree_group_dto_instance = TestCaseTreeGroupDto.from_json(json)
# print the JSON string representation of the object
print TestCaseTreeGroupDto.to_json()

# convert the object into a dict
test_case_tree_group_dto_dict = test_case_tree_group_dto_instance.to_dict()
# create an instance of TestCaseTreeGroupDto from a dict
test_case_tree_group_dto_from_dict = TestCaseTreeGroupDto.from_dict(test_case_tree_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


