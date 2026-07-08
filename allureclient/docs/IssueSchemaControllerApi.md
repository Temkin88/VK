# openapi_client.IssueSchemaControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create28**](IssueSchemaControllerApi.md#create28) | **POST** /issueschema | Create a new issue schema
[**delete27**](IssueSchemaControllerApi.md#delete27) | **DELETE** /issueschema/{id} | Delete an issue schema by id
[**find_all27**](IssueSchemaControllerApi.md#find_all27) | **GET** /issueschema | Find all issue schemas for given project
[**find_one23**](IssueSchemaControllerApi.md#find_one23) | **GET** /issueschema/{id} | Find an issue schema by id
[**patch25**](IssueSchemaControllerApi.md#patch25) | **PATCH** /issueschema/{id} | Patch an issue schema


# **create28**
> IssueSchemaDto create28(issue_schema_create_dto)

Create a new issue schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.issue_schema_create_dto import IssueSchemaCreateDto
from openapi_client.models.issue_schema_dto import IssueSchemaDto
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
    api_instance = openapi_client.IssueSchemaControllerApi(api_client)
    issue_schema_create_dto = openapi_client.IssueSchemaCreateDto() # IssueSchemaCreateDto | 

    try:
        # Create a new issue schema
        api_response = api_instance.create28(issue_schema_create_dto)
        print("The response of IssueSchemaControllerApi->create28:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueSchemaControllerApi->create28: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_schema_create_dto** | [**IssueSchemaCreateDto**](IssueSchemaCreateDto.md)|  | 

### Return type

[**IssueSchemaDto**](IssueSchemaDto.md)

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

# **delete27**
> delete27(id)

Delete an issue schema by id

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
    api_instance = openapi_client.IssueSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete an issue schema by id
        api_instance.delete27(id)
    except Exception as e:
        print("Exception when calling IssueSchemaControllerApi->delete27: %s\n" % e)
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

# **find_all27**
> PageIssueSchemaDto find_all27(project_id, page=page, size=size, sort=sort)

Find all issue schemas for given project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_issue_schema_dto import PageIssueSchemaDto
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
    api_instance = openapi_client.IssueSchemaControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["key,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["key,ASC"])

    try:
        # Find all issue schemas for given project
        api_response = api_instance.find_all27(project_id, page=page, size=size, sort=sort)
        print("The response of IssueSchemaControllerApi->find_all27:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueSchemaControllerApi->find_all27: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;key,ASC&quot;]]

### Return type

[**PageIssueSchemaDto**](PageIssueSchemaDto.md)

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

# **find_one23**
> IssueSchemaDto find_one23(id)

Find an issue schema by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.issue_schema_dto import IssueSchemaDto
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
    api_instance = openapi_client.IssueSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find an issue schema by id
        api_response = api_instance.find_one23(id)
        print("The response of IssueSchemaControllerApi->find_one23:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueSchemaControllerApi->find_one23: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**IssueSchemaDto**](IssueSchemaDto.md)

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

# **patch25**
> IssueSchemaDto patch25(id, issue_schema_patch_dto)

Patch an issue schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.issue_schema_dto import IssueSchemaDto
from openapi_client.models.issue_schema_patch_dto import IssueSchemaPatchDto
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
    api_instance = openapi_client.IssueSchemaControllerApi(api_client)
    id = 56 # int | 
    issue_schema_patch_dto = openapi_client.IssueSchemaPatchDto() # IssueSchemaPatchDto | 

    try:
        # Patch an issue schema
        api_response = api_instance.patch25(id, issue_schema_patch_dto)
        print("The response of IssueSchemaControllerApi->patch25:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueSchemaControllerApi->patch25: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **issue_schema_patch_dto** | [**IssueSchemaPatchDto**](IssueSchemaPatchDto.md)|  | 

### Return type

[**IssueSchemaDto**](IssueSchemaDto.md)

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

