# openapi_client.EnvVarValueControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create34**](EnvVarValueControllerApi.md#create34) | **POST** /evv | Create a new environment value
[**delete32**](EnvVarValueControllerApi.md#delete32) | **DELETE** /evv/{id} | Delete environment value by id
[**find_all34**](EnvVarValueControllerApi.md#find_all34) | **GET** /evv | Find all environment values
[**find_one28**](EnvVarValueControllerApi.md#find_one28) | **GET** /evv/{id} | Find environment value by id
[**patch31**](EnvVarValueControllerApi.md#patch31) | **PATCH** /evv/{id} | Patch environment value
[**suggest16**](EnvVarValueControllerApi.md#suggest16) | **GET** /evv/suggest | Suggest environment values


# **create34**
> EnvVarValueDto create34(env_var_value_create_dto)

Create a new environment value

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_value_create_dto import EnvVarValueCreateDto
from openapi_client.models.env_var_value_dto import EnvVarValueDto
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
    api_instance = openapi_client.EnvVarValueControllerApi(api_client)
    env_var_value_create_dto = openapi_client.EnvVarValueCreateDto() # EnvVarValueCreateDto | 

    try:
        # Create a new environment value
        api_response = api_instance.create34(env_var_value_create_dto)
        print("The response of EnvVarValueControllerApi->create34:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarValueControllerApi->create34: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_var_value_create_dto** | [**EnvVarValueCreateDto**](EnvVarValueCreateDto.md)|  | 

### Return type

[**EnvVarValueDto**](EnvVarValueDto.md)

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

# **delete32**
> delete32(id)

Delete environment value by id

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
    api_instance = openapi_client.EnvVarValueControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete environment value by id
        api_instance.delete32(id)
    except Exception as e:
        print("Exception when calling EnvVarValueControllerApi->delete32: %s\n" % e)
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

# **find_all34**
> List[EnvVarValueDto] find_all34(env_var_id)

Find all environment values

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_value_dto import EnvVarValueDto
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
    api_instance = openapi_client.EnvVarValueControllerApi(api_client)
    env_var_id = 56 # int | 

    try:
        # Find all environment values
        api_response = api_instance.find_all34(env_var_id)
        print("The response of EnvVarValueControllerApi->find_all34:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarValueControllerApi->find_all34: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_var_id** | **int**|  | 

### Return type

[**List[EnvVarValueDto]**](EnvVarValueDto.md)

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

# **find_one28**
> EnvVarValueDto find_one28(id)

Find environment value by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_value_dto import EnvVarValueDto
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
    api_instance = openapi_client.EnvVarValueControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find environment value by id
        api_response = api_instance.find_one28(id)
        print("The response of EnvVarValueControllerApi->find_one28:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarValueControllerApi->find_one28: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EnvVarValueDto**](EnvVarValueDto.md)

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

# **patch31**
> EnvVarValueDto patch31(id, env_var_value_patch_dto)

Patch environment value

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_value_dto import EnvVarValueDto
from openapi_client.models.env_var_value_patch_dto import EnvVarValuePatchDto
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
    api_instance = openapi_client.EnvVarValueControllerApi(api_client)
    id = 56 # int | 
    env_var_value_patch_dto = openapi_client.EnvVarValuePatchDto() # EnvVarValuePatchDto | 

    try:
        # Patch environment value
        api_response = api_instance.patch31(id, env_var_value_patch_dto)
        print("The response of EnvVarValueControllerApi->patch31:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarValueControllerApi->patch31: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **env_var_value_patch_dto** | [**EnvVarValuePatchDto**](EnvVarValuePatchDto.md)|  | 

### Return type

[**EnvVarValueDto**](EnvVarValueDto.md)

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

# **suggest16**
> PageIdAndNameOnlyDto suggest16(env_var_id=env_var_id, query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest environment values

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
    api_instance = openapi_client.EnvVarValueControllerApi(api_client)
    env_var_id = 56 # int |  (optional)
    query = 'query_example' # str |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest environment values
        api_response = api_instance.suggest16(env_var_id=env_var_id, query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of EnvVarValueControllerApi->suggest16:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarValueControllerApi->suggest16: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_var_id** | **int**|  | [optional] 
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

