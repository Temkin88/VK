# TestResultLeafNode



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_uid** | **str** |  | [optional] 
**status** | [**TestStatus**](TestStatus.md) |  | [optional] 
**start** | **int** |  | [optional] 
**stop** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**flaky** | **bool** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**muted** | **bool** |  | [optional] 
**assignee** | **str** |  | [optional] 
**tested_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.test_result_leaf_node import TestResultLeafNode

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultLeafNode from a JSON string
test_result_leaf_node_instance = TestResultLeafNode.from_json(json)
# print the JSON string representation of the object
print TestResultLeafNode.to_json()

# convert the object into a dict
test_result_leaf_node_dict = test_result_leaf_node_instance.to_dict()
# create an instance of TestResultLeafNode from a dict
test_result_leaf_node_from_dict = TestResultLeafNode.from_dict(test_result_leaf_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


