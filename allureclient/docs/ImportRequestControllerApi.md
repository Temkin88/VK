# openapi_client.ImportRequestControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete29**](ImportRequestControllerApi.md#delete29) | **DELETE** /importrequest/{id} | Delete import
[**find_all31**](ImportRequestControllerApi.md#find_all31) | **GET** /importrequest | Find all imports
[**find_one25**](ImportRequestControllerApi.md#find_one25) | **GET** /importrequest/{id} | Find import by id
[**upload3**](ImportRequestControllerApi.md#upload3) | **POST** /importrequest | Upload import file


# **delete29**
> delete29(id)

Delete import

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
    api_instance = openapi_client.ImportRequestControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete import
        api_instance.delete29(id)
    except Exception as e:
        print("Exception when calling ImportRequestControllerApi->delete29: %s\n" % e)
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

# **find_all31**
> PageImportRequestDto find_all31(project_id, page=page, size=size, sort=sort)

Find all imports

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_import_request_dto import PageImportRequestDto
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
    api_instance = openapi_client.ImportRequestControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,DESC"])

    try:
        # Find all imports
        api_response = api_instance.find_all31(project_id, page=page, size=size, sort=sort)
        print("The response of ImportRequestControllerApi->find_all31:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportRequestControllerApi->find_all31: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,DESC&quot;]]

### Return type

[**PageImportRequestDto**](PageImportRequestDto.md)

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

# **find_one25**
> ImportRequestDto find_one25(id)

Find import by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.import_request_dto import ImportRequestDto
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
    api_instance = openapi_client.ImportRequestControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find import by id
        api_response = api_instance.find_one25(id)
        print("The response of ImportRequestControllerApi->find_one25:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportRequestControllerApi->find_one25: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ImportRequestDto**](ImportRequestDto.md)

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

# **upload3**
> ImportRequestDto upload3(project_id, type, file)

Upload import file

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.import_request_dto import ImportRequestDto
from openapi_client.models.import_request_type_dto import ImportRequestTypeDto
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
    api_instance = openapi_client.ImportRequestControllerApi(api_client)
    project_id = 56 # int | 
    type = openapi_client.ImportRequestTypeDto() # ImportRequestTypeDto | 
    file = None # bytearray | 

    try:
        # Upload import file
        api_response = api_instance.upload3(project_id, type, file)
        print("The response of ImportRequestControllerApi->upload3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportRequestControllerApi->upload3: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **type** | [**ImportRequestTypeDto**](.md)|  | 
 **file** | **bytearray**|  | 

### Return type

[**ImportRequestDto**](ImportRequestDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

