# openapi_client.TestCaseScenarioControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scenario**](TestCaseScenarioControllerApi.md#delete_scenario) | **DELETE** /testcase/{id}/scenario | Delete scenario for test case
[**get_scenario**](TestCaseScenarioControllerApi.md#get_scenario) | **GET** /testcase/{id}/scenario | Find scenario for test case
[**get_scenario_from_last_run**](TestCaseScenarioControllerApi.md#get_scenario_from_last_run) | **GET** /testcase/{id}/scenariofromrun | Find scenario for test case from last run
[**update_scenario**](TestCaseScenarioControllerApi.md#update_scenario) | **POST** /testcase/{id}/scenario | Update scenario for test case


# **delete_scenario**
> delete_scenario(id)

Delete scenario for test case

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
    api_instance = openapi_client.TestCaseScenarioControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete scenario for test case
        api_instance.delete_scenario(id)
    except Exception as e:
        print("Exception when calling TestCaseScenarioControllerApi->delete_scenario: %s\n" % e)
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

# **get_scenario**
> TestCaseScenarioDto get_scenario(id)

Find scenario for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_scenario_dto import TestCaseScenarioDto
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
    api_instance = openapi_client.TestCaseScenarioControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find scenario for test case
        api_response = api_instance.get_scenario(id)
        print("The response of TestCaseScenarioControllerApi->get_scenario:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseScenarioControllerApi->get_scenario: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestCaseScenarioDto**](TestCaseScenarioDto.md)

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

# **get_scenario_from_last_run**
> TestCaseScenarioDto get_scenario_from_last_run(id)

Find scenario for test case from last run

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_scenario_dto import TestCaseScenarioDto
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
    api_instance = openapi_client.TestCaseScenarioControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find scenario for test case from last run
        api_response = api_instance.get_scenario_from_last_run(id)
        print("The response of TestCaseScenarioControllerApi->get_scenario_from_last_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseScenarioControllerApi->get_scenario_from_last_run: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestCaseScenarioDto**](TestCaseScenarioDto.md)

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

# **update_scenario**
> TestCaseScenarioDto update_scenario(id, test_case_scenario_dto)

Update scenario for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_scenario_dto import TestCaseScenarioDto
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
    api_instance = openapi_client.TestCaseScenarioControllerApi(api_client)
    id = 56 # int | 
    test_case_scenario_dto = openapi_client.TestCaseScenarioDto() # TestCaseScenarioDto | 

    try:
        # Update scenario for test case
        api_response = api_instance.update_scenario(id, test_case_scenario_dto)
        print("The response of TestCaseScenarioControllerApi->update_scenario:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseScenarioControllerApi->update_scenario: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **test_case_scenario_dto** | [**TestCaseScenarioDto**](TestCaseScenarioDto.md)|  | 

### Return type

[**TestCaseScenarioDto**](TestCaseScenarioDto.md)

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

