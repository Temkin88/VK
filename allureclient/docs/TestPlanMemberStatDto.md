# TestPlanMemberStatDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**test_cases_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.test_plan_member_stat_dto import TestPlanMemberStatDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanMemberStatDto from a JSON string
test_plan_member_stat_dto_instance = TestPlanMemberStatDto.from_json(json)
# print the JSON string representation of the object
print TestPlanMemberStatDto.to_json()

# convert the object into a dict
test_plan_member_stat_dto_dict = test_plan_member_stat_dto_instance.to_dict()
# create an instance of TestPlanMemberStatDto from a dict
test_plan_member_stat_dto_from_dict = TestPlanMemberStatDto.from_dict(test_plan_member_stat_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


