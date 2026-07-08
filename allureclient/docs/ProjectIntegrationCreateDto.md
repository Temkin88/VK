# ProjectIntegrationCreateDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**integration_id** | **int** |  | 
**settings** | **object** |  | [optional] 
**secret** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.project_integration_create_dto import ProjectIntegrationCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIntegrationCreateDto from a JSON string
project_integration_create_dto_instance = ProjectIntegrationCreateDto.from_json(json)
# print the JSON string representation of the object
print ProjectIntegrationCreateDto.to_json()

# convert the object into a dict
project_integration_create_dto_dict = project_integration_create_dto_instance.to_dict()
# create an instance of ProjectIntegrationCreateDto from a dict
project_integration_create_dto_from_dict = ProjectIntegrationCreateDto.from_dict(project_integration_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


