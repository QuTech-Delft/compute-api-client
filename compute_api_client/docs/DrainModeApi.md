# compute_api_client.DrainModeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_drain_mode_drain_mode_get**](DrainModeApi.md#read_drain_mode_drain_mode_get) | **GET** /drain_mode | Retrieve drain mode statistics for all backendtypes
[**update_drain_mode_drain_mode_patch**](DrainModeApi.md#update_drain_mode_drain_mode_patch) | **PATCH** /drain_mode | Enable drain mode for all backendtypes


# **read_drain_mode_drain_mode_get**
> DrainMode read_drain_mode_drain_mode_get()

Retrieve drain mode statistics for all backendtypes

Get drain_mode related stats for all backendtypes.

### Example


```python
import compute_api_client
from compute_api_client.models.drain_mode import DrainMode
from compute_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.DrainModeApi(api_client)

    try:
        # Retrieve drain mode statistics for all backendtypes
        api_response = await api_instance.read_drain_mode_drain_mode_get()
        print("The response of DrainModeApi->read_drain_mode_drain_mode_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DrainModeApi->read_drain_mode_drain_mode_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DrainMode**](DrainMode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_drain_mode_drain_mode_patch**
> DrainMode update_drain_mode_drain_mode_patch(drain_mode_in)

Enable drain mode for all backendtypes

Enable drain_mode for all backend_types.

### Example

* Api Key Authentication (backend):

```python
import compute_api_client
from compute_api_client.models.drain_mode import DrainMode
from compute_api_client.models.drain_mode_in import DrainModeIn
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
    api_instance = compute_api_client.DrainModeApi(api_client)
    drain_mode_in = compute_api_client.DrainModeIn() # DrainModeIn | 

    try:
        # Enable drain mode for all backendtypes
        api_response = await api_instance.update_drain_mode_drain_mode_patch(drain_mode_in)
        print("The response of DrainModeApi->update_drain_mode_drain_mode_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DrainModeApi->update_drain_mode_drain_mode_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drain_mode_in** | [**DrainModeIn**](DrainModeIn.md)|  | 

### Return type

[**DrainMode**](DrainMode.md)

### Authorization

[backend](../README.md#backend)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

