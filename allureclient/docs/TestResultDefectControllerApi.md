# openapi_client.TestResultDefectControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_defect**](TestResultDefectControllerApi.md#create_defect) | **POST** /testresult/{testResultId}/defect | 
[**get_candidates**](TestResultDefectControllerApi.md#get_candidates) | **GET** /testresult/{id}/defect/candidate | 
[**get_defects**](TestResultDefectControllerApi.md#get_defects) | **GET** /testresult/{testResultId}/defect | 
[**get_matches**](TestResultDefectControllerApi.md#get_matches) | **GET** /testresult/defect/match | 
[**get_similar**](TestResultDefectControllerApi.md#get_similar) | **GET** /testresult/{id}/defect/similar | 
[**link**](TestResultDefectControllerApi.md#link) | **POST** /testresult/{testResultId}/defect/{defectId} | 
[**unlink**](TestResultDefectControllerApi.md#unlink) | **DELETE** /testresult/{testResultId}/defect/{defectId} | 


# **create_defect**
> DefectDto create_defect(test_result_id, test_result_new_defect_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.defect_dto import DefectDto
from openapi_client.models.test_result_new_defect_dto import TestResultNewDefectDto
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
    api_instance = openapi_client.TestResultDefectControllerApi(api_client)
    test_result_id = 56 # int | 
    test_result_new_defect_dto = openapi_client.TestResultNewDefectDto() # TestResultNewDefectDto | 

    try:
        api_response = api_instance.create_defect(test_result_id, test_result_new_defect_dto)
        print("The response of TestResultDefectControllerApi->create_defect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultDefectControllerApi->create_defect: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 
 **test_result_new_defect_dto** | [**TestResultNewDefectDto**](TestResultNewDefectDto.md)|  | 

### Return type

[**DefectDto**](DefectDto.md)

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

# **get_candidates**
> PageDefectDto get_candidates(id, threshold=threshold, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_defect_dto import PageDefectDto
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
    api_instance = openapi_client.TestResultDefectControllerApi(api_client)
    id = 56 # int | 
    threshold = 0.7 # float |  (optional) (default to 0.7)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        api_response = api_instance.get_candidates(id, threshold=threshold, page=page, size=size, sort=sort)
        print("The response of TestResultDefectControllerApi->get_candidates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultDefectControllerApi->get_candidates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **threshold** | **float**|  | [optional] [default to 0.7]
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageDefectDto**](PageDefectDto.md)

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

# **get_defects**
> PageDefectRowDto get_defects(test_result_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_defect_row_dto import PageDefectRowDto
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
    api_instance = openapi_client.TestResultDefectControllerApi(api_client)
    test_result_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        api_response = api_instance.get_defects(test_result_id, page=page, size=size, sort=sort)
        print("The response of TestResultDefectControllerApi->get_defects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultDefectControllerApi->get_defects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageDefectRowDto**](PageDefectRowDto.md)

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

# **get_matches**
> PageTestResultDefectMatchDto get_matches(launch_id, message_regex=message_regex, trace_regex=trace_regex, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_defect_match_dto import PageTestResultDefectMatchDto
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
    api_instance = openapi_client.TestResultDefectControllerApi(api_client)
    launch_id = 56 # int | 
    message_regex = 'message_regex_example' # str |  (optional)
    trace_regex = 'trace_regex_example' # str |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        api_response = api_instance.get_matches(launch_id, message_regex=message_regex, trace_regex=trace_regex, page=page, size=size, sort=sort)
        print("The response of TestResultDefectControllerApi->get_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultDefectControllerApi->get_matches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **int**|  | 
 **message_regex** | **str**|  | [optional] 
 **trace_regex** | **str**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageTestResultDefectMatchDto**](PageTestResultDefectMatchDto.md)

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

# **get_similar**
> PageTestResultRowDto get_similar(id, threshold=threshold, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_row_dto import PageTestResultRowDto
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
    api_instance = openapi_client.TestResultDefectControllerApi(api_client)
    id = 56 # int | 
    threshold = 0.7 # float |  (optional) (default to 0.7)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

    try:
        api_response = api_instance.get_similar(id, threshold=threshold, page=page, size=size, sort=sort)
        print("The response of TestResultDefectControllerApi->get_similar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultDefectControllerApi->get_similar: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **threshold** | **float**|  | [optional] [default to 0.7]
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**PageTestResultRowDto**](PageTestResultRowDto.md)

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

# **link**
> DefectDto link(test_result_id, defect_id, test_result_link_defect_dto=test_result_link_defect_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.defect_dto import DefectDto
from openapi_client.models.test_result_link_defect_dto import TestResultLinkDefectDto
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
    api_instance = openapi_client.TestResultDefectControllerApi(api_client)
    test_result_id = 56 # int | 
    defect_id = 56 # int | 
    test_result_link_defect_dto = openapi_client.TestResultLinkDefectDto() # TestResultLinkDefectDto |  (optional)

    try:
        api_response = api_instance.link(test_result_id, defect_id, test_result_link_defect_dto=test_result_link_defect_dto)
        print("The response of TestResultDefectControllerApi->link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultDefectControllerApi->link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 
 **defect_id** | **int**|  | 
 **test_result_link_defect_dto** | [**TestResultLinkDefectDto**](TestResultLinkDefectDto.md)|  | [optional] 

### Return type

[**DefectDto**](DefectDto.md)

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

# **unlink**
> unlink(test_result_id, defect_id)



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
    api_instance = openapi_client.TestResultDefectControllerApi(api_client)
    test_result_id = 56 # int | 
    defect_id = 56 # int | 

    try:
        api_instance.unlink(test_result_id, defect_id)
    except Exception as e:
        print("Exception when calling TestResultDefectControllerApi->unlink: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **int**|  | 
 **defect_id** | **int**|  | 

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

