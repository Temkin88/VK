# openapi_client.TestResultMuteControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mute**](TestResultMuteControllerApi.md#mute) | **POST** /testresult/{id}/mute | Mute test result
[**unmute**](TestResultMuteControllerApi.md#unmute) | **POST** /testresult/{id}/unmute | Unmute test result


# **mute**
> mute(id, test_result_mute_reason)

Mute test result

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_result_mute_reason import TestResultMuteReason
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
    api_instance = openapi_client.TestResultMuteControllerApi(api_client)
    id = 56 # int | 
    test_result_mute_reason = openapi_client.TestResultMuteReason() # TestResultMuteReason | 

    try:
        # Mute test result
        api_instance.mute(id, test_result_mute_reason)
    except Exception as e:
        print("Exception when calling TestResultMuteControllerApi->mute: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_result_mute_reason** | [**TestResultMuteReason**](TestResultMuteReason.md)|  | 

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

# **unmute**
> unmute(id)

Unmute test result

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
    api_instance = openapi_client.TestResultMuteControllerApi(api_client)
    id = 56 # int | 

    try:
        # Unmute test result
        api_instance.unmute(id)
    except Exception as e:
        print("Exception when calling TestResultMuteControllerApi->unmute: %s\n" % e)
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

