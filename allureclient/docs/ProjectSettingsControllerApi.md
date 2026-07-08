# openapi_client.ProjectSettingsControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_launch_close_config**](ProjectSettingsControllerApi.md#get_launch_close_config) | **GET** /projectsettings/launchclose | Get launch close config
[**get_launch_live_doc_config**](ProjectSettingsControllerApi.md#get_launch_live_doc_config) | **GET** /projectsettings/launchlivedoc | Get launch live documentation config
[**set_launch_close_config**](ProjectSettingsControllerApi.md#set_launch_close_config) | **PATCH** /projectsettings/launchclose | Save launch close config
[**set_launch_live_doc_config**](ProjectSettingsControllerApi.md#set_launch_live_doc_config) | **PATCH** /projectsettings/launchlivedoc | Save launch live documentation config


# **get_launch_close_config**
> LaunchCloseConfigDto get_launch_close_config(project_id)

Get launch close config

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_close_config_dto import LaunchCloseConfigDto
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
    api_instance = openapi_client.ProjectSettingsControllerApi(api_client)
    project_id = 56 # int | 

    try:
        # Get launch close config
        api_response = api_instance.get_launch_close_config(project_id)
        print("The response of ProjectSettingsControllerApi->get_launch_close_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSettingsControllerApi->get_launch_close_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**LaunchCloseConfigDto**](LaunchCloseConfigDto.md)

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

# **get_launch_live_doc_config**
> LaunchLiveDocConfigDto get_launch_live_doc_config(project_id)

Get launch live documentation config

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_live_doc_config_dto import LaunchLiveDocConfigDto
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
    api_instance = openapi_client.ProjectSettingsControllerApi(api_client)
    project_id = 56 # int | 

    try:
        # Get launch live documentation config
        api_response = api_instance.get_launch_live_doc_config(project_id)
        print("The response of ProjectSettingsControllerApi->get_launch_live_doc_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSettingsControllerApi->get_launch_live_doc_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**LaunchLiveDocConfigDto**](LaunchLiveDocConfigDto.md)

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

# **set_launch_close_config**
> set_launch_close_config(launch_close_config_dto)

Save launch close config

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_close_config_dto import LaunchCloseConfigDto
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
    api_instance = openapi_client.ProjectSettingsControllerApi(api_client)
    launch_close_config_dto = openapi_client.LaunchCloseConfigDto() # LaunchCloseConfigDto | 

    try:
        # Save launch close config
        api_instance.set_launch_close_config(launch_close_config_dto)
    except Exception as e:
        print("Exception when calling ProjectSettingsControllerApi->set_launch_close_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_close_config_dto** | [**LaunchCloseConfigDto**](LaunchCloseConfigDto.md)|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_launch_live_doc_config**
> set_launch_live_doc_config(launch_live_doc_config_dto)

Save launch live documentation config

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_live_doc_config_dto import LaunchLiveDocConfigDto
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
    api_instance = openapi_client.ProjectSettingsControllerApi(api_client)
    launch_live_doc_config_dto = openapi_client.LaunchLiveDocConfigDto() # LaunchLiveDocConfigDto | 

    try:
        # Save launch live documentation config
        api_instance.set_launch_live_doc_config(launch_live_doc_config_dto)
    except Exception as e:
        print("Exception when calling ProjectSettingsControllerApi->set_launch_live_doc_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_live_doc_config_dto** | [**LaunchLiveDocConfigDto**](LaunchLiveDocConfigDto.md)|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

