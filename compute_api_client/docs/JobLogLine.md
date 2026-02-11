# JobLogLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Timestamp(nanosec) of the recieved log | 
**line** | **str** | The recieved log statement | 

## Example

```python
from compute_api_client.models.job_log_line import JobLogLine

# TODO update the JSON string below
json = "{}"
# create an instance of JobLogLine from a JSON string
job_log_line_instance = JobLogLine.from_json(json)
# print the JSON string representation of the object
print(JobLogLine.to_json())

# convert the object into a dict
job_log_line_dict = job_log_line_instance.to_dict()
# create an instance of JobLogLine from a dict
job_log_line_from_dict = JobLogLine.from_dict(job_log_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


