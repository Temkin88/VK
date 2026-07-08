# ScenarioExportFieldMapping



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **object** |  | [optional] 
**steps_separator** | **str** |  | 
**steps_indent** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.scenario_export_field_mapping import ScenarioExportFieldMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioExportFieldMapping from a JSON string
scenario_export_field_mapping_instance = ScenarioExportFieldMapping.from_json(json)
# print the JSON string representation of the object
print ScenarioExportFieldMapping.to_json()

# convert the object into a dict
scenario_export_field_mapping_dict = scenario_export_field_mapping_instance.to_dict()
# create an instance of ScenarioExportFieldMapping from a dict
scenario_export_field_mapping_from_dict = ScenarioExportFieldMapping.from_dict(scenario_export_field_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


