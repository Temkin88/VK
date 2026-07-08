# openapi_client.WorkflowControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create1**](WorkflowControllerApi.md#create1) | **POST** /workflow | Create a new workflow
[**delete2**](WorkflowControllerApi.md#delete2) | **DELETE** /workflow/{id} | Delete workflow by given id
[**find_all1**](WorkflowControllerApi.md#find_all1) | **GET** /workflow | Find all workflows
[**find_one1**](WorkflowControllerApi.md#find_one1) | **GET** /workflow/{id} | Find workflow by given id
[**patch1**](WorkflowControllerApi.md#patch1) | **PATCH** /workflow/{id} | Patch workflow
[**suggest**](WorkflowControllerApi.md#suggest) | **GET** /workflow/suggest | Suggest workflows


# **create1**
> WorkflowDto create1(workflow_create_dto)

Create a new workflow

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.workflow_create_dto import WorkflowCreateDto
from openapi_client.models.workflow_dto import WorkflowDto
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
    api_instance = openapi_client.WorkflowControllerApi(api_client)
    workflow_create_dto = openapi_client.WorkflowCreateDto() # WorkflowCreateDto | 

    try:
        # Create a new workflow
        api_response = api_instance.create1(workflow_create_dto)
        print("The response of WorkflowControllerApi->create1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowControllerApi->create1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_create_dto** | [**WorkflowCreateDto**](WorkflowCreateDto.md)|  | 

### Return type

[**WorkflowDto**](WorkflowDto.md)

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

# **delete2**
> delete2(id)

Delete workflow by given id

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
    api_instance = openapi_client.WorkflowControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete workflow by given id
        api_instance.delete2(id)
    except Exception as e:
        print("Exception when calling WorkflowControllerApi->delete2: %s\n" % e)
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

# **find_all1**
> PageWorkflowDto find_all1(page=page, size=size, sort=sort)

Find all workflows

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_workflow_dto import PageWorkflowDto
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
    api_instance = openapi_client.WorkflowControllerApi(api_client)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find all workflows
        api_response = api_instance.find_all1(page=page, size=size, sort=sort)
        print("The response of WorkflowControllerApi->find_all1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowControllerApi->find_all1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageWorkflowDto**](PageWorkflowDto.md)

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

# **find_one1**
> WorkflowDto find_one1(id)

Find workflow by given id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.workflow_dto import WorkflowDto
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
    api_instance = openapi_client.WorkflowControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find workflow by given id
        api_response = api_instance.find_one1(id)
        print("The response of WorkflowControllerApi->find_one1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowControllerApi->find_one1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**WorkflowDto**](WorkflowDto.md)

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

# **patch1**
> WorkflowDto patch1(id, workflow_patch_dto)

Patch workflow

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.workflow_dto import WorkflowDto
from openapi_client.models.workflow_patch_dto import WorkflowPatchDto
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
    api_instance = openapi_client.WorkflowControllerApi(api_client)
    id = 56 # int | 
    workflow_patch_dto = openapi_client.WorkflowPatchDto() # WorkflowPatchDto | 

    try:
        # Patch workflow
        api_response = api_instance.patch1(id, workflow_patch_dto)
        print("The response of WorkflowControllerApi->patch1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowControllerApi->patch1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **workflow_patch_dto** | [**WorkflowPatchDto**](WorkflowPatchDto.md)|  | 

### Return type

[**WorkflowDto**](WorkflowDto.md)

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

# **suggest**
> PageIdAndNameOnlyDto suggest(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest workflows

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
    api_instance = openapi_client.WorkflowControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest workflows
        api_response = api_instance.suggest(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of WorkflowControllerApi->suggest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowControllerApi->suggest: %s\n" % e)
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

