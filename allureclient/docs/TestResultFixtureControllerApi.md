# openapi_client.TestResultFixtureControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fixtures**](TestResultFixtureControllerApi.md#get_fixtures) | **GET** /testresult/{testResultId}/fixture | Find fixtures for test result
[**get_fixtures_attachments**](TestResultFixtureControllerApi.md#get_fixtures_attachments) | **GET** /testresult/{testResultId}/fixture/attachment | Find fixtures attachments for test result


# **get_fixtures**
> List[TestFixtureResultDto] get_fixtures(test_result_id)

Find fixtures for test result

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_fixture_result_dto import TestFixtureResultDto
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
    api_instance = openapi_client.TestResultFixtureControllerApi(api_client)
    test_result_id = 56 # int | 

    try:
        # Find fixtures for test result
        api_response = api_instance.get_fixtures(test_result_id)
        print("The response of TestResultFixtureControllerApi->get_fixtures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultFixtureControllerApi->get_fixtures: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 

### Return type

[**List[TestFixtureResultDto]**](TestFixtureResultDto.md)

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

# **get_fixtures_attachments**
> PageTestFixtureResultAttachmentRowDto get_fixtures_attachments(test_result_id, page=page, size=size, sort=sort)

Find fixtures attachments for test result

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_fixture_result_attachment_row_dto import PageTestFixtureResultAttachmentRowDto
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
    api_instance = openapi_client.TestResultFixtureControllerApi(api_client)
    test_result_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find fixtures attachments for test result
        api_response = api_instance.get_fixtures_attachments(test_result_id, page=page, size=size, sort=sort)
        print("The response of TestResultFixtureControllerApi->get_fixtures_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultFixtureControllerApi->get_fixtures_attachments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageTestFixtureResultAttachmentRowDto**](PageTestFixtureResultAttachmentRowDto.md)

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

