# openapi_client.CleanupControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cleanup_launch**](CleanupControllerApi.md#cleanup_launch) | **POST** /cleanup/launch | 
[**trigger_blob_remove_task**](CleanupControllerApi.md#trigger_blob_remove_task) | **POST** /cleanup/scheduler/blob_remove_task | 
[**trigger_cleanup**](CleanupControllerApi.md#trigger_cleanup) | **POST** /cleanup/scheduler/cleaner_schema_project | 
[**trigger_global_cleanup**](CleanupControllerApi.md#trigger_global_cleanup) | **POST** /cleanup/scheduler/cleaner_schema_global | 


# **cleanup_launch**
> cleanup_launch(launch_cleanup_request)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_cleanup_request import LaunchCleanupRequest
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
    api_instance = openapi_client.CleanupControllerApi(api_client)
    launch_cleanup_request = openapi_client.LaunchCleanupRequest() # LaunchCleanupRequest | 

    try:
        api_instance.cleanup_launch(launch_cleanup_request)
    except Exception as e:
        print("Exception when calling CleanupControllerApi->cleanup_launch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_cleanup_request** | [**LaunchCleanupRequest**](LaunchCleanupRequest.md)|  | 

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

# **trigger_blob_remove_task**
> trigger_blob_remove_task()



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
    api_instance = openapi_client.CleanupControllerApi(api_client)

    try:
        api_instance.trigger_blob_remove_task()
    except Exception as e:
        print("Exception when calling CleanupControllerApi->trigger_blob_remove_task: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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

# **trigger_cleanup**
> trigger_cleanup()



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
    api_instance = openapi_client.CleanupControllerApi(api_client)

    try:
        api_instance.trigger_cleanup()
    except Exception as e:
        print("Exception when calling CleanupControllerApi->trigger_cleanup: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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

# **trigger_global_cleanup**
> trigger_global_cleanup()



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
    api_instance = openapi_client.CleanupControllerApi(api_client)

    try:
        api_instance.trigger_global_cleanup()
    except Exception as e:
        print("Exception when calling CleanupControllerApi->trigger_global_cleanup: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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

