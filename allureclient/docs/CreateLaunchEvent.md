# CreateLaunchEvent



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**name** | **str** |  | 
**autoclose** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.create_launch_event import CreateLaunchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLaunchEvent from a JSON string
create_launch_event_instance = CreateLaunchEvent.from_json(json)
# print the JSON string representation of the object
print CreateLaunchEvent.to_json()

# convert the object into a dict
create_launch_event_dict = create_launch_event_instance.to_dict()
# create an instance of CreateLaunchEvent from a dict
create_launch_event_from_dict = CreateLaunchEvent.from_dict(create_launch_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


