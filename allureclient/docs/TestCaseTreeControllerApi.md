# openapi_client.TestCaseTreeControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group1**](TestCaseTreeControllerApi.md#add_group1) | **POST** /testcasetree/group | Add a new group (AQL)
[**add_leaf**](TestCaseTreeControllerApi.md#add_leaf) | **POST** /testcasetree/leaf | Add a new group
[**count_leaves2**](TestCaseTreeControllerApi.md#count_leaves2) | **GET** /testcasetree/countleaves | Count all tree leaves for given path and filter
[**get_groups21**](TestCaseTreeControllerApi.md#get_groups21) | **GET** /testcasetree/group | Find tree groups for node (AQL)
[**get_jobs_info**](TestCaseTreeControllerApi.md#get_jobs_info) | **POST** /testcasetree/job | Get information about jobs that will be used to run selected test cases
[**get_leaves1**](TestCaseTreeControllerApi.md#get_leaves1) | **GET** /testcasetree/leaf | Find tree leaves for node (AQL)
[**get_run_stats**](TestCaseTreeControllerApi.md#get_run_stats) | **POST** /testcasetree/runstats | Get run information
[**rename_group1**](TestCaseTreeControllerApi.md#rename_group1) | **POST** /testcasetree/group/rename | Rename tree group (AQL)
[**rename_leaf**](TestCaseTreeControllerApi.md#rename_leaf) | **POST** /testcasetree/leaf/rename | Rename tree leaf
[**suggest4**](TestCaseTreeControllerApi.md#suggest4) | **GET** /testcasetree/suggest | Tree groups suggest


# **add_group1**
> TestCaseTreeGroupDto add_group1(project_id, test_case_tree_group_add_dto, filter_id=filter_id, search=search, tree_id=tree_id, path=path, base_rql=base_rql)

Add a new group (AQL)

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_tree_group_add_dto import TestCaseTreeGroupAddDto
from openapi_client.models.test_case_tree_group_dto import TestCaseTreeGroupDto
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
    api_instance = openapi_client.TestCaseTreeControllerApi(api_client)
    project_id = 56 # int | 
    test_case_tree_group_add_dto = openapi_client.TestCaseTreeGroupAddDto() # TestCaseTreeGroupAddDto | 
    filter_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    tree_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])
    base_rql = 'base_rql_example' # str |  (optional)

    try:
        # Add a new group (AQL)
        api_response = api_instance.add_group1(project_id, test_case_tree_group_add_dto, filter_id=filter_id, search=search, tree_id=tree_id, path=path, base_rql=base_rql)
        print("The response of TestCaseTreeControllerApi->add_group1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTreeControllerApi->add_group1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_case_tree_group_add_dto** | [**TestCaseTreeGroupAddDto**](TestCaseTreeGroupAddDto.md)|  | 
 **filter_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **tree_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]
 **base_rql** | **str**|  | [optional] 

### Return type

[**TestCaseTreeGroupDto**](TestCaseTreeGroupDto.md)

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

# **add_leaf**
> TestCaseTreeLeafDto add_leaf(project_id, test_case_tree_leaf_add_dto, tree_id=tree_id, path=path)

Add a new group

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_tree_leaf_add_dto import TestCaseTreeLeafAddDto
from openapi_client.models.test_case_tree_leaf_dto import TestCaseTreeLeafDto
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
    api_instance = openapi_client.TestCaseTreeControllerApi(api_client)
    project_id = 56 # int | 
    test_case_tree_leaf_add_dto = openapi_client.TestCaseTreeLeafAddDto() # TestCaseTreeLeafAddDto | 
    tree_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])

    try:
        # Add a new group
        api_response = api_instance.add_leaf(project_id, test_case_tree_leaf_add_dto, tree_id=tree_id, path=path)
        print("The response of TestCaseTreeControllerApi->add_leaf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTreeControllerApi->add_leaf: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_case_tree_leaf_add_dto** | [**TestCaseTreeLeafAddDto**](TestCaseTreeLeafAddDto.md)|  | 
 **tree_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]

### Return type

[**TestCaseTreeLeafDto**](TestCaseTreeLeafDto.md)

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

# **count_leaves2**
> TestCaseTreeFilterCountDto count_leaves2(project_id, search=search, tree_id=tree_id, filter_id=filter_id, path=path)

Count all tree leaves for given path and filter

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_tree_filter_count_dto import TestCaseTreeFilterCountDto
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
    api_instance = openapi_client.TestCaseTreeControllerApi(api_client)
    project_id = 56 # int | 
    search = 'search_example' # str |  (optional)
    tree_id = 56 # int |  (optional)
    filter_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])

    try:
        # Count all tree leaves for given path and filter
        api_response = api_instance.count_leaves2(project_id, search=search, tree_id=tree_id, filter_id=filter_id, path=path)
        print("The response of TestCaseTreeControllerApi->count_leaves2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTreeControllerApi->count_leaves2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **search** | **str**|  | [optional] 
 **tree_id** | **int**|  | [optional] 
 **filter_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]

### Return type

[**TestCaseTreeFilterCountDto**](TestCaseTreeFilterCountDto.md)

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

# **get_groups21**
> PageTestCaseTreeGroupDto get_groups21(project_id, search=search, tree_id=tree_id, filter_id=filter_id, path=path, page=page, size=size, sort=sort, base_rql=base_rql)

Find tree groups for node (AQL)

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
    api_instance = openapi_client.TestCaseTreeControllerApi(api_client)
    project_id = 56 # int | 
    search = 'search_example' # str |  (optional)
    tree_id = 56 # int |  (optional)
    filter_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 100 # int | The size of the page to be returned (optional) (default to 100)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])
    base_rql = 'base_rql_example' # str |  (optional)

    try:
        # Find tree groups for node (AQL)
        api_response = api_instance.get_groups21(project_id, search=search, tree_id=tree_id, filter_id=filter_id, path=path, page=page, size=size, sort=sort, base_rql=base_rql)
        print("The response of TestCaseTreeControllerApi->get_groups21:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTreeControllerApi->get_groups21: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **search** | **str**|  | [optional] 
 **tree_id** | **int**|  | [optional] 
 **filter_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 100]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]
 **base_rql** | **str**|  | [optional] 

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

# **get_jobs_info**
> List[JobTestCasesStatDto] get_jobs_info(test_case_tree_run_stat_request_dto)

Get information about jobs that will be used to run selected test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_test_cases_stat_dto import JobTestCasesStatDto
from openapi_client.models.test_case_tree_run_stat_request_dto import TestCaseTreeRunStatRequestDto
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
    api_instance = openapi_client.TestCaseTreeControllerApi(api_client)
    test_case_tree_run_stat_request_dto = openapi_client.TestCaseTreeRunStatRequestDto() # TestCaseTreeRunStatRequestDto | 

    try:
        # Get information about jobs that will be used to run selected test cases
        api_response = api_instance.get_jobs_info(test_case_tree_run_stat_request_dto)
        print("The response of TestCaseTreeControllerApi->get_jobs_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTreeControllerApi->get_jobs_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_tree_run_stat_request_dto** | [**TestCaseTreeRunStatRequestDto**](TestCaseTreeRunStatRequestDto.md)|  | 

### Return type

[**List[JobTestCasesStatDto]**](JobTestCasesStatDto.md)

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

# **get_leaves1**
> PageTestCaseTreeLeafDto get_leaves1(project_id, search=search, tree_id=tree_id, filter_id=filter_id, path=path, page=page, size=size, sort=sort, base_rql=base_rql)

Find tree leaves for node (AQL)

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
    api_instance = openapi_client.TestCaseTreeControllerApi(api_client)
    project_id = 56 # int | 
    search = 'search_example' # str |  (optional)
    tree_id = 56 # int |  (optional)
    filter_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 100 # int | The size of the page to be returned (optional) (default to 100)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])
    base_rql = 'base_rql_example' # str |  (optional)

    try:
        # Find tree leaves for node (AQL)
        api_response = api_instance.get_leaves1(project_id, search=search, tree_id=tree_id, filter_id=filter_id, path=path, page=page, size=size, sort=sort, base_rql=base_rql)
        print("The response of TestCaseTreeControllerApi->get_leaves1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTreeControllerApi->get_leaves1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **search** | **str**|  | [optional] 
 **tree_id** | **int**|  | [optional] 
 **filter_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 100]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]
 **base_rql** | **str**|  | [optional] 

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

# **get_run_stats**
> TestCaseRunByStats get_run_stats(test_case_tree_run_stat_request_dto)

Get run information

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_run_by_stats import TestCaseRunByStats
from openapi_client.models.test_case_tree_run_stat_request_dto import TestCaseTreeRunStatRequestDto
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
    api_instance = openapi_client.TestCaseTreeControllerApi(api_client)
    test_case_tree_run_stat_request_dto = openapi_client.TestCaseTreeRunStatRequestDto() # TestCaseTreeRunStatRequestDto | 

    try:
        # Get run information
        api_response = api_instance.get_run_stats(test_case_tree_run_stat_request_dto)
        print("The response of TestCaseTreeControllerApi->get_run_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTreeControllerApi->get_run_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_tree_run_stat_request_dto** | [**TestCaseTreeRunStatRequestDto**](TestCaseTreeRunStatRequestDto.md)|  | 

### Return type

[**TestCaseRunByStats**](TestCaseRunByStats.md)

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

# **rename_group1**
> TestCaseTreeGroupDto rename_group1(project_id, test_case_tree_group_rename_dto, filter_id=filter_id, search=search, tree_id=tree_id, path=path, base_rql=base_rql)

Rename tree group (AQL)

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_tree_group_dto import TestCaseTreeGroupDto
from openapi_client.models.test_case_tree_group_rename_dto import TestCaseTreeGroupRenameDto
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
    api_instance = openapi_client.TestCaseTreeControllerApi(api_client)
    project_id = 56 # int | 
    test_case_tree_group_rename_dto = openapi_client.TestCaseTreeGroupRenameDto() # TestCaseTreeGroupRenameDto | 
    filter_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    tree_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])
    base_rql = 'base_rql_example' # str |  (optional)

    try:
        # Rename tree group (AQL)
        api_response = api_instance.rename_group1(project_id, test_case_tree_group_rename_dto, filter_id=filter_id, search=search, tree_id=tree_id, path=path, base_rql=base_rql)
        print("The response of TestCaseTreeControllerApi->rename_group1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTreeControllerApi->rename_group1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **test_case_tree_group_rename_dto** | [**TestCaseTreeGroupRenameDto**](TestCaseTreeGroupRenameDto.md)|  | 
 **filter_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **tree_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]
 **base_rql** | **str**|  | [optional] 

### Return type

[**TestCaseTreeGroupDto**](TestCaseTreeGroupDto.md)

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

# **rename_leaf**
> TestCaseTreeLeafDto rename_leaf(project_id, leaf_id, test_case_tree_leaf_rename_dto)

Rename tree leaf

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_tree_leaf_dto import TestCaseTreeLeafDto
from openapi_client.models.test_case_tree_leaf_rename_dto import TestCaseTreeLeafRenameDto
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
    api_instance = openapi_client.TestCaseTreeControllerApi(api_client)
    project_id = 56 # int | 
    leaf_id = 56 # int | 
    test_case_tree_leaf_rename_dto = openapi_client.TestCaseTreeLeafRenameDto() # TestCaseTreeLeafRenameDto | 

    try:
        # Rename tree leaf
        api_response = api_instance.rename_leaf(project_id, leaf_id, test_case_tree_leaf_rename_dto)
        print("The response of TestCaseTreeControllerApi->rename_leaf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTreeControllerApi->rename_leaf: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **leaf_id** | **int**|  | 
 **test_case_tree_leaf_rename_dto** | [**TestCaseTreeLeafRenameDto**](TestCaseTreeLeafRenameDto.md)|  | 

### Return type

[**TestCaseTreeLeafDto**](TestCaseTreeLeafDto.md)

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

# **suggest4**
> PageIdAndNameOnlyDto suggest4(project_id, query=query, tree_id=tree_id, path=path, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Tree groups suggest

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
    api_instance = openapi_client.TestCaseTreeControllerApi(api_client)
    project_id = 56 # int | 
    query = 'query_example' # str |  (optional)
    tree_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Tree groups suggest
        api_response = api_instance.suggest4(project_id, query=query, tree_id=tree_id, path=path, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of TestCaseTreeControllerApi->suggest4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseTreeControllerApi->suggest4: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **query** | **str**|  | [optional] 
 **tree_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]
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

