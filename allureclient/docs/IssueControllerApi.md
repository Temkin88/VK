# openapi_client.IssueControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create29**](IssueControllerApi.md#create29) | **POST** /issue | Create a new issue
[**delete28**](IssueControllerApi.md#delete28) | **DELETE** /issue/{id} | Delete issue by id
[**find_all28**](IssueControllerApi.md#find_all28) | **GET** /issue | Find all issues
[**find_one24**](IssueControllerApi.md#find_one24) | **GET** /issue/{id} | Find issue by id
[**patch26**](IssueControllerApi.md#patch26) | **PATCH** /issue/{id} | Patch issue schema
[**suggest13**](IssueControllerApi.md#suggest13) | **GET** /issue/suggest | Suggest issues


# **create29**
> IssueDto create29(issue_create_dto)

Create a new issue

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.issue_create_dto import IssueCreateDto
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
    api_instance = openapi_client.IssueControllerApi(api_client)
    issue_create_dto = openapi_client.IssueCreateDto() # IssueCreateDto | 

    try:
        # Create a new issue
        api_response = api_instance.create29(issue_create_dto)
        print("The response of IssueControllerApi->create29:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueControllerApi->create29: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_create_dto** | [**IssueCreateDto**](IssueCreateDto.md)|  | 

### Return type

[**IssueDto**](IssueDto.md)

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

# **delete28**
> delete28(id)

Delete issue by id

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
    api_instance = openapi_client.IssueControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete issue by id
        api_instance.delete28(id)
    except Exception as e:
        print("Exception when calling IssueControllerApi->delete28: %s\n" % e)
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

# **find_all28**
> PageIssueDto find_all28(integration_id, page=page, size=size, sort=sort)

Find all issues

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_issue_dto import PageIssueDto
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
    api_instance = openapi_client.IssueControllerApi(api_client)
    integration_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,ASC"])

    try:
        # Find all issues
        api_response = api_instance.find_all28(integration_id, page=page, size=size, sort=sort)
        print("The response of IssueControllerApi->find_all28:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueControllerApi->find_all28: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,ASC&quot;]]

### Return type

[**PageIssueDto**](PageIssueDto.md)

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

# **find_one24**
> IssueDto find_one24(id)

Find issue by id

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
    api_instance = openapi_client.IssueControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find issue by id
        api_response = api_instance.find_one24(id)
        print("The response of IssueControllerApi->find_one24:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueControllerApi->find_one24: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**IssueDto**](IssueDto.md)

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

# **patch26**
> IssueDto patch26(id, issue_patch_dto)

Patch issue schema

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.issue_dto import IssueDto
from openapi_client.models.issue_patch_dto import IssuePatchDto
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
    api_instance = openapi_client.IssueControllerApi(api_client)
    id = 56 # int | 
    issue_patch_dto = openapi_client.IssuePatchDto() # IssuePatchDto | 

    try:
        # Patch issue schema
        api_response = api_instance.patch26(id, issue_patch_dto)
        print("The response of IssueControllerApi->patch26:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueControllerApi->patch26: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **issue_patch_dto** | [**IssuePatchDto**](IssuePatchDto.md)|  | 

### Return type

[**IssueDto**](IssueDto.md)

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

# **suggest13**
> PageIdAndNameOnlyDto suggest13(query=query, project_id=project_id, integration_id=integration_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest issues

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
    api_instance = openapi_client.IssueControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    integration_id = [56] # List[int] |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest issues
        api_response = api_instance.suggest13(query=query, project_id=project_id, integration_id=integration_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of IssueControllerApi->suggest13:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueControllerApi->suggest13: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **integration_id** | [**List[int]**](int.md)|  | [optional] 
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

