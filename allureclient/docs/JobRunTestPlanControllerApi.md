# openapi_client.JobRunTestPlanControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_by_id1**](JobRunTestPlanControllerApi.md#find_by_id1) | **GET** /jobrun/{id}/plan | Find test plan for execution by external id


# **find_by_id1**
> List[TestCaseInfo] find_by_id1(id, expected=expected)

Find test plan for execution by external id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_info import TestCaseInfo
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
    api_instance = openapi_client.JobRunTestPlanControllerApi(api_client)
    id = 56 # int | 
    expected = False # bool |  (optional) (default to False)

    try:
        # Find test plan for execution by external id
        api_response = api_instance.find_by_id1(id, expected=expected)
        print("The response of JobRunTestPlanControllerApi->find_by_id1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobRunTestPlanControllerApi->find_by_id1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **expected** | **bool**|  | [optional] [default to False]

### Return type

[**List[TestCaseInfo]**](TestCaseInfo.md)

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

