# openapi_client.TestResultSearchControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](TestResultSearchControllerApi.md#search) | **GET** /testresult/__search | Find all test results by given AQL
[**validate_query**](TestResultSearchControllerApi.md#validate_query) | **GET** /testresult/query/validate | Find all test results by given AQL


# **search**
> PageTestResultRowDto search(project_id, rql, page=page, size=size, sort=sort)

Find all test results by given AQL

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
    api_instance = openapi_client.TestResultSearchControllerApi(api_client)
    project_id = 56 # int | 
    rql = 'rql_example' # str | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["created_date,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["created_date,DESC"])

    try:
        # Find all test results by given AQL
        api_response = api_instance.search(project_id, rql, page=page, size=size, sort=sort)
        print("The response of TestResultSearchControllerApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultSearchControllerApi->search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **rql** | **str**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;created_date,DESC&quot;]]

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

# **validate_query**
> AqlValidateResponseDto validate_query(project_id, rql)

Find all test results by given AQL

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
    api_instance = openapi_client.TestResultSearchControllerApi(api_client)
    project_id = 56 # int | 
    rql = 'rql_example' # str | 

    try:
        # Find all test results by given AQL
        api_response = api_instance.validate_query(project_id, rql)
        print("The response of TestResultSearchControllerApi->validate_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultSearchControllerApi->validate_query: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **rql** | **str**|  | 

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

