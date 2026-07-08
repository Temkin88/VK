# openapi_client.TestCaseExportControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_to_tms**](TestCaseExportControllerApi.md#export_to_tms) | **POST** /testcase/tms/sync | 


# **export_to_tms**
> export_to_tms(project_sync_request)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_sync_request import ProjectSyncRequest
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
    api_instance = openapi_client.TestCaseExportControllerApi(api_client)
    project_sync_request = openapi_client.ProjectSyncRequest() # ProjectSyncRequest | 

    try:
        api_instance.export_to_tms(project_sync_request)
    except Exception as e:
        print("Exception when calling TestCaseExportControllerApi->export_to_tms: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_sync_request** | [**ProjectSyncRequest**](ProjectSyncRequest.md)|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

