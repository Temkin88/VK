# GetFields200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**depends_on_fields** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**classifier** | **str** |  | [optional] 
**options** | [**List[ExtFormFieldOption]**](ExtFormFieldOption.md) |  | [optional] 
**default_value** | **str** |  | [optional] 
**multi** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.get_fields200_response_inner import GetFields200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetFields200ResponseInner from a JSON string
get_fields200_response_inner_instance = GetFields200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetFields200ResponseInner.to_json()

# convert the object into a dict
get_fields200_response_inner_dict = get_fields200_response_inner_instance.to_dict()
# create an instance of GetFields200ResponseInner from a dict
get_fields200_response_inner_from_dict = GetFields200ResponseInner.from_dict(get_fields200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


