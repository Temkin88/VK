# TestCaseCsvExportOptions



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**with_headers** | **bool** |  | [optional] 
**column_separator** | **str** |  | [optional] 
**selection** | [**TestCaseTreeSelectionDto**](TestCaseTreeSelectionDto.md) |  | [optional] 
**mapping** | [**List[TestCaseCsvExportOptionsMappingInner]**](TestCaseCsvExportOptionsMappingInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_case_csv_export_options import TestCaseCsvExportOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseCsvExportOptions from a JSON string
test_case_csv_export_options_instance = TestCaseCsvExportOptions.from_json(json)
# print the JSON string representation of the object
print TestCaseCsvExportOptions.to_json()

# convert the object into a dict
test_case_csv_export_options_dict = test_case_csv_export_options_instance.to_dict()
# create an instance of TestCaseCsvExportOptions from a dict
test_case_csv_export_options_from_dict = TestCaseCsvExportOptions.from_dict(test_case_csv_export_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


