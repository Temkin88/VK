# openapi_client.TestResultTreeControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_groups**](TestResultTreeControllerApi.md#get_groups) | **GET** /testresulttree/group | Find tree groups for node
[**get_leafs**](TestResultTreeControllerApi.md#get_leafs) | **GET** /testresulttree/leaf | Find tree leafs for node


# **get_groups**
> PageTestResultTreeGroupDto get_groups(launch_id, search=search, tree_id=tree_id, path=path, page=page, size=size, sort=sort)

Find tree groups for node

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_tree_group_dto import PageTestResultTreeGroupDto
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
    api_instance = openapi_client.TestResultTreeControllerApi(api_client)
    launch_id = 56 # int | 
    search = 'search_example' # str |  (optional)
    tree_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find tree groups for node
        api_response = api_instance.get_groups(launch_id, search=search, tree_id=tree_id, path=path, page=page, size=size, sort=sort)
        print("The response of TestResultTreeControllerApi->get_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultTreeControllerApi->get_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **int**|  | 
 **search** | **str**|  | [optional] 
 **tree_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageTestResultTreeGroupDto**](PageTestResultTreeGroupDto.md)

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

# **get_leafs**
> PageTestResultTreeLeafDto get_leafs(launch_id, search=search, tree_id=tree_id, path=path, page=page, size=size, sort=sort)

Find tree leafs for node

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_test_result_tree_leaf_dto import PageTestResultTreeLeafDto
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
    api_instance = openapi_client.TestResultTreeControllerApi(api_client)
    launch_id = 56 # int | 
    search = 'search_example' # str |  (optional)
    tree_id = 56 # int |  (optional)
    path = [] # List[int] |  (optional) (default to [])
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["name,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,ASC"])

    try:
        # Find tree leafs for node
        api_response = api_instance.get_leafs(launch_id, search=search, tree_id=tree_id, path=path, page=page, size=size, sort=sort)
        print("The response of TestResultTreeControllerApi->get_leafs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultTreeControllerApi->get_leafs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **int**|  | 
 **search** | **str**|  | [optional] 
 **tree_id** | **int**|  | [optional] 
 **path** | [**List[int]**](int.md)|  | [optional] [default to []]
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,ASC&quot;]]

### Return type

[**PageTestResultTreeLeafDto**](PageTestResultTreeLeafDto.md)

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

