# IntegrationValidateDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**IntegrationTypeDto**](IntegrationTypeDto.md) |  | 
**settings** | **object** |  | [optional] 
**default_project_settings** | **object** |  | [optional] 
**default_secret** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.integration_validate_dto import IntegrationValidateDto

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationValidateDto from a JSON string
integration_validate_dto_instance = IntegrationValidateDto.from_json(json)
# print the JSON string representation of the object
print IntegrationValidateDto.to_json()

# convert the object into a dict
integration_validate_dto_dict = integration_validate_dto_instance.to_dict()
# create an instance of IntegrationValidateDto from a dict
integration_validate_dto_from_dict = IntegrationValidateDto.from_dict(integration_validate_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


