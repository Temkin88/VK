# IntegrationFieldsFormDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_fields** | [**List[GetFields200ResponseInner]**](GetFields200ResponseInner.md) |  | [optional] 
**global_fields_values** | **Dict[str, object]** |  | [optional] 
**default_project_fields** | [**List[GetFields200ResponseInner]**](GetFields200ResponseInner.md) |  | [optional] 
**default_project_fields_values** | **Dict[str, object]** |  | [optional] 
**default_secret_fields** | [**List[GetFields200ResponseInner]**](GetFields200ResponseInner.md) |  | [optional] 
**default_secret_specified** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.integration_fields_form_dto import IntegrationFieldsFormDto

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationFieldsFormDto from a JSON string
integration_fields_form_dto_instance = IntegrationFieldsFormDto.from_json(json)
# print the JSON string representation of the object
print IntegrationFieldsFormDto.to_json()

# convert the object into a dict
integration_fields_form_dto_dict = integration_fields_form_dto_instance.to_dict()
# create an instance of IntegrationFieldsFormDto from a dict
integration_fields_form_dto_from_dict = IntegrationFieldsFormDto.from_dict(integration_fields_form_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


