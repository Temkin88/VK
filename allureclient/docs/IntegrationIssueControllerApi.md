# openapi_client.IntegrationIssueControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fix_links**](IntegrationIssueControllerApi.md#fix_links) | **POST** /integration/issue/{integrationId}/fixlinks | Fix issue links without url
[**get_fields**](IntegrationIssueControllerApi.md#get_fields) | **GET** /integration/issue/field | Get available fields for specified project integration, project key and issue type
[**get_issues3**](IntegrationIssueControllerApi.md#get_issues3) | **GET** /integration/issue/suggest | Get available issues for specified project integration
[**get_projects**](IntegrationIssueControllerApi.md#get_projects) | **GET** /integration/issue/project | Get available projects for specified project integration
[**get_types**](IntegrationIssueControllerApi.md#get_types) | **GET** /integration/issue/type | Get available issue types for specified project integration and project key


# **fix_links**
> IntegrationLinksFixedDto fix_links(integration_id)

Fix issue links without url

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.integration_links_fixed_dto import IntegrationLinksFixedDto
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
    api_instance = openapi_client.IntegrationIssueControllerApi(api_client)
    integration_id = 56 # int | 

    try:
        # Fix issue links without url
        api_response = api_instance.fix_links(integration_id)
        print("The response of IntegrationIssueControllerApi->fix_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationIssueControllerApi->fix_links: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**|  | 

### Return type

[**IntegrationLinksFixedDto**](IntegrationLinksFixedDto.md)

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

# **get_fields**
> List[GetFields200ResponseInner] get_fields(project_id, integration_id, project_key, issue_type_id)

Get available fields for specified project integration, project key and issue type

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.get_fields200_response_inner import GetFields200ResponseInner
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
    api_instance = openapi_client.IntegrationIssueControllerApi(api_client)
    project_id = 56 # int | 
    integration_id = 56 # int | 
    project_key = 'project_key_example' # str | 
    issue_type_id = 'issue_type_id_example' # str | 

    try:
        # Get available fields for specified project integration, project key and issue type
        api_response = api_instance.get_fields(project_id, integration_id, project_key, issue_type_id)
        print("The response of IntegrationIssueControllerApi->get_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationIssueControllerApi->get_fields: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **integration_id** | **int**|  | 
 **project_key** | **str**|  | 
 **issue_type_id** | **str**|  | 

### Return type

[**List[GetFields200ResponseInner]**](GetFields200ResponseInner.md)

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

# **get_issues3**
> List[ExtIssueLink] get_issues3(project_id, integration_id, query=query)

Get available issues for specified project integration

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.ext_issue_link import ExtIssueLink
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
    api_instance = openapi_client.IntegrationIssueControllerApi(api_client)
    project_id = 56 # int | 
    integration_id = 56 # int | 
    query = '' # str |  (optional) (default to '')

    try:
        # Get available issues for specified project integration
        api_response = api_instance.get_issues3(project_id, integration_id, query=query)
        print("The response of IntegrationIssueControllerApi->get_issues3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationIssueControllerApi->get_issues3: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **integration_id** | **int**|  | 
 **query** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[ExtIssueLink]**](ExtIssueLink.md)

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

# **get_projects**
> List[ExtProject] get_projects(project_id, integration_id, query=query)

Get available projects for specified project integration

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.ext_project import ExtProject
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
    api_instance = openapi_client.IntegrationIssueControllerApi(api_client)
    project_id = 56 # int | 
    integration_id = 56 # int | 
    query = '' # str |  (optional) (default to '')

    try:
        # Get available projects for specified project integration
        api_response = api_instance.get_projects(project_id, integration_id, query=query)
        print("The response of IntegrationIssueControllerApi->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationIssueControllerApi->get_projects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **integration_id** | **int**|  | 
 **query** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[ExtProject]**](ExtProject.md)

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

# **get_types**
> List[ExtIssueType] get_types(project_id, integration_id, project_key)

Get available issue types for specified project integration and project key

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.ext_issue_type import ExtIssueType
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
    api_instance = openapi_client.IntegrationIssueControllerApi(api_client)
    project_id = 56 # int | 
    integration_id = 56 # int | 
    project_key = 'project_key_example' # str | 

    try:
        # Get available issue types for specified project integration and project key
        api_response = api_instance.get_types(project_id, integration_id, project_key)
        print("The response of IntegrationIssueControllerApi->get_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationIssueControllerApi->get_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **integration_id** | **int**|  | 
 **project_key** | **str**|  | 

### Return type

[**List[ExtIssueType]**](ExtIssueType.md)

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

