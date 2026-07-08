# openapi_client.ProjectCollaboratorControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all22**](ProjectCollaboratorControllerApi.md#find_all22) | **GET** /project/{id}/collaborator | Find all permission sets


# **find_all22**
> PageProjectCollaboratorDto find_all22(id, page=page, size=size, sort=sort)

Find all permission sets

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_project_collaborator_dto import PageProjectCollaboratorDto
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
    api_instance = openapi_client.ProjectCollaboratorControllerApi(api_client)
    id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["username,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["username,ASC"])

    try:
        # Find all permission sets
        api_response = api_instance.find_all22(id, page=page, size=size, sort=sort)
        print("The response of ProjectCollaboratorControllerApi->find_all22:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCollaboratorControllerApi->find_all22: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;username,ASC&quot;]]

### Return type

[**PageProjectCollaboratorDto**](PageProjectCollaboratorDto.md)

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

