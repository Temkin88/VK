# openapi_client.CustomFieldControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create45**](CustomFieldControllerApi.md#create45) | **POST** /cf | 
[**delete43**](CustomFieldControllerApi.md#delete43) | **DELETE** /cf/{id} | 
[**find_all421**](CustomFieldControllerApi.md#find_all421) | **GET** /cf | 
[**find_one37**](CustomFieldControllerApi.md#find_one37) | **GET** /cf/{id} | 
[**merge3**](CustomFieldControllerApi.md#merge3) | **POST** /cf/merge | 
[**patch42**](CustomFieldControllerApi.md#patch42) | **PATCH** /cf/{id} | 
[**suggest21**](CustomFieldControllerApi.md#suggest21) | **GET** /cf/suggest | 


# **create45**
> CustomFieldDto create45(custom_field_create_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_create_dto import CustomFieldCreateDto
from openapi_client.models.custom_field_dto import CustomFieldDto
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
    api_instance = openapi_client.CustomFieldControllerApi(api_client)
    custom_field_create_dto = openapi_client.CustomFieldCreateDto() # CustomFieldCreateDto | 

    try:
        api_response = api_instance.create45(custom_field_create_dto)
        print("The response of CustomFieldControllerApi->create45:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldControllerApi->create45: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_create_dto** | [**CustomFieldCreateDto**](CustomFieldCreateDto.md)|  | 

### Return type

[**CustomFieldDto**](CustomFieldDto.md)

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

# **delete43**
> delete43(id)



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
    api_instance = openapi_client.CustomFieldControllerApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete43(id)
    except Exception as e:
        print("Exception when calling CustomFieldControllerApi->delete43: %s\n" % e)
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

# **find_all421**
> List[CustomFieldDto] find_all421(project_id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_dto import CustomFieldDto
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
    api_instance = openapi_client.CustomFieldControllerApi(api_client)
    project_id = 56 # int | 

    try:
        api_response = api_instance.find_all421(project_id)
        print("The response of CustomFieldControllerApi->find_all421:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldControllerApi->find_all421: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**List[CustomFieldDto]**](CustomFieldDto.md)

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

# **find_one37**
> CustomFieldDto find_one37(id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_dto import CustomFieldDto
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
    api_instance = openapi_client.CustomFieldControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.find_one37(id)
        print("The response of CustomFieldControllerApi->find_one37:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldControllerApi->find_one37: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CustomFieldDto**](CustomFieldDto.md)

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

# **merge3**
> merge3(custom_field_merge_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_merge_dto import CustomFieldMergeDto
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
    api_instance = openapi_client.CustomFieldControllerApi(api_client)
    custom_field_merge_dto = openapi_client.CustomFieldMergeDto() # CustomFieldMergeDto | 

    try:
        api_instance.merge3(custom_field_merge_dto)
    except Exception as e:
        print("Exception when calling CustomFieldControllerApi->merge3: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_merge_dto** | [**CustomFieldMergeDto**](CustomFieldMergeDto.md)|  | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch42**
> CustomFieldDto patch42(id, custom_field_patch_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.custom_field_dto import CustomFieldDto
from openapi_client.models.custom_field_patch_dto import CustomFieldPatchDto
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
    api_instance = openapi_client.CustomFieldControllerApi(api_client)
    id = 56 # int | 
    custom_field_patch_dto = openapi_client.CustomFieldPatchDto() # CustomFieldPatchDto | 

    try:
        api_response = api_instance.patch42(id, custom_field_patch_dto)
        print("The response of CustomFieldControllerApi->patch42:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldControllerApi->patch42: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **custom_field_patch_dto** | [**CustomFieldPatchDto**](CustomFieldPatchDto.md)|  | 

### Return type

[**CustomFieldDto**](CustomFieldDto.md)

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

# **suggest21**
> PageIdAndNameOnlyDto suggest21(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)



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
    api_instance = openapi_client.CustomFieldControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        api_response = api_instance.suggest21(query=query, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of CustomFieldControllerApi->suggest21:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldControllerApi->suggest21: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
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

