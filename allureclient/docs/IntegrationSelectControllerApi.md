# openapi_client.IntegrationSelectControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**select**](IntegrationSelectControllerApi.md#select) | **GET** /integration/select | 


# **select**
> List[ExtSelectValue] select(project_id, integration_id, field_name, params, query=query)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.ext_select_value import ExtSelectValue
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
    api_instance = openapi_client.IntegrationSelectControllerApi(api_client)
    project_id = 56 # int | 
    integration_id = 56 # int | 
    field_name = 'field_name_example' # str | 
    params = {'key': 'params_example'} # Dict[str, str] | 
    query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.select(project_id, integration_id, field_name, params, query=query)
        print("The response of IntegrationSelectControllerApi->select:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationSelectControllerApi->select: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **integration_id** | **int**|  | 
 **field_name** | **str**|  | 
 **params** | [**Dict[str, str]**](str.md)|  | 
 **query** | **str**|  | [optional] 

### Return type

[**List[ExtSelectValue]**](ExtSelectValue.md)

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

