# openapi_client.StatusControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create16**](StatusControllerApi.md#create16) | **POST** /status | Create a new status
[**delete16**](StatusControllerApi.md#delete16) | **DELETE** /status/{id} | Delete status by id
[**find_all15**](StatusControllerApi.md#find_all15) | **GET** /status | Find all statuses
[**find_one13**](StatusControllerApi.md#find_one13) | **GET** /status/{id} | Find status by id
[**patch15**](StatusControllerApi.md#patch15) | **PATCH** /status/{id} | Patch status
[**suggest7**](StatusControllerApi.md#suggest7) | **GET** /status/suggest | Suggest statuses


# **create16**
> StatusDto create16(status_create_dto)

Create a new status

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.status_create_dto import StatusCreateDto
from openapi_client.models.status_dto import StatusDto
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
    api_instance = openapi_client.StatusControllerApi(api_client)
    status_create_dto = openapi_client.StatusCreateDto() # StatusCreateDto | 

    try:
        # Create a new status
        api_response = api_instance.create16(status_create_dto)
        print("The response of StatusControllerApi->create16:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusControllerApi->create16: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_create_dto** | [**StatusCreateDto**](StatusCreateDto.md)|  | 

### Return type

[**StatusDto**](StatusDto.md)

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

# **delete16**
> delete16(id)

Delete status by id

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
    api_instance = openapi_client.StatusControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete status by id
        api_instance.delete16(id)
    except Exception as e:
        print("Exception when calling StatusControllerApi->delete16: %s\n" % e)
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

# **find_all15**
> PageStatusDto find_all15(workflow_id=workflow_id, page=page, size=size, sort=sort)

Find all statuses

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_status_dto import PageStatusDto
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
    api_instance = openapi_client.StatusControllerApi(api_client)
    workflow_id = 56 # int |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find all statuses
        api_response = api_instance.find_all15(workflow_id=workflow_id, page=page, size=size, sort=sort)
        print("The response of StatusControllerApi->find_all15:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusControllerApi->find_all15: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **int**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageStatusDto**](PageStatusDto.md)

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

# **find_one13**
> StatusDto find_one13(id)

Find status by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.status_dto import StatusDto
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
    api_instance = openapi_client.StatusControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find status by id
        api_response = api_instance.find_one13(id)
        print("The response of StatusControllerApi->find_one13:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusControllerApi->find_one13: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**StatusDto**](StatusDto.md)

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

# **patch15**
> StatusDto patch15(id, status_patch_dto)

Patch status

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.status_dto import StatusDto
from openapi_client.models.status_patch_dto import StatusPatchDto
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
    api_instance = openapi_client.StatusControllerApi(api_client)
    id = 56 # int | 
    status_patch_dto = openapi_client.StatusPatchDto() # StatusPatchDto | 

    try:
        # Patch status
        api_response = api_instance.patch15(id, status_patch_dto)
        print("The response of StatusControllerApi->patch15:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusControllerApi->patch15: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **status_patch_dto** | [**StatusPatchDto**](StatusPatchDto.md)|  | 

### Return type

[**StatusDto**](StatusDto.md)

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

# **suggest7**
> PageIdAndNameOnlyDto suggest7(query=query, workflow_id=workflow_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)

Suggest statuses

### Example

```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.StatusControllerApi(api_client)
    query = 'query_example' # str |  (optional)
    workflow_id = 56 # int |  (optional)
    id = [56] # List[int] |  (optional)
    ignore_id = [56] # List[int] |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Suggest statuses
        api_response = api_instance.suggest7(query=query, workflow_id=workflow_id, id=id, ignore_id=ignore_id, page=page, size=size, sort=sort)
        print("The response of StatusControllerApi->suggest7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusControllerApi->suggest7: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **workflow_id** | **int**|  | [optional] 
 **id** | [**List[int]**](int.md)|  | [optional] 
 **ignore_id** | [**List[int]**](int.md)|  | [optional] 
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

