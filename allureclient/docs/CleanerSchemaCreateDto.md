# CleanerSchemaCreateDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**status** | [**TestStatus**](TestStatus.md) |  | 
**target** | [**CleanerSchemaTargetDto**](CleanerSchemaTargetDto.md) |  | 
**delay** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.cleaner_schema_create_dto import CleanerSchemaCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CleanerSchemaCreateDto from a JSON string
cleaner_schema_create_dto_instance = CleanerSchemaCreateDto.from_json(json)
# print the JSON string representation of the object
print CleanerSchemaCreateDto.to_json()

# convert the object into a dict
cleaner_schema_create_dto_dict = cleaner_schema_create_dto_instance.to_dict()
# create an instance of CleanerSchemaCreateDto from a dict
cleaner_schema_create_dto_from_dict = CleanerSchemaCreateDto.from_dict(cleaner_schema_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


