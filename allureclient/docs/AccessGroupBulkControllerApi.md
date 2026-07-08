# openapi_client.AccessGroupBulkControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](AccessGroupBulkControllerApi.md#delete) | **POST** /accessgroup/bulk/delete | Bulk delete teams


# **delete**
> delete(access_group_bulk_dto)

Bulk delete teams

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.access_group_bulk_dto import AccessGroupBulkDto
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
    api_instance = openapi_client.AccessGroupBulkControllerApi(api_client)
    access_group_bulk_dto = openapi_client.AccessGroupBulkDto() # AccessGroupBulkDto | 

    try:
        # Bulk delete teams
        api_instance.delete(access_group_bulk_dto)
    except Exception as e:
        print("Exception when calling AccessGroupBulkControllerApi->delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_group_bulk_dto** | [**AccessGroupBulkDto**](AccessGroupBulkDto.md)|  | 

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

