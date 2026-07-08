# openapi_client.ExportRequestControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete31**](ExportRequestControllerApi.md#delete31) | **DELETE** /export/{id} | Delete report
[**download_export**](ExportRequestControllerApi.md#download_export) | **GET** /export/download/{exportRequestId} | Download prepared export
[**find_all33**](ExportRequestControllerApi.md#find_all33) | **GET** /export | Find all reports
[**find_one27**](ExportRequestControllerApi.md#find_one27) | **GET** /export/{id} | Find report by id


# **delete31**
> delete31(id)

Delete report

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
    api_instance = openapi_client.ExportRequestControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete report
        api_instance.delete31(id)
    except Exception as e:
        print("Exception when calling ExportRequestControllerApi->delete31: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_export**
> object download_export(export_request_id)

Download prepared export

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
    api_instance = openapi_client.ExportRequestControllerApi(api_client)
    export_request_id = 56 # int | 

    try:
        # Download prepared export
        api_response = api_instance.download_export(export_request_id)
        print("The response of ExportRequestControllerApi->download_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportRequestControllerApi->download_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_request_id** | **int**|  | 

### Return type

**object**

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

# **find_all33**
> PageExportRequestDto find_all33(project_id, page=page, size=size, sort=sort)

Find all reports

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_export_request_dto import PageExportRequestDto
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
    api_instance = openapi_client.ExportRequestControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,DESC"])

    try:
        # Find all reports
        api_response = api_instance.find_all33(project_id, page=page, size=size, sort=sort)
        print("The response of ExportRequestControllerApi->find_all33:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportRequestControllerApi->find_all33: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,DESC&quot;]]

### Return type

[**PageExportRequestDto**](PageExportRequestDto.md)

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

# **find_one27**
> ExportRequestDto find_one27(id)

Find report by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.export_request_dto import ExportRequestDto
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
    api_instance = openapi_client.ExportRequestControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find report by id
        api_response = api_instance.find_one27(id)
        print("The response of ExportRequestControllerApi->find_one27:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportRequestControllerApi->find_one27: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ExportRequestDto**](ExportRequestDto.md)

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

