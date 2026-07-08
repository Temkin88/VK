# openapi_client.MuteControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create22**](MuteControllerApi.md#create22) | **POST** /mute | Create a new mute
[**delete22**](MuteControllerApi.md#delete22) | **DELETE** /mute/{id} | Delete mute
[**find_all24**](MuteControllerApi.md#find_all24) | **GET** /mute | Find all mutes for test case


# **create22**
> MuteDto create22(mute_create_dto)

Create a new mute

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.mute_create_dto import MuteCreateDto
from openapi_client.models.mute_dto import MuteDto
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
    api_instance = openapi_client.MuteControllerApi(api_client)
    mute_create_dto = openapi_client.MuteCreateDto() # MuteCreateDto | 

    try:
        # Create a new mute
        api_response = api_instance.create22(mute_create_dto)
        print("The response of MuteControllerApi->create22:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MuteControllerApi->create22: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mute_create_dto** | [**MuteCreateDto**](MuteCreateDto.md)|  | 

### Return type

[**MuteDto**](MuteDto.md)

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

# **delete22**
> delete22(id)

Delete mute

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
    api_instance = openapi_client.MuteControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete mute
        api_instance.delete22(id)
    except Exception as e:
        print("Exception when calling MuteControllerApi->delete22: %s\n" % e)
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

# **find_all24**
> PageMuteDto find_all24(test_case_id, page=page, size=size, sort=sort)

Find all mutes for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_mute_dto import PageMuteDto
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
    api_instance = openapi_client.MuteControllerApi(api_client)
    test_case_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 5 # int | The size of the page to be returned (optional) (default to 5)
    sort = ["createdDate,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,ASC"])

    try:
        # Find all mutes for test case
        api_response = api_instance.find_all24(test_case_id, page=page, size=size, sort=sort)
        print("The response of MuteControllerApi->find_all24:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MuteControllerApi->find_all24: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 5]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,ASC&quot;]]

### Return type

[**PageMuteDto**](PageMuteDto.md)

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

