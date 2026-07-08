# TestCaseBulkExternalLinkDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection** | [**TestCaseTreeSelectionDto**](TestCaseTreeSelectionDto.md) |  | 
**links** | [**List[ExternalLinkDto]**](ExternalLinkDto.md) |  | 

## Example

```python
from openapi_client.models.test_case_bulk_external_link_dto import TestCaseBulkExternalLinkDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseBulkExternalLinkDto from a JSON string
test_case_bulk_external_link_dto_instance = TestCaseBulkExternalLinkDto.from_json(json)
# print the JSON string representation of the object
print TestCaseBulkExternalLinkDto.to_json()

# convert the object into a dict
test_case_bulk_external_link_dto_dict = test_case_bulk_external_link_dto_instance.to_dict()
# create an instance of TestCaseBulkExternalLinkDto from a dict
test_case_bulk_external_link_dto_from_dict = TestCaseBulkExternalLinkDto.from_dict(test_case_bulk_external_link_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


