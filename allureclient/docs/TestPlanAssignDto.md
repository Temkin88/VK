# TestPlanAssignDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection** | [**TestPlanTreeSelectionDto**](TestPlanTreeSelectionDto.md) |  | 
**username** | **str** |  | [optional] 
**job_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.test_plan_assign_dto import TestPlanAssignDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanAssignDto from a JSON string
test_plan_assign_dto_instance = TestPlanAssignDto.from_json(json)
# print the JSON string representation of the object
print TestPlanAssignDto.to_json()

# convert the object into a dict
test_plan_assign_dto_dict = test_plan_assign_dto_instance.to_dict()
# create an instance of TestPlanAssignDto from a dict
test_plan_assign_dto_from_dict = TestPlanAssignDto.from_dict(test_plan_assign_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


