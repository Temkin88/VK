# openapi_client.ProjectControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_stats**](ProjectControllerApi.md#calculate_stats) | **GET** /project/{id}/stats | Find project stats by id
[**create20**](ProjectControllerApi.md#create20) | **POST** /project | Create a new project
[**delete20**](ProjectControllerApi.md#delete20) | **DELETE** /project/{id} | Delete project by id
[**find_all19**](ProjectControllerApi.md#find_all19) | **GET** /project | Find all projects
[**find_one17**](ProjectControllerApi.md#find_one17) | **GET** /project/{id} | Find project by id
[**get_suggest**](ProjectControllerApi.md#get_suggest) | **GET** /project/suggest | Suggest projects
[**patch19**](ProjectControllerApi.md#patch19) | **PATCH** /project/{id} | Patch project
[**set_favorite**](ProjectControllerApi.md#set_favorite) | **POST** /project/{id}/favorite | Mark project as favorite


# **calculate_stats**
> ProjectStatsDto calculate_stats(id)

Find project stats by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_stats_dto import ProjectStatsDto
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
    api_instance = openapi_client.ProjectControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find project stats by id
        api_response = api_instance.calculate_stats(id)
        print("The response of ProjectControllerApi->calculate_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectControllerApi->calculate_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ProjectStatsDto**](ProjectStatsDto.md)

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

# **create20**
> ProjectDto create20(project_create_dto)

Create a new project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_create_dto import ProjectCreateDto
from openapi_client.models.project_dto import ProjectDto
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
    api_instance = openapi_client.ProjectControllerApi(api_client)
    project_create_dto = openapi_client.ProjectCreateDto() # ProjectCreateDto | 

    try:
        # Create a new project
        api_response = api_instance.create20(project_create_dto)
        print("The response of ProjectControllerApi->create20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectControllerApi->create20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create_dto** | [**ProjectCreateDto**](ProjectCreateDto.md)|  | 

### Return type

[**ProjectDto**](ProjectDto.md)

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

# **delete20**
> delete20(id)

Delete project by id

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
    api_instance = openapi_client.ProjectControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete project by id
        api_instance.delete20(id)
    except Exception as e:
        print("Exception when calling ProjectControllerApi->delete20: %s\n" % e)
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all19**
> PageProjectDto find_all19(query=query, my=my, favorite=favorite, page=page, size=size, sort=sort)

Find all projects

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_project_dto import PageProjectDto
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
    api_instance = openapi_client.ProjectControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    my = True # bool |  (optional)
    favorite = True # bool |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find all projects
        api_response = api_instance.find_all19(query=query, my=my, favorite=favorite, page=page, size=size, sort=sort)
        print("The response of ProjectControllerApi->find_all19:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectControllerApi->find_all19: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **my** | **bool**|  | [optional] 
 **favorite** | **bool**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageProjectDto**](PageProjectDto.md)

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

# **find_one17**
> ProjectDto find_one17(id)

Find project by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_dto import ProjectDto
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
    api_instance = openapi_client.ProjectControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find project by id
        api_response = api_instance.find_one17(id)
        print("The response of ProjectControllerApi->find_one17:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectControllerApi->find_one17: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ProjectDto**](ProjectDto.md)

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

# **get_suggest**
> PageProjectSuggestDto get_suggest(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest projects

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_project_suggest_dto import PageProjectSuggestDto
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
    api_instance = openapi_client.ProjectControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest projects
        api_response = api_instance.get_suggest(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of ProjectControllerApi->get_suggest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectControllerApi->get_suggest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **id** | [**List[int]**](int.md)|  | [optional] 
 **ignore_id** | [**List[int]**](int.md)|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageProjectSuggestDto**](PageProjectSuggestDto.md)

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

# **patch19**
> ProjectDto patch19(id, project_patch_dto)

Patch project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_dto import ProjectDto
from openapi_client.models.project_patch_dto import ProjectPatchDto
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
    api_instance = openapi_client.ProjectControllerApi(api_client)
    id = 56 # int | 
    project_patch_dto = openapi_client.ProjectPatchDto() # ProjectPatchDto | 

    try:
        # Patch project
        api_response = api_instance.patch19(id, project_patch_dto)
        print("The response of ProjectControllerApi->patch19:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectControllerApi->patch19: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **project_patch_dto** | [**ProjectPatchDto**](ProjectPatchDto.md)|  | 

### Return type

[**ProjectDto**](ProjectDto.md)

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

# **set_favorite**
> ProjectDto set_favorite(id, favorite=favorite)

Mark project as favorite

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_dto import ProjectDto
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
    api_instance = openapi_client.ProjectControllerApi(api_client)
    id = 56 # int | 
    favorite = True # bool |  (optional)

    try:
        # Mark project as favorite
        api_response = api_instance.set_favorite(id, favorite=favorite)
        print("The response of ProjectControllerApi->set_favorite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectControllerApi->set_favorite: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **favorite** | **bool**|  | [optional] 

### Return type

[**ProjectDto**](ProjectDto.md)

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

