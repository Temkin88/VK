# WidgetCreateDtoOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**launch_rql** | **str** |  | [optional] 
**type** | **str** |  | 
**body** | **str** |  | [optional] 
**tc_rql** | **str** |  | [optional] 
**group_by** | [**GroupBy**](GroupBy.md) |  | [optional] 
**include_in_progress_launches** | **bool** |  | [optional] 
**include_parameters** | **bool** |  | [optional] 
**tree_id** | **int** |  | 
**days_range** | **int** |  | [optional] 
**metric** | [**Metric**](Metric.md) |  | 
**interval** | [**AnalyticInterval**](AnalyticInterval.md) |  | [optional] 

## Example

```python
from openapi_client.models.widget_create_dto_options import WidgetCreateDtoOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetCreateDtoOptions from a JSON string
widget_create_dto_options_instance = WidgetCreateDtoOptions.from_json(json)
# print the JSON string representation of the object
print WidgetCreateDtoOptions.to_json()

# convert the object into a dict
widget_create_dto_options_dict = widget_create_dto_options_instance.to_dict()
# create an instance of WidgetCreateDtoOptions from a dict
widget_create_dto_options_from_dict = WidgetCreateDtoOptions.from_dict(widget_create_dto_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


