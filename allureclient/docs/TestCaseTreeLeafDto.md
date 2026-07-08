# TestCaseTreeLeafDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**automated** | **bool** |  | [optional] 
**external** | **bool** |  | [optional] 
**created_date** | **int** |  | [optional] 
**status_name** | **str** |  | [optional] 
**status_color** | **str** |  | [optional] 
**layer_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.test_case_tree_leaf_dto import TestCaseTreeLeafDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseTreeLeafDto from a JSON string
test_case_tree_leaf_dto_instance = TestCaseTreeLeafDto.from_json(json)
# print the JSON string representation of the object
print TestCaseTreeLeafDto.to_json()

# convert the object into a dict
test_case_tree_leaf_dto_dict = test_case_tree_leaf_dto_instance.to_dict()
# create an instance of TestCaseTreeLeafDto from a dict
test_case_tree_leaf_dto_from_dict = TestCaseTreeLeafDto.from_dict(test_case_tree_leaf_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


