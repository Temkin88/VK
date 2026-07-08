# openapi_client.TestPlanControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign2**](TestPlanControllerApi.md#assign2) | **POST** /testplan/{id}/assign | Assign test plan test cases to user
[**create7**](TestPlanControllerApi.md#create7) | **POST** /testplan | Create a new test plan
[**delete7**](TestPlanControllerApi.md#delete7) | **DELETE** /testplan/{id} | Delete test plan by given id
[**find_all_by_project**](TestPlanControllerApi.md#find_all_by_project) | **GET** /testplan | Find all test plans for given project
[**find_one5**](TestPlanControllerApi.md#find_one5) | **GET** /testplan/{id} | Find test plan by id
[**get_diff**](TestPlanControllerApi.md#get_diff) | **GET** /testplan/{id}/diff | Get test plan test cases changes
[**get_groups1**](TestPlanControllerApi.md#get_groups1) | **GET** /testplan/{id}/tree/group | Find tree groups for node
[**get_jobs**](TestPlanControllerApi.md#get_jobs) | **GET** /testplan/{id}/job | Get test plan jobs statistic
[**get_leafs1**](TestPlanControllerApi.md#get_leafs1) | **GET** /testplan/{id}/tree/leaf | Find tree leafs for node
[**get_members1**](TestPlanControllerApi.md#get_members1) | **GET** /testplan/{id}/member | Get test plan members statistic
[**patch6**](TestPlanControllerApi.md#patch6) | **PATCH** /testplan/{id} | Patch test plan
[**reset_jobs**](TestPlanControllerApi.md#reset_jobs) | **POST** /testplan/{id}/resetjob | Reset test plan
[**run**](TestPlanControllerApi.md#run) | **POST** /testplan/{id}/run | Run test plan by given id
[**set_job_parameters**](TestPlanControllerApi.md#set_job_parameters) | **POST** /testplan/{id}/jobparameter | Configure test plan job parameters
[**suggest2**](TestPlanControllerApi.md#suggest2) | **GET** /testplan/suggest | Suggest for test plans
[**sync**](TestPlanControllerApi.md#sync) | **POST** /testplan/{id}/sync | Sync test plan


# **assign2**
> assign2(id, test_plan_assign_dto)

Assign test plan test cases to user

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_plan_assign_dto import TestPlanAssignDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 
    test_plan_assign_dto = openapi_client.TestPlanAssignDto() # TestPlanAssignDto | 

    try:
        # Assign test plan test cases to user
        api_instance.assign2(id, test_plan_assign_dto)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->assign2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_plan_assign_dto** | [**TestPlanAssignDto**](TestPlanAssignDto.md)|  | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create7**
> TestPlanDto create7(test_plan_create_dto)

Create a new test plan

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_plan_create_dto import TestPlanCreateDto
from openapi_client.models.test_plan_dto import TestPlanDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    test_plan_create_dto = openapi_client.TestPlanCreateDto() # TestPlanCreateDto | 

    try:
        # Create a new test plan
        api_response = api_instance.create7(test_plan_create_dto)
        print("The response of TestPlanControllerApi->create7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->create7: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_plan_create_dto** | [**TestPlanCreateDto**](TestPlanCreateDto.md)|  | 

### Return type

[**TestPlanDto**](TestPlanDto.md)

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

# **delete7**
> delete7(id)

Delete test plan by given id

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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete test plan by given id
        api_instance.delete7(id)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->delete7: %s\n" % e)
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

# **find_all_by_project**
> PageTestPlanDto find_all_by_project(project_id, name=name, page=page, size=size, sort=sort)

Find all test plans for given project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_plan_dto import PageTestPlanDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    project_id = 56 # int | 
    name = 'name_example' # str |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find all test plans for given project
        api_response = api_instance.find_all_by_project(project_id, name=name, page=page, size=size, sort=sort)
        print("The response of TestPlanControllerApi->find_all_by_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->find_all_by_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **name** | **str**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageTestPlanDto**](PageTestPlanDto.md)

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

# **find_one5**
> TestPlanDto find_one5(id)

Find test plan by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_plan_dto import TestPlanDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find test plan by id
        api_response = api_instance.find_one5(id)
        print("The response of TestPlanControllerApi->find_one5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->find_one5: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestPlanDto**](TestPlanDto.md)

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

# **get_diff**
> TestPlanDiffDto get_diff(id)

Get test plan test cases changes

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_plan_diff_dto import TestPlanDiffDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 

    try:
        # Get test plan test cases changes
        api_response = api_instance.get_diff(id)
        print("The response of TestPlanControllerApi->get_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->get_diff: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestPlanDiffDto**](TestPlanDiffDto.md)

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

# **get_groups1**
> PageTestCaseTreeGroupDto get_groups1(id, tree_id=tree_id, path=path, username=username, job_id=job_id, manual=manual, page=page, size=size, sort=sort)

Find tree groups for node

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_case_tree_group_dto import PageTestCaseTreeGroupDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 
    tree_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])
    username = 'username_example' # str |  (optional)
    job_id = 56 # int |  (optional)
    manual = True # bool |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find tree groups for node
        api_response = api_instance.get_groups1(id, tree_id=tree_id, path=path, username=username, job_id=job_id, manual=manual, page=page, size=size, sort=sort)
        print("The response of TestPlanControllerApi->get_groups1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->get_groups1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tree_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]
 **username** | **str**|  | [optional] 
 **job_id** | **int**|  | [optional] 
 **manual** | **bool**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageTestCaseTreeGroupDto**](PageTestCaseTreeGroupDto.md)

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

# **get_jobs**
> List[TestPlanJobStatDto] get_jobs(id)

Get test plan jobs statistic

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_plan_job_stat_dto import TestPlanJobStatDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 

    try:
        # Get test plan jobs statistic
        api_response = api_instance.get_jobs(id)
        print("The response of TestPlanControllerApi->get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->get_jobs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[TestPlanJobStatDto]**](TestPlanJobStatDto.md)

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

# **get_leafs1**
> PageTestCaseTreeLeafDto get_leafs1(id, tree_id=tree_id, path=path, username=username, job_id=job_id, manual=manual, page=page, size=size, sort=sort)

Find tree leafs for node

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_case_tree_leaf_dto import PageTestCaseTreeLeafDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 
    tree_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])
    username = 'username_example' # str |  (optional)
    job_id = 56 # int |  (optional)
    manual = True # bool |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find tree leafs for node
        api_response = api_instance.get_leafs1(id, tree_id=tree_id, path=path, username=username, job_id=job_id, manual=manual, page=page, size=size, sort=sort)
        print("The response of TestPlanControllerApi->get_leafs1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->get_leafs1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tree_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]
 **username** | **str**|  | [optional] 
 **job_id** | **int**|  | [optional] 
 **manual** | **bool**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageTestCaseTreeLeafDto**](PageTestCaseTreeLeafDto.md)

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

# **get_members1**
> List[TestPlanMemberStatDto] get_members1(id)

Get test plan members statistic

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_plan_member_stat_dto import TestPlanMemberStatDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 

    try:
        # Get test plan members statistic
        api_response = api_instance.get_members1(id)
        print("The response of TestPlanControllerApi->get_members1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->get_members1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[TestPlanMemberStatDto]**](TestPlanMemberStatDto.md)

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

# **patch6**
> TestPlanDto patch6(id, test_plan_patch_dto)

Patch test plan

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_plan_dto import TestPlanDto
from openapi_client.models.test_plan_patch_dto import TestPlanPatchDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 
    test_plan_patch_dto = openapi_client.TestPlanPatchDto() # TestPlanPatchDto | 

    try:
        # Patch test plan
        api_response = api_instance.patch6(id, test_plan_patch_dto)
        print("The response of TestPlanControllerApi->patch6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->patch6: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_plan_patch_dto** | [**TestPlanPatchDto**](TestPlanPatchDto.md)|  | 

### Return type

[**TestPlanDto**](TestPlanDto.md)

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

# **reset_jobs**
> TestPlanDto reset_jobs(id)

Reset test plan

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_plan_dto import TestPlanDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 

    try:
        # Reset test plan
        api_response = api_instance.reset_jobs(id)
        print("The response of TestPlanControllerApi->reset_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->reset_jobs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestPlanDto**](TestPlanDto.md)

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

# **run**
> LaunchDto run(id, test_plan_run_request_dto)

Run test plan by given id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_dto import LaunchDto
from openapi_client.models.test_plan_run_request_dto import TestPlanRunRequestDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 
    test_plan_run_request_dto = openapi_client.TestPlanRunRequestDto() # TestPlanRunRequestDto | 

    try:
        # Run test plan by given id
        api_response = api_instance.run(id, test_plan_run_request_dto)
        print("The response of TestPlanControllerApi->run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->run: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_plan_run_request_dto** | [**TestPlanRunRequestDto**](TestPlanRunRequestDto.md)|  | 

### Return type

[**LaunchDto**](LaunchDto.md)

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

# **set_job_parameters**
> set_job_parameters(id, test_plan_job_parameters_dto)

Configure test plan job parameters

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_plan_job_parameters_dto import TestPlanJobParametersDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 
    test_plan_job_parameters_dto = openapi_client.TestPlanJobParametersDto() # TestPlanJobParametersDto | 

    try:
        # Configure test plan job parameters
        api_instance.set_job_parameters(id, test_plan_job_parameters_dto)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->set_job_parameters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_plan_job_parameters_dto** | [**TestPlanJobParametersDto**](TestPlanJobParametersDto.md)|  | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggest2**
> PageTestPlanRowDto suggest2(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest for test plans

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_plan_row_dto import PageTestPlanRowDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest for test plans
        api_response = api_instance.suggest2(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of TestPlanControllerApi->suggest2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->suggest2: %s\n" % e)
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

[**PageTestPlanRowDto**](PageTestPlanRowDto.md)

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

# **sync**
> TestPlanDto sync(id)

Sync test plan

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_plan_dto import TestPlanDto
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
    api_instance = openapi_client.TestPlanControllerApi(api_client)
    id = 56 # int | 

    try:
        # Sync test plan
        api_response = api_instance.sync(id)
        print("The response of TestPlanControllerApi->sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestPlanControllerApi->sync: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestPlanDto**](TestPlanDto.md)

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

