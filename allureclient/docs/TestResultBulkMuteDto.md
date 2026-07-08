# TestResultBulkMuteDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection** | [**TestResultTreeSelectionDto**](TestResultTreeSelectionDto.md) |  | 
**name** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**issues** | [**List[IssueDto]**](IssueDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_result_bulk_mute_dto import TestResultBulkMuteDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultBulkMuteDto from a JSON string
test_result_bulk_mute_dto_instance = TestResultBulkMuteDto.from_json(json)
# print the JSON string representation of the object
print TestResultBulkMuteDto.to_json()

# convert the object into a dict
test_result_bulk_mute_dto_dict = test_result_bulk_mute_dto_instance.to_dict()
# create an instance of TestResultBulkMuteDto from a dict
test_result_bulk_mute_dto_from_dict = TestResultBulkMuteDto.from_dict(test_result_bulk_mute_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


