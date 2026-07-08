# TestFixtureResultDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | [**TestFixtureResultTypeDto**](TestFixtureResultTypeDto.md) |  | [optional] 
**name** | **str** |  | [optional] 
**start** | **int** |  | [optional] 
**stop** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**status** | [**TestStatus**](TestStatus.md) |  | [optional] 
**message** | **str** |  | [optional] 
**trace** | **str** |  | [optional] 
**scenario** | [**TestResultScenarioDto**](TestResultScenarioDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_fixture_result_dto import TestFixtureResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestFixtureResultDto from a JSON string
test_fixture_result_dto_instance = TestFixtureResultDto.from_json(json)
# print the JSON string representation of the object
print TestFixtureResultDto.to_json()

# convert the object into a dict
test_fixture_result_dto_dict = test_fixture_result_dto_instance.to_dict()
# create an instance of TestFixtureResultDto from a dict
test_fixture_result_dto_from_dict = TestFixtureResultDto.from_dict(test_fixture_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


