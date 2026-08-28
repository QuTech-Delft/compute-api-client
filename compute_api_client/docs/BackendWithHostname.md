# BackendWithHostname


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the backend | 
**name** | **str** | The name of the backend | 
**location** | **str** | The location of the backend | 
**backend_type_id** | **int** | The id of the backend type | 
**status** | [**BackendStatus**](BackendStatus.md) | Status of the backend | 
**message** | [**BackendMessage**](BackendMessage.md) | The message obj for a backend | [optional] 
**last_heartbeat** | **datetime** | Time of last heartbeat | 
**hostname** | **str** | The hostname of the backend | 

## Example

```python
from compute_api_client.models.backend_with_hostname import BackendWithHostname

# TODO update the JSON string below
json = "{}"
# create an instance of BackendWithHostname from a JSON string
backend_with_hostname_instance = BackendWithHostname.from_json(json)
# print the JSON string representation of the object
print(BackendWithHostname.to_json())

# convert the object into a dict
backend_with_hostname_dict = backend_with_hostname_instance.to_dict()
# create an instance of BackendWithHostname from a dict
backend_with_hostname_from_dict = BackendWithHostname.from_dict(backend_with_hostname_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


