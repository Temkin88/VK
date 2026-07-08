# TestCaseCsvExportOptionsMappingInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | [**TestResultExportField**](TestResultExportField.md) |  | [optional] 
**custom_field_id** | **int** |  | 
**items_separator** | **str** |  | 
**name** | **str** |  | [optional] 
**name_value_separator** | **str** |  | [optional] 
**params_separator** | **str** |  | [optional] 
**examples_separator** | **str** |  | [optional] 
**role_id** | **int** |  | 
**steps_separator** | **str** |  | 
**steps_indent** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.test_case_csv_export_options_mapping_inner import TestCaseCsvExportOptionsMappingInner

# TODO update the JSON string below
json = "{}"
# create an instance of TestCaseCsvExportOptionsMappingInner from a JSON string
test_case_csv_export_options_mapping_inner_instance = TestCaseCsvExportOptionsMappingInner.from_json(json)
# print the JSON string representation of the object
print TestCaseCsvExportOptionsMappingInner.to_json()

# convert the object into a dict
test_case_csv_export_options_mapping_inner_dict = test_case_csv_export_options_mapping_inner_instance.to_dict()
# create an instance of TestCaseCsvExportOptionsMappingInner from a dict
test_case_csv_export_options_mapping_inner_from_dict = TestCaseCsvExportOptionsMappingInner.from_dict(test_case_csv_export_options_mapping_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


