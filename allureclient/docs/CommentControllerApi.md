# openapi_client.CommentControllerApi

All URIs are relative to *https://allure.vk.team/api/rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create41**](CommentControllerApi.md#create41) | **POST** /comment | Create a new comment
[**delete39**](CommentControllerApi.md#delete39) | **DELETE** /comment/{id} | Delete comment by id
[**find_all38**](CommentControllerApi.md#find_all38) | **GET** /comment | Find all comments
[**find_one33**](CommentControllerApi.md#find_one33) | **GET** /comment/{id} | Find comment by id
[**patch38**](CommentControllerApi.md#patch38) | **PATCH** /comment/{id} | Dynamic update comment


# **create41**
> CommentDto create41(comment_create_dto)

Create a new comment

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.comment_create_dto import CommentCreateDto
from openapi_client.models.comment_dto import CommentDto
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
    api_instance = openapi_client.CommentControllerApi(api_client)
    comment_create_dto = openapi_client.CommentCreateDto() # CommentCreateDto | 

    try:
        # Create a new comment
        api_response = api_instance.create41(comment_create_dto)
        print("The response of CommentControllerApi->create41:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentControllerApi->create41: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_create_dto** | [**CommentCreateDto**](CommentCreateDto.md)|  | 

### Return type

[**CommentDto**](CommentDto.md)

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

# **delete39**
> delete39(id)

Delete comment by id

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
    api_instance = openapi_client.CommentControllerApi(api_client)
    id = 56 # int | 

    try:
        # Delete comment by id
        api_instance.delete39(id)
    except Exception as e:
        print("Exception when calling CommentControllerApi->delete39: %s\n" % e)
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all38**
> PageCommentDto find_all38(test_case_id, page=page, size=size, sort=sort)

Find all comments

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.page_comment_dto import PageCommentDto
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
    api_instance = openapi_client.CommentControllerApi(api_client)
    test_case_id = 56 # int | 
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 10 # int | The size of the page to be returned (optional) (default to 10)
    sort = ["createdDate,ASC"] # List[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createdDate,ASC"])

    try:
        # Find all comments
        api_response = api_instance.find_all38(test_case_id, page=page, size=size, sort=sort)
        print("The response of CommentControllerApi->find_all38:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentControllerApi->find_all38: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_id** | **int**|  | 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createdDate,ASC&quot;]]

### Return type

[**PageCommentDto**](PageCommentDto.md)

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

# **find_one33**
> CommentDto find_one33(id)

Find comment by id

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.comment_dto import CommentDto
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
    api_instance = openapi_client.CommentControllerApi(api_client)
    id = 56 # int | 

    try:
        # Find comment by id
        api_response = api_instance.find_one33(id)
        print("The response of CommentControllerApi->find_one33:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentControllerApi->find_one33: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CommentDto**](CommentDto.md)

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

# **patch38**
> CommentDto patch38(id, comment_patch_dto)

Dynamic update comment

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.comment_dto import CommentDto
from openapi_client.models.comment_patch_dto import CommentPatchDto
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
    api_instance = openapi_client.CommentControllerApi(api_client)
    id = 56 # int | 
    comment_patch_dto = openapi_client.CommentPatchDto() # CommentPatchDto | 

    try:
        # Dynamic update comment
        api_response = api_instance.patch38(id, comment_patch_dto)
        print("The response of CommentControllerApi->patch38:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentControllerApi->patch38: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **comment_patch_dto** | [**CommentPatchDto**](CommentPatchDto.md)|  | 

### Return type

[**CommentDto**](CommentDto.md)

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

