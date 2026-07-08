# openapi_client.LaunchTagControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create25**](LaunchTagControllerApi.md#create25) | **POST** /launch/tag | Create a new Launch tag
[**delete25**](LaunchTagControllerApi.md#delete25) | **DELETE** /launch/tag/{id} | Delete Launch tag by id
[**find_all26**](LaunchTagControllerApi.md#find_all26) | **GET** /launch/tag | Find all tags
[**find_one21**](LaunchTagControllerApi.md#find_one21) | **GET** /launch/tag/{id} | Find Launch tag by id
[**patch23**](LaunchTagControllerApi.md#patch23) | **PATCH** /launch/tag/{id} | Patch Launch tag
[**suggest11**](LaunchTagControllerApi.md#suggest11) | **GET** /launch/tag/suggest | Suggest Launch Tags


# **create25**
> LaunchTagDto create25(launch_tag_create_dto)

Create a new Launch tag

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_tag_create_dto import LaunchTagCreateDto
from openapi_client.models.launch_tag_dto import LaunchTagDto
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
    api_instance = openapi_client.LaunchTagControllerApi(api_client)
    launch_tag_create_dto = openapi_client.LaunchTagCreateDto() # LaunchTagCreateDto | 

    try:
        # Create a new Launch tag
        api_response = api_instance.create25(launch_tag_create_dto)
        print("The response of LaunchTagControllerApi->create25:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchTagControllerApi->create25: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_tag_create_dto** | [**LaunchTagCreateDto**](LaunchTagCreateDto.md)|  | 

### Return type

[**LaunchTagDto**](LaunchTagDto.md)

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

# **delete25**
> delete25(id)

Delete Launch tag by id

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
    api_instance = openapi_client.LaunchTagControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete Launch tag by id
        api_instance.delete25(id)
    except Exception as e:
        print("Exception when calling LaunchTagControllerApi->delete25: %s\n" % e)
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

# **find_all26**
> PageLaunchTagDto find_all26(project_id=project_id, page=page, size=size, sort=sort)

Find all tags

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_launch_tag_dto import PageLaunchTagDto
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
    api_instance = openapi_client.LaunchTagControllerApi(api_client)
    project_id = 56 # int |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find all tags
        api_response = api_instance.find_all26(project_id=project_id, page=page, size=size, sort=sort)
        print("The response of LaunchTagControllerApi->find_all26:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchTagControllerApi->find_all26: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageLaunchTagDto**](PageLaunchTagDto.md)

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

# **find_one21**
> LaunchTagDto find_one21(id)

Find Launch tag by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_tag_dto import LaunchTagDto
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
    api_instance = openapi_client.LaunchTagControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find Launch tag by id
        api_response = api_instance.find_one21(id)
        print("The response of LaunchTagControllerApi->find_one21:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchTagControllerApi->find_one21: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**LaunchTagDto**](LaunchTagDto.md)

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

# **patch23**
> LaunchTagDto patch23(id, launch_tag_patch_dto)

Patch Launch tag

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_tag_dto import LaunchTagDto
from openapi_client.models.launch_tag_patch_dto import LaunchTagPatchDto
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
    api_instance = openapi_client.LaunchTagControllerApi(api_client)
    id = 56 # int | 
    launch_tag_patch_dto = openapi_client.LaunchTagPatchDto() # LaunchTagPatchDto | 

    try:
        # Patch Launch tag
        api_response = api_instance.patch23(id, launch_tag_patch_dto)
        print("The response of LaunchTagControllerApi->patch23:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchTagControllerApi->patch23: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **launch_tag_patch_dto** | [**LaunchTagPatchDto**](LaunchTagPatchDto.md)|  | 

### Return type

[**LaunchTagDto**](LaunchTagDto.md)

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

# **suggest11**
> PageIdAndNameOnlyDto suggest11(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest Launch Tags

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
    api_instance = openapi_client.LaunchTagControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest Launch Tags
        api_response = api_instance.suggest11(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of LaunchTagControllerApi->suggest11:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchTagControllerApi->suggest11: %s\n" % e)
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

