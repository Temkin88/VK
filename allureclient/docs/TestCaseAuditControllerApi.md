# openapi_client.TestCaseAuditControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all12**](TestCaseAuditControllerApi.md#find_all12) | **GET** /testcase/audit | Find audit log for test case


# **find_all12**
> PageTestCaseAuditLogEntryDto find_all12(test_case_id, page=page, size=size, sort=sort)

Find audit log for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_case_audit_log_entry_dto import PageTestCaseAuditLogEntryDto
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
    api_instance = openapi_client.TestCaseAuditControllerApi(api_client)
    test_case_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        # Find audit log for test case
        api_response = api_instance.find_all12(test_case_id, page=page, size=size, sort=sort)
        print("The response of TestCaseAuditControllerApi->find_all12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseAuditControllerApi->find_all12: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageTestCaseAuditLogEntryDto**](PageTestCaseAuditLogEntryDto.md)

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

