# openapi_client.LaunchControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_test_cases**](LaunchControllerApi.md#add_test_cases) | **POST** /launch/{id}/testcase/add | Add test cases to launch
[**add_test_plan**](LaunchControllerApi.md#add_test_plan) | **POST** /launch/{id}/testplan/add | Add test plan to launch
[**apply_defect_matchers**](LaunchControllerApi.md#apply_defect_matchers) | **POST** /launch/{id}/defect/apply | Apply defect matchers to launch
[**close**](LaunchControllerApi.md#close) | **POST** /launch/{id}/close | Close launch
[**copy_launch**](LaunchControllerApi.md#copy_launch) | **POST** /launch/{id}/copy | Copy launch
[**create24**](LaunchControllerApi.md#create24) | **POST** /launch | Create a new launch
[**create26**](LaunchControllerApi.md#create26) | **POST** /launch/new | Create a new launch via event
[**delete24**](LaunchControllerApi.md#delete24) | **DELETE** /launch/{id} | Delete launch by id
[**find_all261**](LaunchControllerApi.md#find_all261) | **GET** /launch | Find all launches preview
[**find_one20**](LaunchControllerApi.md#find_one20) | **GET** /launch/{id} | Find launch by id
[**get_assignees**](LaunchControllerApi.md#get_assignees) | **GET** /launch/{id}/assignees | Get launch assignees
[**get_defects2**](LaunchControllerApi.md#get_defects2) | **GET** /launch/{id}/defect | Get launch defects
[**get_duration**](LaunchControllerApi.md#get_duration) | **GET** /launch/{id}/duration | Get launch duration
[**get_environment**](LaunchControllerApi.md#get_environment) | **GET** /launch/{id}/env | Get launch environment
[**get_jobs1**](LaunchControllerApi.md#get_jobs1) | **GET** /launch/{id}/job | Get launch jobs
[**get_member_stats**](LaunchControllerApi.md#get_member_stats) | **GET** /launch/{id}/memberstats | Get member stats widget data
[**get_muted_test_results**](LaunchControllerApi.md#get_muted_test_results) | **GET** /launch/{id}/muted | Get muted test results
[**get_progress**](LaunchControllerApi.md#get_progress) | **GET** /launch/{id}/progress | Get progress widget data
[**get_retries**](LaunchControllerApi.md#get_retries) | **GET** /launch/{id}/retries | Get retries widget data
[**get_statistic**](LaunchControllerApi.md#get_statistic) | **GET** /launch/{id}/statistic | Get launch statistic
[**get_testers**](LaunchControllerApi.md#get_testers) | **GET** /launch/{id}/tester | Get launch testers
[**get_unresolved_test_results**](LaunchControllerApi.md#get_unresolved_test_results) | **GET** /launch/{id}/unresolved | Get unresolved test results
[**get_variables**](LaunchControllerApi.md#get_variables) | **GET** /launch/{id}/variables | Get variables widget data
[**get_widget_tree**](LaunchControllerApi.md#get_widget_tree) | **GET** /launch/{id}/widget/tree | Get suites for tree data
[**merge**](LaunchControllerApi.md#merge) | **POST** /launch/merge | Merge launches
[**patch22**](LaunchControllerApi.md#patch22) | **PATCH** /launch/{id} | Patch launch
[**reopen**](LaunchControllerApi.md#reopen) | **POST** /launch/{id}/reopen | Reopen launch
[**suggest12**](LaunchControllerApi.md#suggest12) | **GET** /launch/suggest | Suggest for launches
[**suggest_jobs**](LaunchControllerApi.md#suggest_jobs) | **GET** /launch/{id}/job/suggest | Suggest launch jobs


# **add_test_cases**
> add_test_cases(id, launch_test_cases_add_dto)

Add test cases to launch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_test_cases_add_dto import LaunchTestCasesAddDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 
    launch_test_cases_add_dto = openapi_client.LaunchTestCasesAddDto() # LaunchTestCasesAddDto | 

    try:
        # Add test cases to launch
        api_instance.add_test_cases(id, launch_test_cases_add_dto)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->add_test_cases: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **launch_test_cases_add_dto** | [**LaunchTestCasesAddDto**](LaunchTestCasesAddDto.md)|  | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_test_plan**
> add_test_plan(id, launch_test_plan_add_dto)

Add test plan to launch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_test_plan_add_dto import LaunchTestPlanAddDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 
    launch_test_plan_add_dto = openapi_client.LaunchTestPlanAddDto() # LaunchTestPlanAddDto | 

    try:
        # Add test plan to launch
        api_instance.add_test_plan(id, launch_test_plan_add_dto)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->add_test_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **launch_test_plan_add_dto** | [**LaunchTestPlanAddDto**](LaunchTestPlanAddDto.md)|  | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_defect_matchers**
> apply_defect_matchers(id)

Apply defect matchers to launch

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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 

    try:
        # Apply defect matchers to launch
        api_instance.apply_defect_matchers(id)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->apply_defect_matchers: %s\n" % e)
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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close**
> close(id)

Close launch

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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 

    try:
        # Close launch
        api_instance.close(id)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->close: %s\n" % e)
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

# **copy_launch**
> copy_launch(id, launch_copy_rq_dto)

Copy launch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_copy_rq_dto import LaunchCopyRqDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 
    launch_copy_rq_dto = openapi_client.LaunchCopyRqDto() # LaunchCopyRqDto | 

    try:
        # Copy launch
        api_instance.copy_launch(id, launch_copy_rq_dto)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->copy_launch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **launch_copy_rq_dto** | [**LaunchCopyRqDto**](LaunchCopyRqDto.md)|  | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create24**
> LaunchDto create24(launch_create_dto)

Create a new launch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_create_dto import LaunchCreateDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    launch_create_dto = openapi_client.LaunchCreateDto() # LaunchCreateDto | 

    try:
        # Create a new launch
        api_response = api_instance.create24(launch_create_dto)
        print("The response of LaunchControllerApi->create24:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->create24: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_create_dto** | [**LaunchCreateDto**](LaunchCreateDto.md)|  | 

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

# **create26**
> LaunchDto create26(create_launch_event)

Create a new launch via event

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.create_launch_event import CreateLaunchEvent
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    create_launch_event = openapi_client.CreateLaunchEvent() # CreateLaunchEvent | 

    try:
        # Create a new launch via event
        api_response = api_instance.create26(create_launch_event)
        print("The response of LaunchControllerApi->create26:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->create26: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_launch_event** | [**CreateLaunchEvent**](CreateLaunchEvent.md)|  | 

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

# **delete24**
> delete24(id)

Delete launch by id

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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete launch by id
        api_instance.delete24(id)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->delete24: %s\n" % e)
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

# **find_all261**
> PageLaunchDto find_all261(project_id, search=search, page=page, size=size, sort=sort)

Find all launches preview

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_launch_dto import PageLaunchDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    project_id = 56 # int | 
    search = 'search_example' # str |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["created_date,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["created_date,DESC"])

    try:
        # Find all launches preview
        api_response = api_instance.find_all261(project_id, search=search, page=page, size=size, sort=sort)
        print("The response of LaunchControllerApi->find_all261:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->find_all261: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **search** | **str**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;created_date,DESC&quot;]]

### Return type

[**PageLaunchDto**](PageLaunchDto.md)

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

# **find_one20**
> LaunchDto find_one20(id)

Find launch by id

### Example

```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find launch by id
        api_response = api_instance.find_one20(id)
        print("The response of LaunchControllerApi->find_one20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->find_one20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**LaunchDto**](LaunchDto.md)

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

# **get_assignees**
> List[str] get_assignees(id)

Get launch assignees

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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 

    try:
        # Get launch assignees
        api_response = api_instance.get_assignees(id)
        print("The response of LaunchControllerApi->get_assignees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_assignees: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**List[str]**

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

# **get_defects2**
> PageDefectCountRowDto get_defects2(id, page=page, size=size, sort=sort)

Get launch defects

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_defect_count_row_dto import PageDefectCountRowDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        # Get launch defects
        api_response = api_instance.get_defects2(id, page=page, size=size, sort=sort)
        print("The response of LaunchControllerApi->get_defects2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_defects2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageDefectCountRowDto**](PageDefectCountRowDto.md)

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

# **get_duration**
> List[TestDurationCount] get_duration(id)

Get launch duration

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_duration_count import TestDurationCount
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 

    try:
        # Get launch duration
        api_response = api_instance.get_duration(id)
        print("The response of LaunchControllerApi->get_duration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_duration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[TestDurationCount]**](TestDurationCount.md)

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

# **get_environment**
> List[EnvVarValueDto] get_environment(id)

Get launch environment

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.env_var_value_dto import EnvVarValueDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 

    try:
        # Get launch environment
        api_response = api_instance.get_environment(id)
        print("The response of LaunchControllerApi->get_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_environment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[EnvVarValueDto]**](EnvVarValueDto.md)

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

# **get_jobs1**
> List[JobRunDto] get_jobs1(id)

Get launch jobs

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_run_dto import JobRunDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 

    try:
        # Get launch jobs
        api_response = api_instance.get_jobs1(id)
        print("The response of LaunchControllerApi->get_jobs1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_jobs1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[JobRunDto]**](JobRunDto.md)

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

# **get_member_stats**
> PageLaunchMemberStatsDto get_member_stats(id, page=page, size=size, sort=sort)

Get member stats widget data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_launch_member_stats_dto import PageLaunchMemberStatsDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        # Get member stats widget data
        api_response = api_instance.get_member_stats(id, page=page, size=size, sort=sort)
        print("The response of LaunchControllerApi->get_member_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_member_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageLaunchMemberStatsDto**](PageLaunchMemberStatsDto.md)

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

# **get_muted_test_results**
> PageTestResultRowDto get_muted_test_results(id, page=page, size=size, sort=sort)

Get muted test results

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_row_dto import PageTestResultRowDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        # Get muted test results
        api_response = api_instance.get_muted_test_results(id, page=page, size=size, sort=sort)
        print("The response of LaunchControllerApi->get_muted_test_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_muted_test_results: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageTestResultRowDto**](PageTestResultRowDto.md)

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

# **get_progress**
> LaunchProgressDto get_progress(id)

Get progress widget data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_progress_dto import LaunchProgressDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 

    try:
        # Get progress widget data
        api_response = api_instance.get_progress(id)
        print("The response of LaunchControllerApi->get_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_progress: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**LaunchProgressDto**](LaunchProgressDto.md)

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

# **get_retries**
> PageTestResultRetriesRowDto get_retries(id, page=page, size=size, sort=sort)

Get retries widget data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_retries_row_dto import PageTestResultRetriesRowDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["status,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["status,ASC"])

    try:
        # Get retries widget data
        api_response = api_instance.get_retries(id, page=page, size=size, sort=sort)
        print("The response of LaunchControllerApi->get_retries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_retries: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;status,ASC&quot;]]

### Return type

[**PageTestResultRetriesRowDto**](PageTestResultRetriesRowDto.md)

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

# **get_statistic**
> List[TestStatusCount] get_statistic(id)

Get launch statistic

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_status_count import TestStatusCount
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 

    try:
        # Get launch statistic
        api_response = api_instance.get_statistic(id)
        print("The response of LaunchControllerApi->get_statistic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_statistic: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[TestStatusCount]**](TestStatusCount.md)

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

# **get_testers**
> List[str] get_testers(id)

Get launch testers

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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 

    try:
        # Get launch testers
        api_response = api_instance.get_testers(id)
        print("The response of LaunchControllerApi->get_testers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_testers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**List[str]**

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

# **get_unresolved_test_results**
> PageTestResultRowDto get_unresolved_test_results(id, page=page, size=size, sort=sort)

Get unresolved test results

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_row_dto import PageTestResultRowDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        # Get unresolved test results
        api_response = api_instance.get_unresolved_test_results(id, page=page, size=size, sort=sort)
        print("The response of LaunchControllerApi->get_unresolved_test_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_unresolved_test_results: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageTestResultRowDto**](PageTestResultRowDto.md)

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

# **get_variables**
> PageLaunchVariableDto get_variables(id, page=page, size=size, sort=sort)

Get variables widget data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_launch_variable_dto import PageLaunchVariableDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        # Get variables widget data
        api_response = api_instance.get_variables(id, page=page, size=size, sort=sort)
        print("The response of LaunchControllerApi->get_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_variables: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageLaunchVariableDto**](PageLaunchVariableDto.md)

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

# **get_widget_tree**
> PageStatisticWidgetItem get_widget_tree(id, tree_id, page=page, size=size, sort=sort)

Get suites for tree data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_statistic_widget_item import PageStatisticWidgetItem
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 
    tree_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        # Get suites for tree data
        api_response = api_instance.get_widget_tree(id, tree_id, page=page, size=size, sort=sort)
        print("The response of LaunchControllerApi->get_widget_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->get_widget_tree: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tree_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageStatisticWidgetItem**](PageStatisticWidgetItem.md)

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

# **merge**
> IdAndNameOnlyDto merge(launch_merge_dto)

Merge launches

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.id_and_name_only_dto import IdAndNameOnlyDto
from openapi_client.models.launch_merge_dto import LaunchMergeDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    launch_merge_dto = openapi_client.LaunchMergeDto() # LaunchMergeDto | 

    try:
        # Merge launches
        api_response = api_instance.merge(launch_merge_dto)
        print("The response of LaunchControllerApi->merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->merge: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_merge_dto** | [**LaunchMergeDto**](LaunchMergeDto.md)|  | 

### Return type

[**IdAndNameOnlyDto**](IdAndNameOnlyDto.md)

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

# **patch22**
> LaunchDto patch22(id, launch_patch_dto)

Patch launch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_dto import LaunchDto
from openapi_client.models.launch_patch_dto import LaunchPatchDto
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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 
    launch_patch_dto = openapi_client.LaunchPatchDto() # LaunchPatchDto | 

    try:
        # Patch launch
        api_response = api_instance.patch22(id, launch_patch_dto)
        print("The response of LaunchControllerApi->patch22:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->patch22: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **launch_patch_dto** | [**LaunchPatchDto**](LaunchPatchDto.md)|  | 

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

# **reopen**
> reopen(id)

Reopen launch

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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 

    try:
        # Reopen launch
        api_instance.reopen(id)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->reopen: %s\n" % e)
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

# **suggest12**
> PageIdAndNameOnlyDto suggest12(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest for launches

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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest for launches
        api_response = api_instance.suggest12(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of LaunchControllerApi->suggest12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->suggest12: %s\n" % e)
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

# **suggest_jobs**
> PageIdAndNameOnlyDto suggest_jobs(id, query=query, id2=id2, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest launch jobs

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
    api_instance = openapi_client.LaunchControllerApi(api_client)
    id = 56 # int | 
    query = 'query_example' # str |  (optional)
    id2 = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest launch jobs
        api_response = api_instance.suggest_jobs(id, query=query, id2=id2, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of LaunchControllerApi->suggest_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchControllerApi->suggest_jobs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **query** | **str**|  | [optional] 
 **id2** | [**List[int]**](int.md)|  | [optional] 
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

