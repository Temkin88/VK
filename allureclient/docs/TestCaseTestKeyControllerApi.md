# openapi_client.TestCaseTestKeyControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_keys1**](TestCaseTestKeyControllerApi.md#get_keys1) | **GET** /testcase/{testCaseId}/testkey | Find test keys for test case
[**set_keys1**](TestCaseTestKeyControllerApi.md#set_keys1) | **POST** /testcase/{testCaseId}/testkey | Set test keys to test case


# **get_keys1**
> List[TestKeyDto] get_keys1(test_case_id)

Find test keys for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_key_dto import TestKeyDto
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
    api_instance = openapi_client.TestCaseTestKeyControllerApi(api_client)
    test_case_id = 56 # int | 

    try:
        # Find test keys for test case
        api_response = api_instance.get_keys1(test_case_id)
        print("The response of TestCaseTestKeyControllerApi->get_keys1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTestKeyControllerApi->get_keys1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 

### Return type

[**List[TestKeyDto]**](TestKeyDto.md)

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

# **set_keys1**
> List[TestKeyDto] set_keys1(test_case_id, test_key_dto)

Set test keys to test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_key_dto import TestKeyDto
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
    api_instance = openapi_client.TestCaseTestKeyControllerApi(api_client)
    test_case_id = 56 # int | 
    test_key_dto = [openapi_client.TestKeyDto()] # List[TestKeyDto] | 

    try:
        # Set test keys to test case
        api_response = api_instance.set_keys1(test_case_id, test_key_dto)
        print("The response of TestCaseTestKeyControllerApi->set_keys1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTestKeyControllerApi->set_keys1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 
 **test_key_dto** | [**List[TestKeyDto]**](TestKeyDto.md)|  | 

### Return type

[**List[TestKeyDto]**](TestKeyDto.md)

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

