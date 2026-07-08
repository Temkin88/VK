# openapi_client.ProjectPropertyControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create19**](ProjectPropertyControllerApi.md#create19) | **POST** /projectproperty | Create a new project property
[**delete19**](ProjectPropertyControllerApi.md#delete19) | **DELETE** /projectproperty/{id} | Delete project by id
[**find_all18**](ProjectPropertyControllerApi.md#find_all18) | **GET** /projectproperty | Find all project properties
[**find_one16**](ProjectPropertyControllerApi.md#find_one16) | **GET** /projectproperty/{id} | Find project property by id
[**patch18**](ProjectPropertyControllerApi.md#patch18) | **PATCH** /projectproperty/{id} | Patch project property


# **create19**
> ProjectPropertyDto create19(project_property_create_dto)

Create a new project property

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_property_create_dto import ProjectPropertyCreateDto
from openapi_client.models.project_property_dto import ProjectPropertyDto
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
    api_instance = openapi_client.ProjectPropertyControllerApi(api_client)
    project_property_create_dto = openapi_client.ProjectPropertyCreateDto() # ProjectPropertyCreateDto | 

    try:
        # Create a new project property
        api_response = api_instance.create19(project_property_create_dto)
        print("The response of ProjectPropertyControllerApi->create19:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPropertyControllerApi->create19: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_property_create_dto** | [**ProjectPropertyCreateDto**](ProjectPropertyCreateDto.md)|  | 

### Return type

[**ProjectPropertyDto**](ProjectPropertyDto.md)

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

# **delete19**
> delete19(id)

Delete project by id

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
    api_instance = openapi_client.ProjectPropertyControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete project by id
        api_instance.delete19(id)
    except Exception as e:
        print("Exception when calling ProjectPropertyControllerApi->delete19: %s\n" % e)
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all18**
> List[ProjectPropertyDto] find_all18(project_id)

Find all project properties

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_property_dto import ProjectPropertyDto
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
    api_instance = openapi_client.ProjectPropertyControllerApi(api_client)
    project_id = 56 # int | 

    try:
        # Find all project properties
        api_response = api_instance.find_all18(project_id)
        print("The response of ProjectPropertyControllerApi->find_all18:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPropertyControllerApi->find_all18: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**List[ProjectPropertyDto]**](ProjectPropertyDto.md)

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

# **find_one16**
> ProjectPropertyDto find_one16(id)

Find project property by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_property_dto import ProjectPropertyDto
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
    api_instance = openapi_client.ProjectPropertyControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find project property by id
        api_response = api_instance.find_one16(id)
        print("The response of ProjectPropertyControllerApi->find_one16:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPropertyControllerApi->find_one16: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ProjectPropertyDto**](ProjectPropertyDto.md)

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

# **patch18**
> ProjectPropertyDto patch18(id, project_property_patch_dto)

Patch project property

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_property_dto import ProjectPropertyDto
from openapi_client.models.project_property_patch_dto import ProjectPropertyPatchDto
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
    api_instance = openapi_client.ProjectPropertyControllerApi(api_client)
    id = 56 # int | 
    project_property_patch_dto = openapi_client.ProjectPropertyPatchDto() # ProjectPropertyPatchDto | 

    try:
        # Patch project property
        api_response = api_instance.patch18(id, project_property_patch_dto)
        print("The response of ProjectPropertyControllerApi->patch18:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPropertyControllerApi->patch18: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **project_property_patch_dto** | [**ProjectPropertyPatchDto**](ProjectPropertyPatchDto.md)|  | 

### Return type

[**ProjectPropertyDto**](ProjectPropertyDto.md)

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

