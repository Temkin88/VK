# IntegrationExportCreateDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **int** |  | 
**project_id** | **int** |  | 
**disabled** | **bool** |  | [optional] 
**disable_tc_create** | **bool** |  | [optional] 
**disable_launch_sync** | **bool** |  | [optional] 
**project_key** | **str** |  | [optional] 
**tc_aql** | **str** |  | [optional] 
**launch_aql** | **str** |  | [optional] 
**sync_delay_sec** | **int** |  | [optional] 
**settings** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.integration_export_create_dto import IntegrationExportCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationExportCreateDto from a JSON string
integration_export_create_dto_instance = IntegrationExportCreateDto.from_json(json)
# print the JSON string representation of the object
print IntegrationExportCreateDto.to_json()

# convert the object into a dict
integration_export_create_dto_dict = integration_export_create_dto_instance.to_dict()
# create an instance of IntegrationExportCreateDto from a dict
integration_export_create_dto_from_dict = IntegrationExportCreateDto.from_dict(integration_export_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


