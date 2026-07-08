# IssueToCreateDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **int** |  | [optional] 
**project_key** | **str** |  | [optional] 
**issue_type_id** | **str** |  | [optional] 
**fields** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.issue_to_create_dto import IssueToCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of IssueToCreateDto from a JSON string
issue_to_create_dto_instance = IssueToCreateDto.from_json(json)
# print the JSON string representation of the object
print IssueToCreateDto.to_json()

# convert the object into a dict
issue_to_create_dto_dict = issue_to_create_dto_instance.to_dict()
# create an instance of IssueToCreateDto from a dict
issue_to_create_dto_from_dict = IssueToCreateDto.from_dict(issue_to_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


