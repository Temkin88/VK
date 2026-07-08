# TestCaseBulkCfvDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection** | [**TestCaseTreeSelectionDto**](TestCaseTreeSelectionDto.md) |  | 
**cfv** | [**List[CustomFieldValueDto]**](CustomFieldValueDto.md) |  | 

## Example

```python
from openapi_client.models.test_case_bulk_cfv_dto import TestCaseBulkCfvDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseBulkCfvDto from a JSON string
test_case_bulk_cfv_dto_instance = TestCaseBulkCfvDto.from_json(json)
# print the JSON string representation of the object
print TestCaseBulkCfvDto.to_json()

# convert the object into a dict
test_case_bulk_cfv_dto_dict = test_case_bulk_cfv_dto_instance.to_dict()
# create an instance of TestCaseBulkCfvDto from a dict
test_case_bulk_cfv_dto_from_dict = TestCaseBulkCfvDto.from_dict(test_case_bulk_cfv_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


