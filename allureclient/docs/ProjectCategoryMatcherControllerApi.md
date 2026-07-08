# openapi_client.ProjectCategoryMatcherControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](ProjectCategoryMatcherControllerApi.md#add) | **POST** /project/{projectId}/categorymatcher | 
[**find_all20**](ProjectCategoryMatcherControllerApi.md#find_all20) | **GET** /project/{projectId}/categorymatcher | 
[**remove**](ProjectCategoryMatcherControllerApi.md#remove) | **POST** /project/{projectId}/categorymatcher/remove | 


# **add**
> CategoryMatcherDto add(project_id, project_category_matcher_add_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.category_matcher_dto import CategoryMatcherDto
from openapi_client.models.project_category_matcher_add_dto import ProjectCategoryMatcherAddDto
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
    api_instance = openapi_client.ProjectCategoryMatcherControllerApi(api_client)
    project_id = 56 # int | 
    project_category_matcher_add_dto = openapi_client.ProjectCategoryMatcherAddDto() # ProjectCategoryMatcherAddDto | 

    try:
        api_response = api_instance.add(project_id, project_category_matcher_add_dto)
        print("The response of ProjectCategoryMatcherControllerApi->add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCategoryMatcherControllerApi->add: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **project_category_matcher_add_dto** | [**ProjectCategoryMatcherAddDto**](ProjectCategoryMatcherAddDto.md)|  | 

### Return type

[**CategoryMatcherDto**](CategoryMatcherDto.md)

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

# **find_all20**
> PageCategoryMatcherDto find_all20(project_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_category_matcher_dto import PageCategoryMatcherDto
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
    api_instance = openapi_client.ProjectCategoryMatcherControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        api_response = api_instance.find_all20(project_id, page=page, size=size, sort=sort)
        print("The response of ProjectCategoryMatcherControllerApi->find_all20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCategoryMatcherControllerApi->find_all20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageCategoryMatcherDto**](PageCategoryMatcherDto.md)

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

# **remove**
> remove(project_id, project_category_matcher_remove_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_category_matcher_remove_dto import ProjectCategoryMatcherRemoveDto
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
    api_instance = openapi_client.ProjectCategoryMatcherControllerApi(api_client)
    project_id = 56 # int | 
    project_category_matcher_remove_dto = openapi_client.ProjectCategoryMatcherRemoveDto() # ProjectCategoryMatcherRemoveDto | 

    try:
        api_instance.remove(project_id, project_category_matcher_remove_dto)
    except Exception as e:
        print("Exception when calling ProjectCategoryMatcherControllerApi->remove: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **project_category_matcher_remove_dto** | [**ProjectCategoryMatcherRemoveDto**](ProjectCategoryMatcherRemoveDto.md)|  | 

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

