# openapi_client.JobControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create27**](JobControllerApi.md#create27) | **POST** /job | Create a new job
[**delete26**](JobControllerApi.md#delete26) | **DELETE** /job/{id} | Delete job by id
[**find_all271**](JobControllerApi.md#find_all271) | **GET** /job | Find job by given project and external id
[**find_one22**](JobControllerApi.md#find_one22) | **GET** /job/{id} | Find job by id
[**get_candidate**](JobControllerApi.md#get_candidate) | **GET** /job/candidate | Get suggest for job candidate
[**get_groups2**](JobControllerApi.md#get_groups2) | **GET** /job/{id}/tree/group | Find tree groups for node
[**get_leaves**](JobControllerApi.md#get_leaves) | **GET** /job/{id}/tree/leaf | Find tree leaves for node
[**get_suggest1**](JobControllerApi.md#get_suggest1) | **GET** /job/suggest | Suggest for jobs
[**patch24**](JobControllerApi.md#patch24) | **PATCH** /job/{id} | Patch job
[**run4**](JobControllerApi.md#run4) | **POST** /job/{id}/run | Run job to a new launch
[**sync2**](JobControllerApi.md#sync2) | **POST** /job/{id}/sync | Sync job with build server


# **create27**
> JobDto create27(job_create_dto)

Create a new job

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_create_dto import JobCreateDto
from openapi_client.models.job_dto import JobDto
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
    api_instance = openapi_client.JobControllerApi(api_client)
    job_create_dto = openapi_client.JobCreateDto() # JobCreateDto | 

    try:
        # Create a new job
        api_response = api_instance.create27(job_create_dto)
        print("The response of JobControllerApi->create27:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControllerApi->create27: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_create_dto** | [**JobCreateDto**](JobCreateDto.md)|  | 

### Return type

[**JobDto**](JobDto.md)

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

# **delete26**
> delete26(id)

Delete job by id

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
    api_instance = openapi_client.JobControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete job by id
        api_instance.delete26(id)
    except Exception as e:
        print("Exception when calling JobControllerApi->delete26: %s\n" % e)
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

# **find_all271**
> PageJobDto find_all271(project_id, external_id, page=page, size=size, sort=sort)

Find job by given project and external id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_job_dto import PageJobDto
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
    api_instance = openapi_client.JobControllerApi(api_client)
    project_id = 56 # int | 
    external_id = 'external_id_example' # str | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find job by given project and external id
        api_response = api_instance.find_all271(project_id, external_id, page=page, size=size, sort=sort)
        print("The response of JobControllerApi->find_all271:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControllerApi->find_all271: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **external_id** | **str**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageJobDto**](PageJobDto.md)

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

# **find_one22**
> JobDto find_one22(id)

Find job by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_dto import JobDto
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
    api_instance = openapi_client.JobControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find job by id
        api_response = api_instance.find_one22(id)
        print("The response of JobControllerApi->find_one22:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControllerApi->find_one22: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**JobDto**](JobDto.md)

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

# **get_candidate**
> List[JobDto] get_candidate(project_id, integration_id, query=query)

Get suggest for job candidate

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_dto import JobDto
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
    api_instance = openapi_client.JobControllerApi(api_client)
    project_id = 56 # int | 
    integration_id = 56 # int | 
    query = '' # str |  (optional) (default to '')

    try:
        # Get suggest for job candidate
        api_response = api_instance.get_candidate(project_id, integration_id, query=query)
        print("The response of JobControllerApi->get_candidate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControllerApi->get_candidate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **integration_id** | **int**|  | 
 **query** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[JobDto]**](JobDto.md)

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

# **get_groups2**
> PageTestCaseTreeGroupDto get_groups2(id, tree_id=tree_id, path=path, page=page, size=size, sort=sort)

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
    api_instance = openapi_client.JobControllerApi(api_client)
    id = 56 # int | 
    tree_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find tree groups for node
        api_response = api_instance.get_groups2(id, tree_id=tree_id, path=path, page=page, size=size, sort=sort)
        print("The response of JobControllerApi->get_groups2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControllerApi->get_groups2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tree_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]
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

# **get_leaves**
> PageTestCaseTreeLeafDto get_leaves(id, tree_id=tree_id, path=path, page=page, size=size, sort=sort)

Find tree leaves for node

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
    api_instance = openapi_client.JobControllerApi(api_client)
    id = 56 # int | 
    tree_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find tree leaves for node
        api_response = api_instance.get_leaves(id, tree_id=tree_id, path=path, page=page, size=size, sort=sort)
        print("The response of JobControllerApi->get_leaves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControllerApi->get_leaves: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tree_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]
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

# **get_suggest1**
> PageIdAndNameOnlyDto get_suggest1(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest for jobs

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
    api_instance = openapi_client.JobControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest for jobs
        api_response = api_instance.get_suggest1(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of JobControllerApi->get_suggest1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControllerApi->get_suggest1: %s\n" % e)
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

# **patch24**
> JobDto patch24(id, job_patch_dto)

Patch job

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_dto import JobDto
from openapi_client.models.job_patch_dto import JobPatchDto
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
    api_instance = openapi_client.JobControllerApi(api_client)
    id = 56 # int | 
    job_patch_dto = openapi_client.JobPatchDto() # JobPatchDto | 

    try:
        # Patch job
        api_response = api_instance.patch24(id, job_patch_dto)
        print("The response of JobControllerApi->patch24:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControllerApi->patch24: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **job_patch_dto** | [**JobPatchDto**](JobPatchDto.md)|  | 

### Return type

[**JobDto**](JobDto.md)

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

# **run4**
> LaunchDto run4(id, job_run_request_dto)

Run job to a new launch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_run_request_dto import JobRunRequestDto
from openapi_client.models.launch_dto import LaunchDto
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
    api_instance = openapi_client.JobControllerApi(api_client)
    id = 56 # int | 
    job_run_request_dto = openapi_client.JobRunRequestDto() # JobRunRequestDto | 

    try:
        # Run job to a new launch
        api_response = api_instance.run4(id, job_run_request_dto)
        print("The response of JobControllerApi->run4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControllerApi->run4: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **job_run_request_dto** | [**JobRunRequestDto**](JobRunRequestDto.md)|  | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync2**
> JobDto sync2(id)

Sync job with build server

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_dto import JobDto
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
    api_instance = openapi_client.JobControllerApi(api_client)
    id = 56 # int | 

    try:
        # Sync job with build server
        api_response = api_instance.sync2(id)
        print("The response of JobControllerApi->sync2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControllerApi->sync2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**JobDto**](JobDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

