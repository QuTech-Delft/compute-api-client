# HTTPInternalServerError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 

## Example

```python
from compute_api_client.models.http_internal_server_error import HTTPInternalServerError

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPInternalServerError from a JSON string
http_internal_server_error_instance = HTTPInternalServerError.from_json(json)
# print the JSON string representation of the object
print(HTTPInternalServerError.to_json())

# convert the object into a dict
http_internal_server_error_dict = http_internal_server_error_instance.to_dict()
# create an instance of HTTPInternalServerError from a dict
http_internal_server_error_from_dict = HTTPInternalServerError.from_dict(http_internal_server_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


