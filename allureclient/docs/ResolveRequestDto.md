# ResolveRequestDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TestStatus**](TestStatus.md) |  | 
**message** | **str** |  | [optional] 
**trace** | **str** |  | [optional] 
**start** | **int** |  | [optional] 
**stop** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**execution** | [**TestResultScenarioDto**](TestResultScenarioDto.md) |  | [optional] 
**category_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.resolve_request_dto import ResolveRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveRequestDto from a JSON string
resolve_request_dto_instance = ResolveRequestDto.from_json(json)
# print the JSON string representation of the object
print ResolveRequestDto.to_json()

# convert the object into a dict
resolve_request_dto_dict = resolve_request_dto_instance.to_dict()
# create an instance of ResolveRequestDto from a dict
resolve_request_dto_from_dict = ResolveRequestDto.from_dict(resolve_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


