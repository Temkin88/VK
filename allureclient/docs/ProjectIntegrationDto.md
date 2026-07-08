# ProjectIntegrationDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**info** | [**IntegrationInfoDto**](IntegrationInfoDto.md) |  | [optional] 
**disabled** | **bool** |  | [optional] 
**settings** | **object** |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.project_integration_dto import ProjectIntegrationDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIntegrationDto from a JSON string
project_integration_dto_instance = ProjectIntegrationDto.from_json(json)
# print the JSON string representation of the object
print ProjectIntegrationDto.to_json()

# convert the object into a dict
project_integration_dto_dict = project_integration_dto_instance.to_dict()
# create an instance of ProjectIntegrationDto from a dict
project_integration_dto_from_dict = ProjectIntegrationDto.from_dict(project_integration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


