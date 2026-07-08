# IntegrationCreateDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | [**IntegrationTypeDto**](IntegrationTypeDto.md) |  | 
**settings** | **object** |  | 
**default_project_settings** | **object** |  | [optional] 
**default_secret** | **object** |  | [optional] 
**enabled_by_default** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.integration_create_dto import IntegrationCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationCreateDto from a JSON string
integration_create_dto_instance = IntegrationCreateDto.from_json(json)
# print the JSON string representation of the object
print IntegrationCreateDto.to_json()

# convert the object into a dict
integration_create_dto_dict = integration_create_dto_instance.to_dict()
# create an instance of IntegrationCreateDto from a dict
integration_create_dto_from_dict = IntegrationCreateDto.from_dict(integration_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


