# openapi_client.WidgetControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create2**](WidgetControllerApi.md#create2) | **POST** /widget | 
[**delete3**](WidgetControllerApi.md#delete3) | **DELETE** /widget/{id} | 
[**find_all_by_dashboard**](WidgetControllerApi.md#find_all_by_dashboard) | **GET** /widget | 
[**find_one2**](WidgetControllerApi.md#find_one2) | **GET** /widget/{id} | 
[**get_data**](WidgetControllerApi.md#get_data) | **GET** /widget/{id}/data | 
[**patch2**](WidgetControllerApi.md#patch2) | **PATCH** /widget/{id} | 


# **create2**
> WidgetDto create2(widget_create_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.widget_create_dto import WidgetCreateDto
from openapi_client.models.widget_dto import WidgetDto
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
    api_instance = openapi_client.WidgetControllerApi(api_client)
    widget_create_dto = openapi_client.WidgetCreateDto() # WidgetCreateDto | 

    try:
        api_response = api_instance.create2(widget_create_dto)
        print("The response of WidgetControllerApi->create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetControllerApi->create2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_create_dto** | [**WidgetCreateDto**](WidgetCreateDto.md)|  | 

### Return type

[**WidgetDto**](WidgetDto.md)

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

# **delete3**
> delete3(id)



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
    api_instance = openapi_client.WidgetControllerApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete3(id)
    except Exception as e:
        print("Exception when calling WidgetControllerApi->delete3: %s\n" % e)
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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_by_dashboard**
> PageWidgetDto find_all_by_dashboard(dashboard_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_widget_dto import PageWidgetDto
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
    api_instance = openapi_client.WidgetControllerApi(api_client)
    dashboard_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        api_response = api_instance.find_all_by_dashboard(dashboard_id, page=page, size=size, sort=sort)
        print("The response of WidgetControllerApi->find_all_by_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetControllerApi->find_all_by_dashboard: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageWidgetDto**](PageWidgetDto.md)

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

# **find_one2**
> WidgetDto find_one2(id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.widget_dto import WidgetDto
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
    api_instance = openapi_client.WidgetControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.find_one2(id)
        print("The response of WidgetControllerApi->find_one2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetControllerApi->find_one2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**WidgetDto**](WidgetDto.md)

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

# **get_data**
> WidgetDataDto get_data(id, parameters)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.widget_data_dto import WidgetDataDto
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
    api_instance = openapi_client.WidgetControllerApi(api_client)
    id = 56 # int | 
    parameters = {'key': openapi_client.List[str]()} # MultiValueMapStringString | 

    try:
        api_response = api_instance.get_data(id, parameters)
        print("The response of WidgetControllerApi->get_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetControllerApi->get_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **parameters** | [**MultiValueMapStringString**](List[str].md)|  | 

### Return type

[**WidgetDataDto**](WidgetDataDto.md)

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

# **patch2**
> WidgetDto patch2(id, widget_patch_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.widget_dto import WidgetDto
from openapi_client.models.widget_patch_dto import WidgetPatchDto
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
    api_instance = openapi_client.WidgetControllerApi(api_client)
    id = 56 # int | 
    widget_patch_dto = openapi_client.WidgetPatchDto() # WidgetPatchDto | 

    try:
        api_response = api_instance.patch2(id, widget_patch_dto)
        print("The response of WidgetControllerApi->patch2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetControllerApi->patch2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **widget_patch_dto** | [**WidgetPatchDto**](WidgetPatchDto.md)|  | 

### Return type

[**WidgetDto**](WidgetDto.md)

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

