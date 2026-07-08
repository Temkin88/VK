# openapi_client.TestKeyControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_one9**](TestKeyControllerApi.md#find_one9) | **GET** /testkey/{id} | Find test key by id


# **find_one9**
> TestKeyDto find_one9(id)

Find test key by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_key_dto import TestKeyDto
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
    api_instance = openapi_client.TestKeyControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find test key by id
        api_response = api_instance.find_one9(id)
        print("The response of TestKeyControllerApi->find_one9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestKeyControllerApi->find_one9: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestKeyDto**](TestKeyDto.md)

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

