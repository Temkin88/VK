# TestKeySchemaCreateDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**key** | **str** |  | 
**integration_id** | **int** |  | 

## Example

```python
from openapi_client.models.test_key_schema_create_dto import TestKeySchemaCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestKeySchemaCreateDto from a JSON string
test_key_schema_create_dto_instance = TestKeySchemaCreateDto.from_json(json)
# print the JSON string representation of the object
print TestKeySchemaCreateDto.to_json()

# convert the object into a dict
test_key_schema_create_dto_dict = test_key_schema_create_dto_instance.to_dict()
# create an instance of TestKeySchemaCreateDto from a dict
test_key_schema_create_dto_from_dict = TestKeySchemaCreateDto.from_dict(test_key_schema_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


