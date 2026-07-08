# TestResultTreeLeafDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | [**TestStatus**](TestStatus.md) |  | [optional] 
**start** | **int** |  | [optional] 
**stop** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**flaky** | **bool** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**manual** | **bool** |  | [optional] 
**assignee** | **str** |  | [optional] 
**tested_by** | **str** |  | [optional] 
**layer_name** | **str** |  | [optional] 
**test_case_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.test_result_tree_leaf_dto import TestResultTreeLeafDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultTreeLeafDto from a JSON string
test_result_tree_leaf_dto_instance = TestResultTreeLeafDto.from_json(json)
# print the JSON string representation of the object
print TestResultTreeLeafDto.to_json()

# convert the object into a dict
test_result_tree_leaf_dto_dict = test_result_tree_leaf_dto_instance.to_dict()
# create an instance of TestResultTreeLeafDto from a dict
test_result_tree_leaf_dto_from_dict = TestResultTreeLeafDto.from_dict(test_result_tree_leaf_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


