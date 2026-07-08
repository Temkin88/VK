# openapi_client.IntegrationTmsControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_projects**](IntegrationTmsControllerApi.md#find_projects) | **GET** /integration/tms/projects | Get available projects for tms


# **find_projects**
> List[ExtProject] find_projects(project_id, integration_id, query=query)

Get available projects for tms

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.ext_project import ExtProject
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
    api_instance = openapi_client.IntegrationTmsControllerApi(api_client)
    project_id = 56 # int | 
    integration_id = 56 # int | 
    query = '' # str |  (optional) (default to '')

    try:
        # Get available projects for tms
        api_response = api_instance.find_projects(project_id, integration_id, query=query)
        print("The response of IntegrationTmsControllerApi->find_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationTmsControllerApi->find_projects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **integration_id** | **int**|  | 
 **query** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[ExtProject]**](ExtProject.md)

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

