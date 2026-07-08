# TestCaseAuditLogEntryDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**action_type** | [**AuditActionTypeDto**](AuditActionTypeDto.md) |  | [optional] 
**data** | [**List[TestCaseAuditLogData]**](TestCaseAuditLogData.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_case_audit_log_entry_dto import TestCaseAuditLogEntryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseAuditLogEntryDto from a JSON string
test_case_audit_log_entry_dto_instance = TestCaseAuditLogEntryDto.from_json(json)
# print the JSON string representation of the object
print TestCaseAuditLogEntryDto.to_json()

# convert the object into a dict
test_case_audit_log_entry_dto_dict = test_case_audit_log_entry_dto_instance.to_dict()
# create an instance of TestCaseAuditLogEntryDto from a dict
test_case_audit_log_entry_dto_from_dict = TestCaseAuditLogEntryDto.from_dict(test_case_audit_log_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


