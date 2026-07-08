# openapi_client.TestCaseCloneControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone**](TestCaseCloneControllerApi.md#clone) | **POST** /testcase/{id}/clone | Clone test case


# **clone**
> TestCaseRowDto clone(id, test_case_clone_rq_dto)

Clone test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_clone_rq_dto import TestCaseCloneRqDto
from openapi_client.models.test_case_row_dto import TestCaseRowDto
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
    api_instance = openapi_client.TestCaseCloneControllerApi(api_client)
    id = 56 # int | 
    test_case_clone_rq_dto = openapi_client.TestCaseCloneRqDto() # TestCaseCloneRqDto | 

    try:
        # Clone test case
        api_response = api_instance.clone(id, test_case_clone_rq_dto)
        print("The response of TestCaseCloneControllerApi->clone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseCloneControllerApi->clone: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_case_clone_rq_dto** | [**TestCaseCloneRqDto**](TestCaseCloneRqDto.md)|  | 

### Return type

[**TestCaseRowDto**](TestCaseRowDto.md)

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

