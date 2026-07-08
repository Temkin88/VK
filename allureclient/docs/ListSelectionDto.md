# ListSelectionDto



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverted** | **bool** |  | [optional] 
**ids** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.list_selection_dto import ListSelectionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListSelectionDto from a JSON string
list_selection_dto_instance = ListSelectionDto.from_json(json)
# print the JSON string representation of the object
print ListSelectionDto.to_json()

# convert the object into a dict
list_selection_dto_dict = list_selection_dto_instance.to_dict()
# create an instance of ListSelectionDto from a dict
list_selection_dto_from_dict = ListSelectionDto.from_dict(list_selection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


