# openapi_client.BlobStorageControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_storage_statistic**](BlobStorageControllerApi.md#get_storage_statistic) | **GET** /storage/stats | Get blob storage statistic


# **get_storage_statistic**
> BlobStorageStats get_storage_statistic()

Get blob storage statistic

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.blob_storage_stats import BlobStorageStats
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
    api_instance = openapi_client.BlobStorageControllerApi(api_client)

    try:
        # Get blob storage statistic
        api_response = api_instance.get_storage_statistic()
        print("The response of BlobStorageControllerApi->get_storage_statistic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlobStorageControllerApi->get_storage_statistic: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**BlobStorageStats**](BlobStorageStats.md)

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

