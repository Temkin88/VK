# TestResultTree



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**shown** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**context** | [**GroupNodeContext**](GroupNodeContext.md) |  | [optional] 
**groups** | [**List[TestResultGroupNode]**](TestResultGroupNode.md) |  | [optional] 
**uid** | **str** |  | [optional] 
**leafs** | [**List[TestResultLeafNode]**](TestResultLeafNode.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_result_tree import TestResultTree

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultTree from a JSON string
test_result_tree_instance = TestResultTree.from_json(json)
# print the JSON string representation of the object
print TestResultTree.to_json()

# convert the object into a dict
test_result_tree_dict = test_result_tree_instance.to_dict()
# create an instance of TestResultTree from a dict
test_result_tree_from_dict = TestResultTree.from_dict(test_result_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


