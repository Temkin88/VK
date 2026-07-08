# openapi_client.AccessGroupControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_projects**](AccessGroupControllerApi.md#add_projects) | **POST** /accessgroup/{id}/project | Add projects to group
[**add_users**](AccessGroupControllerApi.md#add_users) | **POST** /accessgroup/{id}/user | Add users to group
[**create48**](AccessGroupControllerApi.md#create48) | **POST** /accessgroup | Create a new group
[**delete_by_id5**](AccessGroupControllerApi.md#delete_by_id5) | **DELETE** /accessgroup/{id} | Delete group by id
[**delete_projects**](AccessGroupControllerApi.md#delete_projects) | **DELETE** /accessgroup/{id}/project | Delete projects from group
[**delete_users1**](AccessGroupControllerApi.md#delete_users1) | **DELETE** /accessgroup/{id}/user | Delete users from group
[**fetch_by_id**](AccessGroupControllerApi.md#fetch_by_id) | **GET** /accessgroup/{id} | Find group by id
[**find_all42**](AccessGroupControllerApi.md#find_all42) | **GET** /accessgroup | Find all groups
[**get_projects1**](AccessGroupControllerApi.md#get_projects1) | **GET** /accessgroup/{id}/project | Get group&#39;s projects
[**get_users**](AccessGroupControllerApi.md#get_users) | **GET** /accessgroup/{id}/user | Get group&#39;s users
[**patch_by_id**](AccessGroupControllerApi.md#patch_by_id) | **PATCH** /accessgroup/{id} | Patch group
[**suggest23**](AccessGroupControllerApi.md#suggest23) | **GET** /accessgroup/suggest | Suggests groups


# **add_projects**
> AccessGroupDto add_projects(id, access_group_projects_add_dto)

Add projects to group

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.access_group_dto import AccessGroupDto
from openapi_client.models.access_group_projects_add_dto import AccessGroupProjectsAddDto
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
    api_instance = openapi_client.AccessGroupControllerApi(api_client)
    id = 56 # int | 
    access_group_projects_add_dto = openapi_client.AccessGroupProjectsAddDto() # AccessGroupProjectsAddDto | 

    try:
        # Add projects to group
        api_response = api_instance.add_projects(id, access_group_projects_add_dto)
        print("The response of AccessGroupControllerApi->add_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessGroupControllerApi->add_projects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **access_group_projects_add_dto** | [**AccessGroupProjectsAddDto**](AccessGroupProjectsAddDto.md)|  | 

### Return type

[**AccessGroupDto**](AccessGroupDto.md)

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

# **add_users**
> AccessGroupDto add_users(id, access_group_users_add_dto)

Add users to group

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.access_group_dto import AccessGroupDto
from openapi_client.models.access_group_users_add_dto import AccessGroupUsersAddDto
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
    api_instance = openapi_client.AccessGroupControllerApi(api_client)
    id = 56 # int | 
    access_group_users_add_dto = openapi_client.AccessGroupUsersAddDto() # AccessGroupUsersAddDto | 

    try:
        # Add users to group
        api_response = api_instance.add_users(id, access_group_users_add_dto)
        print("The response of AccessGroupControllerApi->add_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessGroupControllerApi->add_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **access_group_users_add_dto** | [**AccessGroupUsersAddDto**](AccessGroupUsersAddDto.md)|  | 

### Return type

[**AccessGroupDto**](AccessGroupDto.md)

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

# **create48**
> AccessGroupDto create48(access_group_create_dto)

Create a new group

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.access_group_create_dto import AccessGroupCreateDto
from openapi_client.models.access_group_dto import AccessGroupDto
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
    api_instance = openapi_client.AccessGroupControllerApi(api_client)
    access_group_create_dto = openapi_client.AccessGroupCreateDto() # AccessGroupCreateDto | 

    try:
        # Create a new group
        api_response = api_instance.create48(access_group_create_dto)
        print("The response of AccessGroupControllerApi->create48:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessGroupControllerApi->create48: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_group_create_dto** | [**AccessGroupCreateDto**](AccessGroupCreateDto.md)|  | 

### Return type

[**AccessGroupDto**](AccessGroupDto.md)

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

# **delete_by_id5**
> delete_by_id5(id)

Delete group by id

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
    api_instance = openapi_client.AccessGroupControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete group by id
        api_instance.delete_by_id5(id)
    except Exception as e:
        print("Exception when calling AccessGroupControllerApi->delete_by_id5: %s\n" % e)
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

# **delete_projects**
> delete_projects(id, project_id)

Delete projects from group

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
    api_instance = openapi_client.AccessGroupControllerApi(api_client)
    id = 56 # int | 
    project_id = [56] # List[int] | 

    try:
        # Delete projects from group
        api_instance.delete_projects(id, project_id)
    except Exception as e:
        print("Exception when calling AccessGroupControllerApi->delete_projects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **project_id** | [**List[int]**](int.md)|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users1**
> delete_users1(id, username)

Delete users from group

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
    api_instance = openapi_client.AccessGroupControllerApi(api_client)
    id = 56 # int | 
    username = ['username_example'] # List[str] | 

    try:
        # Delete users from group
        api_instance.delete_users1(id, username)
    except Exception as e:
        print("Exception when calling AccessGroupControllerApi->delete_users1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_by_id**
> AccessGroupDto fetch_by_id(id)

Find group by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.access_group_dto import AccessGroupDto
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
    api_instance = openapi_client.AccessGroupControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find group by id
        api_response = api_instance.fetch_by_id(id)
        print("The response of AccessGroupControllerApi->fetch_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessGroupControllerApi->fetch_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AccessGroupDto**](AccessGroupDto.md)

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

# **find_all42**
> PageAccessGroupDto find_all42(query=query, project_id=project_id, page=page, size=size, sort=sort)

Find all groups

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_access_group_dto import PageAccessGroupDto
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
    api_instance = openapi_client.AccessGroupControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find all groups
        api_response = api_instance.find_all42(query=query, project_id=project_id, page=page, size=size, sort=sort)
        print("The response of AccessGroupControllerApi->find_all42:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessGroupControllerApi->find_all42: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageAccessGroupDto**](PageAccessGroupDto.md)

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

# **get_projects1**
> PageAccessGroupPaDto get_projects1(id, query=query, permissions_set_id=permissions_set_id, page=page, size=size, sort=sort)

Get group's projects

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_access_group_pa_dto import PageAccessGroupPaDto
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
    api_instance = openapi_client.AccessGroupControllerApi(api_client)
    id = 56 # int | 
    query = 'query_example' # str |  (optional)
    permissions_set_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Get group's projects
        api_response = api_instance.get_projects1(id, query=query, permissions_set_id=permissions_set_id, page=page, size=size, sort=sort)
        print("The response of AccessGroupControllerApi->get_projects1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessGroupControllerApi->get_projects1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **query** | **str**|  | [optional] 
 **permissions_set_id** | [**List[int]**](int.md)|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageAccessGroupPaDto**](PageAccessGroupPaDto.md)

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

# **get_users**
> PageAccessGroupUserDto get_users(id, query=query, page=page, size=size, sort=sort)

Get group's users

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_access_group_user_dto import PageAccessGroupUserDto
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
    api_instance = openapi_client.AccessGroupControllerApi(api_client)
    id = 56 # int | 
    query = 'query_example' # str |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["username,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["username,ASC"])

    try:
        # Get group's users
        api_response = api_instance.get_users(id, query=query, page=page, size=size, sort=sort)
        print("The response of AccessGroupControllerApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessGroupControllerApi->get_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **query** | **str**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;username,ASC&quot;]]

### Return type

[**PageAccessGroupUserDto**](PageAccessGroupUserDto.md)

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

# **patch_by_id**
> AccessGroupDto patch_by_id(id, access_group_patch_dto)

Patch group

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.access_group_dto import AccessGroupDto
from openapi_client.models.access_group_patch_dto import AccessGroupPatchDto
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
    api_instance = openapi_client.AccessGroupControllerApi(api_client)
    id = 56 # int | 
    access_group_patch_dto = openapi_client.AccessGroupPatchDto() # AccessGroupPatchDto | 

    try:
        # Patch group
        api_response = api_instance.patch_by_id(id, access_group_patch_dto)
        print("The response of AccessGroupControllerApi->patch_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessGroupControllerApi->patch_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **access_group_patch_dto** | [**AccessGroupPatchDto**](AccessGroupPatchDto.md)|  | 

### Return type

[**AccessGroupDto**](AccessGroupDto.md)

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

# **suggest23**
> PageIdAndNameOnlyDto suggest23(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggests groups

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_id_and_name_only_dto import PageIdAndNameOnlyDto
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
    api_instance = openapi_client.AccessGroupControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggests groups
        api_response = api_instance.suggest23(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of AccessGroupControllerApi->suggest23:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessGroupControllerApi->suggest23: %s\n" % e)
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

[**PageIdAndNameOnlyDto**](PageIdAndNameOnlyDto.md)

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

