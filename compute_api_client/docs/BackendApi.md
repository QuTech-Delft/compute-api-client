# compute_api_client.BackendApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_backend_backends_post**](BackendApi.md#create_backend_backends_post) | **POST** /backends | Create backend
[**read_backend_backends_id_get**](BackendApi.md#read_backend_backends_id_get) | **GET** /backends/{id} | Retrieve backend
[**read_backends_backends_get**](BackendApi.md#read_backends_backends_get) | **GET** /backends | List backends


# **create_backend_backends_post**
> BackendWithAuthentication create_backend_backends_post(backend)

Create backend

Create new backend.

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
    api_instance = compute_api_client.BackendApi(api_client)
    backend = compute_api_client.Backend() # Backend | 

    try:
        # Create backend
        api_response = api_instance.create_backend_backends_post(backend)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackendApi->create_backend_backends_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backend** | [**Backend**](Backend.md)|  | 

### Return type

[**BackendWithAuthentication**](BackendWithAuthentication.md)

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

# **read_backend_backends_id_get**
> Backend read_backend_backends_id_get(id)

Retrieve backend

Get backend by ID.

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
    api_instance = compute_api_client.BackendApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve backend
        api_response = api_instance.read_backend_backends_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackendApi->read_backend_backends_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Backend**](Backend.md)

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

# **read_backends_backends_get**
> list[Backend] read_backends_backends_get()

List backends

Read backends.

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
    api_instance = compute_api_client.BackendApi(api_client)
    
    try:
        # List backends
        api_response = api_instance.read_backends_backends_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackendApi->read_backends_backends_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Backend]**](Backend.md)

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

