# WidgetDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**dashboard_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**WidgetTypeDto**](WidgetTypeDto.md) |  | [optional] 
**options** | [**WidgetCreateDtoOptions**](WidgetCreateDtoOptions.md) |  | [optional] 
**grid_pos** | [**GridPosDto**](GridPosDto.md) |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.widget_dto import WidgetDto

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetDto from a JSON string
widget_dto_instance = WidgetDto.from_json(json)
# print the JSON string representation of the object
print WidgetDto.to_json()

# convert the object into a dict
widget_dto_dict = widget_dto_instance.to_dict()
# create an instance of WidgetDto from a dict
widget_dto_from_dict = WidgetDto.from_dict(widget_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


