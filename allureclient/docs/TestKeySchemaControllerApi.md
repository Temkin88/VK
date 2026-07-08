# openapi_client.TestKeySchemaControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create10**](TestKeySchemaControllerApi.md#create10) | **POST** /testkeyschema | Create a new test key schema
[**delete10**](TestKeySchemaControllerApi.md#delete10) | **DELETE** /testkeyschema/{id} | Delete a test key schema by id
[**find_all8**](TestKeySchemaControllerApi.md#find_all8) | **GET** /testkeyschema | Find all test key schemas for given project
[**find_one8**](TestKeySchemaControllerApi.md#find_one8) | **GET** /testkeyschema/{id} | Find a test key schema by id
[**patch9**](TestKeySchemaControllerApi.md#patch9) | **PATCH** /testkeyschema/{id} | Patch a test key schema


# **create10**
> TestKeySchemaDto create10(test_key_schema_create_dto)

Create a new test key schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_key_schema_create_dto import TestKeySchemaCreateDto
from openapi_client.models.test_key_schema_dto import TestKeySchemaDto
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
    api_instance = openapi_client.TestKeySchemaControllerApi(api_client)
    test_key_schema_create_dto = openapi_client.TestKeySchemaCreateDto() # TestKeySchemaCreateDto | 

    try:
        # Create a new test key schema
        api_response = api_instance.create10(test_key_schema_create_dto)
        print("The response of TestKeySchemaControllerApi->create10:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestKeySchemaControllerApi->create10: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_key_schema_create_dto** | [**TestKeySchemaCreateDto**](TestKeySchemaCreateDto.md)|  | 

### Return type

[**TestKeySchemaDto**](TestKeySchemaDto.md)

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

# **delete10**
> delete10(id)

Delete a test key schema by id

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
    api_instance = openapi_client.TestKeySchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete a test key schema by id
        api_instance.delete10(id)
    except Exception as e:
        print("Exception when calling TestKeySchemaControllerApi->delete10: %s\n" % e)
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

# **find_all8**
> PageTestKeySchemaDto find_all8(project_id, page=page, size=size, sort=sort)

Find all test key schemas for given project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_key_schema_dto import PageTestKeySchemaDto
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
    api_instance = openapi_client.TestKeySchemaControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["key,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["key,ASC"])

    try:
        # Find all test key schemas for given project
        api_response = api_instance.find_all8(project_id, page=page, size=size, sort=sort)
        print("The response of TestKeySchemaControllerApi->find_all8:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestKeySchemaControllerApi->find_all8: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;key,ASC&quot;]]

### Return type

[**PageTestKeySchemaDto**](PageTestKeySchemaDto.md)

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

# **find_one8**
> TestKeySchemaDto find_one8(id)

Find a test key schema by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_key_schema_dto import TestKeySchemaDto
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
    api_instance = openapi_client.TestKeySchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find a test key schema by id
        api_response = api_instance.find_one8(id)
        print("The response of TestKeySchemaControllerApi->find_one8:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestKeySchemaControllerApi->find_one8: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestKeySchemaDto**](TestKeySchemaDto.md)

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

# **patch9**
> TestKeySchemaDto patch9(id, test_key_schema_patch_dto)

Patch a test key schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_key_schema_dto import TestKeySchemaDto
from openapi_client.models.test_key_schema_patch_dto import TestKeySchemaPatchDto
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
    api_instance = openapi_client.TestKeySchemaControllerApi(api_client)
    id = 56 # int | 
    test_key_schema_patch_dto = openapi_client.TestKeySchemaPatchDto() # TestKeySchemaPatchDto | 

    try:
        # Patch a test key schema
        api_response = api_instance.patch9(id, test_key_schema_patch_dto)
        print("The response of TestKeySchemaControllerApi->patch9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestKeySchemaControllerApi->patch9: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_key_schema_patch_dto** | [**TestKeySchemaPatchDto**](TestKeySchemaPatchDto.md)|  | 

### Return type

[**TestKeySchemaDto**](TestKeySchemaDto.md)

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

