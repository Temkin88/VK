# openapi_client.PermissionSetControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create21**](PermissionSetControllerApi.md#create21) | **POST** /permissionset | Create a new permission set
[**delete21**](PermissionSetControllerApi.md#delete21) | **DELETE** /permissionset/{id} | Delete permission set by id
[**find_all23**](PermissionSetControllerApi.md#find_all23) | **GET** /permissionset | Find all permission sets
[**find_one18**](PermissionSetControllerApi.md#find_one18) | **GET** /permissionset/{id} | Find permission set by id
[**patch20**](PermissionSetControllerApi.md#patch20) | **PATCH** /permissionset/{id} | Patch permission set
[**suggest9**](PermissionSetControllerApi.md#suggest9) | **GET** /permissionset/suggest | Suggests permission sets


# **create21**
> PermissionSetDto create21(permission_set_create_dto)

Create a new permission set

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.permission_set_create_dto import PermissionSetCreateDto
from openapi_client.models.permission_set_dto import PermissionSetDto
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
    api_instance = openapi_client.PermissionSetControllerApi(api_client)
    permission_set_create_dto = openapi_client.PermissionSetCreateDto() # PermissionSetCreateDto | 

    try:
        # Create a new permission set
        api_response = api_instance.create21(permission_set_create_dto)
        print("The response of PermissionSetControllerApi->create21:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionSetControllerApi->create21: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_set_create_dto** | [**PermissionSetCreateDto**](PermissionSetCreateDto.md)|  | 

### Return type

[**PermissionSetDto**](PermissionSetDto.md)

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

# **delete21**
> delete21(id)

Delete permission set by id

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
    api_instance = openapi_client.PermissionSetControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete permission set by id
        api_instance.delete21(id)
    except Exception as e:
        print("Exception when calling PermissionSetControllerApi->delete21: %s\n" % e)
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

# **find_all23**
> PagePermissionSetDto find_all23(page=page, size=size, sort=sort)

Find all permission sets

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_permission_set_dto import PagePermissionSetDto
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
    api_instance = openapi_client.PermissionSetControllerApi(api_client)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find all permission sets
        api_response = api_instance.find_all23(page=page, size=size, sort=sort)
        print("The response of PermissionSetControllerApi->find_all23:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionSetControllerApi->find_all23: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PagePermissionSetDto**](PagePermissionSetDto.md)

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

# **find_one18**
> PermissionSetDto find_one18(id)

Find permission set by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.permission_set_dto import PermissionSetDto
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
    api_instance = openapi_client.PermissionSetControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find permission set by id
        api_response = api_instance.find_one18(id)
        print("The response of PermissionSetControllerApi->find_one18:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionSetControllerApi->find_one18: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PermissionSetDto**](PermissionSetDto.md)

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

# **patch20**
> PermissionSetDto patch20(id, permission_set_patch_dto)

Patch permission set

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.permission_set_dto import PermissionSetDto
from openapi_client.models.permission_set_patch_dto import PermissionSetPatchDto
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
    api_instance = openapi_client.PermissionSetControllerApi(api_client)
    id = 56 # int | 
    permission_set_patch_dto = openapi_client.PermissionSetPatchDto() # PermissionSetPatchDto | 

    try:
        # Patch permission set
        api_response = api_instance.patch20(id, permission_set_patch_dto)
        print("The response of PermissionSetControllerApi->patch20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionSetControllerApi->patch20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **permission_set_patch_dto** | [**PermissionSetPatchDto**](PermissionSetPatchDto.md)|  | 

### Return type

[**PermissionSetDto**](PermissionSetDto.md)

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

# **suggest9**
> PageIdAndNameOnlyDto suggest9(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggests permission sets

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
    api_instance = openapi_client.PermissionSetControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggests permission sets
        api_response = api_instance.suggest9(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of PermissionSetControllerApi->suggest9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionSetControllerApi->suggest9: %s\n" % e)
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

