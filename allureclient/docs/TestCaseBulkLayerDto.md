# TestCaseBulkLayerDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection** | [**TestCaseTreeSelectionDto**](TestCaseTreeSelectionDto.md) |  | 
**layer_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.test_case_bulk_layer_dto import TestCaseBulkLayerDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseBulkLayerDto from a JSON string
test_case_bulk_layer_dto_instance = TestCaseBulkLayerDto.from_json(json)
# print the JSON string representation of the object
print TestCaseBulkLayerDto.to_json()

# convert the object into a dict
test_case_bulk_layer_dto_dict = test_case_bulk_layer_dto_instance.to_dict()
# create an instance of TestCaseBulkLayerDto from a dict
test_case_bulk_layer_dto_from_dict = TestCaseBulkLayerDto.from_dict(test_case_bulk_layer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


