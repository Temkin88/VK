# openapi_client.TestCaseRelationControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_relations**](TestCaseRelationControllerApi.md#get_relations) | **GET** /testcase/{testCaseId}/relation | Find relations for test case
[**set_relations**](TestCaseRelationControllerApi.md#set_relations) | **POST** /testcase/{testCaseId}/relation | Set relations for test case


# **get_relations**
> List[TestCaseRelationDto] get_relations(test_case_id)

Find relations for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_relation_dto import TestCaseRelationDto
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
    api_instance = openapi_client.TestCaseRelationControllerApi(api_client)
    test_case_id = 56 # int | 

    try:
        # Find relations for test case
        api_response = api_instance.get_relations(test_case_id)
        print("The response of TestCaseRelationControllerApi->get_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseRelationControllerApi->get_relations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 

### Return type

[**List[TestCaseRelationDto]**](TestCaseRelationDto.md)

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

# **set_relations**
> List[TestCaseRelationDto] set_relations(test_case_id, test_case_relation_dto)

Set relations for test case

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_relation_dto import TestCaseRelationDto
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
    api_instance = openapi_client.TestCaseRelationControllerApi(api_client)
    test_case_id = 56 # int | 
    test_case_relation_dto = [openapi_client.TestCaseRelationDto()] # List[TestCaseRelationDto] | 

    try:
        # Set relations for test case
        api_response = api_instance.set_relations(test_case_id, test_case_relation_dto)
        print("The response of TestCaseRelationControllerApi->set_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseRelationControllerApi->set_relations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 
 **test_case_relation_dto** | [**List[TestCaseRelationDto]**](TestCaseRelationDto.md)|  | 

### Return type

[**List[TestCaseRelationDto]**](TestCaseRelationDto.md)

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

