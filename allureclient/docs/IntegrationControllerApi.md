# openapi_client.IntegrationControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create30**](IntegrationControllerApi.md#create30) | **POST** /integration | 
[**create_project_integration**](IntegrationControllerApi.md#create_project_integration) | **POST** /integration/project | 
[**delete_by_id1**](IntegrationControllerApi.md#delete_by_id1) | **DELETE** /integration/{id} | 
[**delete_project_integration**](IntegrationControllerApi.md#delete_project_integration) | **DELETE** /integration/{integrationId}/project/{projectId} | 
[**find_one_by_id**](IntegrationControllerApi.md#find_one_by_id) | **GET** /integration/{id} | 
[**find_project_integration_by_id**](IntegrationControllerApi.md#find_project_integration_by_id) | **GET** /integration/{integrationId}/project/{projectId} | 
[**get_available_integrations**](IntegrationControllerApi.md#get_available_integrations) | **GET** /integration/available | 
[**get_global_fields1**](IntegrationControllerApi.md#get_global_fields1) | **GET** /integration/globalfields | 
[**get_integration_projects**](IntegrationControllerApi.md#get_integration_projects) | **GET** /integration/{id}/project | 
[**get_integrations**](IntegrationControllerApi.md#get_integrations) | **GET** /integration | 
[**get_project_available_integrations**](IntegrationControllerApi.md#get_project_available_integrations) | **GET** /integration/project/{projectId}/available | 
[**get_project_integration_fields1**](IntegrationControllerApi.md#get_project_integration_fields1) | **GET** /integration/projectfields | 
[**get_project_integrations**](IntegrationControllerApi.md#get_project_integrations) | **GET** /integration/project/{projectId} | 
[**patch27**](IntegrationControllerApi.md#patch27) | **PATCH** /integration/{id} | 
[**patch_project_integration**](IntegrationControllerApi.md#patch_project_integration) | **PATCH** /integration/{integrationId}/project/{projectId} | 
[**suggest14**](IntegrationControllerApi.md#suggest14) | **GET** /integration/suggest | Suggest integrations
[**validate**](IntegrationControllerApi.md#validate) | **POST** /integration/validate | 
[**validate1**](IntegrationControllerApi.md#validate1) | **POST** /integration/project/validate | 


# **create30**
> IntegrationDto create30(integration_create_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.integration_create_dto import IntegrationCreateDto
from openapi_client.models.integration_dto import IntegrationDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    integration_create_dto = openapi_client.IntegrationCreateDto() # IntegrationCreateDto | 

    try:
        api_response = api_instance.create30(integration_create_dto)
        print("The response of IntegrationControllerApi->create30:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->create30: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_create_dto** | [**IntegrationCreateDto**](IntegrationCreateDto.md)|  | 

### Return type

[**IntegrationDto**](IntegrationDto.md)

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

# **create_project_integration**
> ProjectIntegrationDto create_project_integration(project_integration_create_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_integration_create_dto import ProjectIntegrationCreateDto
from openapi_client.models.project_integration_dto import ProjectIntegrationDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    project_integration_create_dto = openapi_client.ProjectIntegrationCreateDto() # ProjectIntegrationCreateDto | 

    try:
        api_response = api_instance.create_project_integration(project_integration_create_dto)
        print("The response of IntegrationControllerApi->create_project_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->create_project_integration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_integration_create_dto** | [**ProjectIntegrationCreateDto**](ProjectIntegrationCreateDto.md)|  | 

### Return type

[**ProjectIntegrationDto**](ProjectIntegrationDto.md)

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

# **delete_by_id1**
> delete_by_id1(id)



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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_by_id1(id)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->delete_by_id1: %s\n" % e)
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

# **delete_project_integration**
> delete_project_integration(integration_id, project_id)



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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    integration_id = 56 # int | 
    project_id = 56 # int | 

    try:
        api_instance.delete_project_integration(integration_id, project_id)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->delete_project_integration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**|  | 
 **project_id** | **int**|  | 

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

# **find_one_by_id**
> IntegrationDto find_one_by_id(id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.integration_dto import IntegrationDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.find_one_by_id(id)
        print("The response of IntegrationControllerApi->find_one_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->find_one_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**IntegrationDto**](IntegrationDto.md)

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

# **find_project_integration_by_id**
> ProjectIntegrationDto find_project_integration_by_id(integration_id, project_id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_integration_dto import ProjectIntegrationDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    integration_id = 56 # int | 
    project_id = 56 # int | 

    try:
        api_response = api_instance.find_project_integration_by_id(integration_id, project_id)
        print("The response of IntegrationControllerApi->find_project_integration_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->find_project_integration_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**ProjectIntegrationDto**](ProjectIntegrationDto.md)

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

# **get_available_integrations**
> PageIntegrationInfoDto get_available_integrations(query=query, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_integration_info_dto import PageIntegrationInfoDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        api_response = api_instance.get_available_integrations(query=query, page=page, size=size, sort=sort)
        print("The response of IntegrationControllerApi->get_available_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->get_available_integrations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageIntegrationInfoDto**](PageIntegrationInfoDto.md)

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

# **get_global_fields1**
> IntegrationFieldsFormDto get_global_fields1(type, integration_id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.integration_fields_form_dto import IntegrationFieldsFormDto
from openapi_client.models.integration_type_dto import IntegrationTypeDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    type = openapi_client.IntegrationTypeDto() # IntegrationTypeDto | 
    integration_id = 56 # int | 

    try:
        api_response = api_instance.get_global_fields1(type, integration_id)
        print("The response of IntegrationControllerApi->get_global_fields1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->get_global_fields1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**IntegrationTypeDto**](.md)|  | 
 **integration_id** | **int**|  | 

### Return type

[**IntegrationFieldsFormDto**](IntegrationFieldsFormDto.md)

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

# **get_integration_projects**
> PageProjectSuggestDto get_integration_projects(id, query=query, my=my, favorite=favorite, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_project_suggest_dto import PageProjectSuggestDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    id = 56 # int | 
    query = 'query_example' # str |  (optional)
    my = True # bool |  (optional)
    favorite = True # bool |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        api_response = api_instance.get_integration_projects(id, query=query, my=my, favorite=favorite, page=page, size=size, sort=sort)
        print("The response of IntegrationControllerApi->get_integration_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->get_integration_projects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **query** | **str**|  | [optional] 
 **my** | **bool**|  | [optional] 
 **favorite** | **bool**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageProjectSuggestDto**](PageProjectSuggestDto.md)

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

# **get_integrations**
> PageIntegrationDto get_integrations(page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_integration_dto import PageIntegrationDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        api_response = api_instance.get_integrations(page=page, size=size, sort=sort)
        print("The response of IntegrationControllerApi->get_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->get_integrations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageIntegrationDto**](PageIntegrationDto.md)

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

# **get_project_available_integrations**
> PageIntegrationDto get_project_available_integrations(project_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_integration_dto import PageIntegrationDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        api_response = api_instance.get_project_available_integrations(project_id, page=page, size=size, sort=sort)
        print("The response of IntegrationControllerApi->get_project_available_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->get_project_available_integrations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageIntegrationDto**](PageIntegrationDto.md)

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

# **get_project_integration_fields1**
> ProjectIntegrationFieldsFormDto get_project_integration_fields1(integration_id, project_id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_integration_fields_form_dto import ProjectIntegrationFieldsFormDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    integration_id = 56 # int | 
    project_id = 56 # int | 

    try:
        api_response = api_instance.get_project_integration_fields1(integration_id, project_id)
        print("The response of IntegrationControllerApi->get_project_integration_fields1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->get_project_integration_fields1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**ProjectIntegrationFieldsFormDto**](ProjectIntegrationFieldsFormDto.md)

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

# **get_project_integrations**
> PageProjectIntegrationDto get_project_integrations(project_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_project_integration_dto import PageProjectIntegrationDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    project_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        api_response = api_instance.get_project_integrations(project_id, page=page, size=size, sort=sort)
        print("The response of IntegrationControllerApi->get_project_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->get_project_integrations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageProjectIntegrationDto**](PageProjectIntegrationDto.md)

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

# **patch27**
> IntegrationDto patch27(id, integration_patch_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.integration_dto import IntegrationDto
from openapi_client.models.integration_patch_dto import IntegrationPatchDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    id = 56 # int | 
    integration_patch_dto = openapi_client.IntegrationPatchDto() # IntegrationPatchDto | 

    try:
        api_response = api_instance.patch27(id, integration_patch_dto)
        print("The response of IntegrationControllerApi->patch27:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->patch27: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **integration_patch_dto** | [**IntegrationPatchDto**](IntegrationPatchDto.md)|  | 

### Return type

[**IntegrationDto**](IntegrationDto.md)

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

# **patch_project_integration**
> ProjectIntegrationDto patch_project_integration(integration_id, project_id, project_integration_patch_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_integration_dto import ProjectIntegrationDto
from openapi_client.models.project_integration_patch_dto import ProjectIntegrationPatchDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    integration_id = 56 # int | 
    project_id = 56 # int | 
    project_integration_patch_dto = openapi_client.ProjectIntegrationPatchDto() # ProjectIntegrationPatchDto | 

    try:
        api_response = api_instance.patch_project_integration(integration_id, project_id, project_integration_patch_dto)
        print("The response of IntegrationControllerApi->patch_project_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->patch_project_integration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**|  | 
 **project_id** | **int**|  | 
 **project_integration_patch_dto** | [**ProjectIntegrationPatchDto**](ProjectIntegrationPatchDto.md)|  | 

### Return type

[**ProjectIntegrationDto**](ProjectIntegrationDto.md)

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

# **suggest14**
> PageIdAndNameOnlyDto suggest14(query=query, project_id=project_id, id=id, ignore_id=ignore_id, operation=operation, integration_type=integration_type, page=page, size=size, sort=sort)

Suggest integrations

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.integration_operation_type_dto import IntegrationOperationTypeDto
from openapi_client.models.integration_type_dto import IntegrationTypeDto
from openapi_client.models.page_id_and_name_only_dto import PageIdAndNameOnlyDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    project_id = 56 # int |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    operation = [openapi_client.IntegrationOperationTypeDto()] # List[IntegrationOperationTypeDto] |  (optional)
    integration_type = [openapi_client.IntegrationTypeDto()] # List[IntegrationTypeDto] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest integrations
        api_response = api_instance.suggest14(query=query, project_id=project_id, id=id, ignore_id=ignore_id, operation=operation, integration_type=integration_type, page=page, size=size, sort=sort)
        print("The response of IntegrationControllerApi->suggest14:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->suggest14: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **id** | [**List[int]**](int.md)|  | [optional] 
 **ignore_id** | [**List[int]**](int.md)|  | [optional] 
 **operation** | [**List[IntegrationOperationTypeDto]**](IntegrationOperationTypeDto.md)|  | [optional] 
 **integration_type** | [**List[IntegrationTypeDto]**](IntegrationTypeDto.md)|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageIdAndNameOnlyDto**](PageIdAndNameOnlyDto.md)

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

# **validate**
> validate(integration_validate_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.integration_validate_dto import IntegrationValidateDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    integration_validate_dto = openapi_client.IntegrationValidateDto() # IntegrationValidateDto | 

    try:
        api_instance.validate(integration_validate_dto)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->validate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_validate_dto** | [**IntegrationValidateDto**](IntegrationValidateDto.md)|  | 

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

# **validate1**
> validate1(project_integration_validate_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.project_integration_validate_dto import ProjectIntegrationValidateDto
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
    api_instance = openapi_client.IntegrationControllerApi(api_client)
    project_integration_validate_dto = openapi_client.ProjectIntegrationValidateDto() # ProjectIntegrationValidateDto | 

    try:
        api_instance.validate1(project_integration_validate_dto)
    except Exception as e:
        print("Exception when calling IntegrationControllerApi->validate1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_integration_validate_dto** | [**ProjectIntegrationValidateDto**](ProjectIntegrationValidateDto.md)|  | 

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

