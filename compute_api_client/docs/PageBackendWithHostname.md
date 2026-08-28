# PageBackendWithHostname


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BackendWithHostname]**](BackendWithHostname.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | 

## Example

```python
from compute_api_client.models.page_backend_with_hostname import PageBackendWithHostname

# TODO update the JSON string below
json = "{}"
# create an instance of PageBackendWithHostname from a JSON string
page_backend_with_hostname_instance = PageBackendWithHostname.from_json(json)
# print the JSON string representation of the object
print(PageBackendWithHostname.to_json())

# convert the object into a dict
page_backend_with_hostname_dict = page_backend_with_hostname_instance.to_dict()
# create an instance of PageBackendWithHostname from a dict
page_backend_with_hostname_from_dict = PageBackendWithHostname.from_dict(page_backend_with_hostname_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


