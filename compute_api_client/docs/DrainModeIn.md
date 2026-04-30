# DrainModeIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | If the drain mode is enabled | 
**reason** | **str** | The reason for drain mode | 

## Example

```python
from compute_api_client.models.drain_mode_in import DrainModeIn

# TODO update the JSON string below
json = "{}"
# create an instance of DrainModeIn from a JSON string
drain_mode_in_instance = DrainModeIn.from_json(json)
# print the JSON string representation of the object
print(DrainModeIn.to_json())

# convert the object into a dict
drain_mode_in_dict = drain_mode_in_instance.to_dict()
# create an instance of DrainModeIn from a dict
drain_mode_in_from_dict = DrainModeIn.from_dict(drain_mode_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


