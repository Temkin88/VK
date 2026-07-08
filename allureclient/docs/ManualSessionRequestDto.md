# ManualSessionRequestDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**launch_id** | **int** |  | 
**environment** | [**List[SessionVariable]**](SessionVariable.md) |  | [optional] 

## Example

```python
from openapi_client.models.manual_session_request_dto import ManualSessionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ManualSessionRequestDto from a JSON string
manual_session_request_dto_instance = ManualSessionRequestDto.from_json(json)
# print the JSON string representation of the object
print ManualSessionRequestDto.to_json()

# convert the object into a dict
manual_session_request_dto_dict = manual_session_request_dto_instance.to_dict()
# create an instance of ManualSessionRequestDto from a dict
manual_session_request_dto_from_dict = ManualSessionRequestDto.from_dict(manual_session_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


