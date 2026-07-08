# TestResultScenarioDtoAttachmentsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**content_length** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**entity** | **str** |  | 

## Example

```python
from openapi_client.models.test_result_scenario_dto_attachments_inner import TestResultScenarioDtoAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultScenarioDtoAttachmentsInner from a JSON string
test_result_scenario_dto_attachments_inner_instance = TestResultScenarioDtoAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print TestResultScenarioDtoAttachmentsInner.to_json()

# convert the object into a dict
test_result_scenario_dto_attachments_inner_dict = test_result_scenario_dto_attachments_inner_instance.to_dict()
# create an instance of TestResultScenarioDtoAttachmentsInner from a dict
test_result_scenario_dto_attachments_inner_from_dict = TestResultScenarioDtoAttachmentsInner.from_dict(test_result_scenario_dto_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


