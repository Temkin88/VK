# openapi_client.TestResultRerunControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retry**](TestResultRerunControllerApi.md#retry) | **POST** /testresult/{testResultId}/rerun | Schedule manual rerun for test case
[**retry1**](TestResultRerunControllerApi.md#retry1) | **POST** /testresult/{testResultId}/retry | Schedule manual rerun for test case


# **retry**
> IdAndNameOnlyDto retry(test_result_id, test_result_rerun_dto)

Schedule manual rerun for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.id_and_name_only_dto import IdAndNameOnlyDto
from openapi_client.models.test_result_rerun_dto import TestResultRerunDto
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
    api_instance = openapi_client.TestResultRerunControllerApi(api_client)
    test_result_id = 56 # int | 
    test_result_rerun_dto = openapi_client.TestResultRerunDto() # TestResultRerunDto | 

    try:
        # Schedule manual rerun for test case
        api_response = api_instance.retry(test_result_id, test_result_rerun_dto)
        print("The response of TestResultRerunControllerApi->retry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultRerunControllerApi->retry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 
 **test_result_rerun_dto** | [**TestResultRerunDto**](TestResultRerunDto.md)|  | 

### Return type

[**IdAndNameOnlyDto**](IdAndNameOnlyDto.md)

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

# **retry1**
> IdAndNameOnlyDto retry1(test_result_id, test_result_rerun_dto)

Schedule manual rerun for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.id_and_name_only_dto import IdAndNameOnlyDto
from openapi_client.models.test_result_rerun_dto import TestResultRerunDto
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
    api_instance = openapi_client.TestResultRerunControllerApi(api_client)
    test_result_id = 56 # int | 
    test_result_rerun_dto = openapi_client.TestResultRerunDto() # TestResultRerunDto | 

    try:
        # Schedule manual rerun for test case
        api_response = api_instance.retry1(test_result_id, test_result_rerun_dto)
        print("The response of TestResultRerunControllerApi->retry1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultRerunControllerApi->retry1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 
 **test_result_rerun_dto** | [**TestResultRerunDto**](TestResultRerunDto.md)|  | 

### Return type

[**IdAndNameOnlyDto**](IdAndNameOnlyDto.md)

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

