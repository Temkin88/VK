# openapi_client.TestCaseExampleControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate**](TestCaseExampleControllerApi.md#generate) | **POST** /testcase/example/nwise | 
[**get_examples**](TestCaseExampleControllerApi.md#get_examples) | **GET** /testcase/{testCaseId}/example | 
[**set_examples**](TestCaseExampleControllerApi.md#set_examples) | **POST** /testcase/{testCaseId}/example | 


# **generate**
> List[TestCaseExampleDto] generate(test_case_parameter_values, n=n)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_example_dto import TestCaseExampleDto
from openapi_client.models.test_case_parameter_values import TestCaseParameterValues
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
    api_instance = openapi_client.TestCaseExampleControllerApi(api_client)
    test_case_parameter_values = [openapi_client.TestCaseParameterValues()] # List[TestCaseParameterValues] | 
    n = 1 # int |  (optional) (default to 1)

    try:
        api_response = api_instance.generate(test_case_parameter_values, n=n)
        print("The response of TestCaseExampleControllerApi->generate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseExampleControllerApi->generate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_parameter_values** | [**List[TestCaseParameterValues]**](TestCaseParameterValues.md)|  | 
 **n** | **int**|  | [optional] [default to 1]

### Return type

[**List[TestCaseExampleDto]**](TestCaseExampleDto.md)

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

# **get_examples**
> PageTestCaseExampleDto get_examples(test_case_id, page=page, size=size, sort=sort)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_case_example_dto import PageTestCaseExampleDto
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
    api_instance = openapi_client.TestCaseExampleControllerApi(api_client)
    test_case_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["id,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["id,ASC"])

    try:
        api_response = api_instance.get_examples(test_case_id, page=page, size=size, sort=sort)
        print("The response of TestCaseExampleControllerApi->get_examples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseExampleControllerApi->get_examples: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;id,ASC&quot;]]

### Return type

[**PageTestCaseExampleDto**](PageTestCaseExampleDto.md)

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

# **set_examples**
> List[TestCaseExampleDto] set_examples(test_case_id, parameter_value_dto)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.parameter_value_dto import ParameterValueDto
from openapi_client.models.test_case_example_dto import TestCaseExampleDto
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
    api_instance = openapi_client.TestCaseExampleControllerApi(api_client)
    test_case_id = 56 # int | 
    parameter_value_dto = None # List[List[ParameterValueDto]] | 

    try:
        api_response = api_instance.set_examples(test_case_id, parameter_value_dto)
        print("The response of TestCaseExampleControllerApi->set_examples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseExampleControllerApi->set_examples: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 
 **parameter_value_dto** | [**List[List[ParameterValueDto]]**](List.md)|  | 

### Return type

[**List[TestCaseExampleDto]**](TestCaseExampleDto.md)

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

