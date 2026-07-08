# openapi_client.JobRunControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_by_id**](JobRunControllerApi.md#find_by_id) | **GET** /jobrun/{id} | Get job run by id
[**rerun1**](JobRunControllerApi.md#rerun1) | **POST** /jobrun/{id}/rerun | Rerun job
[**upload2**](JobRunControllerApi.md#upload2) | **POST** /jobrun/{id}/upload | Manually upload job run results
[**upload_archives1**](JobRunControllerApi.md#upload_archives1) | **POST** /jobrun/{id}/upload/archive | Manually upload job run results
[**upload_files1**](JobRunControllerApi.md#upload_files1) | **POST** /jobrun/{id}/upload/file | Manually upload job run results


# **find_by_id**
> JobRunDto find_by_id(id)

Get job run by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_run_dto import JobRunDto
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
    api_instance = openapi_client.JobRunControllerApi(api_client)
    id = 56 # int | 

    try:
        # Get job run by id
        api_response = api_instance.find_by_id(id)
        print("The response of JobRunControllerApi->find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobRunControllerApi->find_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**JobRunDto**](JobRunDto.md)

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

# **rerun1**
> rerun1(id, job_rerun_request_dto)

Rerun job

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_rerun_request_dto import JobRerunRequestDto
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
    api_instance = openapi_client.JobRunControllerApi(api_client)
    id = 56 # int | 
    job_rerun_request_dto = openapi_client.JobRerunRequestDto() # JobRerunRequestDto | 

    try:
        # Rerun job
        api_instance.rerun1(id, job_rerun_request_dto)
    except Exception as e:
        print("Exception when calling JobRunControllerApi->rerun1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **job_rerun_request_dto** | [**JobRerunRequestDto**](JobRerunRequestDto.md)|  | 

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

# **upload2**
> FileUploadResponseDto upload2(id, info=info, file=file, archive=archive)

Manually upload job run results

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.file_upload_response_dto import FileUploadResponseDto
from openapi_client.models.job_run_upload_info_dto import JobRunUploadInfoDto
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
    api_instance = openapi_client.JobRunControllerApi(api_client)
    id = 56 # int | 
    info = openapi_client.JobRunUploadInfoDto() # JobRunUploadInfoDto |  (optional)
    file = None # List[bytearray] |  (optional)
    archive = None # List[bytearray] |  (optional)

    try:
        # Manually upload job run results
        api_response = api_instance.upload2(id, info=info, file=file, archive=archive)
        print("The response of JobRunControllerApi->upload2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobRunControllerApi->upload2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **info** | [**JobRunUploadInfoDto**](JobRunUploadInfoDto.md)|  | [optional] 
 **file** | **List[bytearray]**|  | [optional] 
 **archive** | **List[bytearray]**|  | [optional] 

### Return type

[**FileUploadResponseDto**](FileUploadResponseDto.md)

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

# **upload_archives1**
> FileUploadResponseDto upload_archives1(id, file, info=info)

Manually upload job run results

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.file_upload_response_dto import FileUploadResponseDto
from openapi_client.models.job_run_upload_info_dto import JobRunUploadInfoDto
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
    api_instance = openapi_client.JobRunControllerApi(api_client)
    id = 56 # int | 
    file = None # List[bytearray] | 
    info = openapi_client.JobRunUploadInfoDto() # JobRunUploadInfoDto |  (optional)

    try:
        # Manually upload job run results
        api_response = api_instance.upload_archives1(id, file, info=info)
        print("The response of JobRunControllerApi->upload_archives1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobRunControllerApi->upload_archives1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **file** | **List[bytearray]**|  | 
 **info** | [**JobRunUploadInfoDto**](JobRunUploadInfoDto.md)|  | [optional] 

### Return type

[**FileUploadResponseDto**](FileUploadResponseDto.md)

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

# **upload_files1**
> FileUploadResponseDto upload_files1(id, file, info=info)

Manually upload job run results

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.file_upload_response_dto import FileUploadResponseDto
from openapi_client.models.job_run_upload_info_dto import JobRunUploadInfoDto
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
    api_instance = openapi_client.JobRunControllerApi(api_client)
    id = 56 # int | 
    file = None # List[bytearray] | 
    info = openapi_client.JobRunUploadInfoDto() # JobRunUploadInfoDto |  (optional)

    try:
        # Manually upload job run results
        api_response = api_instance.upload_files1(id, file, info=info)
        print("The response of JobRunControllerApi->upload_files1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobRunControllerApi->upload_files1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **file** | **List[bytearray]**|  | 
 **info** | [**JobRunUploadInfoDto**](JobRunUploadInfoDto.md)|  | [optional] 

### Return type

[**FileUploadResponseDto**](FileUploadResponseDto.md)

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

