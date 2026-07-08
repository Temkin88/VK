# openapi_client.TreePathControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create3**](TreePathControllerApi.md#create3) | **POST** /treepath | 
[**delete4**](TreePathControllerApi.md#delete4) | **DELETE** /treepath/{id} | 
[**find_all2**](TreePathControllerApi.md#find_all2) | **GET** /treepath | 
[**find_by_tree_id_and_path**](TreePathControllerApi.md#find_by_tree_id_and_path) | **GET** /treepath/path | 


# **create3**
> TreePathDto create3(tree_path_create_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.tree_path_create_dto import TreePathCreateDto
from openapi_client.models.tree_path_dto import TreePathDto
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
    api_instance = openapi_client.TreePathControllerApi(api_client)
    tree_path_create_dto = openapi_client.TreePathCreateDto() # TreePathCreateDto | 

    try:
        api_response = api_instance.create3(tree_path_create_dto)
        print("The response of TreePathControllerApi->create3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TreePathControllerApi->create3: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tree_path_create_dto** | [**TreePathCreateDto**](TreePathCreateDto.md)|  | 

### Return type

[**TreePathDto**](TreePathDto.md)

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

# **delete4**
> delete4(id)



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
    api_instance = openapi_client.TreePathControllerApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete4(id)
    except Exception as e:
        print("Exception when calling TreePathControllerApi->delete4: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all2**
> PageTreePathDto find_all2(tree_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_tree_path_dto import PageTreePathDto
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
    api_instance = openapi_client.TreePathControllerApi(api_client)
    tree_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        api_response = api_instance.find_all2(tree_id, page=page, size=size, sort=sort)
        print("The response of TreePathControllerApi->find_all2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TreePathControllerApi->find_all2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tree_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageTreePathDto**](PageTreePathDto.md)

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

# **find_by_tree_id_and_path**
> TreePathDto find_by_tree_id_and_path(tree_id, path)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.tree_path_dto import TreePathDto
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
    api_instance = openapi_client.TreePathControllerApi(api_client)
    tree_id = 56 # int | 
    path = [56] # List[int] | 

    try:
        api_response = api_instance.find_by_tree_id_and_path(tree_id, path)
        print("The response of TreePathControllerApi->find_by_tree_id_and_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TreePathControllerApi->find_by_tree_id_and_path: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tree_id** | **int**|  | 
 **path** | [**List[int]**](int.md)|  | 

### Return type

[**TreePathDto**](TreePathDto.md)

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

