# AnalyticAutomationTrendDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** |  | [optional] 
**automated_count** | **int** |  | [optional] 
**manual_count** | **int** |  | [optional] 
**sum_duration_automated** | **int** |  | [optional] 
**sum_duration_manual** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.analytic_automation_trend_dto import AnalyticAutomationTrendDto

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticAutomationTrendDto from a JSON string
analytic_automation_trend_dto_instance = AnalyticAutomationTrendDto.from_json(json)
# print the JSON string representation of the object
print AnalyticAutomationTrendDto.to_json()

# convert the object into a dict
analytic_automation_trend_dto_dict = analytic_automation_trend_dto_instance.to_dict()
# create an instance of AnalyticAutomationTrendDto from a dict
analytic_automation_trend_dto_from_dict = AnalyticAutomationTrendDto.from_dict(analytic_automation_trend_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


