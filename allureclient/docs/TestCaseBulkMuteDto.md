# TestCaseBulkMuteDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection** | [**TestCaseTreeSelectionDto**](TestCaseTreeSelectionDto.md) |  | 
**mute** | [**MuteDto**](MuteDto.md) |  | 

## Example

```python
from openapi_client.models.test_case_bulk_mute_dto import TestCaseBulkMuteDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseBulkMuteDto from a JSON string
test_case_bulk_mute_dto_instance = TestCaseBulkMuteDto.from_json(json)
# print the JSON string representation of the object
print TestCaseBulkMuteDto.to_json()

# convert the object into a dict
test_case_bulk_mute_dto_dict = test_case_bulk_mute_dto_instance.to_dict()
# create an instance of TestCaseBulkMuteDto from a dict
test_case_bulk_mute_dto_from_dict = TestCaseBulkMuteDto.from_dict(test_case_bulk_mute_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


