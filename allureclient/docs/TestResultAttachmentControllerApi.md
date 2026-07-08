# openapi_client.TestResultAttachmentControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create6**](TestResultAttachmentControllerApi.md#create6) | **POST** /testresult/attachment | 
[**delete6**](TestResultAttachmentControllerApi.md#delete6) | **DELETE** /testresult/attachment/{id} | 
[**find_all5**](TestResultAttachmentControllerApi.md#find_all5) | **GET** /testresult/attachment | 
[**patch5**](TestResultAttachmentControllerApi.md#patch5) | **PATCH** /testresult/attachment/{id} | 
[**read_content**](TestResultAttachmentControllerApi.md#read_content) | **GET** /testresult/attachment/{id}/content | 
[**update_content**](TestResultAttachmentControllerApi.md#update_content) | **PUT** /testresult/attachment/{id}/content | 


# **create6**
> List[TestResultAttachmentRowDto] create6(test_result_id, file)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_result_attachment_row_dto import TestResultAttachmentRowDto
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
    api_instance = openapi_client.TestResultAttachmentControllerApi(api_client)
    test_result_id = 56 # int | 
    file = None # List[bytearray] | 

    try:
        api_response = api_instance.create6(test_result_id, file)
        print("The response of TestResultAttachmentControllerApi->create6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultAttachmentControllerApi->create6: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 
 **file** | **List[bytearray]**|  | 

### Return type

[**List[TestResultAttachmentRowDto]**](TestResultAttachmentRowDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete6**
> delete6(id)



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
    api_instance = openapi_client.TestResultAttachmentControllerApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete6(id)
    except Exception as e:
        print("Exception when calling TestResultAttachmentControllerApi->delete6: %s\n" % e)
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

# **find_all5**
> PageTestResultAttachmentRowDto find_all5(test_result_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_attachment_row_dto import PageTestResultAttachmentRowDto
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
    api_instance = openapi_client.TestResultAttachmentControllerApi(api_client)
    test_result_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        api_response = api_instance.find_all5(test_result_id, page=page, size=size, sort=sort)
        print("The response of TestResultAttachmentControllerApi->find_all5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultAttachmentControllerApi->find_all5: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageTestResultAttachmentRowDto**](PageTestResultAttachmentRowDto.md)

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

# **patch5**
> TestResultAttachmentRowDto patch5(id, test_result_attachment_patch_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_result_attachment_patch_dto import TestResultAttachmentPatchDto
from openapi_client.models.test_result_attachment_row_dto import TestResultAttachmentRowDto
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
    api_instance = openapi_client.TestResultAttachmentControllerApi(api_client)
    id = 56 # int | 
    test_result_attachment_patch_dto = openapi_client.TestResultAttachmentPatchDto() # TestResultAttachmentPatchDto | 

    try:
        api_response = api_instance.patch5(id, test_result_attachment_patch_dto)
        print("The response of TestResultAttachmentControllerApi->patch5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultAttachmentControllerApi->patch5: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_result_attachment_patch_dto** | [**TestResultAttachmentPatchDto**](TestResultAttachmentPatchDto.md)|  | 

### Return type

[**TestResultAttachmentRowDto**](TestResultAttachmentRowDto.md)

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

# **read_content**
> object read_content(id, inline=inline)



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
    api_instance = openapi_client.TestResultAttachmentControllerApi(api_client)
    id = 56 # int | 
    inline = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.read_content(id, inline=inline)
        print("The response of TestResultAttachmentControllerApi->read_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultAttachmentControllerApi->read_content: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **inline** | **bool**|  | [optional] [default to False]

### Return type

**object**

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

# **update_content**
> TestResultAttachmentRowDto update_content(id, file)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_result_attachment_row_dto import TestResultAttachmentRowDto
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
    api_instance = openapi_client.TestResultAttachmentControllerApi(api_client)
    id = 56 # int | 
    file = None # bytearray | 

    try:
        api_response = api_instance.update_content(id, file)
        print("The response of TestResultAttachmentControllerApi->update_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultAttachmentControllerApi->update_content: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **file** | **bytearray**|  | 

### Return type

[**TestResultAttachmentRowDto**](TestResultAttachmentRowDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

