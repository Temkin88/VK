# TestLayerDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**created_date** | **int** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.test_layer_dto import TestLayerDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestLayerDto from a JSON string
test_layer_dto_instance = TestLayerDto.from_json(json)
# print the JSON string representation of the object
print TestLayerDto.to_json()

# convert the object into a dict
test_layer_dto_dict = test_layer_dto_instance.to_dict()
# create an instance of TestLayerDto from a dict
test_layer_dto_from_dict = TestLayerDto.from_dict(test_layer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


