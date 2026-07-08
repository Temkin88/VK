# openapi_client.GlobalSettingsControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_global_permissions**](GlobalSettingsControllerApi.md#get_global_permissions) | **GET** /globalsettings/globalpermissions | Returns all global permissions for user
[**get_global_settings**](GlobalSettingsControllerApi.md#get_global_settings) | **GET** /globalsettings | Returns global settings
[**patch_project_create**](GlobalSettingsControllerApi.md#patch_project_create) | **PATCH** /globalsettings/projectcreate | Patch global settings


# **get_global_permissions**
> GlobalPermissionsDto get_global_permissions()

Returns all global permissions for user

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.global_permissions_dto import GlobalPermissionsDto
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
    api_instance = openapi_client.GlobalSettingsControllerApi(api_client)

    try:
        # Returns all global permissions for user
        api_response = api_instance.get_global_permissions()
        print("The response of GlobalSettingsControllerApi->get_global_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalSettingsControllerApi->get_global_permissions: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GlobalPermissionsDto**](GlobalPermissionsDto.md)

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

# **get_global_settings**
> GlobalSettingsDto get_global_settings()

Returns global settings

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.global_settings_dto import GlobalSettingsDto
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
    api_instance = openapi_client.GlobalSettingsControllerApi(api_client)

    try:
        # Returns global settings
        api_response = api_instance.get_global_settings()
        print("The response of GlobalSettingsControllerApi->get_global_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalSettingsControllerApi->get_global_settings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GlobalSettingsDto**](GlobalSettingsDto.md)

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

# **patch_project_create**
> patch_project_create(global_settings_project_create_patch_dto)

Patch global settings

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.global_settings_project_create_patch_dto import GlobalSettingsProjectCreatePatchDto
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
    api_instance = openapi_client.GlobalSettingsControllerApi(api_client)
    global_settings_project_create_patch_dto = openapi_client.GlobalSettingsProjectCreatePatchDto() # GlobalSettingsProjectCreatePatchDto | 

    try:
        # Patch global settings
        api_instance.patch_project_create(global_settings_project_create_patch_dto)
    except Exception as e:
        print("Exception when calling GlobalSettingsControllerApi->patch_project_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_settings_project_create_patch_dto** | [**GlobalSettingsProjectCreatePatchDto**](GlobalSettingsProjectCreatePatchDto.md)|  | 

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

