# StatisticDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed** | **int** |  | [optional] 
**broken** | **int** |  | [optional] 
**passed** | **int** |  | [optional] 
**skipped** | **int** |  | [optional] 
**unknown** | **int** |  | [optional] 
**in_progress** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.statistic_dto import StatisticDto

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticDto from a JSON string
statistic_dto_instance = StatisticDto.from_json(json)
# print the JSON string representation of the object
print StatisticDto.to_json()

# convert the object into a dict
statistic_dto_dict = statistic_dto_instance.to_dict()
# create an instance of StatisticDto from a dict
statistic_dto_from_dict = StatisticDto.from_dict(statistic_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


