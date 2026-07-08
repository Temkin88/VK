# openapi_client.IntegrationWebhookControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create31**](IntegrationWebhookControllerApi.md#create31) | **POST** /integration/webhook | Create a new webhook config
[**delete_by_id2**](IntegrationWebhookControllerApi.md#delete_by_id2) | **DELETE** /integration/webhook/{id} | Delete webhook config
[**find_all29**](IntegrationWebhookControllerApi.md#find_all29) | **GET** /integration/webhook | Find all webhook configs for integration
[**find_all_logs**](IntegrationWebhookControllerApi.md#find_all_logs) | **GET** /integration/webhook/log | Find all webhook logs by integration or webhook
[**patch28**](IntegrationWebhookControllerApi.md#patch28) | **PATCH** /integration/webhook/{id} | Patch webhook config


# **create31**
> IntegrationWebhookTokenDto create31(integration_webhook_create_dto)

Create a new webhook config

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.integration_webhook_create_dto import IntegrationWebhookCreateDto
from openapi_client.models.integration_webhook_token_dto import IntegrationWebhookTokenDto
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
    api_instance = openapi_client.IntegrationWebhookControllerApi(api_client)
    integration_webhook_create_dto = openapi_client.IntegrationWebhookCreateDto() # IntegrationWebhookCreateDto | 

    try:
        # Create a new webhook config
        api_response = api_instance.create31(integration_webhook_create_dto)
        print("The response of IntegrationWebhookControllerApi->create31:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationWebhookControllerApi->create31: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_webhook_create_dto** | [**IntegrationWebhookCreateDto**](IntegrationWebhookCreateDto.md)|  | 

### Return type

[**IntegrationWebhookTokenDto**](IntegrationWebhookTokenDto.md)

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

# **delete_by_id2**
> delete_by_id2(id)

Delete webhook config

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
    api_instance = openapi_client.IntegrationWebhookControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete webhook config
        api_instance.delete_by_id2(id)
    except Exception as e:
        print("Exception when calling IntegrationWebhookControllerApi->delete_by_id2: %s\n" % e)
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

# **find_all29**
> PageIntegrationWebhookDto find_all29(integration_id, page=page, size=size, sort=sort)

Find all webhook configs for integration

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_integration_webhook_dto import PageIntegrationWebhookDto
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
    api_instance = openapi_client.IntegrationWebhookControllerApi(api_client)
    integration_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        # Find all webhook configs for integration
        api_response = api_instance.find_all29(integration_id, page=page, size=size, sort=sort)
        print("The response of IntegrationWebhookControllerApi->find_all29:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationWebhookControllerApi->find_all29: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageIntegrationWebhookDto**](PageIntegrationWebhookDto.md)

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

# **find_all_logs**
> PageIntegrationWebhookLogDto find_all_logs(integration_id=integration_id, webhook_id=webhook_id, page=page, size=size, sort=sort)

Find all webhook logs by integration or webhook

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_integration_webhook_log_dto import PageIntegrationWebhookLogDto
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
    api_instance = openapi_client.IntegrationWebhookControllerApi(api_client)
    integration_id = 56 # int |  (optional)
    webhook_id = 56 # int |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        # Find all webhook logs by integration or webhook
        api_response = api_instance.find_all_logs(integration_id=integration_id, webhook_id=webhook_id, page=page, size=size, sort=sort)
        print("The response of IntegrationWebhookControllerApi->find_all_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationWebhookControllerApi->find_all_logs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**|  | [optional] 
 **webhook_id** | **int**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageIntegrationWebhookLogDto**](PageIntegrationWebhookLogDto.md)

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

# **patch28**
> IntegrationWebhookDto patch28(id, integration_webhook_patch_dto)

Patch webhook config

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.integration_webhook_dto import IntegrationWebhookDto
from openapi_client.models.integration_webhook_patch_dto import IntegrationWebhookPatchDto
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
    api_instance = openapi_client.IntegrationWebhookControllerApi(api_client)
    id = 56 # int | 
    integration_webhook_patch_dto = openapi_client.IntegrationWebhookPatchDto() # IntegrationWebhookPatchDto | 

    try:
        # Patch webhook config
        api_response = api_instance.patch28(id, integration_webhook_patch_dto)
        print("The response of IntegrationWebhookControllerApi->patch28:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationWebhookControllerApi->patch28: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **integration_webhook_patch_dto** | [**IntegrationWebhookPatchDto**](IntegrationWebhookPatchDto.md)|  | 

### Return type

[**IntegrationWebhookDto**](IntegrationWebhookDto.md)

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

