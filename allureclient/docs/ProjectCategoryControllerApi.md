# openapi_client.ProjectCategoryControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add1**](ProjectCategoryControllerApi.md#add1) | **POST** /project/{projectId}/category | 
[**find_all21**](ProjectCategoryControllerApi.md#find_all21) | **GET** /project/{projectId}/category | 
[**remove1**](ProjectCategoryControllerApi.md#remove1) | **POST** /project/{projectId}/category/remove | 


# **add1**
> CategoryDto add1(project_id, project_category_add_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.category_dto import CategoryDto
from openapi_client.models.project_category_add_dto import ProjectCategoryAddDto
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
    api_instance = openapi_client.ProjectCategoryControllerApi(api_client)
    project_id = 56 # int | 
    project_category_add_dto = openapi_client.ProjectCategoryAddDto() # ProjectCategoryAddDto | 

    try:
        api_response = api_instance.add1(project_id, project_category_add_dto)
        print("The response of ProjectCategoryControllerApi->add1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCategoryControllerApi->add1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **project_category_add_dto** | [**ProjectCategoryAddDto**](ProjectCategoryAddDto.md)|  | 

### Return type

[**CategoryDto**](CategoryDto.md)

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

# **find_all21**
> PageCategoryDto find_all21(project_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_category_dto import PageCategoryDto
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
    api_instance = openapi_client.ProjectCategoryControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        api_response = api_instance.find_all21(project_id, page=page, size=size, sort=sort)
        print("The response of ProjectCategoryControllerApi->find_all21:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCategoryControllerApi->find_all21: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageCategoryDto**](PageCategoryDto.md)

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

# **remove1**
> remove1(project_id, project_category_remove_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_category_remove_dto import ProjectCategoryRemoveDto
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
    api_instance = openapi_client.ProjectCategoryControllerApi(api_client)
    project_id = 56 # int | 
    project_category_remove_dto = openapi_client.ProjectCategoryRemoveDto() # ProjectCategoryRemoveDto | 

    try:
        api_instance.remove1(project_id, project_category_remove_dto)
    except Exception as e:
        print("Exception when calling ProjectCategoryControllerApi->remove1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **project_category_remove_dto** | [**ProjectCategoryRemoveDto**](ProjectCategoryRemoveDto.md)|  | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

