# File


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**commit_id** | **int** |  | 
**content** | **str** |  | 
**language_id** | **int** |  | 
**compile_stage** | [**CompileStage**](CompileStage.md) |  | 
**compile_properties** | **Dict[str, object]** |  | 
**generated** | **bool** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from compute_api_client.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print File.to_json()

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_form_dict = file.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


