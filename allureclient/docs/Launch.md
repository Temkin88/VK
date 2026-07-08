# Launch



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**autoclose** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.launch import Launch

# TODO update the JSON string below
json = "{}"
# create an instance of Launch from a JSON string
launch_instance = Launch.from_json(json)
# print the JSON string representation of the object
print Launch.to_json()

# convert the object into a dict
launch_dict = launch_instance.to_dict()
# create an instance of Launch from a dict
launch_from_dict = Launch.from_dict(launch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


