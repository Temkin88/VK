# openapi_client.CategoryMatcherControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create46**](CategoryMatcherControllerApi.md#create46) | **POST** /categorymatcher | 
[**delete_by_id4**](CategoryMatcherControllerApi.md#delete_by_id4) | **DELETE** /categorymatcher/{id} | 
[**find_all422**](CategoryMatcherControllerApi.md#find_all422) | **GET** /categorymatcher | 
[**patch43**](CategoryMatcherControllerApi.md#patch43) | **PATCH** /categorymatcher/{id} | 


# **create46**
> CategoryMatcherDto create46(category_matcher_create_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.category_matcher_create_dto import CategoryMatcherCreateDto
from openapi_client.models.category_matcher_dto import CategoryMatcherDto
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
    api_instance = openapi_client.CategoryMatcherControllerApi(api_client)
    category_matcher_create_dto = openapi_client.CategoryMatcherCreateDto() # CategoryMatcherCreateDto | 

    try:
        api_response = api_instance.create46(category_matcher_create_dto)
        print("The response of CategoryMatcherControllerApi->create46:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryMatcherControllerApi->create46: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_matcher_create_dto** | [**CategoryMatcherCreateDto**](CategoryMatcherCreateDto.md)|  | 

### Return type

[**CategoryMatcherDto**](CategoryMatcherDto.md)

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

# **delete_by_id4**
> delete_by_id4(id)



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
    api_instance = openapi_client.CategoryMatcherControllerApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_by_id4(id)
    except Exception as e:
        print("Exception when calling CategoryMatcherControllerApi->delete_by_id4: %s\n" % e)
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

# **find_all422**
> PageCategoryMatcherDto find_all422(excluded_project_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_category_matcher_dto import PageCategoryMatcherDto
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
    api_instance = openapi_client.CategoryMatcherControllerApi(api_client)
    excluded_project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        api_response = api_instance.find_all422(excluded_project_id, page=page, size=size, sort=sort)
        print("The response of CategoryMatcherControllerApi->find_all422:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryMatcherControllerApi->find_all422: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **excluded_project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageCategoryMatcherDto**](PageCategoryMatcherDto.md)

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

# **patch43**
> CategoryMatcherDto patch43(id, category_matcher_patch_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.category_matcher_dto import CategoryMatcherDto
from openapi_client.models.category_matcher_patch_dto import CategoryMatcherPatchDto
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
    api_instance = openapi_client.CategoryMatcherControllerApi(api_client)
    id = 56 # int | 
    category_matcher_patch_dto = openapi_client.CategoryMatcherPatchDto() # CategoryMatcherPatchDto | 

    try:
        api_response = api_instance.patch43(id, category_matcher_patch_dto)
        print("The response of CategoryMatcherControllerApi->patch43:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryMatcherControllerApi->patch43: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **category_matcher_patch_dto** | [**CategoryMatcherPatchDto**](CategoryMatcherPatchDto.md)|  | 

### Return type

[**CategoryMatcherDto**](CategoryMatcherDto.md)

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

