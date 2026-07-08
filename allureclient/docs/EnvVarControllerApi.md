# openapi_client.EnvVarControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create36**](EnvVarControllerApi.md#create36) | **POST** /ev | Create a new environment variable
[**create37**](EnvVarControllerApi.md#create37) | **POST** /environment | Create a new environment variable
[**delete34**](EnvVarControllerApi.md#delete34) | **DELETE** /environment/{id} | Delete environment variable by id
[**delete35**](EnvVarControllerApi.md#delete35) | **DELETE** /ev/{id} | Delete environment variable by id
[**find_all36**](EnvVarControllerApi.md#find_all36) | **GET** /ev | Find all environment variables
[**find_all37**](EnvVarControllerApi.md#find_all37) | **GET** /environment | Find all environment variables
[**find_one30**](EnvVarControllerApi.md#find_one30) | **GET** /environment/{id} | Find environment variable by id
[**find_one31**](EnvVarControllerApi.md#find_one31) | **GET** /ev/{id} | Find environment variable by id
[**merge1**](EnvVarControllerApi.md#merge1) | **POST** /ev/merge | Merge environment variables
[**merge2**](EnvVarControllerApi.md#merge2) | **POST** /environment/merge | Merge environment variables
[**patch33**](EnvVarControllerApi.md#patch33) | **PATCH** /environment/{id} | Patch environment variable
[**patch34**](EnvVarControllerApi.md#patch34) | **PATCH** /ev/{id} | Patch environment variable
[**suggest17**](EnvVarControllerApi.md#suggest17) | **GET** /environment/suggest | Suggest environment variables
[**suggest18**](EnvVarControllerApi.md#suggest18) | **GET** /ev/suggest | Suggest environment variables


# **create36**
> EnvVarDto create36(env_var_create_dto)

Create a new environment variable

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_create_dto import EnvVarCreateDto
from openapi_client.models.env_var_dto import EnvVarDto
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
    api_instance = openapi_client.EnvVarControllerApi(api_client)
    env_var_create_dto = openapi_client.EnvVarCreateDto() # EnvVarCreateDto | 

    try:
        # Create a new environment variable
        api_response = api_instance.create36(env_var_create_dto)
        print("The response of EnvVarControllerApi->create36:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->create36: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_var_create_dto** | [**EnvVarCreateDto**](EnvVarCreateDto.md)|  | 

### Return type

[**EnvVarDto**](EnvVarDto.md)

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

# **create37**
> EnvVarDto create37(env_var_create_dto)

Create a new environment variable

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_create_dto import EnvVarCreateDto
from openapi_client.models.env_var_dto import EnvVarDto
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
    api_instance = openapi_client.EnvVarControllerApi(api_client)
    env_var_create_dto = openapi_client.EnvVarCreateDto() # EnvVarCreateDto | 

    try:
        # Create a new environment variable
        api_response = api_instance.create37(env_var_create_dto)
        print("The response of EnvVarControllerApi->create37:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->create37: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_var_create_dto** | [**EnvVarCreateDto**](EnvVarCreateDto.md)|  | 

### Return type

[**EnvVarDto**](EnvVarDto.md)

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

# **delete34**
> delete34(id)

Delete environment variable by id

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
    api_instance = openapi_client.EnvVarControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete environment variable by id
        api_instance.delete34(id)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->delete34: %s\n" % e)
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

# **delete35**
> delete35(id)

Delete environment variable by id

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
    api_instance = openapi_client.EnvVarControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete environment variable by id
        api_instance.delete35(id)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->delete35: %s\n" % e)
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

# **find_all36**
> List[EnvVarDto] find_all36()

Find all environment variables

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_dto import EnvVarDto
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
    api_instance = openapi_client.EnvVarControllerApi(api_client)

    try:
        # Find all environment variables
        api_response = api_instance.find_all36()
        print("The response of EnvVarControllerApi->find_all36:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->find_all36: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[EnvVarDto]**](EnvVarDto.md)

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

# **find_all37**
> List[EnvVarDto] find_all37()

Find all environment variables

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_dto import EnvVarDto
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
    api_instance = openapi_client.EnvVarControllerApi(api_client)

    try:
        # Find all environment variables
        api_response = api_instance.find_all37()
        print("The response of EnvVarControllerApi->find_all37:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->find_all37: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[EnvVarDto]**](EnvVarDto.md)

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

# **find_one30**
> EnvVarDto find_one30(id)

Find environment variable by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_dto import EnvVarDto
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
    api_instance = openapi_client.EnvVarControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find environment variable by id
        api_response = api_instance.find_one30(id)
        print("The response of EnvVarControllerApi->find_one30:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->find_one30: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EnvVarDto**](EnvVarDto.md)

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

# **find_one31**
> EnvVarDto find_one31(id)

Find environment variable by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_dto import EnvVarDto
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
    api_instance = openapi_client.EnvVarControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find environment variable by id
        api_response = api_instance.find_one31(id)
        print("The response of EnvVarControllerApi->find_one31:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->find_one31: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EnvVarDto**](EnvVarDto.md)

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

# **merge1**
> merge1(env_var_merge_dto)

Merge environment variables

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_merge_dto import EnvVarMergeDto
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
    api_instance = openapi_client.EnvVarControllerApi(api_client)
    env_var_merge_dto = openapi_client.EnvVarMergeDto() # EnvVarMergeDto | 

    try:
        # Merge environment variables
        api_instance.merge1(env_var_merge_dto)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->merge1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_var_merge_dto** | [**EnvVarMergeDto**](EnvVarMergeDto.md)|  | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge2**
> merge2(env_var_merge_dto)

Merge environment variables

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_merge_dto import EnvVarMergeDto
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
    api_instance = openapi_client.EnvVarControllerApi(api_client)
    env_var_merge_dto = openapi_client.EnvVarMergeDto() # EnvVarMergeDto | 

    try:
        # Merge environment variables
        api_instance.merge2(env_var_merge_dto)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->merge2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_var_merge_dto** | [**EnvVarMergeDto**](EnvVarMergeDto.md)|  | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch33**
> EnvVarDto patch33(id, env_var_patch_dto)

Patch environment variable

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_dto import EnvVarDto
from openapi_client.models.env_var_patch_dto import EnvVarPatchDto
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
    api_instance = openapi_client.EnvVarControllerApi(api_client)
    id = 56 # int | 
    env_var_patch_dto = openapi_client.EnvVarPatchDto() # EnvVarPatchDto | 

    try:
        # Patch environment variable
        api_response = api_instance.patch33(id, env_var_patch_dto)
        print("The response of EnvVarControllerApi->patch33:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->patch33: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **env_var_patch_dto** | [**EnvVarPatchDto**](EnvVarPatchDto.md)|  | 

### Return type

[**EnvVarDto**](EnvVarDto.md)

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

# **patch34**
> EnvVarDto patch34(id, env_var_patch_dto)

Patch environment variable

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_dto import EnvVarDto
from openapi_client.models.env_var_patch_dto import EnvVarPatchDto
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
    api_instance = openapi_client.EnvVarControllerApi(api_client)
    id = 56 # int | 
    env_var_patch_dto = openapi_client.EnvVarPatchDto() # EnvVarPatchDto | 

    try:
        # Patch environment variable
        api_response = api_instance.patch34(id, env_var_patch_dto)
        print("The response of EnvVarControllerApi->patch34:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->patch34: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **env_var_patch_dto** | [**EnvVarPatchDto**](EnvVarPatchDto.md)|  | 

### Return type

[**EnvVarDto**](EnvVarDto.md)

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

# **suggest17**
> PageIdAndNameOnlyDto suggest17(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest environment variables

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
    api_instance = openapi_client.EnvVarControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest environment variables
        api_response = api_instance.suggest17(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of EnvVarControllerApi->suggest17:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->suggest17: %s\n" % e)
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

# **suggest18**
> PageIdAndNameOnlyDto suggest18(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest environment variables

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
    api_instance = openapi_client.EnvVarControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest environment variables
        api_response = api_instance.suggest18(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of EnvVarControllerApi->suggest18:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvVarControllerApi->suggest18: %s\n" % e)
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

