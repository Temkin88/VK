# DefectOverviewDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**closed** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**description_html** | **str** |  | [optional] 
**last_found_date** | **int** |  | [optional] 
**last_found_launch** | [**IdAndNameOnlyDto**](IdAndNameOnlyDto.md) |  | [optional] 
**found_at_launch** | [**IdAndNameOnlyDto**](IdAndNameOnlyDto.md) |  | [optional] 
**issue** | [**IssueDto**](IssueDto.md) |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.defect_overview_dto import DefectOverviewDto

# TODO update the JSON string below
json = "{}"
# create an instance of DefectOverviewDto from a JSON string
defect_overview_dto_instance = DefectOverviewDto.from_json(json)
# print the JSON string representation of the object
print DefectOverviewDto.to_json()

# convert the object into a dict
defect_overview_dto_dict = defect_overview_dto_instance.to_dict()
# create an instance of DefectOverviewDto from a dict
defect_overview_dto_from_dict = DefectOverviewDto.from_dict(defect_overview_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


