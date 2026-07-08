# openapi_client.LaunchDiffControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**failed_to_passed_diff**](LaunchDiffControllerApi.md#failed_to_passed_diff) | **GET** /launch/diff/fixed | Find fixed
[**get_new**](LaunchDiffControllerApi.md#get_new) | **GET** /launch/diff/new | New tests
[**get_status_matrix**](LaunchDiffControllerApi.md#get_status_matrix) | **GET** /launch/diff/matrix | Get status matrix for given launches with overlay parameter
[**missed**](LaunchDiffControllerApi.md#missed) | **GET** /launch/diff/missed | Missed tests
[**passed_to_failed_diff**](LaunchDiffControllerApi.md#passed_to_failed_diff) | **GET** /launch/diff/failed | Find failed
[**status_changed**](LaunchDiffControllerApi.md#status_changed) | **GET** /launch/diff/status-changed | Find status changed difference


# **failed_to_passed_diff**
> List[LaunchDiffStatusChangeDto] failed_to_passed_diff(var_from, to, search=search)

Find fixed

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_diff_status_change_dto import LaunchDiffStatusChangeDto
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
    api_instance = openapi_client.LaunchDiffControllerApi(api_client)
    var_from = 56 # int | 
    to = 56 # int | 
    search = 'search_example' # str |  (optional)

    try:
        # Find fixed
        api_response = api_instance.failed_to_passed_diff(var_from, to, search=search)
        print("The response of LaunchDiffControllerApi->failed_to_passed_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchDiffControllerApi->failed_to_passed_diff: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | 
 **to** | **int**|  | 
 **search** | **str**|  | [optional] 

### Return type

[**List[LaunchDiffStatusChangeDto]**](LaunchDiffStatusChangeDto.md)

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

# **get_new**
> List[LaunchDiffTestResultDto] get_new(var_from, to, search=search)

New tests

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_diff_test_result_dto import LaunchDiffTestResultDto
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
    api_instance = openapi_client.LaunchDiffControllerApi(api_client)
    var_from = 56 # int | 
    to = 56 # int | 
    search = 'search_example' # str |  (optional)

    try:
        # New tests
        api_response = api_instance.get_new(var_from, to, search=search)
        print("The response of LaunchDiffControllerApi->get_new:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchDiffControllerApi->get_new: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | 
 **to** | **int**|  | 
 **search** | **str**|  | [optional] 

### Return type

[**List[LaunchDiffTestResultDto]**](LaunchDiffTestResultDto.md)

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

# **get_status_matrix**
> PageLaunchDiffRow get_status_matrix(launch_ids, mode=mode, status_change=status_change, search=search, page=page, size=size, sort=sort)

Get status matrix for given launches with overlay parameter

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_diff_mode import LaunchDiffMode
from openapi_client.models.page_launch_diff_row import PageLaunchDiffRow
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
    api_instance = openapi_client.LaunchDiffControllerApi(api_client)
    launch_ids = [56] # List[int] | 
    mode = openapi_client.LaunchDiffMode() # LaunchDiffMode |  (optional)
    status_change = False # bool |  (optional) (default to False)
    search = 'search_example' # str |  (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,DESC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,DESC"])

    try:
        # Get status matrix for given launches with overlay parameter
        api_response = api_instance.get_status_matrix(launch_ids, mode=mode, status_change=status_change, search=search, page=page, size=size, sort=sort)
        print("The response of LaunchDiffControllerApi->get_status_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchDiffControllerApi->get_status_matrix: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_ids** | [**List[int]**](int.md)|  | 
 **mode** | [**LaunchDiffMode**](.md)|  | [optional] 
 **status_change** | **bool**|  | [optional] [default to False]
 **search** | **str**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,DESC&quot;]]

### Return type

[**PageLaunchDiffRow**](PageLaunchDiffRow.md)

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

# **missed**
> List[LaunchDiffTestResultDto] missed(var_from, to, search=search)

Missed tests

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_diff_test_result_dto import LaunchDiffTestResultDto
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
    api_instance = openapi_client.LaunchDiffControllerApi(api_client)
    var_from = 56 # int | 
    to = 56 # int | 
    search = 'search_example' # str |  (optional)

    try:
        # Missed tests
        api_response = api_instance.missed(var_from, to, search=search)
        print("The response of LaunchDiffControllerApi->missed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchDiffControllerApi->missed: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | 
 **to** | **int**|  | 
 **search** | **str**|  | [optional] 

### Return type

[**List[LaunchDiffTestResultDto]**](LaunchDiffTestResultDto.md)

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

# **passed_to_failed_diff**
> List[LaunchDiffStatusChangeDto] passed_to_failed_diff(var_from, to, search=search)

Find failed

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_diff_status_change_dto import LaunchDiffStatusChangeDto
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
    api_instance = openapi_client.LaunchDiffControllerApi(api_client)
    var_from = 56 # int | 
    to = 56 # int | 
    search = 'search_example' # str |  (optional)

    try:
        # Find failed
        api_response = api_instance.passed_to_failed_diff(var_from, to, search=search)
        print("The response of LaunchDiffControllerApi->passed_to_failed_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchDiffControllerApi->passed_to_failed_diff: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | 
 **to** | **int**|  | 
 **search** | **str**|  | [optional] 

### Return type

[**List[LaunchDiffStatusChangeDto]**](LaunchDiffStatusChangeDto.md)

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

# **status_changed**
> List[LaunchDiffStatusChangeDto] status_changed(var_from, to, search=search)

Find status changed difference

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_diff_status_change_dto import LaunchDiffStatusChangeDto
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
    api_instance = openapi_client.LaunchDiffControllerApi(api_client)
    var_from = 56 # int | 
    to = 56 # int | 
    search = 'search_example' # str |  (optional)

    try:
        # Find status changed difference
        api_response = api_instance.status_changed(var_from, to, search=search)
        print("The response of LaunchDiffControllerApi->status_changed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LaunchDiffControllerApi->status_changed: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | 
 **to** | **int**|  | 
 **search** | **str**|  | [optional] 

### Return type

[**List[LaunchDiffStatusChangeDto]**](LaunchDiffStatusChangeDto.md)

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

