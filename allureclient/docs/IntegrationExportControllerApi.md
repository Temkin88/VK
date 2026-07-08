# openapi_client.IntegrationExportControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create32**](IntegrationExportControllerApi.md#create32) | **POST** /integration/export | 
[**delete_by_id3**](IntegrationExportControllerApi.md#delete_by_id3) | **DELETE** /integration/export/{id} | 
[**find_all30**](IntegrationExportControllerApi.md#find_all30) | **GET** /integration/export | 
[**find_by_id2**](IntegrationExportControllerApi.md#find_by_id2) | **GET** /integration/export/{id} | 
[**get_fields1**](IntegrationExportControllerApi.md#get_fields1) | **GET** /integration/export/field | Get export form fields for specified project integration
[**patch29**](IntegrationExportControllerApi.md#patch29) | **PATCH** /integration/export/{id} | 


# **create32**
> IntegrationExportDto create32(integration_export_create_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.integration_export_create_dto import IntegrationExportCreateDto
from openapi_client.models.integration_export_dto import IntegrationExportDto
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
    api_instance = openapi_client.IntegrationExportControllerApi(api_client)
    integration_export_create_dto = openapi_client.IntegrationExportCreateDto() # IntegrationExportCreateDto | 

    try:
        api_response = api_instance.create32(integration_export_create_dto)
        print("The response of IntegrationExportControllerApi->create32:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationExportControllerApi->create32: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_export_create_dto** | [**IntegrationExportCreateDto**](IntegrationExportCreateDto.md)|  | 

### Return type

[**IntegrationExportDto**](IntegrationExportDto.md)

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

# **delete_by_id3**
> delete_by_id3(id)



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
    api_instance = openapi_client.IntegrationExportControllerApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_by_id3(id)
    except Exception as e:
        print("Exception when calling IntegrationExportControllerApi->delete_by_id3: %s\n" % e)
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

# **find_all30**
> PageIntegrationExportDto find_all30(integration_id, project_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_integration_export_dto import PageIntegrationExportDto
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
    api_instance = openapi_client.IntegrationExportControllerApi(api_client)
    integration_id = 56 # int | 
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        api_response = api_instance.find_all30(integration_id, project_id, page=page, size=size, sort=sort)
        print("The response of IntegrationExportControllerApi->find_all30:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationExportControllerApi->find_all30: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**|  | 
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageIntegrationExportDto**](PageIntegrationExportDto.md)

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

# **find_by_id2**
> IntegrationExportDto find_by_id2(id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.integration_export_dto import IntegrationExportDto
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
    api_instance = openapi_client.IntegrationExportControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.find_by_id2(id)
        print("The response of IntegrationExportControllerApi->find_by_id2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationExportControllerApi->find_by_id2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**IntegrationExportDto**](IntegrationExportDto.md)

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

# **get_fields1**
> List[GetFields200ResponseInner] get_fields1(integration_id, project_id)

Get export form fields for specified project integration

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
    api_instance = openapi_client.IntegrationExportControllerApi(api_client)
    integration_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Get export form fields for specified project integration
        api_response = api_instance.get_fields1(integration_id, project_id)
        print("The response of IntegrationExportControllerApi->get_fields1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationExportControllerApi->get_fields1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**|  | 
 **project_id** | **int**|  | 

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

# **patch29**
> IntegrationExportDto patch29(id, integration_export_patch_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.integration_export_dto import IntegrationExportDto
from openapi_client.models.integration_export_patch_dto import IntegrationExportPatchDto
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
    api_instance = openapi_client.IntegrationExportControllerApi(api_client)
    id = 56 # int | 
    integration_export_patch_dto = openapi_client.IntegrationExportPatchDto() # IntegrationExportPatchDto | 

    try:
        api_response = api_instance.patch29(id, integration_export_patch_dto)
        print("The response of IntegrationExportControllerApi->patch29:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationExportControllerApi->patch29: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **integration_export_patch_dto** | [**IntegrationExportPatchDto**](IntegrationExportPatchDto.md)|  | 

### Return type

[**IntegrationExportDto**](IntegrationExportDto.md)

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

