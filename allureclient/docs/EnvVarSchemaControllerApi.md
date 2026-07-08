# openapi_client.EnvVarSchemaControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create35**](EnvVarSchemaControllerApi.md#create35) | **POST** /evschema | Create a new env var schema
[**delete33**](EnvVarSchemaControllerApi.md#delete33) | **DELETE** /evschema/{id} | Delete env var schema by id
[**find_all35**](EnvVarSchemaControllerApi.md#find_all35) | **GET** /evschema | Find all env var schemas for given project
[**find_one29**](EnvVarSchemaControllerApi.md#find_one29) | **GET** /evschema/{id} | Find env var schema by id
[**patch32**](EnvVarSchemaControllerApi.md#patch32) | **PATCH** /evschema/{id} | Patch env var schema


# **create35**
> EnvVarSchemaDto create35(env_var_schema_create_dto)

Create a new env var schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_schema_create_dto import EnvVarSchemaCreateDto
from openapi_client.models.env_var_schema_dto import EnvVarSchemaDto
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
    api_instance = openapi_client.EnvVarSchemaControllerApi(api_client)
    env_var_schema_create_dto = openapi_client.EnvVarSchemaCreateDto() # EnvVarSchemaCreateDto | 

    try:
        # Create a new env var schema
        api_response = api_instance.create35(env_var_schema_create_dto)
        print("The response of EnvVarSchemaControllerApi->create35:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarSchemaControllerApi->create35: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_var_schema_create_dto** | [**EnvVarSchemaCreateDto**](EnvVarSchemaCreateDto.md)|  | 

### Return type

[**EnvVarSchemaDto**](EnvVarSchemaDto.md)

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

# **delete33**
> delete33(id)

Delete env var schema by id

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
    api_instance = openapi_client.EnvVarSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete env var schema by id
        api_instance.delete33(id)
    except Exception as e:
        print("Exception when calling EnvVarSchemaControllerApi->delete33: %s\n" % e)
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

# **find_all35**
> PageEnvVarSchemaDto find_all35(project_id, page=page, size=size, sort=sort)

Find all env var schemas for given project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_env_var_schema_dto import PageEnvVarSchemaDto
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
    api_instance = openapi_client.EnvVarSchemaControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        # Find all env var schemas for given project
        api_response = api_instance.find_all35(project_id, page=page, size=size, sort=sort)
        print("The response of EnvVarSchemaControllerApi->find_all35:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarSchemaControllerApi->find_all35: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageEnvVarSchemaDto**](PageEnvVarSchemaDto.md)

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

# **find_one29**
> EnvVarSchemaDto find_one29(id)

Find env var schema by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_schema_dto import EnvVarSchemaDto
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
    api_instance = openapi_client.EnvVarSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find env var schema by id
        api_response = api_instance.find_one29(id)
        print("The response of EnvVarSchemaControllerApi->find_one29:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarSchemaControllerApi->find_one29: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EnvVarSchemaDto**](EnvVarSchemaDto.md)

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

# **patch32**
> EnvVarSchemaDto patch32(id, env_var_schema_patch_dto)

Patch env var schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_schema_dto import EnvVarSchemaDto
from openapi_client.models.env_var_schema_patch_dto import EnvVarSchemaPatchDto
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
    api_instance = openapi_client.EnvVarSchemaControllerApi(api_client)
    id = 56 # int | 
    env_var_schema_patch_dto = openapi_client.EnvVarSchemaPatchDto() # EnvVarSchemaPatchDto | 

    try:
        # Patch env var schema
        api_response = api_instance.patch32(id, env_var_schema_patch_dto)
        print("The response of EnvVarSchemaControllerApi->patch32:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarSchemaControllerApi->patch32: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **env_var_schema_patch_dto** | [**EnvVarSchemaPatchDto**](EnvVarSchemaPatchDto.md)|  | 

### Return type

[**EnvVarSchemaDto**](EnvVarSchemaDto.md)

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

