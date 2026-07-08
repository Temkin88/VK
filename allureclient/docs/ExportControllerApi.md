# openapi_client.ExportControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate1**](ExportControllerApi.md#generate1) | **POST** /export/launch/pdf | Generate launch pdf report
[**generate_test_case_csv_export**](ExportControllerApi.md#generate_test_case_csv_export) | **POST** /export/testcase/csv | Generate test cases csv report
[**generate_test_case_pdf_export**](ExportControllerApi.md#generate_test_case_pdf_export) | **POST** /export/testcase/pdf | Generate test cases pdf report
[**generate_test_result_csv_export**](ExportControllerApi.md#generate_test_result_csv_export) | **POST** /export/testresult/csv | Generate test results csv report
[**get_supported_launch_pdf_content**](ExportControllerApi.md#get_supported_launch_pdf_content) | **GET** /export/launch/pdf/structure | Get supported launch pdf report parts
[**get_supported_tc_fields**](ExportControllerApi.md#get_supported_tc_fields) | **GET** /export/testcase/csv/mapping | Get supported test case export fields
[**get_supported_tr_fields**](ExportControllerApi.md#get_supported_tr_fields) | **GET** /export/testresult/csv/mapping | Get supported test result export fields


# **generate1**
> ExportRequestDto generate1(launch_pdf_options, shared=shared)

Generate launch pdf report

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.export_request_dto import ExportRequestDto
from openapi_client.models.launch_pdf_options import LaunchPdfOptions
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
    api_instance = openapi_client.ExportControllerApi(api_client)
    launch_pdf_options = openapi_client.LaunchPdfOptions() # LaunchPdfOptions | 
    shared = True # bool |  (optional) (default to True)

    try:
        # Generate launch pdf report
        api_response = api_instance.generate1(launch_pdf_options, shared=shared)
        print("The response of ExportControllerApi->generate1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportControllerApi->generate1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_pdf_options** | [**LaunchPdfOptions**](LaunchPdfOptions.md)|  | 
 **shared** | **bool**|  | [optional] [default to True]

### Return type

[**ExportRequestDto**](ExportRequestDto.md)

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

# **generate_test_case_csv_export**
> ExportRequestDto generate_test_case_csv_export(test_case_csv_export_options, shared=shared)

Generate test cases csv report

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.export_request_dto import ExportRequestDto
from openapi_client.models.test_case_csv_export_options import TestCaseCsvExportOptions
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
    api_instance = openapi_client.ExportControllerApi(api_client)
    test_case_csv_export_options = openapi_client.TestCaseCsvExportOptions() # TestCaseCsvExportOptions | 
    shared = True # bool |  (optional) (default to True)

    try:
        # Generate test cases csv report
        api_response = api_instance.generate_test_case_csv_export(test_case_csv_export_options, shared=shared)
        print("The response of ExportControllerApi->generate_test_case_csv_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportControllerApi->generate_test_case_csv_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_csv_export_options** | [**TestCaseCsvExportOptions**](TestCaseCsvExportOptions.md)|  | 
 **shared** | **bool**|  | [optional] [default to True]

### Return type

[**ExportRequestDto**](ExportRequestDto.md)

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

# **generate_test_case_pdf_export**
> ExportRequestDto generate_test_case_pdf_export(test_case_pdf_options, shared=shared)

Generate test cases pdf report

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.export_request_dto import ExportRequestDto
from openapi_client.models.test_case_pdf_options import TestCasePdfOptions
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
    api_instance = openapi_client.ExportControllerApi(api_client)
    test_case_pdf_options = openapi_client.TestCasePdfOptions() # TestCasePdfOptions | 
    shared = True # bool |  (optional) (default to True)

    try:
        # Generate test cases pdf report
        api_response = api_instance.generate_test_case_pdf_export(test_case_pdf_options, shared=shared)
        print("The response of ExportControllerApi->generate_test_case_pdf_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportControllerApi->generate_test_case_pdf_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_pdf_options** | [**TestCasePdfOptions**](TestCasePdfOptions.md)|  | 
 **shared** | **bool**|  | [optional] [default to True]

### Return type

[**ExportRequestDto**](ExportRequestDto.md)

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

# **generate_test_result_csv_export**
> ExportRequestDto generate_test_result_csv_export(test_result_csv_export_options, shared=shared)

Generate test results csv report

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.export_request_dto import ExportRequestDto
from openapi_client.models.test_result_csv_export_options import TestResultCsvExportOptions
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
    api_instance = openapi_client.ExportControllerApi(api_client)
    test_result_csv_export_options = openapi_client.TestResultCsvExportOptions() # TestResultCsvExportOptions | 
    shared = True # bool |  (optional) (default to True)

    try:
        # Generate test results csv report
        api_response = api_instance.generate_test_result_csv_export(test_result_csv_export_options, shared=shared)
        print("The response of ExportControllerApi->generate_test_result_csv_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportControllerApi->generate_test_result_csv_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_csv_export_options** | [**TestResultCsvExportOptions**](TestResultCsvExportOptions.md)|  | 
 **shared** | **bool**|  | [optional] [default to True]

### Return type

[**ExportRequestDto**](ExportRequestDto.md)

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

# **get_supported_launch_pdf_content**
> LaunchPdfStructure get_supported_launch_pdf_content()

Get supported launch pdf report parts

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.launch_pdf_structure import LaunchPdfStructure
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
    api_instance = openapi_client.ExportControllerApi(api_client)

    try:
        # Get supported launch pdf report parts
        api_response = api_instance.get_supported_launch_pdf_content()
        print("The response of ExportControllerApi->get_supported_launch_pdf_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportControllerApi->get_supported_launch_pdf_content: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**LaunchPdfStructure**](LaunchPdfStructure.md)

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

# **get_supported_tc_fields**
> List[TestCaseExportField] get_supported_tc_fields()

Get supported test case export fields

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_export_field import TestCaseExportField
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
    api_instance = openapi_client.ExportControllerApi(api_client)

    try:
        # Get supported test case export fields
        api_response = api_instance.get_supported_tc_fields()
        print("The response of ExportControllerApi->get_supported_tc_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportControllerApi->get_supported_tc_fields: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[TestCaseExportField]**](TestCaseExportField.md)

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

# **get_supported_tr_fields**
> List[TestResultExportField] get_supported_tr_fields()

Get supported test result export fields

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_result_export_field import TestResultExportField
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
    api_instance = openapi_client.ExportControllerApi(api_client)

    try:
        # Get supported test result export fields
        api_response = api_instance.get_supported_tr_fields()
        print("The response of ExportControllerApi->get_supported_tr_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportControllerApi->get_supported_tr_fields: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[TestResultExportField]**](TestResultExportField.md)

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

