# openapi_client.DefectMatcherControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create39**](DefectMatcherControllerApi.md#create39) | **POST** /defect/matcher | 
[**delete37**](DefectMatcherControllerApi.md#delete37) | **DELETE** /defect/matcher/{id} | 
[**patch36**](DefectMatcherControllerApi.md#patch36) | **PATCH** /defect/matcher/{id} | 


# **create39**
> DefectMatcherDto create39(defect_matcher_create_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.defect_matcher_create_dto import DefectMatcherCreateDto
from openapi_client.models.defect_matcher_dto import DefectMatcherDto
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
    api_instance = openapi_client.DefectMatcherControllerApi(api_client)
    defect_matcher_create_dto = openapi_client.DefectMatcherCreateDto() # DefectMatcherCreateDto | 

    try:
        api_response = api_instance.create39(defect_matcher_create_dto)
        print("The response of DefectMatcherControllerApi->create39:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefectMatcherControllerApi->create39: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **defect_matcher_create_dto** | [**DefectMatcherCreateDto**](DefectMatcherCreateDto.md)|  | 

### Return type

[**DefectMatcherDto**](DefectMatcherDto.md)

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

# **delete37**
> delete37(id)



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
    api_instance = openapi_client.DefectMatcherControllerApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete37(id)
    except Exception as e:
        print("Exception when calling DefectMatcherControllerApi->delete37: %s\n" % e)
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

# **patch36**
> DefectMatcherDto patch36(id, defect_matcher_patch_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.defect_matcher_dto import DefectMatcherDto
from openapi_client.models.defect_matcher_patch_dto import DefectMatcherPatchDto
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
    api_instance = openapi_client.DefectMatcherControllerApi(api_client)
    id = 56 # int | 
    defect_matcher_patch_dto = openapi_client.DefectMatcherPatchDto() # DefectMatcherPatchDto | 

    try:
        api_response = api_instance.patch36(id, defect_matcher_patch_dto)
        print("The response of DefectMatcherControllerApi->patch36:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefectMatcherControllerApi->patch36: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **defect_matcher_patch_dto** | [**DefectMatcherPatchDto**](DefectMatcherPatchDto.md)|  | 

### Return type

[**DefectMatcherDto**](DefectMatcherDto.md)

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

