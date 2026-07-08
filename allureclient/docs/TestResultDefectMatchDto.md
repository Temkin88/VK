# TestResultDefectMatchDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | [**TestStatus**](TestStatus.md) |  | [optional] 
**message** | **str** |  | [optional] 
**trace** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.test_result_defect_match_dto import TestResultDefectMatchDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultDefectMatchDto from a JSON string
test_result_defect_match_dto_instance = TestResultDefectMatchDto.from_json(json)
# print the JSON string representation of the object
print TestResultDefectMatchDto.to_json()

# convert the object into a dict
test_result_defect_match_dto_dict = test_result_defect_match_dto_instance.to_dict()
# create an instance of TestResultDefectMatchDto from a dict
test_result_defect_match_dto_from_dict = TestResultDefectMatchDto.from_dict(test_result_defect_match_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


