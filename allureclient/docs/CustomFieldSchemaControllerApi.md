# openapi_client.CustomFieldSchemaControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create44**](CustomFieldSchemaControllerApi.md#create44) | **POST** /cfschema | Create a new custom field schema
[**delete42**](CustomFieldSchemaControllerApi.md#delete42) | **DELETE** /cfschema/{id} | Delete custom field schema by id
[**find_all41**](CustomFieldSchemaControllerApi.md#find_all41) | **GET** /cfschema | Find all custom field schemas for given project
[**find_one36**](CustomFieldSchemaControllerApi.md#find_one36) | **GET** /cfschema/{id} | Find custom field schema by id
[**patch41**](CustomFieldSchemaControllerApi.md#patch41) | **PATCH** /cfschema/{id} | Patch custom field schema


# **create44**
> CustomFieldSchemaDto create44(custom_field_schema_create_dto)

Create a new custom field schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_schema_create_dto import CustomFieldSchemaCreateDto
from openapi_client.models.custom_field_schema_dto import CustomFieldSchemaDto
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
    api_instance = openapi_client.CustomFieldSchemaControllerApi(api_client)
    custom_field_schema_create_dto = openapi_client.CustomFieldSchemaCreateDto() # CustomFieldSchemaCreateDto | 

    try:
        # Create a new custom field schema
        api_response = api_instance.create44(custom_field_schema_create_dto)
        print("The response of CustomFieldSchemaControllerApi->create44:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldSchemaControllerApi->create44: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_schema_create_dto** | [**CustomFieldSchemaCreateDto**](CustomFieldSchemaCreateDto.md)|  | 

### Return type

[**CustomFieldSchemaDto**](CustomFieldSchemaDto.md)

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

# **delete42**
> delete42(id)

Delete custom field schema by id

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
    api_instance = openapi_client.CustomFieldSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete custom field schema by id
        api_instance.delete42(id)
    except Exception as e:
        print("Exception when calling CustomFieldSchemaControllerApi->delete42: %s\n" % e)
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

# **find_all41**
> PageCustomFieldSchemaDto find_all41(project_id, page=page, size=size, sort=sort)

Find all custom field schemas for given project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_custom_field_schema_dto import PageCustomFieldSchemaDto
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
    api_instance = openapi_client.CustomFieldSchemaControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["id,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["id,ASC"])

    try:
        # Find all custom field schemas for given project
        api_response = api_instance.find_all41(project_id, page=page, size=size, sort=sort)
        print("The response of CustomFieldSchemaControllerApi->find_all41:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldSchemaControllerApi->find_all41: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;id,ASC&quot;]]

### Return type

[**PageCustomFieldSchemaDto**](PageCustomFieldSchemaDto.md)

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

# **find_one36**
> CustomFieldSchemaDto find_one36(id)

Find custom field schema by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_schema_dto import CustomFieldSchemaDto
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
    api_instance = openapi_client.CustomFieldSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find custom field schema by id
        api_response = api_instance.find_one36(id)
        print("The response of CustomFieldSchemaControllerApi->find_one36:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldSchemaControllerApi->find_one36: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CustomFieldSchemaDto**](CustomFieldSchemaDto.md)

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

# **patch41**
> CustomFieldSchemaDto patch41(id, custom_field_schema_patch_dto)

Patch custom field schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_schema_dto import CustomFieldSchemaDto
from openapi_client.models.custom_field_schema_patch_dto import CustomFieldSchemaPatchDto
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
    api_instance = openapi_client.CustomFieldSchemaControllerApi(api_client)
    id = 56 # int | 
    custom_field_schema_patch_dto = openapi_client.CustomFieldSchemaPatchDto() # CustomFieldSchemaPatchDto | 

    try:
        # Patch custom field schema
        api_response = api_instance.patch41(id, custom_field_schema_patch_dto)
        print("The response of CustomFieldSchemaControllerApi->patch41:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldSchemaControllerApi->patch41: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **custom_field_schema_patch_dto** | [**CustomFieldSchemaPatchDto**](CustomFieldSchemaPatchDto.md)|  | 

### Return type

[**CustomFieldSchemaDto**](CustomFieldSchemaDto.md)

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

