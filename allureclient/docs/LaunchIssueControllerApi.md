# openapi_client.LaunchIssueControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export**](LaunchIssueControllerApi.md#export) | **POST** /launch/{launchId}/issue/export | Export launch data to issue issueTracker
[**get_issues2**](LaunchIssueControllerApi.md#get_issues2) | **GET** /launch/issue | Get all issues used in launches


# **export**
> export(launch_id, issue_dto)

Export launch data to issue issueTracker

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.issue_dto import IssueDto
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
    api_instance = openapi_client.LaunchIssueControllerApi(api_client)
    launch_id = 56 # int | 
    issue_dto = [openapi_client.IssueDto()] # List[IssueDto] | 

    try:
        # Export launch data to issue issueTracker
        api_instance.export(launch_id, issue_dto)
    except Exception as e:
        print("Exception when calling LaunchIssueControllerApi->export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **int**|  | 
 **issue_dto** | [**List[IssueDto]**](IssueDto.md)|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issues2**
> List[IssueDto] get_issues2(project_id)

Get all issues used in launches

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.issue_dto import IssueDto
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
    api_instance = openapi_client.LaunchIssueControllerApi(api_client)
    project_id = 56 # int | 

    try:
        # Get all issues used in launches
        api_response = api_instance.get_issues2(project_id)
        print("The response of LaunchIssueControllerApi->get_issues2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchIssueControllerApi->get_issues2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**List[IssueDto]**](IssueDto.md)

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

