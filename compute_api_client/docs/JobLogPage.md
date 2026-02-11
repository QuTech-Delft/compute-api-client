# JobLogPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[JobLogLine]**](JobLogLine.md) | The logline data | 
**next_start** | **int** |  | [optional] 

## Example

```python
from compute_api_client.models.job_log_page import JobLogPage

# TODO update the JSON string below
json = "{}"
# create an instance of JobLogPage from a JSON string
job_log_page_instance = JobLogPage.from_json(json)
# print the JSON string representation of the object
print(JobLogPage.to_json())

# convert the object into a dict
job_log_page_dict = job_log_page_instance.to_dict()
# create an instance of JobLogPage from a dict
job_log_page_from_dict = JobLogPage.from_dict(job_log_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


