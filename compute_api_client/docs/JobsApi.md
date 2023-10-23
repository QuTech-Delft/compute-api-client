# compute_api_client.JobsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job_jobs_post**](JobsApi.md#create_job_jobs_post) | **POST** /jobs | Create job
[**delete_job_jobs_id_delete**](JobsApi.md#delete_job_jobs_id_delete) | **DELETE** /jobs/{id} | Destroy job
[**read_job_jobs_id_get**](JobsApi.md#read_job_jobs_id_get) | **GET** /jobs/{id} | Retrieve job
[**read_jobs_jobs_get**](JobsApi.md#read_jobs_jobs_get) | **GET** /jobs | List jobs
[**start_job_jobs_id_start_patch**](JobsApi.md#start_job_jobs_id_start_patch) | **PATCH** /jobs/{id}/start | Start job


# **create_job_jobs_post**
> Job create_job_jobs_post(job_in)

Create job

Create new job.

### Example

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
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

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.JobsApi(api_client)
    job_in = compute_api_client.JobIn() # JobIn | 

    try:
        # Create job
        api_response = api_instance.create_job_jobs_post(job_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->create_job_jobs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_in** | [**JobIn**](JobIn.md)|  | 

### Return type

[**Job**](Job.md)

### Authorization

[user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_jobs_id_delete**
> delete_job_jobs_id_delete(id)

Destroy job

Delete a job.

### Example

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
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

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.JobsApi(api_client)
    id = 56 # int | 

    try:
        # Destroy job
        api_instance.delete_job_jobs_id_delete(id)
    except ApiException as e:
        print("Exception when calling JobsApi->delete_job_jobs_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[user](../README.md#user)

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

# **read_job_jobs_id_get**
> Job read_job_jobs_id_get(id)

Retrieve job

Get job by ID.

### Example

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
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

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.JobsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve job
        api_response = api_instance.read_job_jobs_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->read_job_jobs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Job**](Job.md)

### Authorization

[user](../README.md#user)

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

# **read_jobs_jobs_get**
> list[Job] read_jobs_jobs_get()

List jobs

List jobs.

### Example

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
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

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.JobsApi(api_client)
    
    try:
        # List jobs
        api_response = api_instance.read_jobs_jobs_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->read_jobs_jobs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Job]**](Job.md)

### Authorization

[user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_job_jobs_id_start_patch**
> Job start_job_jobs_id_start_patch(id)

Start job

Start a job.

### Example

* Api Key Authentication (backend):
```python
from __future__ import print_function
import time
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
configuration.api_key['backend'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['backend'] = 'Bearer'

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.JobsApi(api_client)
    id = 56 # int | 

    try:
        # Start job
        api_response = api_instance.start_job_jobs_id_start_patch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->start_job_jobs_id_start_patch: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
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
configuration.api_key['backend'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['backend'] = 'Bearer'

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.JobsApi(api_client)
    id = 56 # int | 

    try:
        # Start job
        api_response = api_instance.start_job_jobs_id_start_patch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->start_job_jobs_id_start_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Job**](Job.md)

### Authorization

[backend](../README.md#backend), [user](../README.md#user)

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

