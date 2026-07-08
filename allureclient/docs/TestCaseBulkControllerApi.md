# openapi_client.TestCaseBulkControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cfv_add**](TestCaseBulkControllerApi.md#cfv_add) | **POST** /testcase/bulk/cfv/add | Add custom field values for all test cases
[**cfv_remove**](TestCaseBulkControllerApi.md#cfv_remove) | **POST** /testcase/bulk/cfv/remove | Remove custom field values for all test cases
[**clone_all**](TestCaseBulkControllerApi.md#clone_all) | **POST** /testcase/bulk/clone | Clone test cases by ids
[**create_test_plan**](TestCaseBulkControllerApi.md#create_test_plan) | **POST** /testcase/bulk/testplan/create | Create test plan from selected test cases
[**delete_all**](TestCaseBulkControllerApi.md#delete_all) | **POST** /testcase/bulk/remove | Remove test cases by ids
[**external_link_add**](TestCaseBulkControllerApi.md#external_link_add) | **POST** /testcase/bulk/externallink/add | Add external link for all test cases
[**issue_add**](TestCaseBulkControllerApi.md#issue_add) | **POST** /testcase/bulk/issue/add | Add issues for all test cases
[**issue_remove**](TestCaseBulkControllerApi.md#issue_remove) | **POST** /testcase/bulk/issue/remove | Remove issues for all test cases
[**layer_set**](TestCaseBulkControllerApi.md#layer_set) | **POST** /testcase/bulk/layer/set | Set specified layer for all test cases
[**member_add**](TestCaseBulkControllerApi.md#member_add) | **POST** /testcase/bulk/member/add | Add members for all test cases
[**member_remove**](TestCaseBulkControllerApi.md#member_remove) | **POST** /testcase/bulk/member/remove | Remove member for all test cases
[**move_all**](TestCaseBulkControllerApi.md#move_all) | **POST** /testcase/bulk/move | Move test cases to other project
[**mute_add**](TestCaseBulkControllerApi.md#mute_add) | **POST** /testcase/bulk/mute/add | Add mute for all test cases
[**run1**](TestCaseBulkControllerApi.md#run1) | **POST** /testcase/bulk/run/new | Run selected test cases in a new launch
[**run2**](TestCaseBulkControllerApi.md#run2) | **POST** /testcase/bulk/run | Run selected test cases in a new launch
[**run3**](TestCaseBulkControllerApi.md#run3) | **POST** /testcase/bulk/run/existing | Run selected test cases in an existing launch
[**status_set**](TestCaseBulkControllerApi.md#status_set) | **POST** /testcase/bulk/status/set | Set specified status for all test cases
[**tags_add1**](TestCaseBulkControllerApi.md#tags_add1) | **POST** /testcase/bulk/tag/add | Add tags for all test cases
[**tags_remove1**](TestCaseBulkControllerApi.md#tags_remove1) | **POST** /testcase/bulk/tag/remove | Remove tags for all test cases


# **cfv_add**
> cfv_add(test_case_bulk_cfv_dto)

Add custom field values for all test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_cfv_dto import TestCaseBulkCfvDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_cfv_dto = openapi_client.TestCaseBulkCfvDto() # TestCaseBulkCfvDto | 

    try:
        # Add custom field values for all test cases
        api_instance.cfv_add(test_case_bulk_cfv_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->cfv_add: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_cfv_dto** | [**TestCaseBulkCfvDto**](TestCaseBulkCfvDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cfv_remove**
> cfv_remove(test_case_bulk_entity_ids_dto)

Remove custom field values for all test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_entity_ids_dto import TestCaseBulkEntityIdsDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_entity_ids_dto = openapi_client.TestCaseBulkEntityIdsDto() # TestCaseBulkEntityIdsDto | 

    try:
        # Remove custom field values for all test cases
        api_instance.cfv_remove(test_case_bulk_entity_ids_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->cfv_remove: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_entity_ids_dto** | [**TestCaseBulkEntityIdsDto**](TestCaseBulkEntityIdsDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_all**
> clone_all(test_case_bulk_clone_dto)

Clone test cases by ids

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_clone_dto import TestCaseBulkCloneDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_clone_dto = openapi_client.TestCaseBulkCloneDto() # TestCaseBulkCloneDto | 

    try:
        # Clone test cases by ids
        api_instance.clone_all(test_case_bulk_clone_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->clone_all: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_clone_dto** | [**TestCaseBulkCloneDto**](TestCaseBulkCloneDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_test_plan**
> TestPlanDto create_test_plan(test_case_bulk_test_plan_create_dto)

Create test plan from selected test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_test_plan_create_dto import TestCaseBulkTestPlanCreateDto
from openapi_client.models.test_plan_dto import TestPlanDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_test_plan_create_dto = openapi_client.TestCaseBulkTestPlanCreateDto() # TestCaseBulkTestPlanCreateDto | 

    try:
        # Create test plan from selected test cases
        api_response = api_instance.create_test_plan(test_case_bulk_test_plan_create_dto)
        print("The response of TestCaseBulkControllerApi->create_test_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->create_test_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_test_plan_create_dto** | [**TestCaseBulkTestPlanCreateDto**](TestCaseBulkTestPlanCreateDto.md)|  | 

### Return type

[**TestPlanDto**](TestPlanDto.md)

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

# **delete_all**
> delete_all(test_case_bulk_dto)

Remove test cases by ids

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_dto import TestCaseBulkDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_dto = openapi_client.TestCaseBulkDto() # TestCaseBulkDto | 

    try:
        # Remove test cases by ids
        api_instance.delete_all(test_case_bulk_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->delete_all: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_dto** | [**TestCaseBulkDto**](TestCaseBulkDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_link_add**
> external_link_add(test_case_bulk_external_link_dto)

Add external link for all test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_external_link_dto import TestCaseBulkExternalLinkDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_external_link_dto = openapi_client.TestCaseBulkExternalLinkDto() # TestCaseBulkExternalLinkDto | 

    try:
        # Add external link for all test cases
        api_instance.external_link_add(test_case_bulk_external_link_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->external_link_add: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_external_link_dto** | [**TestCaseBulkExternalLinkDto**](TestCaseBulkExternalLinkDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_add**
> issue_add(test_case_bulk_issue_dto)

Add issues for all test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_issue_dto import TestCaseBulkIssueDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_issue_dto = openapi_client.TestCaseBulkIssueDto() # TestCaseBulkIssueDto | 

    try:
        # Add issues for all test cases
        api_instance.issue_add(test_case_bulk_issue_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->issue_add: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_issue_dto** | [**TestCaseBulkIssueDto**](TestCaseBulkIssueDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_remove**
> issue_remove(test_case_bulk_entity_ids_dto)

Remove issues for all test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_entity_ids_dto import TestCaseBulkEntityIdsDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_entity_ids_dto = openapi_client.TestCaseBulkEntityIdsDto() # TestCaseBulkEntityIdsDto | 

    try:
        # Remove issues for all test cases
        api_instance.issue_remove(test_case_bulk_entity_ids_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->issue_remove: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_entity_ids_dto** | [**TestCaseBulkEntityIdsDto**](TestCaseBulkEntityIdsDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_set**
> layer_set(test_case_bulk_layer_dto)

Set specified layer for all test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_layer_dto import TestCaseBulkLayerDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_layer_dto = openapi_client.TestCaseBulkLayerDto() # TestCaseBulkLayerDto | 

    try:
        # Set specified layer for all test cases
        api_instance.layer_set(test_case_bulk_layer_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->layer_set: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_layer_dto** | [**TestCaseBulkLayerDto**](TestCaseBulkLayerDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_add**
> member_add(test_case_bulk_member_dto)

Add members for all test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_member_dto import TestCaseBulkMemberDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_member_dto = openapi_client.TestCaseBulkMemberDto() # TestCaseBulkMemberDto | 

    try:
        # Add members for all test cases
        api_instance.member_add(test_case_bulk_member_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->member_add: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_member_dto** | [**TestCaseBulkMemberDto**](TestCaseBulkMemberDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_remove**
> member_remove(test_case_bulk_entity_ids_dto)

Remove member for all test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_entity_ids_dto import TestCaseBulkEntityIdsDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_entity_ids_dto = openapi_client.TestCaseBulkEntityIdsDto() # TestCaseBulkEntityIdsDto | 

    try:
        # Remove member for all test cases
        api_instance.member_remove(test_case_bulk_entity_ids_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->member_remove: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_entity_ids_dto** | [**TestCaseBulkEntityIdsDto**](TestCaseBulkEntityIdsDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_all**
> move_all(test_case_bulk_project_change_dto)

Move test cases to other project

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_project_change_dto import TestCaseBulkProjectChangeDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_project_change_dto = openapi_client.TestCaseBulkProjectChangeDto() # TestCaseBulkProjectChangeDto | 

    try:
        # Move test cases to other project
        api_instance.move_all(test_case_bulk_project_change_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->move_all: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_project_change_dto** | [**TestCaseBulkProjectChangeDto**](TestCaseBulkProjectChangeDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mute_add**
> mute_add(test_case_bulk_mute_dto)

Add mute for all test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_mute_dto import TestCaseBulkMuteDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_mute_dto = openapi_client.TestCaseBulkMuteDto() # TestCaseBulkMuteDto | 

    try:
        # Add mute for all test cases
        api_instance.mute_add(test_case_bulk_mute_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->mute_add: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_mute_dto** | [**TestCaseBulkMuteDto**](TestCaseBulkMuteDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run1**
> LaunchDto run1(test_case_bulk_run_new_launch_dto)

Run selected test cases in a new launch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_dto import LaunchDto
from openapi_client.models.test_case_bulk_run_new_launch_dto import TestCaseBulkRunNewLaunchDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_run_new_launch_dto = openapi_client.TestCaseBulkRunNewLaunchDto() # TestCaseBulkRunNewLaunchDto | 

    try:
        # Run selected test cases in a new launch
        api_response = api_instance.run1(test_case_bulk_run_new_launch_dto)
        print("The response of TestCaseBulkControllerApi->run1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->run1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_run_new_launch_dto** | [**TestCaseBulkRunNewLaunchDto**](TestCaseBulkRunNewLaunchDto.md)|  | 

### Return type

[**LaunchDto**](LaunchDto.md)

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

# **run2**
> LaunchDto run2(test_case_bulk_run_new_launch_dto)

Run selected test cases in a new launch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_dto import LaunchDto
from openapi_client.models.test_case_bulk_run_new_launch_dto import TestCaseBulkRunNewLaunchDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_run_new_launch_dto = openapi_client.TestCaseBulkRunNewLaunchDto() # TestCaseBulkRunNewLaunchDto | 

    try:
        # Run selected test cases in a new launch
        api_response = api_instance.run2(test_case_bulk_run_new_launch_dto)
        print("The response of TestCaseBulkControllerApi->run2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->run2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_run_new_launch_dto** | [**TestCaseBulkRunNewLaunchDto**](TestCaseBulkRunNewLaunchDto.md)|  | 

### Return type

[**LaunchDto**](LaunchDto.md)

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

# **run3**
> LaunchDto run3(test_case_bulk_run_existing_launch_dto)

Run selected test cases in an existing launch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_dto import LaunchDto
from openapi_client.models.test_case_bulk_run_existing_launch_dto import TestCaseBulkRunExistingLaunchDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_run_existing_launch_dto = openapi_client.TestCaseBulkRunExistingLaunchDto() # TestCaseBulkRunExistingLaunchDto | 

    try:
        # Run selected test cases in an existing launch
        api_response = api_instance.run3(test_case_bulk_run_existing_launch_dto)
        print("The response of TestCaseBulkControllerApi->run3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->run3: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_run_existing_launch_dto** | [**TestCaseBulkRunExistingLaunchDto**](TestCaseBulkRunExistingLaunchDto.md)|  | 

### Return type

[**LaunchDto**](LaunchDto.md)

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

# **status_set**
> status_set(test_case_bulk_status_dto)

Set specified status for all test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_status_dto import TestCaseBulkStatusDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_status_dto = openapi_client.TestCaseBulkStatusDto() # TestCaseBulkStatusDto | 

    try:
        # Set specified status for all test cases
        api_instance.status_set(test_case_bulk_status_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->status_set: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_status_dto** | [**TestCaseBulkStatusDto**](TestCaseBulkStatusDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_add1**
> tags_add1(test_case_bulk_tag_dto)

Add tags for all test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_tag_dto import TestCaseBulkTagDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_tag_dto = openapi_client.TestCaseBulkTagDto() # TestCaseBulkTagDto | 

    try:
        # Add tags for all test cases
        api_instance.tags_add1(test_case_bulk_tag_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->tags_add1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_tag_dto** | [**TestCaseBulkTagDto**](TestCaseBulkTagDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_remove1**
> tags_remove1(test_case_bulk_entity_ids_dto)

Remove tags for all test cases

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_bulk_entity_ids_dto import TestCaseBulkEntityIdsDto
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
    api_instance = openapi_client.TestCaseBulkControllerApi(api_client)
    test_case_bulk_entity_ids_dto = openapi_client.TestCaseBulkEntityIdsDto() # TestCaseBulkEntityIdsDto | 

    try:
        # Remove tags for all test cases
        api_instance.tags_remove1(test_case_bulk_entity_ids_dto)
    except Exception as e:
        print("Exception when calling TestCaseBulkControllerApi->tags_remove1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_bulk_entity_ids_dto** | [**TestCaseBulkEntityIdsDto**](TestCaseBulkEntityIdsDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

