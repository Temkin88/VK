# IframeBulkCreateTestCaseDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **int** |  | 
**issue_key** | **str** |  | 
**to_create** | [**List[TestCaseCreateDto]**](TestCaseCreateDto.md) |  | 

## Example

```python
from openapi_client.models.iframe_bulk_create_test_case_dto import IframeBulkCreateTestCaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of IframeBulkCreateTestCaseDto from a JSON string
iframe_bulk_create_test_case_dto_instance = IframeBulkCreateTestCaseDto.from_json(json)
# print the JSON string representation of the object
print IframeBulkCreateTestCaseDto.to_json()

# convert the object into a dict
iframe_bulk_create_test_case_dto_dict = iframe_bulk_create_test_case_dto_instance.to_dict()
# create an instance of IframeBulkCreateTestCaseDto from a dict
iframe_bulk_create_test_case_dto_from_dict = IframeBulkCreateTestCaseDto.from_dict(iframe_bulk_create_test_case_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


