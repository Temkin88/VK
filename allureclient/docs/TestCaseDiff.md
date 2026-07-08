# TestCaseDiff



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | [**DiffValueChangeLong**](DiffValueChangeLong.md) |  | [optional] 
**name** | [**DiffValueChangeString**](DiffValueChangeString.md) |  | [optional] 
**automated** | [**DiffValueChangeBoolean**](DiffValueChangeBoolean.md) |  | [optional] 
**deleted** | [**DiffValueChangeBoolean**](DiffValueChangeBoolean.md) |  | [optional] 
**description** | [**DiffValueChangeString**](DiffValueChangeString.md) |  | [optional] 
**description_html** | [**DiffValueChangeString**](DiffValueChangeString.md) |  | [optional] 
**precondition** | [**DiffValueChangeString**](DiffValueChangeString.md) |  | [optional] 
**precondition_html** | [**DiffValueChangeString**](DiffValueChangeString.md) |  | [optional] 
**expected_result** | [**DiffValueChangeString**](DiffValueChangeString.md) |  | [optional] 
**expected_result_html** | [**DiffValueChangeString**](DiffValueChangeString.md) |  | [optional] 
**status_id** | [**DiffValueChangeLong**](DiffValueChangeLong.md) |  | [optional] 
**workflow_id** | [**DiffValueChangeLong**](DiffValueChangeLong.md) |  | [optional] 
**test_layer_id** | [**DiffValueChangeLong**](DiffValueChangeLong.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_case_diff import TestCaseDiff

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseDiff from a JSON string
test_case_diff_instance = TestCaseDiff.from_json(json)
# print the JSON string representation of the object
print TestCaseDiff.to_json()

# convert the object into a dict
test_case_diff_dict = test_case_diff_instance.to_dict()
# create an instance of TestCaseDiff from a dict
test_case_diff_from_dict = TestCaseDiff.from_dict(test_case_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


