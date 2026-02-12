# Queue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_jobs_in_queue** | **int** | The number of jobs in queue for a backendtype | 
**min_wait_time_in_queue_secs** | **float** | The minimum wait time in a queue for a backendtype | 
**avg_wait_time_in_queue_secs** | **float** | The average wait time in a queue for a backendtype | 
**max_wait_time_in_queue_secs** | **float** | The max wait time in a queue for a backendtype | 

## Example

```python
from compute_api_client.models.queue import Queue

# TODO update the JSON string below
json = "{}"
# create an instance of Queue from a JSON string
queue_instance = Queue.from_json(json)
# print the JSON string representation of the object
print(Queue.to_json())

# convert the object into a dict
queue_dict = queue_instance.to_dict()
# create an instance of Queue from a dict
queue_from_dict = Queue.from_dict(queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


