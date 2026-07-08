# IframeTestCaseWithIssueDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **int** |  | 
**issue_key** | **str** |  | 
**test_case_ids** | **List[int]** |  | 

## Example

```python
from openapi_client.models.iframe_test_case_with_issue_dto import IframeTestCaseWithIssueDto

# TODO update the JSON string below
json = "{}"
# create an instance of IframeTestCaseWithIssueDto from a JSON string
iframe_test_case_with_issue_dto_instance = IframeTestCaseWithIssueDto.from_json(json)
# print the JSON string representation of the object
print IframeTestCaseWithIssueDto.to_json()

# convert the object into a dict
iframe_test_case_with_issue_dto_dict = iframe_test_case_with_issue_dto_instance.to_dict()
# create an instance of IframeTestCaseWithIssueDto from a dict
iframe_test_case_with_issue_dto_from_dict = IframeTestCaseWithIssueDto.from_dict(iframe_test_case_with_issue_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


