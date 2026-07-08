# openapi_client.TestCaseSyncControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sync1**](TestCaseSyncControllerApi.md#sync1) | **POST** /testcase/bulk/sync | Clone test case


# **sync1**
> sync1(test_case_sync_rq_dto)

Clone test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_sync_rq_dto import TestCaseSyncRqDto
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
    api_instance = openapi_client.TestCaseSyncControllerApi(api_client)
    test_case_sync_rq_dto = openapi_client.TestCaseSyncRqDto() # TestCaseSyncRqDto | 

    try:
        # Clone test case
        api_instance.sync1(test_case_sync_rq_dto)
    except Exception as e:
        print("Exception when calling TestCaseSyncControllerApi->sync1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_sync_rq_dto** | [**TestCaseSyncRqDto**](TestCaseSyncRqDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

