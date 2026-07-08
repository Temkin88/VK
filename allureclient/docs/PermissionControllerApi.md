# openapi_client.PermissionControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_permissions_on_project**](PermissionControllerApi.md#get_permissions_on_project) | **GET** /permission | Get user permissions for project


# **get_permissions_on_project**
> List[PermissionDto] get_permissions_on_project(project_id)

Get user permissions for project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.permission_dto import PermissionDto
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
    api_instance = openapi_client.PermissionControllerApi(api_client)
    project_id = 56 # int | 

    try:
        # Get user permissions for project
        api_response = api_instance.get_permissions_on_project(project_id)
        print("The response of PermissionControllerApi->get_permissions_on_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionControllerApi->get_permissions_on_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**List[PermissionDto]**](PermissionDto.md)

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

