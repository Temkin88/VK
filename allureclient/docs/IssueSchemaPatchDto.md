# IssueSchemaPatchDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**integration_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.issue_schema_patch_dto import IssueSchemaPatchDto

# TODO update the JSON string below
json = "{}"
# create an instance of IssueSchemaPatchDto from a JSON string
issue_schema_patch_dto_instance = IssueSchemaPatchDto.from_json(json)
# print the JSON string representation of the object
print IssueSchemaPatchDto.to_json()

# convert the object into a dict
issue_schema_patch_dto_dict = issue_schema_patch_dto_instance.to_dict()
# create an instance of IssueSchemaPatchDto from a dict
issue_schema_patch_dto_from_dict = IssueSchemaPatchDto.from_dict(issue_schema_patch_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


