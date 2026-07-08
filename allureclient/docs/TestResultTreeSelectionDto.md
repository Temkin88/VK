# TestResultTreeSelectionDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverted** | **bool** |  | [optional] 
**groups_include** | **List[List[int]]** |  | [optional] 
**groups_exclude** | **List[List[int]]** |  | [optional] 
**leafs_include** | **List[int]** |  | [optional] 
**leafs_exclude** | **List[int]** |  | [optional] 
**path** | **List[int]** |  | [optional] 
**launch_id** | **int** |  | [optional] 
**tree_id** | **int** |  | [optional] 
**search** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.test_result_tree_selection_dto import TestResultTreeSelectionDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultTreeSelectionDto from a JSON string
test_result_tree_selection_dto_instance = TestResultTreeSelectionDto.from_json(json)
# print the JSON string representation of the object
print TestResultTreeSelectionDto.to_json()

# convert the object into a dict
test_result_tree_selection_dto_dict = test_result_tree_selection_dto_instance.to_dict()
# create an instance of TestResultTreeSelectionDto from a dict
test_result_tree_selection_dto_from_dict = TestResultTreeSelectionDto.from_dict(test_result_tree_selection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


