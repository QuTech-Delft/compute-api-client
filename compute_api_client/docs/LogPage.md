# LogPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[LogLine]**](LogLine.md) |  | 
**next_start** | **int** |  | [optional] 

## Example

```python
from compute_api_client.models.log_page import LogPage

# TODO update the JSON string below
json = "{}"
# create an instance of LogPage from a JSON string
log_page_instance = LogPage.from_json(json)
# print the JSON string representation of the object
print(LogPage.to_json())

# convert the object into a dict
log_page_dict = log_page_instance.to_dict()
# create an instance of LogPage from a dict
log_page_from_dict = LogPage.from_dict(log_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


