# openapi_client.RoleSchemaControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create17**](RoleSchemaControllerApi.md#create17) | **POST** /roleschema | Create a new role schema
[**delete17**](RoleSchemaControllerApi.md#delete17) | **DELETE** /roleschema/{id} | Delete role schema by id
[**find_all16**](RoleSchemaControllerApi.md#find_all16) | **GET** /roleschema | Find all role schemas for given project
[**find_one14**](RoleSchemaControllerApi.md#find_one14) | **GET** /roleschema/{id} | Find role schema by id
[**patch16**](RoleSchemaControllerApi.md#patch16) | **PATCH** /roleschema/{id} | Patch role schema


# **create17**
> RoleSchemaDto create17(role_schema_create_dto)

Create a new role schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.role_schema_create_dto import RoleSchemaCreateDto
from openapi_client.models.role_schema_dto import RoleSchemaDto
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
    api_instance = openapi_client.RoleSchemaControllerApi(api_client)
    role_schema_create_dto = openapi_client.RoleSchemaCreateDto() # RoleSchemaCreateDto | 

    try:
        # Create a new role schema
        api_response = api_instance.create17(role_schema_create_dto)
        print("The response of RoleSchemaControllerApi->create17:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleSchemaControllerApi->create17: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_schema_create_dto** | [**RoleSchemaCreateDto**](RoleSchemaCreateDto.md)|  | 

### Return type

[**RoleSchemaDto**](RoleSchemaDto.md)

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

# **delete17**
> delete17(id)

Delete role schema by id

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
    api_instance = openapi_client.RoleSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete role schema by id
        api_instance.delete17(id)
    except Exception as e:
        print("Exception when calling RoleSchemaControllerApi->delete17: %s\n" % e)
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

# **find_all16**
> PageRoleSchemaDto find_all16(project_id, page=page, size=size, sort=sort)

Find all role schemas for given project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_role_schema_dto import PageRoleSchemaDto
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
    api_instance = openapi_client.RoleSchemaControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        # Find all role schemas for given project
        api_response = api_instance.find_all16(project_id, page=page, size=size, sort=sort)
        print("The response of RoleSchemaControllerApi->find_all16:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleSchemaControllerApi->find_all16: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageRoleSchemaDto**](PageRoleSchemaDto.md)

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

# **find_one14**
> RoleSchemaDto find_one14(id)

Find role schema by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.role_schema_dto import RoleSchemaDto
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
    api_instance = openapi_client.RoleSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find role schema by id
        api_response = api_instance.find_one14(id)
        print("The response of RoleSchemaControllerApi->find_one14:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleSchemaControllerApi->find_one14: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RoleSchemaDto**](RoleSchemaDto.md)

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

# **patch16**
> RoleSchemaDto patch16(id, role_schema_patch_dto)

Patch role schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.role_schema_dto import RoleSchemaDto
from openapi_client.models.role_schema_patch_dto import RoleSchemaPatchDto
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
    api_instance = openapi_client.RoleSchemaControllerApi(api_client)
    id = 56 # int | 
    role_schema_patch_dto = openapi_client.RoleSchemaPatchDto() # RoleSchemaPatchDto | 

    try:
        # Patch role schema
        api_response = api_instance.patch16(id, role_schema_patch_dto)
        print("The response of RoleSchemaControllerApi->patch16:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleSchemaControllerApi->patch16: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **role_schema_patch_dto** | [**RoleSchemaPatchDto**](RoleSchemaPatchDto.md)|  | 

### Return type

[**RoleSchemaDto**](RoleSchemaDto.md)

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

