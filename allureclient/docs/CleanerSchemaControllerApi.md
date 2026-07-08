# openapi_client.CleanerSchemaControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create42**](CleanerSchemaControllerApi.md#create42) | **POST** /cleanerschema | Create a new cleaner schema
[**delete40**](CleanerSchemaControllerApi.md#delete40) | **DELETE** /cleanerschema/{id} | Delete cleaner schema by id
[**find_all39**](CleanerSchemaControllerApi.md#find_all39) | **GET** /cleanerschema | Find all cleaner schemas for given project
[**find_all_global_schemas**](CleanerSchemaControllerApi.md#find_all_global_schemas) | **GET** /cleanerschema/global | Find all global cleaner schemas
[**find_one34**](CleanerSchemaControllerApi.md#find_one34) | **GET** /cleanerschema/{id} | Find cleaner schema by id
[**patch39**](CleanerSchemaControllerApi.md#patch39) | **PATCH** /cleanerschema/{id} | Patch cleaner schema


# **create42**
> CleanerSchemaDto create42(cleaner_schema_create_dto)

Create a new cleaner schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.cleaner_schema_create_dto import CleanerSchemaCreateDto
from openapi_client.models.cleaner_schema_dto import CleanerSchemaDto
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
    api_instance = openapi_client.CleanerSchemaControllerApi(api_client)
    cleaner_schema_create_dto = openapi_client.CleanerSchemaCreateDto() # CleanerSchemaCreateDto | 

    try:
        # Create a new cleaner schema
        api_response = api_instance.create42(cleaner_schema_create_dto)
        print("The response of CleanerSchemaControllerApi->create42:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CleanerSchemaControllerApi->create42: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cleaner_schema_create_dto** | [**CleanerSchemaCreateDto**](CleanerSchemaCreateDto.md)|  | 

### Return type

[**CleanerSchemaDto**](CleanerSchemaDto.md)

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

# **delete40**
> delete40(id)

Delete cleaner schema by id

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
    api_instance = openapi_client.CleanerSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete cleaner schema by id
        api_instance.delete40(id)
    except Exception as e:
        print("Exception when calling CleanerSchemaControllerApi->delete40: %s\n" % e)
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

# **find_all39**
> PageCleanerSchemaDto find_all39(project_id, page=page, size=size, sort=sort)

Find all cleaner schemas for given project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_cleaner_schema_dto import PageCleanerSchemaDto
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
    api_instance = openapi_client.CleanerSchemaControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["id,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["id,ASC"])

    try:
        # Find all cleaner schemas for given project
        api_response = api_instance.find_all39(project_id, page=page, size=size, sort=sort)
        print("The response of CleanerSchemaControllerApi->find_all39:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CleanerSchemaControllerApi->find_all39: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;id,ASC&quot;]]

### Return type

[**PageCleanerSchemaDto**](PageCleanerSchemaDto.md)

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

# **find_all_global_schemas**
> PageCleanerSchemaDto find_all_global_schemas(page=page, size=size, sort=sort)

Find all global cleaner schemas

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_cleaner_schema_dto import PageCleanerSchemaDto
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
    api_instance = openapi_client.CleanerSchemaControllerApi(api_client)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["id,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["id,ASC"])

    try:
        # Find all global cleaner schemas
        api_response = api_instance.find_all_global_schemas(page=page, size=size, sort=sort)
        print("The response of CleanerSchemaControllerApi->find_all_global_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CleanerSchemaControllerApi->find_all_global_schemas: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;id,ASC&quot;]]

### Return type

[**PageCleanerSchemaDto**](PageCleanerSchemaDto.md)

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

# **find_one34**
> CleanerSchemaDto find_one34(id)

Find cleaner schema by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.cleaner_schema_dto import CleanerSchemaDto
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
    api_instance = openapi_client.CleanerSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find cleaner schema by id
        api_response = api_instance.find_one34(id)
        print("The response of CleanerSchemaControllerApi->find_one34:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CleanerSchemaControllerApi->find_one34: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CleanerSchemaDto**](CleanerSchemaDto.md)

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

# **patch39**
> CleanerSchemaDto patch39(id, cleaner_schema_patch_dto)

Patch cleaner schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.cleaner_schema_dto import CleanerSchemaDto
from openapi_client.models.cleaner_schema_patch_dto import CleanerSchemaPatchDto
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
    api_instance = openapi_client.CleanerSchemaControllerApi(api_client)
    id = 56 # int | 
    cleaner_schema_patch_dto = openapi_client.CleanerSchemaPatchDto() # CleanerSchemaPatchDto | 

    try:
        # Patch cleaner schema
        api_response = api_instance.patch39(id, cleaner_schema_patch_dto)
        print("The response of CleanerSchemaControllerApi->patch39:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CleanerSchemaControllerApi->patch39: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **cleaner_schema_patch_dto** | [**CleanerSchemaPatchDto**](CleanerSchemaPatchDto.md)|  | 

### Return type

[**CleanerSchemaDto**](CleanerSchemaDto.md)

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

