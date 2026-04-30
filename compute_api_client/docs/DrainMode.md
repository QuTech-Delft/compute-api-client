# DrainMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the drainmode object | 
**enabled** | **bool** | If the drain mode is enabled | 
**running_jobs** | **int** | The total running batch jobs on all backend types | 
**pending_jobs** | **int** | The total pending batch jobs on all backend types | 
**safe_to_deploy** | **bool** | If it is safe to go ahead with deployment | 

## Example

```python
from compute_api_client.models.drain_mode import DrainMode

# TODO update the JSON string below
json = "{}"
# create an instance of DrainMode from a JSON string
drain_mode_instance = DrainMode.from_json(json)
# print the JSON string representation of the object
print(DrainMode.to_json())

# convert the object into a dict
drain_mode_dict = drain_mode_instance.to_dict()
# create an instance of DrainMode from a dict
drain_mode_from_dict = DrainMode.from_dict(drain_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


