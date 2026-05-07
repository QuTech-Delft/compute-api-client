# HTTPTooManyRequestsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 

## Example

```python
from compute_api_client.models.http_too_many_requests_error import HTTPTooManyRequestsError

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPTooManyRequestsError from a JSON string
http_too_many_requests_error_instance = HTTPTooManyRequestsError.from_json(json)
# print the JSON string representation of the object
print(HTTPTooManyRequestsError.to_json())

# convert the object into a dict
http_too_many_requests_error_dict = http_too_many_requests_error_instance.to_dict()
# create an instance of HTTPTooManyRequestsError from a dict
http_too_many_requests_error_from_dict = HTTPTooManyRequestsError.from_dict(http_too_many_requests_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


