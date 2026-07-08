# ImportRequestDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**type** | [**ImportRequestTypeDto**](ImportRequestTypeDto.md) |  | [optional] 
**state** | [**ImportRequestStateDto**](ImportRequestStateDto.md) |  | [optional] 
**storage_key** | **str** |  | [optional] 
**original_file_name** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**content_length** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**count_imported** | **int** |  | [optional] 
**count_failed** | **int** |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.import_request_dto import ImportRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImportRequestDto from a JSON string
import_request_dto_instance = ImportRequestDto.from_json(json)
# print the JSON string representation of the object
print ImportRequestDto.to_json()

# convert the object into a dict
import_request_dto_dict = import_request_dto_instance.to_dict()
# create an instance of ImportRequestDto from a dict
import_request_dto_from_dict = ImportRequestDto.from_dict(import_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


