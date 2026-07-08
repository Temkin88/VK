# openapi_client.TestCaseOverviewControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_overview**](TestCaseOverviewControllerApi.md#get_overview) | **GET** /testcase/{testCaseId}/overview | Get test case overview


# **get_overview**
> TestCaseOverviewDto get_overview(test_case_id)

Get test case overview

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_overview_dto import TestCaseOverviewDto
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
    api_instance = openapi_client.TestCaseOverviewControllerApi(api_client)
    test_case_id = 56 # int | 

    try:
        # Get test case overview
        api_response = api_instance.get_overview(test_case_id)
        print("The response of TestCaseOverviewControllerApi->get_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseOverviewControllerApi->get_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 

### Return type

[**TestCaseOverviewDto**](TestCaseOverviewDto.md)

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

