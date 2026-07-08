# openapi_client.TestCaseCsvImportControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info**](TestCaseCsvImportControllerApi.md#info) | **POST** /testcase/import/csv/{importRequestId}/info | Get testcase csv import file and return import info
[**preview**](TestCaseCsvImportControllerApi.md#preview) | **POST** /testcase/import/csv/{importRequestId}/preview | Preview testcase csv import
[**submit**](TestCaseCsvImportControllerApi.md#submit) | **POST** /testcase/import/csv/{importRequestId}/submit | Submit testcase csv import


# **info**
> ImportRequestInfoDto info(import_request_id, csv_import_options)

Get testcase csv import file and return import info

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.csv_import_options import CsvImportOptions
from openapi_client.models.import_request_info_dto import ImportRequestInfoDto
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
    api_instance = openapi_client.TestCaseCsvImportControllerApi(api_client)
    import_request_id = 56 # int | 
    csv_import_options = openapi_client.CsvImportOptions() # CsvImportOptions | 

    try:
        # Get testcase csv import file and return import info
        api_response = api_instance.info(import_request_id, csv_import_options)
        print("The response of TestCaseCsvImportControllerApi->info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseCsvImportControllerApi->info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_request_id** | **int**|  | 
 **csv_import_options** | [**CsvImportOptions**](CsvImportOptions.md)|  | 

### Return type

[**ImportRequestInfoDto**](ImportRequestInfoDto.md)

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

# **preview**
> TestCaseOverviewDto preview(import_request_id, test_case_csv_preview_options)

Preview testcase csv import

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_csv_preview_options import TestCaseCsvPreviewOptions
from openapi_client.models.test_case_overview_dto import TestCaseOverviewDto
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
    api_instance = openapi_client.TestCaseCsvImportControllerApi(api_client)
    import_request_id = 56 # int | 
    test_case_csv_preview_options = openapi_client.TestCaseCsvPreviewOptions() # TestCaseCsvPreviewOptions | 

    try:
        # Preview testcase csv import
        api_response = api_instance.preview(import_request_id, test_case_csv_preview_options)
        print("The response of TestCaseCsvImportControllerApi->preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseCsvImportControllerApi->preview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_request_id** | **int**|  | 
 **test_case_csv_preview_options** | [**TestCaseCsvPreviewOptions**](TestCaseCsvPreviewOptions.md)|  | 

### Return type

[**TestCaseOverviewDto**](TestCaseOverviewDto.md)

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

# **submit**
> submit(import_request_id, test_case_csv_import_options)

Submit testcase csv import

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_csv_import_options import TestCaseCsvImportOptions
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
    api_instance = openapi_client.TestCaseCsvImportControllerApi(api_client)
    import_request_id = 56 # int | 
    test_case_csv_import_options = openapi_client.TestCaseCsvImportOptions() # TestCaseCsvImportOptions | 

    try:
        # Submit testcase csv import
        api_instance.submit(import_request_id, test_case_csv_import_options)
    except Exception as e:
        print("Exception when calling TestCaseCsvImportControllerApi->submit: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_request_id** | **int**|  | 
 **test_case_csv_import_options** | [**TestCaseCsvImportOptions**](TestCaseCsvImportOptions.md)|  | 

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

