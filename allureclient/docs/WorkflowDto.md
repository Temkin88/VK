# WorkflowDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**statuses** | [**List[StatusDto]**](StatusDto.md) |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.workflow_dto import WorkflowDto

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowDto from a JSON string
workflow_dto_instance = WorkflowDto.from_json(json)
# print the JSON string representation of the object
print WorkflowDto.to_json()

# convert the object into a dict
workflow_dto_dict = workflow_dto_instance.to_dict()
# create an instance of WorkflowDto from a dict
workflow_dto_from_dict = WorkflowDto.from_dict(workflow_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


