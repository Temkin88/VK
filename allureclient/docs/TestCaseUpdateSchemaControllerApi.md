# openapi_client.TestCaseUpdateSchemaControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create12**](TestCaseUpdateSchemaControllerApi.md#create12) | **POST** /testcaseupdateschema | Create a new test case update schema
[**delete12**](TestCaseUpdateSchemaControllerApi.md#delete12) | **DELETE** /testcaseupdateschema/{id} | Delete test case update schema by id
[**find_all10**](TestCaseUpdateSchemaControllerApi.md#find_all10) | **GET** /testcaseupdateschema | Find all test case update schemas for given project
[**find_one10**](TestCaseUpdateSchemaControllerApi.md#find_one10) | **GET** /testcaseupdateschema/{id} | Find a test case update schemas by id
[**patch11**](TestCaseUpdateSchemaControllerApi.md#patch11) | **PATCH** /testcaseupdateschema/{id} | Patch test case update schema


# **create12**
> TestCaseUpdateSchemaDto create12(test_case_update_schema_create_dto)

Create a new test case update schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_update_schema_create_dto import TestCaseUpdateSchemaCreateDto
from openapi_client.models.test_case_update_schema_dto import TestCaseUpdateSchemaDto
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
    api_instance = openapi_client.TestCaseUpdateSchemaControllerApi(api_client)
    test_case_update_schema_create_dto = openapi_client.TestCaseUpdateSchemaCreateDto() # TestCaseUpdateSchemaCreateDto | 

    try:
        # Create a new test case update schema
        api_response = api_instance.create12(test_case_update_schema_create_dto)
        print("The response of TestCaseUpdateSchemaControllerApi->create12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseUpdateSchemaControllerApi->create12: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_update_schema_create_dto** | [**TestCaseUpdateSchemaCreateDto**](TestCaseUpdateSchemaCreateDto.md)|  | 

### Return type

[**TestCaseUpdateSchemaDto**](TestCaseUpdateSchemaDto.md)

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

# **delete12**
> delete12(id)

Delete test case update schema by id

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
    api_instance = openapi_client.TestCaseUpdateSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete test case update schema by id
        api_instance.delete12(id)
    except Exception as e:
        print("Exception when calling TestCaseUpdateSchemaControllerApi->delete12: %s\n" % e)
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

# **find_all10**
> List[TestCaseUpdateSchemaDto] find_all10(project_id)

Find all test case update schemas for given project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_update_schema_dto import TestCaseUpdateSchemaDto
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
    api_instance = openapi_client.TestCaseUpdateSchemaControllerApi(api_client)
    project_id = 56 # int | 

    try:
        # Find all test case update schemas for given project
        api_response = api_instance.find_all10(project_id)
        print("The response of TestCaseUpdateSchemaControllerApi->find_all10:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseUpdateSchemaControllerApi->find_all10: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**List[TestCaseUpdateSchemaDto]**](TestCaseUpdateSchemaDto.md)

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

# **find_one10**
> TestCaseUpdateSchemaDto find_one10(id)

Find a test case update schemas by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_update_schema_dto import TestCaseUpdateSchemaDto
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
    api_instance = openapi_client.TestCaseUpdateSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find a test case update schemas by id
        api_response = api_instance.find_one10(id)
        print("The response of TestCaseUpdateSchemaControllerApi->find_one10:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseUpdateSchemaControllerApi->find_one10: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestCaseUpdateSchemaDto**](TestCaseUpdateSchemaDto.md)

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

# **patch11**
> TestCaseUpdateSchemaDto patch11(id, test_case_update_schema_patch_dto)

Patch test case update schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_update_schema_dto import TestCaseUpdateSchemaDto
from openapi_client.models.test_case_update_schema_patch_dto import TestCaseUpdateSchemaPatchDto
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
    api_instance = openapi_client.TestCaseUpdateSchemaControllerApi(api_client)
    id = 56 # int | 
    test_case_update_schema_patch_dto = openapi_client.TestCaseUpdateSchemaPatchDto() # TestCaseUpdateSchemaPatchDto | 

    try:
        # Patch test case update schema
        api_response = api_instance.patch11(id, test_case_update_schema_patch_dto)
        print("The response of TestCaseUpdateSchemaControllerApi->patch11:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseUpdateSchemaControllerApi->patch11: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_case_update_schema_patch_dto** | [**TestCaseUpdateSchemaPatchDto**](TestCaseUpdateSchemaPatchDto.md)|  | 

### Return type

[**TestCaseUpdateSchemaDto**](TestCaseUpdateSchemaDto.md)

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

