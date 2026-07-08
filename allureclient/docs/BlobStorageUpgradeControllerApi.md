# openapi_client.BlobStorageUpgradeControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**migrate_stats**](BlobStorageUpgradeControllerApi.md#migrate_stats) | **GET** /storage/upgrade/v2 | 
[**migrate_test_case_attachments**](BlobStorageUpgradeControllerApi.md#migrate_test_case_attachments) | **POST** /storage/upgrade/v2/test-case-attachment | 
[**migrate_test_fixture_result**](BlobStorageUpgradeControllerApi.md#migrate_test_fixture_result) | **POST** /storage/upgrade/v2/test-fixture-result | 
[**migrate_test_fixture_result_attachment**](BlobStorageUpgradeControllerApi.md#migrate_test_fixture_result_attachment) | **POST** /storage/upgrade/v2/test-fixture-result-attachment | 
[**migrate_test_result**](BlobStorageUpgradeControllerApi.md#migrate_test_result) | **POST** /storage/upgrade/v2/test-result | 
[**migrate_test_result_attachment**](BlobStorageUpgradeControllerApi.md#migrate_test_result_attachment) | **POST** /storage/upgrade/v2/test-result-attachment | 


# **migrate_stats**
> BlobStorageUpdateStats migrate_stats()



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.blob_storage_update_stats import BlobStorageUpdateStats
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
    api_instance = openapi_client.BlobStorageUpgradeControllerApi(api_client)

    try:
        api_response = api_instance.migrate_stats()
        print("The response of BlobStorageUpgradeControllerApi->migrate_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlobStorageUpgradeControllerApi->migrate_stats: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**BlobStorageUpdateStats**](BlobStorageUpdateStats.md)

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

# **migrate_test_case_attachments**
> migrate_test_case_attachments(project_id, limit, remove_on_error=remove_on_error)



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
    api_instance = openapi_client.BlobStorageUpgradeControllerApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int | 
    remove_on_error = False # bool |  (optional) (default to False)

    try:
        api_instance.migrate_test_case_attachments(project_id, limit, remove_on_error=remove_on_error)
    except Exception as e:
        print("Exception when calling BlobStorageUpgradeControllerApi->migrate_test_case_attachments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | 
 **remove_on_error** | **bool**|  | [optional] [default to False]

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_test_fixture_result**
> migrate_test_fixture_result(project_id, limit, remove_on_error=remove_on_error)



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
    api_instance = openapi_client.BlobStorageUpgradeControllerApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int | 
    remove_on_error = False # bool |  (optional) (default to False)

    try:
        api_instance.migrate_test_fixture_result(project_id, limit, remove_on_error=remove_on_error)
    except Exception as e:
        print("Exception when calling BlobStorageUpgradeControllerApi->migrate_test_fixture_result: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | 
 **remove_on_error** | **bool**|  | [optional] [default to False]

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_test_fixture_result_attachment**
> migrate_test_fixture_result_attachment(project_id, limit, remove_on_error=remove_on_error)



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
    api_instance = openapi_client.BlobStorageUpgradeControllerApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int | 
    remove_on_error = False # bool |  (optional) (default to False)

    try:
        api_instance.migrate_test_fixture_result_attachment(project_id, limit, remove_on_error=remove_on_error)
    except Exception as e:
        print("Exception when calling BlobStorageUpgradeControllerApi->migrate_test_fixture_result_attachment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | 
 **remove_on_error** | **bool**|  | [optional] [default to False]

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_test_result**
> migrate_test_result(project_id, limit, remove_on_error=remove_on_error)



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
    api_instance = openapi_client.BlobStorageUpgradeControllerApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int | 
    remove_on_error = False # bool |  (optional) (default to False)

    try:
        api_instance.migrate_test_result(project_id, limit, remove_on_error=remove_on_error)
    except Exception as e:
        print("Exception when calling BlobStorageUpgradeControllerApi->migrate_test_result: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | 
 **remove_on_error** | **bool**|  | [optional] [default to False]

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_test_result_attachment**
> migrate_test_result_attachment(project_id, limit, remove_on_error=remove_on_error)



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
    api_instance = openapi_client.BlobStorageUpgradeControllerApi(api_client)
    project_id = 56 # int | 
    limit = 56 # int | 
    remove_on_error = False # bool |  (optional) (default to False)

    try:
        api_instance.migrate_test_result_attachment(project_id, limit, remove_on_error=remove_on_error)
    except Exception as e:
        print("Exception when calling BlobStorageUpgradeControllerApi->migrate_test_result_attachment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **limit** | **int**|  | 
 **remove_on_error** | **bool**|  | [optional] [default to False]

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

