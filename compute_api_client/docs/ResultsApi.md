# compute_api_client.ResultsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_result_results_post**](ResultsApi.md#create_result_results_post) | **POST** /results | Create result
[**delete_results_by_job_id_results_job_job_id_delete**](ResultsApi.md#delete_results_by_job_id_results_job_job_id_delete) | **DELETE** /results/job/{job_id} | Delete results by job ID
[**read_result_results_id_get**](ResultsApi.md#read_result_results_id_get) | **GET** /results/{id} | Retrieve result
[**read_results_by_job_id_results_job_job_id_get**](ResultsApi.md#read_results_by_job_id_results_job_job_id_get) | **GET** /results/job/{job_id} | Retrieve results by job ID


# **create_result_results_post**
> Result create_result_results_post(result_in)

Create result

Create new result.

### Example

* Api Key Authentication (backend):
```python
import time
import os
import compute_api_client
from compute_api_client.models.result import Result
from compute_api_client.models.result_in import ResultIn
from compute_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: backend
configuration.api_key['backend'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['backend'] = 'Bearer'

# Enter a context with an instance of the API client
async with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.ResultsApi(api_client)
    result_in = compute_api_client.ResultIn() # ResultIn | 

    try:
        # Create result
        api_response = await api_instance.create_result_results_post(result_in)
        print("The response of ResultsApi->create_result_results_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResultsApi->create_result_results_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_in** | [**ResultIn**](ResultIn.md)|  | 

### Return type

[**Result**](Result.md)

### Authorization

[backend](../README.md#backend)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_results_by_job_id_results_job_job_id_delete**
> delete_results_by_job_id_results_job_job_id_delete(job_id)

Delete results by job ID

Delete results by job ID.

### Example

* Api Key Authentication (backend):
```python
import time
import os
import compute_api_client
from compute_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: backend
configuration.api_key['backend'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['backend'] = 'Bearer'

# Enter a context with an instance of the API client
async with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.ResultsApi(api_client)
    job_id = 56 # int | 

    try:
        # Delete results by job ID
        await api_instance.delete_results_by_job_id_results_job_job_id_delete(job_id)
    except Exception as e:
        print("Exception when calling ResultsApi->delete_results_by_job_id_results_job_job_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[backend](../README.md#backend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_result_results_id_get**
> Result read_result_results_id_get(id)

Retrieve result

Get result by ID.

### Example

* Api Key Authentication (user_bearer):
* Api Key Authentication (user):
```python
import time
import os
import compute_api_client
from compute_api_client.models.result import Result
from compute_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user_bearer
configuration.api_key['user_bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user_bearer'] = 'Bearer'

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
async with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.ResultsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve result
        api_response = await api_instance.read_result_results_id_get(id)
        print("The response of ResultsApi->read_result_results_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResultsApi->read_result_results_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Result**](Result.md)

### Authorization

[user_bearer](../README.md#user_bearer), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_results_by_job_id_results_job_job_id_get**
> List[Result] read_results_by_job_id_results_job_job_id_get(job_id)

Retrieve results by job ID

Get results by job ID.

### Example

* Api Key Authentication (user_bearer):
* Api Key Authentication (user):
```python
import time
import os
import compute_api_client
from compute_api_client.models.result import Result
from compute_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user_bearer
configuration.api_key['user_bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user_bearer'] = 'Bearer'

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
async with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.ResultsApi(api_client)
    job_id = 56 # int | 

    try:
        # Retrieve results by job ID
        api_response = await api_instance.read_results_by_job_id_results_job_job_id_get(job_id)
        print("The response of ResultsApi->read_results_by_job_id_results_job_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResultsApi->read_results_by_job_id_results_job_job_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**|  | 

### Return type

[**List[Result]**](Result.md)

### Authorization

[user_bearer](../README.md#user_bearer), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

