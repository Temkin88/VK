# WidgetOptionsAnalyticGraph



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tc_rql** | **str** |  | [optional] 
**launch_rql** | **str** |  | [optional] 
**iterations** | **int** |  | [optional] 
**interval** | [**AnalyticInterval**](AnalyticInterval.md) |  | [optional] 
**metric** | **str** |  | 

## Example

```python
from openapi_client.models.widget_options_analytic_graph import WidgetOptionsAnalyticGraph

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetOptionsAnalyticGraph from a JSON string
widget_options_analytic_graph_instance = WidgetOptionsAnalyticGraph.from_json(json)
# print the JSON string representation of the object
print WidgetOptionsAnalyticGraph.to_json()

# convert the object into a dict
widget_options_analytic_graph_dict = widget_options_analytic_graph_instance.to_dict()
# create an instance of WidgetOptionsAnalyticGraph from a dict
widget_options_analytic_graph_from_dict = WidgetOptionsAnalyticGraph.from_dict(widget_options_analytic_graph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


