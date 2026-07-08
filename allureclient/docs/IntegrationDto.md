# IntegrationDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**info** | [**IntegrationInfoDto**](IntegrationInfoDto.md) |  | [optional] 
**projects_count** | **int** |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.integration_dto import IntegrationDto

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationDto from a JSON string
integration_dto_instance = IntegrationDto.from_json(json)
# print the JSON string representation of the object
print IntegrationDto.to_json()

# convert the object into a dict
integration_dto_dict = integration_dto_instance.to_dict()
# create an instance of IntegrationDto from a dict
integration_dto_from_dict = IntegrationDto.from_dict(integration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


