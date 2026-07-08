# openapi_client.TestResultControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create5**](TestResultControllerApi.md#create5) | **POST** /testresult | Creates a test result
[**defects**](TestResultControllerApi.md#defects) | **GET** /testresult/defects | Find defects by launch id
[**delete_by_id**](TestResultControllerApi.md#delete_by_id) | **DELETE** /testresult/{id} | Delete test result by given id
[**find_all4**](TestResultControllerApi.md#find_all4) | **GET** /testresult | Finds all test results by given launch
[**find_execution**](TestResultControllerApi.md#find_execution) | **GET** /testresult/{id}/execution | Find all execution for given test result
[**find_history**](TestResultControllerApi.md#find_history) | **GET** /testresult/{id}/history | Find all history for given test result
[**find_one4**](TestResultControllerApi.md#find_one4) | **GET** /testresult/{id} | 
[**find_retries**](TestResultControllerApi.md#find_retries) | **GET** /testresult/{id}/retries | Find all retries for given test result
[**patch4**](TestResultControllerApi.md#patch4) | **PATCH** /testresult/{id} | Patches a test result by given id
[**timeline**](TestResultControllerApi.md#timeline) | **GET** /testresult/timeline | Find timeline data


# **create5**
> TestResultDto create5(test_result_create_dto)

Creates a test result

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_result_create_dto import TestResultCreateDto
from openapi_client.models.test_result_dto import TestResultDto
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
    api_instance = openapi_client.TestResultControllerApi(api_client)
    test_result_create_dto = openapi_client.TestResultCreateDto() # TestResultCreateDto | 

    try:
        # Creates a test result
        api_response = api_instance.create5(test_result_create_dto)
        print("The response of TestResultControllerApi->create5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultControllerApi->create5: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_create_dto** | [**TestResultCreateDto**](TestResultCreateDto.md)|  | 

### Return type

[**TestResultDto**](TestResultDto.md)

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

# **defects**
> TestResultTree defects(launch_id)

Find defects by launch id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_result_tree import TestResultTree
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
    api_instance = openapi_client.TestResultControllerApi(api_client)
    launch_id = 56 # int | 

    try:
        # Find defects by launch id
        api_response = api_instance.defects(launch_id)
        print("The response of TestResultControllerApi->defects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultControllerApi->defects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **int**|  | 

### Return type

[**TestResultTree**](TestResultTree.md)

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

# **delete_by_id**
> delete_by_id(id)

Delete test result by given id

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
    api_instance = openapi_client.TestResultControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete test result by given id
        api_instance.delete_by_id(id)
    except Exception as e:
        print("Exception when calling TestResultControllerApi->delete_by_id: %s\n" % e)
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

# **find_all4**
> PageTestResultDto find_all4(launch_id, page=page, size=size, sort=sort)

Finds all test results by given launch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_dto import PageTestResultDto
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
    api_instance = openapi_client.TestResultControllerApi(api_client)
    launch_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,DESC"])

    try:
        # Finds all test results by given launch
        api_response = api_instance.find_all4(launch_id, page=page, size=size, sort=sort)
        print("The response of TestResultControllerApi->find_all4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultControllerApi->find_all4: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,DESC&quot;]]

### Return type

[**PageTestResultDto**](PageTestResultDto.md)

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

# **find_execution**
> TestResultScenarioDto find_execution(id)

Find all execution for given test result

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_result_scenario_dto import TestResultScenarioDto
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
    api_instance = openapi_client.TestResultControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find all execution for given test result
        api_response = api_instance.find_execution(id)
        print("The response of TestResultControllerApi->find_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultControllerApi->find_execution: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestResultScenarioDto**](TestResultScenarioDto.md)

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

# **find_history**
> PageTestResultHistoryDto find_history(id, search=search, page=page, size=size, sort=sort)

Find all history for given test result

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_history_dto import PageTestResultHistoryDto
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
    api_instance = openapi_client.TestResultControllerApi(api_client)
    id = 56 # int | 
    search = 'search_example' # str |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,DESC"])

    try:
        # Find all history for given test result
        api_response = api_instance.find_history(id, search=search, page=page, size=size, sort=sort)
        print("The response of TestResultControllerApi->find_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultControllerApi->find_history: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **search** | **str**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,DESC&quot;]]

### Return type

[**PageTestResultHistoryDto**](PageTestResultHistoryDto.md)

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

# **find_one4**
> TestResultDto find_one4(id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_result_dto import TestResultDto
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
    api_instance = openapi_client.TestResultControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.find_one4(id)
        print("The response of TestResultControllerApi->find_one4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultControllerApi->find_one4: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestResultDto**](TestResultDto.md)

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

# **find_retries**
> PageTestResultHistoryDto find_retries(id, page=page, size=size, sort=sort)

Find all retries for given test result

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_history_dto import PageTestResultHistoryDto
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
    api_instance = openapi_client.TestResultControllerApi(api_client)
    id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["start,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["start,DESC"])

    try:
        # Find all retries for given test result
        api_response = api_instance.find_retries(id, page=page, size=size, sort=sort)
        print("The response of TestResultControllerApi->find_retries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultControllerApi->find_retries: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;start,DESC&quot;]]

### Return type

[**PageTestResultHistoryDto**](PageTestResultHistoryDto.md)

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

# **patch4**
> TestResultDto patch4(id, test_result_patch_dto)

Patches a test result by given id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_result_dto import TestResultDto
from openapi_client.models.test_result_patch_dto import TestResultPatchDto
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
    api_instance = openapi_client.TestResultControllerApi(api_client)
    id = 56 # int | 
    test_result_patch_dto = openapi_client.TestResultPatchDto() # TestResultPatchDto | 

    try:
        # Patches a test result by given id
        api_response = api_instance.patch4(id, test_result_patch_dto)
        print("The response of TestResultControllerApi->patch4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultControllerApi->patch4: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_result_patch_dto** | [**TestResultPatchDto**](TestResultPatchDto.md)|  | 

### Return type

[**TestResultDto**](TestResultDto.md)

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

# **timeline**
> TestResultTree timeline(launch_id)

Find timeline data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_result_tree import TestResultTree
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
    api_instance = openapi_client.TestResultControllerApi(api_client)
    launch_id = 56 # int | 

    try:
        # Find timeline data
        api_response = api_instance.timeline(launch_id)
        print("The response of TestResultControllerApi->timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultControllerApi->timeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **int**|  | 

### Return type

[**TestResultTree**](TestResultTree.md)

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

