# openapi_client.TestResultTreeSelectionControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_leaves**](TestResultTreeSelectionControllerApi.md#count_leaves) | **POST** /testresulttree/select | Count test cases by tree select


# **count_leaves**
> int count_leaves(test_result_tree_selection_dto)

Count test cases by tree select

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_result_tree_selection_dto import TestResultTreeSelectionDto
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
    api_instance = openapi_client.TestResultTreeSelectionControllerApi(api_client)
    test_result_tree_selection_dto = openapi_client.TestResultTreeSelectionDto() # TestResultTreeSelectionDto | 

    try:
        # Count test cases by tree select
        api_response = api_instance.count_leaves(test_result_tree_selection_dto)
        print("The response of TestResultTreeSelectionControllerApi->count_leaves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultTreeSelectionControllerApi->count_leaves: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_tree_selection_dto** | [**TestResultTreeSelectionDto**](TestResultTreeSelectionDto.md)|  | 

### Return type

**int**

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

