# openapi_client.FilterControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create33**](FilterControllerApi.md#create33) | **POST** /filter | Create a new filter
[**delete30**](FilterControllerApi.md#delete30) | **DELETE** /filter/{id} | Delete filter by id
[**find_all32**](FilterControllerApi.md#find_all32) | **GET** /filter | Find all filters by given project
[**find_one26**](FilterControllerApi.md#find_one26) | **GET** /filter/{id} | Find filter by id
[**get_base**](FilterControllerApi.md#get_base) | **GET** /filter/base | Get default filter
[**patch30**](FilterControllerApi.md#patch30) | **PATCH** /filter/{id} | Patch filter
[**set_base**](FilterControllerApi.md#set_base) | **POST** /filter/base | Set filter as default
[**suggest15**](FilterControllerApi.md#suggest15) | **GET** /filter/suggest | Get suggest for filters


# **create33**
> FilterDto create33(filter_create_dto)

Create a new filter

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.filter_create_dto import FilterCreateDto
from openapi_client.models.filter_dto import FilterDto
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
    api_instance = openapi_client.FilterControllerApi(api_client)
    filter_create_dto = openapi_client.FilterCreateDto() # FilterCreateDto | 

    try:
        # Create a new filter
        api_response = api_instance.create33(filter_create_dto)
        print("The response of FilterControllerApi->create33:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterControllerApi->create33: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_create_dto** | [**FilterCreateDto**](FilterCreateDto.md)|  | 

### Return type

[**FilterDto**](FilterDto.md)

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

# **delete30**
> delete30(id)

Delete filter by id

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
    api_instance = openapi_client.FilterControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete filter by id
        api_instance.delete30(id)
    except Exception as e:
        print("Exception when calling FilterControllerApi->delete30: %s\n" % e)
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

# **find_all32**
> PageFilterDto find_all32(project_id, page=page, size=size, sort=sort)

Find all filters by given project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_filter_dto import PageFilterDto
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
    api_instance = openapi_client.FilterControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find all filters by given project
        api_response = api_instance.find_all32(project_id, page=page, size=size, sort=sort)
        print("The response of FilterControllerApi->find_all32:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterControllerApi->find_all32: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageFilterDto**](PageFilterDto.md)

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

# **find_one26**
> FilterDto find_one26(id)

Find filter by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.filter_dto import FilterDto
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
    api_instance = openapi_client.FilterControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find filter by id
        api_response = api_instance.find_one26(id)
        print("The response of FilterControllerApi->find_one26:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterControllerApi->find_one26: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**FilterDto**](FilterDto.md)

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

# **get_base**
> FilterDto get_base(project_id)

Get default filter

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.filter_dto import FilterDto
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
    api_instance = openapi_client.FilterControllerApi(api_client)
    project_id = 56 # int | 

    try:
        # Get default filter
        api_response = api_instance.get_base(project_id)
        print("The response of FilterControllerApi->get_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterControllerApi->get_base: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**FilterDto**](FilterDto.md)

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

# **patch30**
> FilterDto patch30(id, filter_patch_dto)

Patch filter

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.filter_dto import FilterDto
from openapi_client.models.filter_patch_dto import FilterPatchDto
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
    api_instance = openapi_client.FilterControllerApi(api_client)
    id = 56 # int | 
    filter_patch_dto = openapi_client.FilterPatchDto() # FilterPatchDto | 

    try:
        # Patch filter
        api_response = api_instance.patch30(id, filter_patch_dto)
        print("The response of FilterControllerApi->patch30:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterControllerApi->patch30: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **filter_patch_dto** | [**FilterPatchDto**](FilterPatchDto.md)|  | 

### Return type

[**FilterDto**](FilterDto.md)

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

# **set_base**
> set_base(project_id, filter_base_set_dto)

Set filter as default

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.filter_base_set_dto import FilterBaseSetDto
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
    api_instance = openapi_client.FilterControllerApi(api_client)
    project_id = 56 # int | 
    filter_base_set_dto = openapi_client.FilterBaseSetDto() # FilterBaseSetDto | 

    try:
        # Set filter as default
        api_instance.set_base(project_id, filter_base_set_dto)
    except Exception as e:
        print("Exception when calling FilterControllerApi->set_base: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **filter_base_set_dto** | [**FilterBaseSetDto**](FilterBaseSetDto.md)|  | 

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

# **suggest15**
> PageIdAndNameOnlyDto suggest15(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Get suggest for filters

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
    api_instance = openapi_client.FilterControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Get suggest for filters
        api_response = api_instance.suggest15(query=query, project_id=project_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of FilterControllerApi->suggest15:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterControllerApi->suggest15: %s\n" % e)
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

