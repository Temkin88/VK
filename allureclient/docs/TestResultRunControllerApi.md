# openapi_client.TestResultRunControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign**](TestResultRunControllerApi.md#assign) | **POST** /testresult/{id}/assign | Assign test result
[**resolve**](TestResultRunControllerApi.md#resolve) | **POST** /testresult/{id}/resolve | Resolve test result


# **assign**
> TestResultRowDto assign(id, assign_request_dto)

Assign test result

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.assign_request_dto import AssignRequestDto
from openapi_client.models.test_result_row_dto import TestResultRowDto
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
    api_instance = openapi_client.TestResultRunControllerApi(api_client)
    id = 56 # int | 
    assign_request_dto = openapi_client.AssignRequestDto() # AssignRequestDto | 

    try:
        # Assign test result
        api_response = api_instance.assign(id, assign_request_dto)
        print("The response of TestResultRunControllerApi->assign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultRunControllerApi->assign: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **assign_request_dto** | [**AssignRequestDto**](AssignRequestDto.md)|  | 

### Return type

[**TestResultRowDto**](TestResultRowDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve**
> TestResultRowDto resolve(id, resolve_request_dto)

Resolve test result

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.resolve_request_dto import ResolveRequestDto
from openapi_client.models.test_result_row_dto import TestResultRowDto
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
    api_instance = openapi_client.TestResultRunControllerApi(api_client)
    id = 56 # int | 
    resolve_request_dto = openapi_client.ResolveRequestDto() # ResolveRequestDto | 

    try:
        # Resolve test result
        api_response = api_instance.resolve(id, resolve_request_dto)
        print("The response of TestResultRunControllerApi->resolve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultRunControllerApi->resolve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **resolve_request_dto** | [**ResolveRequestDto**](ResolveRequestDto.md)|  | 

### Return type

[**TestResultRowDto**](TestResultRowDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

