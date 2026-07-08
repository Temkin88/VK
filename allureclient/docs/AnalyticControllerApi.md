# openapi_client.AnalyticControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**automation_chart**](AnalyticControllerApi.md#automation_chart) | **GET** /analytic/{id}/automation_chart | 
[**group_by_automation**](AnalyticControllerApi.md#group_by_automation) | **GET** /analytic/{id}/group_by_automation | 
[**group_by_status**](AnalyticControllerApi.md#group_by_status) | **GET** /analytic/{id}/group_by_status | 
[**last_results**](AnalyticControllerApi.md#last_results) | **GET** /analytic/{id}/tc_last_result | 
[**launch_duration_histogram**](AnalyticControllerApi.md#launch_duration_histogram) | **GET** /analytic/{id}/launch_duration_histogram | 
[**mute_trend**](AnalyticControllerApi.md#mute_trend) | **GET** /analytic/{id}/mute_trend | 
[**statistic_trend**](AnalyticControllerApi.md#statistic_trend) | **GET** /analytic/{id}/statistic_trend | 
[**success_rate**](AnalyticControllerApi.md#success_rate) | **GET** /analytic/{id}/tc_success_rate | 


# **automation_chart**
> List[AnalyticAutomationTrendDto] automation_chart(id, tc_rql=tc_rql, launch_rql=launch_rql, var_from=var_from, to=to, interval=interval)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.analytic_automation_trend_dto import AnalyticAutomationTrendDto
from openapi_client.models.analytic_interval import AnalyticInterval
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
    api_instance = openapi_client.AnalyticControllerApi(api_client)
    id = 56 # int | 
    tc_rql = 'tc_rql_example' # str |  (optional)
    launch_rql = 'launch_rql_example' # str |  (optional)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    interval = openapi_client.AnalyticInterval() # AnalyticInterval |  (optional)

    try:
        api_response = api_instance.automation_chart(id, tc_rql=tc_rql, launch_rql=launch_rql, var_from=var_from, to=to, interval=interval)
        print("The response of AnalyticControllerApi->automation_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticControllerApi->automation_chart: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tc_rql** | **str**|  | [optional] 
 **launch_rql** | **str**|  | [optional] 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **interval** | [**AnalyticInterval**](.md)|  | [optional] 

### Return type

[**List[AnalyticAutomationTrendDto]**](AnalyticAutomationTrendDto.md)

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

# **group_by_automation**
> List[AnalyticTcAutomationCountDto] group_by_automation(id, tc_rql=tc_rql)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.analytic_tc_automation_count_dto import AnalyticTcAutomationCountDto
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
    api_instance = openapi_client.AnalyticControllerApi(api_client)
    id = 56 # int | 
    tc_rql = 'tc_rql_example' # str |  (optional)

    try:
        api_response = api_instance.group_by_automation(id, tc_rql=tc_rql)
        print("The response of AnalyticControllerApi->group_by_automation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticControllerApi->group_by_automation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tc_rql** | **str**|  | [optional] 

### Return type

[**List[AnalyticTcAutomationCountDto]**](AnalyticTcAutomationCountDto.md)

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

# **group_by_status**
> List[AnalyticTcStatusCountDto] group_by_status(id, tc_rql=tc_rql)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.analytic_tc_status_count_dto import AnalyticTcStatusCountDto
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
    api_instance = openapi_client.AnalyticControllerApi(api_client)
    id = 56 # int | 
    tc_rql = 'tc_rql_example' # str |  (optional)

    try:
        api_response = api_instance.group_by_status(id, tc_rql=tc_rql)
        print("The response of AnalyticControllerApi->group_by_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticControllerApi->group_by_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tc_rql** | **str**|  | [optional] 

### Return type

[**List[AnalyticTcStatusCountDto]**](AnalyticTcStatusCountDto.md)

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

# **last_results**
> List[TestCaseLastResultDto] last_results(id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.test_case_last_result_dto import TestCaseLastResultDto
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
    api_instance = openapi_client.AnalyticControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.last_results(id)
        print("The response of AnalyticControllerApi->last_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticControllerApi->last_results: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[TestCaseLastResultDto]**](TestCaseLastResultDto.md)

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

# **launch_duration_histogram**
> List[AnalyticLaunchDurationHistogramDto] launch_duration_histogram(id, tc_rql=tc_rql, launch_rql=launch_rql, var_from=var_from, to=to, buckets=buckets)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.analytic_launch_duration_histogram_dto import AnalyticLaunchDurationHistogramDto
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
    api_instance = openapi_client.AnalyticControllerApi(api_client)
    id = 56 # int | 
    tc_rql = 'tc_rql_example' # str |  (optional)
    launch_rql = 'launch_rql_example' # str |  (optional)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    buckets = 10 # int |  (optional) (default to 10)

    try:
        api_response = api_instance.launch_duration_histogram(id, tc_rql=tc_rql, launch_rql=launch_rql, var_from=var_from, to=to, buckets=buckets)
        print("The response of AnalyticControllerApi->launch_duration_histogram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticControllerApi->launch_duration_histogram: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tc_rql** | **str**|  | [optional] 
 **launch_rql** | **str**|  | [optional] 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **buckets** | **int**|  | [optional] [default to 10]

### Return type

[**List[AnalyticLaunchDurationHistogramDto]**](AnalyticLaunchDurationHistogramDto.md)

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

# **mute_trend**
> List[AnalyticMuteTrendDto] mute_trend(id, var_from=var_from, to=to, interval=interval)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.analytic_interval import AnalyticInterval
from openapi_client.models.analytic_mute_trend_dto import AnalyticMuteTrendDto
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
    api_instance = openapi_client.AnalyticControllerApi(api_client)
    id = 56 # int | 
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    interval = openapi_client.AnalyticInterval() # AnalyticInterval |  (optional)

    try:
        api_response = api_instance.mute_trend(id, var_from=var_from, to=to, interval=interval)
        print("The response of AnalyticControllerApi->mute_trend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticControllerApi->mute_trend: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **interval** | [**AnalyticInterval**](.md)|  | [optional] 

### Return type

[**List[AnalyticMuteTrendDto]**](AnalyticMuteTrendDto.md)

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

# **statistic_trend**
> List[AnalyticTrByStatusTrendDto] statistic_trend(id, tc_rql=tc_rql, launch_rql=launch_rql, var_from=var_from, to=to, interval=interval)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.analytic_interval import AnalyticInterval
from openapi_client.models.analytic_tr_by_status_trend_dto import AnalyticTrByStatusTrendDto
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
    api_instance = openapi_client.AnalyticControllerApi(api_client)
    id = 56 # int | 
    tc_rql = 'tc_rql_example' # str |  (optional)
    launch_rql = 'launch_rql_example' # str |  (optional)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    interval = openapi_client.AnalyticInterval() # AnalyticInterval |  (optional)

    try:
        api_response = api_instance.statistic_trend(id, tc_rql=tc_rql, launch_rql=launch_rql, var_from=var_from, to=to, interval=interval)
        print("The response of AnalyticControllerApi->statistic_trend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticControllerApi->statistic_trend: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tc_rql** | **str**|  | [optional] 
 **launch_rql** | **str**|  | [optional] 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **interval** | [**AnalyticInterval**](.md)|  | [optional] 

### Return type

[**List[AnalyticTrByStatusTrendDto]**](AnalyticTrByStatusTrendDto.md)

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

# **success_rate**
> List[AnalyticDto] success_rate(id, tc_rql=tc_rql, launch_rql=launch_rql, var_from=var_from, to=to, interval=interval)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.analytic_dto import AnalyticDto
from openapi_client.models.analytic_interval import AnalyticInterval
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
    api_instance = openapi_client.AnalyticControllerApi(api_client)
    id = 56 # int | 
    tc_rql = 'tc_rql_example' # str |  (optional)
    launch_rql = 'launch_rql_example' # str |  (optional)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    interval = openapi_client.AnalyticInterval() # AnalyticInterval |  (optional)

    try:
        api_response = api_instance.success_rate(id, tc_rql=tc_rql, launch_rql=launch_rql, var_from=var_from, to=to, interval=interval)
        print("The response of AnalyticControllerApi->success_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticControllerApi->success_rate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tc_rql** | **str**|  | [optional] 
 **launch_rql** | **str**|  | [optional] 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **interval** | [**AnalyticInterval**](.md)|  | [optional] 

### Return type

[**List[AnalyticDto]**](AnalyticDto.md)

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

