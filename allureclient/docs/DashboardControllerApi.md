# openapi_client.DashboardControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create40**](DashboardControllerApi.md#create40) | **POST** /dashboard | 
[**delete38**](DashboardControllerApi.md#delete38) | **DELETE** /dashboard/{id} | 
[**find_all_by_project1**](DashboardControllerApi.md#find_all_by_project1) | **GET** /dashboard | 
[**find_one32**](DashboardControllerApi.md#find_one32) | **GET** /dashboard/{id} | 
[**patch37**](DashboardControllerApi.md#patch37) | **PATCH** /dashboard/{id} | 


# **create40**
> DashboardOverviewDto create40(dashboard_create_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.dashboard_create_dto import DashboardCreateDto
from openapi_client.models.dashboard_overview_dto import DashboardOverviewDto
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
    api_instance = openapi_client.DashboardControllerApi(api_client)
    dashboard_create_dto = openapi_client.DashboardCreateDto() # DashboardCreateDto | 

    try:
        api_response = api_instance.create40(dashboard_create_dto)
        print("The response of DashboardControllerApi->create40:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardControllerApi->create40: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_create_dto** | [**DashboardCreateDto**](DashboardCreateDto.md)|  | 

### Return type

[**DashboardOverviewDto**](DashboardOverviewDto.md)

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

# **delete38**
> delete38(id)



### Example

```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.DashboardControllerApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete38(id)
    except Exception as e:
        print("Exception when calling DashboardControllerApi->delete38: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_by_project1**
> PageDashboardDto find_all_by_project1(project_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_dashboard_dto import PageDashboardDto
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
    api_instance = openapi_client.DashboardControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        api_response = api_instance.find_all_by_project1(project_id, page=page, size=size, sort=sort)
        print("The response of DashboardControllerApi->find_all_by_project1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardControllerApi->find_all_by_project1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageDashboardDto**](PageDashboardDto.md)

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

# **find_one32**
> DashboardOverviewDto find_one32(id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.dashboard_overview_dto import DashboardOverviewDto
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
    api_instance = openapi_client.DashboardControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.find_one32(id)
        print("The response of DashboardControllerApi->find_one32:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardControllerApi->find_one32: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DashboardOverviewDto**](DashboardOverviewDto.md)

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

# **patch37**
> DashboardOverviewDto patch37(id, dashboard_patch_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.dashboard_overview_dto import DashboardOverviewDto
from openapi_client.models.dashboard_patch_dto import DashboardPatchDto
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
    api_instance = openapi_client.DashboardControllerApi(api_client)
    id = 56 # int | 
    dashboard_patch_dto = openapi_client.DashboardPatchDto() # DashboardPatchDto | 

    try:
        api_response = api_instance.patch37(id, dashboard_patch_dto)
        print("The response of DashboardControllerApi->patch37:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardControllerApi->patch37: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **dashboard_patch_dto** | [**DashboardPatchDto**](DashboardPatchDto.md)|  | 

### Return type

[**DashboardOverviewDto**](DashboardOverviewDto.md)

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

