# DefectCreateDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**issue** | [**IssueToCreateDto**](IssueToCreateDto.md) |  | [optional] 
**link_issue** | [**DefectIssueLinkDto**](DefectIssueLinkDto.md) |  | [optional] 
**matcher** | [**Matcher**](Matcher.md) |  | [optional] 

## Example

```python
from openapi_client.models.defect_create_dto import DefectCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DefectCreateDto from a JSON string
defect_create_dto_instance = DefectCreateDto.from_json(json)
# print the JSON string representation of the object
print DefectCreateDto.to_json()

# convert the object into a dict
defect_create_dto_dict = defect_create_dto_instance.to_dict()
# create an instance of DefectCreateDto from a dict
defect_create_dto_from_dict = DefectCreateDto.from_dict(defect_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


