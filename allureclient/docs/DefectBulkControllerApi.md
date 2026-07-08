# openapi_client.DefectBulkControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close1**](DefectBulkControllerApi.md#close1) | **POST** /defect/bulk/close | 
[**remove2**](DefectBulkControllerApi.md#remove2) | **POST** /defect/bulk/remove | 
[**reopen1**](DefectBulkControllerApi.md#reopen1) | **POST** /defect/bulk/reopen | 


# **close1**
> close1(defect_bulk_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.defect_bulk_dto import DefectBulkDto
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
    api_instance = openapi_client.DefectBulkControllerApi(api_client)
    defect_bulk_dto = openapi_client.DefectBulkDto() # DefectBulkDto | 

    try:
        api_instance.close1(defect_bulk_dto)
    except Exception as e:
        print("Exception when calling DefectBulkControllerApi->close1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **defect_bulk_dto** | [**DefectBulkDto**](DefectBulkDto.md)|  | 

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

# **remove2**
> remove2(defect_bulk_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.defect_bulk_dto import DefectBulkDto
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
    api_instance = openapi_client.DefectBulkControllerApi(api_client)
    defect_bulk_dto = openapi_client.DefectBulkDto() # DefectBulkDto | 

    try:
        api_instance.remove2(defect_bulk_dto)
    except Exception as e:
        print("Exception when calling DefectBulkControllerApi->remove2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **defect_bulk_dto** | [**DefectBulkDto**](DefectBulkDto.md)|  | 

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

# **reopen1**
> reopen1(defect_bulk_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.defect_bulk_dto import DefectBulkDto
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
    api_instance = openapi_client.DefectBulkControllerApi(api_client)
    defect_bulk_dto = openapi_client.DefectBulkDto() # DefectBulkDto | 

    try:
        api_instance.reopen1(defect_bulk_dto)
    except Exception as e:
        print("Exception when calling DefectBulkControllerApi->reopen1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **defect_bulk_dto** | [**DefectBulkDto**](DefectBulkDto.md)|  | 

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

