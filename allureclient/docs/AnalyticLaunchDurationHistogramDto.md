# AnalyticLaunchDurationHistogramDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **int** |  | [optional] 
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 
**passed_count** | **int** |  | [optional] 
**failed_count** | **int** |  | [optional] 
**broken_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.analytic_launch_duration_histogram_dto import AnalyticLaunchDurationHistogramDto

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticLaunchDurationHistogramDto from a JSON string
analytic_launch_duration_histogram_dto_instance = AnalyticLaunchDurationHistogramDto.from_json(json)
# print the JSON string representation of the object
print AnalyticLaunchDurationHistogramDto.to_json()

# convert the object into a dict
analytic_launch_duration_histogram_dto_dict = analytic_launch_duration_histogram_dto_instance.to_dict()
# create an instance of AnalyticLaunchDurationHistogramDto from a dict
analytic_launch_duration_histogram_dto_from_dict = AnalyticLaunchDurationHistogramDto.from_dict(analytic_launch_duration_histogram_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


