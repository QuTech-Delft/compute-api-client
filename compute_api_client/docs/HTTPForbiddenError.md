# HTTPForbiddenError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 

## Example

```python
from compute_api_client.models.http_forbidden_error import HTTPForbiddenError

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPForbiddenError from a JSON string
http_forbidden_error_instance = HTTPForbiddenError.from_json(json)
# print the JSON string representation of the object
print(HTTPForbiddenError.to_json())

# convert the object into a dict
http_forbidden_error_dict = http_forbidden_error_instance.to_dict()
# create an instance of HTTPForbiddenError from a dict
http_forbidden_error_from_dict = HTTPForbiddenError.from_dict(http_forbidden_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


