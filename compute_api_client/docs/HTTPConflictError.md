# HTTPConflictError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 

## Example

```python
from compute_api_client.models.http_conflict_error import HTTPConflictError

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPConflictError from a JSON string
http_conflict_error_instance = HTTPConflictError.from_json(json)
# print the JSON string representation of the object
print(HTTPConflictError.to_json())

# convert the object into a dict
http_conflict_error_dict = http_conflict_error_instance.to_dict()
# create an instance of HTTPConflictError from a dict
http_conflict_error_from_dict = HTTPConflictError.from_dict(http_conflict_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


