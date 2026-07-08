# openapi_client.RoleControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create18**](RoleControllerApi.md#create18) | **POST** /role | Create a new role
[**delete18**](RoleControllerApi.md#delete18) | **DELETE** /role/{id} | Delete role by id
[**find_all17**](RoleControllerApi.md#find_all17) | **GET** /role | Find all roles
[**find_one15**](RoleControllerApi.md#find_one15) | **GET** /role/{id} | Find role by id
[**patch17**](RoleControllerApi.md#patch17) | **PATCH** /role/{id} | Patch a role
[**suggest8**](RoleControllerApi.md#suggest8) | **GET** /role/suggest | Suggest roles


# **create18**
> RoleDto create18(role_create_dto)

Create a new role

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.role_create_dto import RoleCreateDto
from openapi_client.models.role_dto import RoleDto
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
    api_instance = openapi_client.RoleControllerApi(api_client)
    role_create_dto = openapi_client.RoleCreateDto() # RoleCreateDto | 

    try:
        # Create a new role
        api_response = api_instance.create18(role_create_dto)
        print("The response of RoleControllerApi->create18:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleControllerApi->create18: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_create_dto** | [**RoleCreateDto**](RoleCreateDto.md)|  | 

### Return type

[**RoleDto**](RoleDto.md)

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

# **delete18**
> delete18(id)

Delete role by id

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
    api_instance = openapi_client.RoleControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete role by id
        api_instance.delete18(id)
    except Exception as e:
        print("Exception when calling RoleControllerApi->delete18: %s\n" % e)
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

# **find_all17**
> List[RoleDto] find_all17()

Find all roles

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.role_dto import RoleDto
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
    api_instance = openapi_client.RoleControllerApi(api_client)

    try:
        # Find all roles
        api_response = api_instance.find_all17()
        print("The response of RoleControllerApi->find_all17:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleControllerApi->find_all17: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[RoleDto]**](RoleDto.md)

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

# **find_one15**
> RoleDto find_one15(id)

Find role by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.role_dto import RoleDto
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
    api_instance = openapi_client.RoleControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find role by id
        api_response = api_instance.find_one15(id)
        print("The response of RoleControllerApi->find_one15:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleControllerApi->find_one15: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RoleDto**](RoleDto.md)

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

# **patch17**
> RoleDto patch17(id, role_patch_dto)

Patch a role

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.role_dto import RoleDto
from openapi_client.models.role_patch_dto import RolePatchDto
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
    api_instance = openapi_client.RoleControllerApi(api_client)
    id = 56 # int | 
    role_patch_dto = openapi_client.RolePatchDto() # RolePatchDto | 

    try:
        # Patch a role
        api_response = api_instance.patch17(id, role_patch_dto)
        print("The response of RoleControllerApi->patch17:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleControllerApi->patch17: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **role_patch_dto** | [**RolePatchDto**](RolePatchDto.md)|  | 

### Return type

[**RoleDto**](RoleDto.md)

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

# **suggest8**
> PageIdAndNameOnlyDto suggest8(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest roles

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
    api_instance = openapi_client.RoleControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest roles
        api_response = api_instance.suggest8(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of RoleControllerApi->suggest8:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleControllerApi->suggest8: %s\n" % e)
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

