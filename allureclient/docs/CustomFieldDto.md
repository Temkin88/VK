# CustomFieldDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.custom_field_dto import CustomFieldDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldDto from a JSON string
custom_field_dto_instance = CustomFieldDto.from_json(json)
# print the JSON string representation of the object
print CustomFieldDto.to_json()

# convert the object into a dict
custom_field_dto_dict = custom_field_dto_instance.to_dict()
# create an instance of CustomFieldDto from a dict
custom_field_dto_from_dict = CustomFieldDto.from_dict(custom_field_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


