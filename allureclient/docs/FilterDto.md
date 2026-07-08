# FilterDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**base** | **bool** |  | [optional] 
**shared** | **bool** |  | [optional] 
**editable** | **bool** |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.filter_dto import FilterDto

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDto from a JSON string
filter_dto_instance = FilterDto.from_json(json)
# print the JSON string representation of the object
print FilterDto.to_json()

# convert the object into a dict
filter_dto_dict = filter_dto_instance.to_dict()
# create an instance of FilterDto from a dict
filter_dto_from_dict = FilterDto.from_dict(filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


