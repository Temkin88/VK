# openapi_client.TestCaseSearchControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search1**](TestCaseSearchControllerApi.md#search1) | **GET** /testcase/__search | Find all test cases by given AQL
[**validate_query1**](TestCaseSearchControllerApi.md#validate_query1) | **GET** /testcase/query/validate | Find all test cases by given AQL


# **search1**
> PageTestCaseDto search1(project_id, rql, deleted=deleted, page=page, size=size, sort=sort)

Find all test cases by given AQL

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
    api_instance = openapi_client.TestCaseSearchControllerApi(api_client)
    project_id = 56 # int | 
    rql = 'rql_example' # str | 
    deleted = False # bool |  (optional) (default to False)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,DESC"])

    try:
        # Find all test cases by given AQL
        api_response = api_instance.search1(project_id, rql, deleted=deleted, page=page, size=size, sort=sort)
        print("The response of TestCaseSearchControllerApi->search1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseSearchControllerApi->search1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **rql** | **str**|  | 
 **deleted** | **bool**|  | [optional] [default to False]
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,DESC&quot;]]

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

# **validate_query1**
> AqlValidateResponseDto validate_query1(project_id, rql, deleted=deleted)

Find all test cases by given AQL

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.aql_validate_response_dto import AqlValidateResponseDto
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
    api_instance = openapi_client.TestCaseSearchControllerApi(api_client)
    project_id = 56 # int | 
    rql = 'rql_example' # str | 
    deleted = False # bool |  (optional) (default to False)

    try:
        # Find all test cases by given AQL
        api_response = api_instance.validate_query1(project_id, rql, deleted=deleted)
        print("The response of TestCaseSearchControllerApi->validate_query1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseSearchControllerApi->validate_query1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **rql** | **str**|  | 
 **deleted** | **bool**|  | [optional] [default to False]

### Return type

[**AqlValidateResponseDto**](AqlValidateResponseDto.md)

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

