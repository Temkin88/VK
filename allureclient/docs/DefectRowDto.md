# DefectRowDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**closed** | **bool** |  | [optional] 
**issue** | [**IssueDto**](IssueDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.defect_row_dto import DefectRowDto

# TODO update the JSON string below
json = "{}"
# create an instance of DefectRowDto from a JSON string
defect_row_dto_instance = DefectRowDto.from_json(json)
# print the JSON string representation of the object
print DefectRowDto.to_json()

# convert the object into a dict
defect_row_dto_dict = defect_row_dto_instance.to_dict()
# create an instance of DefectRowDto from a dict
defect_row_dto_from_dict = DefectRowDto.from_dict(defect_row_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


