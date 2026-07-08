# openapi_client.IframeControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_test_cases**](IframeControllerApi.md#bulk_create_test_cases) | **POST** /iframe/testcases | Bulk create a new test cases from iframe
[**create_test_case**](IframeControllerApi.md#create_test_case) | **POST** /iframe/testcase | Create a new test case from iframe
[**get_launches**](IframeControllerApi.md#get_launches) | **GET** /iframe/launch | 
[**get_statistic1**](IframeControllerApi.md#get_statistic1) | **GET** /iframe/launch/{launchId}/statistic | Get launch statistic
[**get_test_cases**](IframeControllerApi.md#get_test_cases) | **GET** /iframe/testcase | Get pageble list of testcases
[**get_test_results**](IframeControllerApi.md#get_test_results) | **GET** /iframe/testresult | Get test results for launch
[**link_test_case_with_issue**](IframeControllerApi.md#link_test_case_with_issue) | **POST** /iframe/testcases/linkissue | Link test cases with issue from iframe


# **bulk_create_test_cases**
> List[TestCaseDto] bulk_create_test_cases(iframe_bulk_create_test_case_dto)

Bulk create a new test cases from iframe

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.iframe_bulk_create_test_case_dto import IframeBulkCreateTestCaseDto
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
    api_instance = openapi_client.IframeControllerApi(api_client)
    iframe_bulk_create_test_case_dto = openapi_client.IframeBulkCreateTestCaseDto() # IframeBulkCreateTestCaseDto | 

    try:
        # Bulk create a new test cases from iframe
        api_response = api_instance.bulk_create_test_cases(iframe_bulk_create_test_case_dto)
        print("The response of IframeControllerApi->bulk_create_test_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IframeControllerApi->bulk_create_test_cases: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iframe_bulk_create_test_case_dto** | [**IframeBulkCreateTestCaseDto**](IframeBulkCreateTestCaseDto.md)|  | 

### Return type

[**List[TestCaseDto]**](TestCaseDto.md)

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

# **create_test_case**
> TestCaseDto create_test_case(iframe_create_test_case_dto)

Create a new test case from iframe

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.iframe_create_test_case_dto import IframeCreateTestCaseDto
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
    api_instance = openapi_client.IframeControllerApi(api_client)
    iframe_create_test_case_dto = openapi_client.IframeCreateTestCaseDto() # IframeCreateTestCaseDto | 

    try:
        # Create a new test case from iframe
        api_response = api_instance.create_test_case(iframe_create_test_case_dto)
        print("The response of IframeControllerApi->create_test_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IframeControllerApi->create_test_case: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iframe_create_test_case_dto** | [**IframeCreateTestCaseDto**](IframeCreateTestCaseDto.md)|  | 

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

# **get_launches**
> PageLaunchPreviewDto get_launches(issue_key, integration_id=integration_id, issue_tracker_id=issue_tracker_id, closed=closed, with_job=with_job, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_launch_preview_dto import PageLaunchPreviewDto
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
    api_instance = openapi_client.IframeControllerApi(api_client)
    issue_key = 'issue_key_example' # str | 
    integration_id = 56 # int |  (optional)
    issue_tracker_id = 56 # int |  (optional)
    closed = True # bool |  (optional)
    with_job = True # bool |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["created_date,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["created_date,DESC"])

    try:
        api_response = api_instance.get_launches(issue_key, integration_id=integration_id, issue_tracker_id=issue_tracker_id, closed=closed, with_job=with_job, page=page, size=size, sort=sort)
        print("The response of IframeControllerApi->get_launches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IframeControllerApi->get_launches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_key** | **str**|  | 
 **integration_id** | **int**|  | [optional] 
 **issue_tracker_id** | **int**|  | [optional] 
 **closed** | **bool**|  | [optional] 
 **with_job** | **bool**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;created_date,DESC&quot;]]

### Return type

[**PageLaunchPreviewDto**](PageLaunchPreviewDto.md)

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

# **get_statistic1**
> List[TestStatusCount] get_statistic1(launch_id)

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
    api_instance = openapi_client.IframeControllerApi(api_client)
    launch_id = 56 # int | 

    try:
        # Get launch statistic
        api_response = api_instance.get_statistic1(launch_id)
        print("The response of IframeControllerApi->get_statistic1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IframeControllerApi->get_statistic1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **int**|  | 

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

# **get_test_cases**
> PageTestCaseDto get_test_cases(issue_key, integration_id=integration_id, issue_tracker_id=issue_tracker_id, search=search, status=status, automated=automated, page=page, size=size, sort=sort)

Get pageble list of testcases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_case_dto import PageTestCaseDto
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
    api_instance = openapi_client.IframeControllerApi(api_client)
    issue_key = 'issue_key_example' # str | 
    integration_id = 56 # int |  (optional)
    issue_tracker_id = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    status = [56] # List[int] |  (optional)
    automated = True # bool |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Get pageble list of testcases
        api_response = api_instance.get_test_cases(issue_key, integration_id=integration_id, issue_tracker_id=issue_tracker_id, search=search, status=status, automated=automated, page=page, size=size, sort=sort)
        print("The response of IframeControllerApi->get_test_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IframeControllerApi->get_test_cases: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_key** | **str**|  | 
 **integration_id** | **int**|  | [optional] 
 **issue_tracker_id** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **status** | [**List[int]**](int.md)|  | [optional] 
 **automated** | **bool**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageTestCaseDto**](PageTestCaseDto.md)

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

# **get_test_results**
> PageTestResultDto get_test_results(launch_id, status=status, manual=manual, page=page, size=size, sort=sort)

Get test results for launch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_dto import PageTestResultDto
from openapi_client.models.test_status import TestStatus
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
    api_instance = openapi_client.IframeControllerApi(api_client)
    launch_id = 56 # int | 
    status = [openapi_client.TestStatus()] # List[TestStatus] |  (optional)
    manual = True # bool |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,DESC"])

    try:
        # Get test results for launch
        api_response = api_instance.get_test_results(launch_id, status=status, manual=manual, page=page, size=size, sort=sort)
        print("The response of IframeControllerApi->get_test_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IframeControllerApi->get_test_results: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **int**|  | 
 **status** | [**List[TestStatus]**](TestStatus.md)|  | [optional] 
 **manual** | **bool**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,DESC&quot;]]

### Return type

[**PageTestResultDto**](PageTestResultDto.md)

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

# **link_test_case_with_issue**
> link_test_case_with_issue(iframe_test_case_with_issue_dto)

Link test cases with issue from iframe

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.iframe_test_case_with_issue_dto import IframeTestCaseWithIssueDto
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
    api_instance = openapi_client.IframeControllerApi(api_client)
    iframe_test_case_with_issue_dto = openapi_client.IframeTestCaseWithIssueDto() # IframeTestCaseWithIssueDto | 

    try:
        # Link test cases with issue from iframe
        api_instance.link_test_case_with_issue(iframe_test_case_with_issue_dto)
    except Exception as e:
        print("Exception when calling IframeControllerApi->link_test_case_with_issue: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iframe_test_case_with_issue_dto** | [**IframeTestCaseWithIssueDto**](IframeTestCaseWithIssueDto.md)|  | 

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

