# openapi_client.WorkflowSchemaControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](WorkflowSchemaControllerApi.md#create) | **POST** /workflowschema | Create a new workflow schema
[**delete1**](WorkflowSchemaControllerApi.md#delete1) | **DELETE** /workflowschema/{id} | Delete workflow schema by given id
[**find_all**](WorkflowSchemaControllerApi.md#find_all) | **GET** /workflowschema | Find all workflow schemas for given project
[**find_one**](WorkflowSchemaControllerApi.md#find_one) | **GET** /workflowschema/{id} | Find workflow schema by given id
[**patch**](WorkflowSchemaControllerApi.md#patch) | **PATCH** /workflowschema/{id} | Update workflow schema


# **create**
> WorkflowSchemaDto create(workflow_schema_create_dto)

Create a new workflow schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.workflow_schema_create_dto import WorkflowSchemaCreateDto
from openapi_client.models.workflow_schema_dto import WorkflowSchemaDto
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
    api_instance = openapi_client.WorkflowSchemaControllerApi(api_client)
    workflow_schema_create_dto = openapi_client.WorkflowSchemaCreateDto() # WorkflowSchemaCreateDto | 

    try:
        # Create a new workflow schema
        api_response = api_instance.create(workflow_schema_create_dto)
        print("The response of WorkflowSchemaControllerApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowSchemaControllerApi->create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_schema_create_dto** | [**WorkflowSchemaCreateDto**](WorkflowSchemaCreateDto.md)|  | 

### Return type

[**WorkflowSchemaDto**](WorkflowSchemaDto.md)

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

# **delete1**
> delete1(id)

Delete workflow schema by given id

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
    api_instance = openapi_client.WorkflowSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete workflow schema by given id
        api_instance.delete1(id)
    except Exception as e:
        print("Exception when calling WorkflowSchemaControllerApi->delete1: %s\n" % e)
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

# **find_all**
> PageWorkflowSchemaDto find_all(project_id, page=page, size=size, sort=sort)

Find all workflow schemas for given project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_workflow_schema_dto import PageWorkflowSchemaDto
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
    api_instance = openapi_client.WorkflowSchemaControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["id,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["id,ASC"])

    try:
        # Find all workflow schemas for given project
        api_response = api_instance.find_all(project_id, page=page, size=size, sort=sort)
        print("The response of WorkflowSchemaControllerApi->find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowSchemaControllerApi->find_all: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;id,ASC&quot;]]

### Return type

[**PageWorkflowSchemaDto**](PageWorkflowSchemaDto.md)

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

# **find_one**
> WorkflowSchemaDto find_one(id)

Find workflow schema by given id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.workflow_schema_dto import WorkflowSchemaDto
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
    api_instance = openapi_client.WorkflowSchemaControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find workflow schema by given id
        api_response = api_instance.find_one(id)
        print("The response of WorkflowSchemaControllerApi->find_one:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowSchemaControllerApi->find_one: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**WorkflowSchemaDto**](WorkflowSchemaDto.md)

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

# **patch**
> WorkflowSchemaDto patch(id, workflow_schema_patch_dto)

Update workflow schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.workflow_schema_dto import WorkflowSchemaDto
from openapi_client.models.workflow_schema_patch_dto import WorkflowSchemaPatchDto
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
    api_instance = openapi_client.WorkflowSchemaControllerApi(api_client)
    id = 56 # int | 
    workflow_schema_patch_dto = openapi_client.WorkflowSchemaPatchDto() # WorkflowSchemaPatchDto | 

    try:
        # Update workflow schema
        api_response = api_instance.patch(id, workflow_schema_patch_dto)
        print("The response of WorkflowSchemaControllerApi->patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowSchemaControllerApi->patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **workflow_schema_patch_dto** | [**WorkflowSchemaPatchDto**](WorkflowSchemaPatchDto.md)|  | 

### Return type

[**WorkflowSchemaDto**](WorkflowSchemaDto.md)

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

