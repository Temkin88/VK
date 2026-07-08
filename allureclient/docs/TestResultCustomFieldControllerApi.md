# openapi_client.TestResultCustomFieldControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cfv**](TestResultCustomFieldControllerApi.md#get_cfv) | **GET** /testresult/{testResultId}/cfv | Find custom field values for test result
[**set_issues1**](TestResultCustomFieldControllerApi.md#set_issues1) | **POST** /testresult/{testResultId}/cfv | Set custom field values to test result


# **get_cfv**
> List[CustomFieldValueDto] get_cfv(test_result_id)

Find custom field values for test result

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_value_dto import CustomFieldValueDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://allure.vk.team/api/rs
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://allure.vk.team/api/rs"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultCustomFieldControllerApi(api_client)
    test_result_id = 56 # int | 

    try:
        # Find custom field values for test result
        api_response = api_instance.get_cfv(test_result_id)
        print("The response of TestResultCustomFieldControllerApi->get_cfv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultCustomFieldControllerApi->get_cfv: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 

### Return type

[**List[CustomFieldValueDto]**](CustomFieldValueDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_issues1**
> List[CustomFieldValueDto] set_issues1(test_result_id, custom_field_value_dto)

Set custom field values to test result

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_value_dto import CustomFieldValueDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://allure.vk.team/api/rs
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://allure.vk.team/api/rs"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultCustomFieldControllerApi(api_client)
    test_result_id = 56 # int | 
    custom_field_value_dto = [openapi_client.CustomFieldValueDto()] # List[CustomFieldValueDto] | 

    try:
        # Set custom field values to test result
        api_response = api_instance.set_issues1(test_result_id, custom_field_value_dto)
        print("The response of TestResultCustomFieldControllerApi->set_issues1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultCustomFieldControllerApi->set_issues1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 
 **custom_field_value_dto** | [**List[CustomFieldValueDto]**](CustomFieldValueDto.md)|  | 

### Return type

[**List[CustomFieldValueDto]**](CustomFieldValueDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

