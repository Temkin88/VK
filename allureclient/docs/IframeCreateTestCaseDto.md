# IframeCreateTestCaseDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **int** |  | 
**issue_key** | **str** |  | 
**to_create** | [**TestCaseCreateDto**](TestCaseCreateDto.md) |  | 

## Example

```python
from openapi_client.models.iframe_create_test_case_dto import IframeCreateTestCaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of IframeCreateTestCaseDto from a JSON string
iframe_create_test_case_dto_instance = IframeCreateTestCaseDto.from_json(json)
# print the JSON string representation of the object
print IframeCreateTestCaseDto.to_json()

# convert the object into a dict
iframe_create_test_case_dto_dict = iframe_create_test_case_dto_instance.to_dict()
# create an instance of IframeCreateTestCaseDto from a dict
iframe_create_test_case_dto_from_dict = IframeCreateTestCaseDto.from_dict(iframe_create_test_case_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


