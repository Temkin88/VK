# openapi_client.CustomFieldValueControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create43**](CustomFieldValueControllerApi.md#create43) | **POST** /cfv | Create a new custom field value
[**delete41**](CustomFieldValueControllerApi.md#delete41) | **DELETE** /cfv/{id} | Delete custom field value by id
[**find_all40**](CustomFieldValueControllerApi.md#find_all40) | **GET** /cfv | Find all custom field values
[**find_one35**](CustomFieldValueControllerApi.md#find_one35) | **GET** /cfv/{id} | Find custom field value by id
[**patch40**](CustomFieldValueControllerApi.md#patch40) | **PATCH** /cfv/{id} | Patch custom field value
[**suggest20**](CustomFieldValueControllerApi.md#suggest20) | **GET** /cfv/suggest | Suggest custom field values


# **create43**
> CustomFieldValueDto create43(custom_field_value_create_dto)

Create a new custom field value

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_value_create_dto import CustomFieldValueCreateDto
from openapi_client.models.custom_field_value_dto import CustomFieldValueDto
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
    api_instance = openapi_client.CustomFieldValueControllerApi(api_client)
    custom_field_value_create_dto = openapi_client.CustomFieldValueCreateDto() # CustomFieldValueCreateDto | 

    try:
        # Create a new custom field value
        api_response = api_instance.create43(custom_field_value_create_dto)
        print("The response of CustomFieldValueControllerApi->create43:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldValueControllerApi->create43: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_value_create_dto** | [**CustomFieldValueCreateDto**](CustomFieldValueCreateDto.md)|  | 

### Return type

[**CustomFieldValueDto**](CustomFieldValueDto.md)

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

# **delete41**
> delete41(id)

Delete custom field value by id

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
    api_instance = openapi_client.CustomFieldValueControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete custom field value by id
        api_instance.delete41(id)
    except Exception as e:
        print("Exception when calling CustomFieldValueControllerApi->delete41: %s\n" % e)
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

# **find_all40**
> PageCustomFieldValueDto find_all40(custom_field_id, page=page, size=size, sort=sort)

Find all custom field values

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_custom_field_value_dto import PageCustomFieldValueDto
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
    api_instance = openapi_client.CustomFieldValueControllerApi(api_client)
    custom_field_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find all custom field values
        api_response = api_instance.find_all40(custom_field_id, page=page, size=size, sort=sort)
        print("The response of CustomFieldValueControllerApi->find_all40:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldValueControllerApi->find_all40: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageCustomFieldValueDto**](PageCustomFieldValueDto.md)

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

# **find_one35**
> CustomFieldValueDto find_one35(id)

Find custom field value by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_value_dto import CustomFieldValueDto
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
    api_instance = openapi_client.CustomFieldValueControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find custom field value by id
        api_response = api_instance.find_one35(id)
        print("The response of CustomFieldValueControllerApi->find_one35:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldValueControllerApi->find_one35: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CustomFieldValueDto**](CustomFieldValueDto.md)

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

# **patch40**
> CustomFieldValueDto patch40(id, custom_field_value_patch_dto)

Patch custom field value

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_value_dto import CustomFieldValueDto
from openapi_client.models.custom_field_value_patch_dto import CustomFieldValuePatchDto
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
    api_instance = openapi_client.CustomFieldValueControllerApi(api_client)
    id = 56 # int | 
    custom_field_value_patch_dto = openapi_client.CustomFieldValuePatchDto() # CustomFieldValuePatchDto | 

    try:
        # Patch custom field value
        api_response = api_instance.patch40(id, custom_field_value_patch_dto)
        print("The response of CustomFieldValueControllerApi->patch40:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldValueControllerApi->patch40: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **custom_field_value_patch_dto** | [**CustomFieldValuePatchDto**](CustomFieldValuePatchDto.md)|  | 

### Return type

[**CustomFieldValueDto**](CustomFieldValueDto.md)

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

# **suggest20**
> PageIdAndNameOnlyDto suggest20(custom_field_id=custom_field_id, query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest custom field values

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
    api_instance = openapi_client.CustomFieldValueControllerApi(api_client)
    custom_field_id = 56 # int |  (optional)
    query = 'query_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest custom field values
        api_response = api_instance.suggest20(custom_field_id=custom_field_id, query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of CustomFieldValueControllerApi->suggest20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldValueControllerApi->suggest20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **int**|  | [optional] 
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

