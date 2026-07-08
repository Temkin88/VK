# TestCaseAttachmentPatchDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.test_case_attachment_patch_dto import TestCaseAttachmentPatchDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseAttachmentPatchDto from a JSON string
test_case_attachment_patch_dto_instance = TestCaseAttachmentPatchDto.from_json(json)
# print the JSON string representation of the object
print TestCaseAttachmentPatchDto.to_json()

# convert the object into a dict
test_case_attachment_patch_dto_dict = test_case_attachment_patch_dto_instance.to_dict()
# create an instance of TestCaseAttachmentPatchDto from a dict
test_case_attachment_patch_dto_from_dict = TestCaseAttachmentPatchDto.from_dict(test_case_attachment_patch_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


