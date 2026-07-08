# openapi_client.TestFixtureResultAttachmentControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create11**](TestFixtureResultAttachmentControllerApi.md#create11) | **POST** /testfixtureresult/attachment | 
[**delete11**](TestFixtureResultAttachmentControllerApi.md#delete11) | **DELETE** /testfixtureresult/attachment/{id} | 
[**find_all9**](TestFixtureResultAttachmentControllerApi.md#find_all9) | **GET** /testfixtureresult/attachment | 
[**patch10**](TestFixtureResultAttachmentControllerApi.md#patch10) | **PATCH** /testfixtureresult/attachment/{id} | 
[**read_content1**](TestFixtureResultAttachmentControllerApi.md#read_content1) | **GET** /testfixtureresult/attachment/{id}/content | 
[**update_content1**](TestFixtureResultAttachmentControllerApi.md#update_content1) | **PUT** /testfixtureresult/attachment/{id}/content | 


# **create11**
> List[TestFixtureResultAttachmentRowDto] create11(tfr_id, file)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_fixture_result_attachment_row_dto import TestFixtureResultAttachmentRowDto
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
    api_instance = openapi_client.TestFixtureResultAttachmentControllerApi(api_client)
    tfr_id = 56 # int | 
    file = None # List[bytearray] | 

    try:
        api_response = api_instance.create11(tfr_id, file)
        print("The response of TestFixtureResultAttachmentControllerApi->create11:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFixtureResultAttachmentControllerApi->create11: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tfr_id** | **int**|  | 
 **file** | **List[bytearray]**|  | 

### Return type

[**List[TestFixtureResultAttachmentRowDto]**](TestFixtureResultAttachmentRowDto.md)

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

# **delete11**
> delete11(id)



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
    api_instance = openapi_client.TestFixtureResultAttachmentControllerApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete11(id)
    except Exception as e:
        print("Exception when calling TestFixtureResultAttachmentControllerApi->delete11: %s\n" % e)
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

# **find_all9**
> PageTestFixtureResultAttachmentRowDto find_all9(tfr_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_fixture_result_attachment_row_dto import PageTestFixtureResultAttachmentRowDto
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
    api_instance = openapi_client.TestFixtureResultAttachmentControllerApi(api_client)
    tfr_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        api_response = api_instance.find_all9(tfr_id, page=page, size=size, sort=sort)
        print("The response of TestFixtureResultAttachmentControllerApi->find_all9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFixtureResultAttachmentControllerApi->find_all9: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tfr_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageTestFixtureResultAttachmentRowDto**](PageTestFixtureResultAttachmentRowDto.md)

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

# **patch10**
> TestFixtureResultAttachmentRowDto patch10(id, test_fixture_result_attachment_patch_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_fixture_result_attachment_patch_dto import TestFixtureResultAttachmentPatchDto
from openapi_client.models.test_fixture_result_attachment_row_dto import TestFixtureResultAttachmentRowDto
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
    api_instance = openapi_client.TestFixtureResultAttachmentControllerApi(api_client)
    id = 56 # int | 
    test_fixture_result_attachment_patch_dto = openapi_client.TestFixtureResultAttachmentPatchDto() # TestFixtureResultAttachmentPatchDto | 

    try:
        api_response = api_instance.patch10(id, test_fixture_result_attachment_patch_dto)
        print("The response of TestFixtureResultAttachmentControllerApi->patch10:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFixtureResultAttachmentControllerApi->patch10: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_fixture_result_attachment_patch_dto** | [**TestFixtureResultAttachmentPatchDto**](TestFixtureResultAttachmentPatchDto.md)|  | 

### Return type

[**TestFixtureResultAttachmentRowDto**](TestFixtureResultAttachmentRowDto.md)

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

# **read_content1**
> object read_content1(id, inline=inline)



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
    api_instance = openapi_client.TestFixtureResultAttachmentControllerApi(api_client)
    id = 56 # int | 
    inline = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.read_content1(id, inline=inline)
        print("The response of TestFixtureResultAttachmentControllerApi->read_content1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFixtureResultAttachmentControllerApi->read_content1: %s\n" % e)
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

# **update_content1**
> TestFixtureResultAttachmentRowDto update_content1(id, file)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_fixture_result_attachment_row_dto import TestFixtureResultAttachmentRowDto
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
    api_instance = openapi_client.TestFixtureResultAttachmentControllerApi(api_client)
    id = 56 # int | 
    file = None # bytearray | 

    try:
        api_response = api_instance.update_content1(id, file)
        print("The response of TestFixtureResultAttachmentControllerApi->update_content1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFixtureResultAttachmentControllerApi->update_content1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **file** | **bytearray**|  | 

### Return type

[**TestFixtureResultAttachmentRowDto**](TestFixtureResultAttachmentRowDto.md)

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

