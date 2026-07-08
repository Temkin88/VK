# openapi_client.TestResultEnvVarControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_env_var_values**](TestResultEnvVarControllerApi.md#get_env_var_values) | **GET** /testresult/{testResultId}/evv | Find environment variables for test result


# **get_env_var_values**
> List[EnvVarValueDto] get_env_var_values(test_result_id)

Find environment variables for test result

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_value_dto import EnvVarValueDto
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
    api_instance = openapi_client.TestResultEnvVarControllerApi(api_client)
    test_result_id = 56 # int | 

    try:
        # Find environment variables for test result
        api_response = api_instance.get_env_var_values(test_result_id)
        print("The response of TestResultEnvVarControllerApi->get_env_var_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultEnvVarControllerApi->get_env_var_values: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 

### Return type

[**List[EnvVarValueDto]**](EnvVarValueDto.md)

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

