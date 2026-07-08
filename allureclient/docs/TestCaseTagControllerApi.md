# openapi_client.TestCaseTagControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tags**](TestCaseTagControllerApi.md#get_tags) | **GET** /testcase/{testCaseId}/tag | Find tags for test case
[**set_tags**](TestCaseTagControllerApi.md#set_tags) | **POST** /testcase/{testCaseId}/tag | Set test tags for test case


# **get_tags**
> List[TestTagDto] get_tags(test_case_id)

Find tags for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_tag_dto import TestTagDto
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
    api_instance = openapi_client.TestCaseTagControllerApi(api_client)
    test_case_id = 56 # int | 

    try:
        # Find tags for test case
        api_response = api_instance.get_tags(test_case_id)
        print("The response of TestCaseTagControllerApi->get_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTagControllerApi->get_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 

### Return type

[**List[TestTagDto]**](TestTagDto.md)

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

# **set_tags**
> List[TestTagDto] set_tags(test_case_id, test_tag_dto)

Set test tags for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_tag_dto import TestTagDto
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
    api_instance = openapi_client.TestCaseTagControllerApi(api_client)
    test_case_id = 56 # int | 
    test_tag_dto = [openapi_client.TestTagDto()] # List[TestTagDto] | 

    try:
        # Set test tags for test case
        api_response = api_instance.set_tags(test_case_id, test_tag_dto)
        print("The response of TestCaseTagControllerApi->set_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTagControllerApi->set_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 
 **test_tag_dto** | [**List[TestTagDto]**](TestTagDto.md)|  | 

### Return type

[**List[TestTagDto]**](TestTagDto.md)

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

