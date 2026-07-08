# openapi_client.ProjectAccessControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project_collaborators**](ProjectAccessControllerApi.md#add_project_collaborators) | **POST** /project/access/{projectId}/collaborator | Add collaborators to project
[**add_project_groups**](ProjectAccessControllerApi.md#add_project_groups) | **POST** /project/access/{projectId}/group | Add groups to project
[**delete_project_groups**](ProjectAccessControllerApi.md#delete_project_groups) | **DELETE** /project/access/{projectId}/group | Delete groups from project
[**delete_users**](ProjectAccessControllerApi.md#delete_users) | **DELETE** /project/access/{projectId}/collaborator | Delete collaborators from project
[**get_project_access_groups**](ProjectAccessControllerApi.md#get_project_access_groups) | **GET** /project/access/{projectId}/group | Get project access groups
[**get_project_collaborators**](ProjectAccessControllerApi.md#get_project_collaborators) | **GET** /project/access/{projectId}/collaborator | Get project collaborators


# **add_project_collaborators**
> List[ProjectCollaboratorAccessDto] add_project_collaborators(project_id, project_access_collaborator_add_dto)

Add collaborators to project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_access_collaborator_add_dto import ProjectAccessCollaboratorAddDto
from openapi_client.models.project_collaborator_access_dto import ProjectCollaboratorAccessDto
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
    api_instance = openapi_client.ProjectAccessControllerApi(api_client)
    project_id = 56 # int | 
    project_access_collaborator_add_dto = openapi_client.ProjectAccessCollaboratorAddDto() # ProjectAccessCollaboratorAddDto | 

    try:
        # Add collaborators to project
        api_response = api_instance.add_project_collaborators(project_id, project_access_collaborator_add_dto)
        print("The response of ProjectAccessControllerApi->add_project_collaborators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAccessControllerApi->add_project_collaborators: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **project_access_collaborator_add_dto** | [**ProjectAccessCollaboratorAddDto**](ProjectAccessCollaboratorAddDto.md)|  | 

### Return type

[**List[ProjectCollaboratorAccessDto]**](ProjectCollaboratorAccessDto.md)

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

# **add_project_groups**
> List[ProjectGroupAccessDto] add_project_groups(project_id, project_access_group_add_dto)

Add groups to project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_access_group_add_dto import ProjectAccessGroupAddDto
from openapi_client.models.project_group_access_dto import ProjectGroupAccessDto
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
    api_instance = openapi_client.ProjectAccessControllerApi(api_client)
    project_id = 56 # int | 
    project_access_group_add_dto = openapi_client.ProjectAccessGroupAddDto() # ProjectAccessGroupAddDto | 

    try:
        # Add groups to project
        api_response = api_instance.add_project_groups(project_id, project_access_group_add_dto)
        print("The response of ProjectAccessControllerApi->add_project_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAccessControllerApi->add_project_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **project_access_group_add_dto** | [**ProjectAccessGroupAddDto**](ProjectAccessGroupAddDto.md)|  | 

### Return type

[**List[ProjectGroupAccessDto]**](ProjectGroupAccessDto.md)

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

# **delete_project_groups**
> delete_project_groups(project_id, group_id)

Delete groups from project

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
    api_instance = openapi_client.ProjectAccessControllerApi(api_client)
    project_id = 56 # int | 
    group_id = [56] # List[int] | 

    try:
        # Delete groups from project
        api_instance.delete_project_groups(project_id, group_id)
    except Exception as e:
        print("Exception when calling ProjectAccessControllerApi->delete_project_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **group_id** | [**List[int]**](int.md)|  | 

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

# **delete_users**
> delete_users(project_id, username)

Delete collaborators from project

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
    api_instance = openapi_client.ProjectAccessControllerApi(api_client)
    project_id = 56 # int | 
    username = ['username_example'] # List[str] | 

    try:
        # Delete collaborators from project
        api_instance.delete_users(project_id, username)
    except Exception as e:
        print("Exception when calling ProjectAccessControllerApi->delete_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **username** | [**List[str]**](str.md)|  | 

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

# **get_project_access_groups**
> PageProjectGroupAccessDto get_project_access_groups(project_id, query=query, permissions_set_id=permissions_set_id, page=page, size=size, sort=sort)

Get project access groups

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_project_group_access_dto import PageProjectGroupAccessDto
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
    api_instance = openapi_client.ProjectAccessControllerApi(api_client)
    project_id = 56 # int | 
    query = 'query_example' # str |  (optional)
    permissions_set_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Get project access groups
        api_response = api_instance.get_project_access_groups(project_id, query=query, permissions_set_id=permissions_set_id, page=page, size=size, sort=sort)
        print("The response of ProjectAccessControllerApi->get_project_access_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAccessControllerApi->get_project_access_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **query** | **str**|  | [optional] 
 **permissions_set_id** | [**List[int]**](int.md)|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageProjectGroupAccessDto**](PageProjectGroupAccessDto.md)

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

# **get_project_collaborators**
> PageProjectCollaboratorAccessDto get_project_collaborators(project_id, query=query, permissions_set_id=permissions_set_id, page=page, size=size, sort=sort)

Get project collaborators

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_project_collaborator_access_dto import PageProjectCollaboratorAccessDto
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
    api_instance = openapi_client.ProjectAccessControllerApi(api_client)
    project_id = 56 # int | 
    query = 'query_example' # str |  (optional)
    permissions_set_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["username,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["username,ASC"])

    try:
        # Get project collaborators
        api_response = api_instance.get_project_collaborators(project_id, query=query, permissions_set_id=permissions_set_id, page=page, size=size, sort=sort)
        print("The response of ProjectAccessControllerApi->get_project_collaborators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAccessControllerApi->get_project_collaborators: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **query** | **str**|  | [optional] 
 **permissions_set_id** | [**List[int]**](int.md)|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;username,ASC&quot;]]

### Return type

[**PageProjectCollaboratorAccessDto**](PageProjectCollaboratorAccessDto.md)

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

