# openapi_client.TestTagControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create15**](TestTagControllerApi.md#create15) | **POST** /tag | Create a new test tag
[**delete15**](TestTagControllerApi.md#delete15) | **DELETE** /tag/{id} | Delete test tag by id
[**find_all14**](TestTagControllerApi.md#find_all14) | **GET** /tag | Find all test tags
[**find_one12**](TestTagControllerApi.md#find_one12) | **GET** /tag/{id} | Find test tag by id
[**patch14**](TestTagControllerApi.md#patch14) | **PATCH** /tag/{id} | Patch test tag
[**suggest6**](TestTagControllerApi.md#suggest6) | **GET** /tag/suggest | Suggest test tags


# **create15**
> TestTagDto create15(test_tag_create_dto)

Create a new test tag

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_tag_create_dto import TestTagCreateDto
from openapi_client.models.test_tag_dto import TestTagDto
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
    api_instance = openapi_client.TestTagControllerApi(api_client)
    test_tag_create_dto = openapi_client.TestTagCreateDto() # TestTagCreateDto | 

    try:
        # Create a new test tag
        api_response = api_instance.create15(test_tag_create_dto)
        print("The response of TestTagControllerApi->create15:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestTagControllerApi->create15: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_tag_create_dto** | [**TestTagCreateDto**](TestTagCreateDto.md)|  | 

### Return type

[**TestTagDto**](TestTagDto.md)

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

# **delete15**
> delete15(id)

Delete test tag by id

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
    api_instance = openapi_client.TestTagControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete test tag by id
        api_instance.delete15(id)
    except Exception as e:
        print("Exception when calling TestTagControllerApi->delete15: %s\n" % e)
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

# **find_all14**
> List[TestTagDto] find_all14()

Find all test tags

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_tag_dto import TestTagDto
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
    api_instance = openapi_client.TestTagControllerApi(api_client)

    try:
        # Find all test tags
        api_response = api_instance.find_all14()
        print("The response of TestTagControllerApi->find_all14:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestTagControllerApi->find_all14: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[TestTagDto]**](TestTagDto.md)

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

# **find_one12**
> TestTagDto find_one12(id)

Find test tag by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_tag_dto import TestTagDto
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
    api_instance = openapi_client.TestTagControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find test tag by id
        api_response = api_instance.find_one12(id)
        print("The response of TestTagControllerApi->find_one12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestTagControllerApi->find_one12: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestTagDto**](TestTagDto.md)

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

# **patch14**
> TestTagDto patch14(id, test_tag_patch_dto)

Patch test tag

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_tag_dto import TestTagDto
from openapi_client.models.test_tag_patch_dto import TestTagPatchDto
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
    api_instance = openapi_client.TestTagControllerApi(api_client)
    id = 56 # int | 
    test_tag_patch_dto = openapi_client.TestTagPatchDto() # TestTagPatchDto | 

    try:
        # Patch test tag
        api_response = api_instance.patch14(id, test_tag_patch_dto)
        print("The response of TestTagControllerApi->patch14:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestTagControllerApi->patch14: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_tag_patch_dto** | [**TestTagPatchDto**](TestTagPatchDto.md)|  | 

### Return type

[**TestTagDto**](TestTagDto.md)

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

# **suggest6**
> PageIdAndNameOnlyDto suggest6(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest test tags

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
    api_instance = openapi_client.TestTagControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest test tags
        api_response = api_instance.suggest6(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of TestTagControllerApi->suggest6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestTagControllerApi->suggest6: %s\n" % e)
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

