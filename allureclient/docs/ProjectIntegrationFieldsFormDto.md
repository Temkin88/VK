# ProjectIntegrationFieldsFormDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_fields** | [**List[GetFields200ResponseInner]**](GetFields200ResponseInner.md) |  | [optional] 
**project_fields_values** | **Dict[str, object]** |  | [optional] 
**default_project_fields_values** | **Dict[str, object]** |  | [optional] 
**secret_fields** | [**List[GetFields200ResponseInner]**](GetFields200ResponseInner.md) |  | [optional] 
**secret_specified** | **bool** |  | [optional] 
**default_secret_specified** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.project_integration_fields_form_dto import ProjectIntegrationFieldsFormDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIntegrationFieldsFormDto from a JSON string
project_integration_fields_form_dto_instance = ProjectIntegrationFieldsFormDto.from_json(json)
# print the JSON string representation of the object
print ProjectIntegrationFieldsFormDto.to_json()

# convert the object into a dict
project_integration_fields_form_dto_dict = project_integration_fields_form_dto_instance.to_dict()
# create an instance of ProjectIntegrationFieldsFormDto from a dict
project_integration_fields_form_dto_from_dict = ProjectIntegrationFieldsFormDto.from_dict(project_integration_fields_form_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


