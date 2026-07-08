# openapi_client.TestCaseControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create13**](TestCaseControllerApi.md#create13) | **POST** /testcase | Create a new test case
[**delete13**](TestCaseControllerApi.md#delete13) | **DELETE** /testcase/{id} | Delete test case by id
[**detach_automation**](TestCaseControllerApi.md#detach_automation) | **POST** /testcase/{id}/detachautomation | Detach automation from test case
[**find_all11**](TestCaseControllerApi.md#find_all11) | **GET** /testcase | Find all test cases for specified project
[**find_all_deleted**](TestCaseControllerApi.md#find_all_deleted) | **GET** /testcase/deleted | Find all deleted test cases for given project
[**find_all_muted**](TestCaseControllerApi.md#find_all_muted) | **GET** /testcase/muted | Find all muted test cases for given project
[**find_history1**](TestCaseControllerApi.md#find_history1) | **GET** /testcase/{id}/history | Find run history for test case
[**find_history2**](TestCaseControllerApi.md#find_history2) | **GET** /testcase/history | Find run history for test case
[**find_one11**](TestCaseControllerApi.md#find_one11) | **GET** /testcase/{id} | Find test case by id
[**find_workflow**](TestCaseControllerApi.md#find_workflow) | **GET** /testcase/{id}/workflow | Find workflow for test case
[**patch12**](TestCaseControllerApi.md#patch12) | **PATCH** /testcase/{id} | 
[**restore**](TestCaseControllerApi.md#restore) | **POST** /testcase/{id}/restore | Restore test case by id
[**suggest5**](TestCaseControllerApi.md#suggest5) | **GET** /testcase/suggest | Find suggest for test case


# **create13**
> TestCaseDto create13(test_case_create_dto)

Create a new test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_create_dto import TestCaseCreateDto
from openapi_client.models.test_case_dto import TestCaseDto
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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    test_case_create_dto = openapi_client.TestCaseCreateDto() # TestCaseCreateDto | 

    try:
        # Create a new test case
        api_response = api_instance.create13(test_case_create_dto)
        print("The response of TestCaseControllerApi->create13:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->create13: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_create_dto** | [**TestCaseCreateDto**](TestCaseCreateDto.md)|  | 

### Return type

[**TestCaseDto**](TestCaseDto.md)

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

# **delete13**
> delete13(id, force=force)

Delete test case by id

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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    id = 56 # int | 
    force = True # bool |  (optional)

    try:
        # Delete test case by id
        api_instance.delete13(id, force=force)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->delete13: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **force** | **bool**|  | [optional] 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_automation**
> TestCaseDto detach_automation(id, test_case_detach_automation_rq_dto)

Detach automation from test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_detach_automation_rq_dto import TestCaseDetachAutomationRqDto
from openapi_client.models.test_case_dto import TestCaseDto
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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    id = 56 # int | 
    test_case_detach_automation_rq_dto = openapi_client.TestCaseDetachAutomationRqDto() # TestCaseDetachAutomationRqDto | 

    try:
        # Detach automation from test case
        api_response = api_instance.detach_automation(id, test_case_detach_automation_rq_dto)
        print("The response of TestCaseControllerApi->detach_automation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->detach_automation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_case_detach_automation_rq_dto** | [**TestCaseDetachAutomationRqDto**](TestCaseDetachAutomationRqDto.md)|  | 

### Return type

[**TestCaseDto**](TestCaseDto.md)

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

# **find_all11**
> PageTestCaseRowDto find_all11(project_id, page=page, size=size, sort=sort)

Find all test cases for specified project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_case_row_dto import PageTestCaseRowDto
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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,DESC"])

    try:
        # Find all test cases for specified project
        api_response = api_instance.find_all11(project_id, page=page, size=size, sort=sort)
        print("The response of TestCaseControllerApi->find_all11:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->find_all11: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,DESC&quot;]]

### Return type

[**PageTestCaseRowDto**](PageTestCaseRowDto.md)

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

# **find_all_deleted**
> PageTestCaseRowDto find_all_deleted(project_id, page=page, size=size, sort=sort)

Find all deleted test cases for given project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_case_row_dto import PageTestCaseRowDto
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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,DESC"])

    try:
        # Find all deleted test cases for given project
        api_response = api_instance.find_all_deleted(project_id, page=page, size=size, sort=sort)
        print("The response of TestCaseControllerApi->find_all_deleted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->find_all_deleted: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,DESC&quot;]]

### Return type

[**PageTestCaseRowDto**](PageTestCaseRowDto.md)

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

# **find_all_muted**
> PageTestCaseRowDto find_all_muted(project_id, page=page, size=size, sort=sort)

Find all muted test cases for given project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_case_row_dto import PageTestCaseRowDto
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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,DESC"])

    try:
        # Find all muted test cases for given project
        api_response = api_instance.find_all_muted(project_id, page=page, size=size, sort=sort)
        print("The response of TestCaseControllerApi->find_all_muted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->find_all_muted: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,DESC&quot;]]

### Return type

[**PageTestCaseRowDto**](PageTestCaseRowDto.md)

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

# **find_history1**
> PageTestResultHistoryDto find_history1(id, search=search, page=page, size=size, sort=sort)

Find run history for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_history_dto import PageTestResultHistoryDto
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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    id = 56 # int | 
    search = 'search_example' # str |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,DESC"])

    try:
        # Find run history for test case
        api_response = api_instance.find_history1(id, search=search, page=page, size=size, sort=sort)
        print("The response of TestCaseControllerApi->find_history1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->find_history1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **search** | **str**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,DESC&quot;]]

### Return type

[**PageTestResultHistoryDto**](PageTestResultHistoryDto.md)

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

# **find_history2**
> PageTestResultHistoryDto find_history2(test_case_id, project_id=project_id, launch_id=launch_id, test_result_id=test_result_id, search=search, page=page, size=size, sort=sort)

Find run history for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_history_dto import PageTestResultHistoryDto
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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    test_case_id = 56 # int | 
    project_id = 56 # int |  (optional)
    launch_id = 56 # int |  (optional)
    test_result_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,DESC"])

    try:
        # Find run history for test case
        api_response = api_instance.find_history2(test_case_id, project_id=project_id, launch_id=launch_id, test_result_id=test_result_id, search=search, page=page, size=size, sort=sort)
        print("The response of TestCaseControllerApi->find_history2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->find_history2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 
 **project_id** | **int**|  | [optional] 
 **launch_id** | **int**|  | [optional] 
 **test_result_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,DESC&quot;]]

### Return type

[**PageTestResultHistoryDto**](PageTestResultHistoryDto.md)

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

# **find_one11**
> TestCaseDto find_one11(id)

Find test case by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_dto import TestCaseDto
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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find test case by id
        api_response = api_instance.find_one11(id)
        print("The response of TestCaseControllerApi->find_one11:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->find_one11: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestCaseDto**](TestCaseDto.md)

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

# **find_workflow**
> WorkflowDto find_workflow(id)

Find workflow for test case

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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find workflow for test case
        api_response = api_instance.find_workflow(id)
        print("The response of TestCaseControllerApi->find_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->find_workflow: %s\n" % e)
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

# **patch12**
> TestCaseDto patch12(id, test_case_patch_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_dto import TestCaseDto
from openapi_client.models.test_case_patch_dto import TestCasePatchDto
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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    id = 56 # int | 
    test_case_patch_dto = openapi_client.TestCasePatchDto() # TestCasePatchDto | 

    try:
        api_response = api_instance.patch12(id, test_case_patch_dto)
        print("The response of TestCaseControllerApi->patch12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->patch12: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_case_patch_dto** | [**TestCasePatchDto**](TestCasePatchDto.md)|  | 

### Return type

[**TestCaseDto**](TestCaseDto.md)

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

# **restore**
> TestCaseDto restore(id)

Restore test case by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_dto import TestCaseDto
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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    id = 56 # int | 

    try:
        # Restore test case by id
        api_response = api_instance.restore(id)
        print("The response of TestCaseControllerApi->restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->restore: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestCaseDto**](TestCaseDto.md)

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

# **suggest5**
> PageIdAndNameOnlyDto suggest5(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Find suggest for test case

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
    api_instance = openapi_client.TestCaseControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find suggest for test case
        api_response = api_instance.suggest5(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of TestCaseControllerApi->suggest5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseControllerApi->suggest5: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 
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

