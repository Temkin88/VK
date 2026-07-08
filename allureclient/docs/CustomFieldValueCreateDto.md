# CustomFieldValueCreateDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**custom_field** | [**IdOnlyDto**](IdOnlyDto.md) |  | 

## Example

```python
from openapi_client.models.custom_field_value_create_dto import CustomFieldValueCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldValueCreateDto from a JSON string
custom_field_value_create_dto_instance = CustomFieldValueCreateDto.from_json(json)
# print the JSON string representation of the object
print CustomFieldValueCreateDto.to_json()

# convert the object into a dict
custom_field_value_create_dto_dict = custom_field_value_create_dto_instance.to_dict()
# create an instance of CustomFieldValueCreateDto from a dict
custom_field_value_create_dto_from_dict = CustomFieldValueCreateDto.from_dict(custom_field_value_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


