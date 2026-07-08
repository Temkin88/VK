# openapi_client.LaunchUploadControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload**](LaunchUploadControllerApi.md#upload) | **POST** /launch/{launchId}/upload | Manually upload launch results
[**upload1**](LaunchUploadControllerApi.md#upload1) | **POST** /launch/upload | Create launch from uploaded results
[**upload_archives**](LaunchUploadControllerApi.md#upload_archives) | **POST** /launch/{launchId}/upload/archive | Manually upload launch results
[**upload_files**](LaunchUploadControllerApi.md#upload_files) | **POST** /launch/{launchId}/upload/file | Manually upload launch results


# **upload**
> LaunchUploadResponseDto upload(launch_id, info, file=file, archive=archive)

Manually upload launch results

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_existing_upload_dto import LaunchExistingUploadDto
from openapi_client.models.launch_upload_response_dto import LaunchUploadResponseDto
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
    api_instance = openapi_client.LaunchUploadControllerApi(api_client)
    launch_id = 56 # int | 
    info = openapi_client.LaunchExistingUploadDto() # LaunchExistingUploadDto | 
    file = None # List[bytearray] |  (optional)
    archive = None # List[bytearray] |  (optional)

    try:
        # Manually upload launch results
        api_response = api_instance.upload(launch_id, info, file=file, archive=archive)
        print("The response of LaunchUploadControllerApi->upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchUploadControllerApi->upload: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **int**|  | 
 **info** | [**LaunchExistingUploadDto**](LaunchExistingUploadDto.md)|  | 
 **file** | **List[bytearray]**|  | [optional] 
 **archive** | **List[bytearray]**|  | [optional] 

### Return type

[**LaunchUploadResponseDto**](LaunchUploadResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload1**
> LaunchUploadResponseDto upload1(info, file=file, archive=archive)

Create launch from uploaded results

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_create_and_upload_dto import LaunchCreateAndUploadDto
from openapi_client.models.launch_upload_response_dto import LaunchUploadResponseDto
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
    api_instance = openapi_client.LaunchUploadControllerApi(api_client)
    info = openapi_client.LaunchCreateAndUploadDto() # LaunchCreateAndUploadDto | 
    file = None # List[bytearray] |  (optional)
    archive = None # List[bytearray] |  (optional)

    try:
        # Create launch from uploaded results
        api_response = api_instance.upload1(info, file=file, archive=archive)
        print("The response of LaunchUploadControllerApi->upload1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchUploadControllerApi->upload1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **info** | [**LaunchCreateAndUploadDto**](LaunchCreateAndUploadDto.md)|  | 
 **file** | **List[bytearray]**|  | [optional] 
 **archive** | **List[bytearray]**|  | [optional] 

### Return type

[**LaunchUploadResponseDto**](LaunchUploadResponseDto.md)

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

# **upload_archives**
> LaunchUploadResponseDto upload_archives(launch_id, info, file)

Manually upload launch results

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_existing_upload_dto import LaunchExistingUploadDto
from openapi_client.models.launch_upload_response_dto import LaunchUploadResponseDto
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
    api_instance = openapi_client.LaunchUploadControllerApi(api_client)
    launch_id = 56 # int | 
    info = openapi_client.LaunchExistingUploadDto() # LaunchExistingUploadDto | 
    file = None # List[bytearray] | 

    try:
        # Manually upload launch results
        api_response = api_instance.upload_archives(launch_id, info, file)
        print("The response of LaunchUploadControllerApi->upload_archives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchUploadControllerApi->upload_archives: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **int**|  | 
 **info** | [**LaunchExistingUploadDto**](LaunchExistingUploadDto.md)|  | 
 **file** | **List[bytearray]**|  | 

### Return type

[**LaunchUploadResponseDto**](LaunchUploadResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_files**
> LaunchUploadResponseDto upload_files(launch_id, info, file)

Manually upload launch results

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_existing_upload_dto import LaunchExistingUploadDto
from openapi_client.models.launch_upload_response_dto import LaunchUploadResponseDto
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
    api_instance = openapi_client.LaunchUploadControllerApi(api_client)
    launch_id = 56 # int | 
    info = openapi_client.LaunchExistingUploadDto() # LaunchExistingUploadDto | 
    file = None # List[bytearray] | 

    try:
        # Manually upload launch results
        api_response = api_instance.upload_files(launch_id, info, file)
        print("The response of LaunchUploadControllerApi->upload_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchUploadControllerApi->upload_files: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **int**|  | 
 **info** | [**LaunchExistingUploadDto**](LaunchExistingUploadDto.md)|  | 
 **file** | **List[bytearray]**|  | 

### Return type

[**LaunchUploadResponseDto**](LaunchUploadResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

