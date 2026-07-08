# openapi_client.TestCaseIssueControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_issues1**](TestCaseIssueControllerApi.md#get_issues1) | **GET** /testcase/{testCaseId}/issue | Find issues for test case
[**set_issues2**](TestCaseIssueControllerApi.md#set_issues2) | **POST** /testcase/{testCaseId}/issue | Set issues to test case


# **get_issues1**
> List[IssueDto] get_issues1(test_case_id)

Find issues for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.issue_dto import IssueDto
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
    api_instance = openapi_client.TestCaseIssueControllerApi(api_client)
    test_case_id = 56 # int | 

    try:
        # Find issues for test case
        api_response = api_instance.get_issues1(test_case_id)
        print("The response of TestCaseIssueControllerApi->get_issues1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseIssueControllerApi->get_issues1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 

### Return type

[**List[IssueDto]**](IssueDto.md)

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

# **set_issues2**
> List[IssueDto] set_issues2(test_case_id, issue_dto)

Set issues to test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.issue_dto import IssueDto
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
    api_instance = openapi_client.TestCaseIssueControllerApi(api_client)
    test_case_id = 56 # int | 
    issue_dto = [openapi_client.IssueDto()] # List[IssueDto] | 

    try:
        # Set issues to test case
        api_response = api_instance.set_issues2(test_case_id, issue_dto)
        print("The response of TestCaseIssueControllerApi->set_issues2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseIssueControllerApi->set_issues2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 
 **issue_dto** | [**List[IssueDto]**](IssueDto.md)|  | 

### Return type

[**List[IssueDto]**](IssueDto.md)

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

