# openapi_client.MarkdownPreviewControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**to_html**](MarkdownPreviewControllerApi.md#to_html) | **GET** /md/preview | Converts markdown text to html
[**to_html1**](MarkdownPreviewControllerApi.md#to_html1) | **POST** /md/preview | Converts markdown text to html


# **to_html**
> str to_html(body)

Converts markdown text to html

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
    api_instance = openapi_client.MarkdownPreviewControllerApi(api_client)
    body = 'body_example' # str | 

    try:
        # Converts markdown text to html
        api_response = api_instance.to_html(body)
        print("The response of MarkdownPreviewControllerApi->to_html:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkdownPreviewControllerApi->to_html: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **to_html1**
> str to_html1(body)

Converts markdown text to html

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
    api_instance = openapi_client.MarkdownPreviewControllerApi(api_client)
    body = 'body_example' # str | 

    try:
        # Converts markdown text to html
        api_response = api_instance.to_html1(body)
        print("The response of MarkdownPreviewControllerApi->to_html1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkdownPreviewControllerApi->to_html1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

