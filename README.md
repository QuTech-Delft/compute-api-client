# compute-api-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The `compute_api_client` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3
* python-dateutil
* aiohttp
* pydantic

## Getting Started

In your own code, to use this library to connect and interact with compute-api-client,
you can run the following:

```python

import time
import compute_api_client
from compute_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
async with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.AlgorithmsApi(api_client)
    algorithm_in = compute_api_client.AlgorithmIn() # AlgorithmIn | 

    try:
        # Create algorithm
        api_response = await api_instance.create_algorithm_algorithms_post(algorithm_in)
        print("The response of AlgorithmsApi->create_algorithm_algorithms_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlgorithmsApi->create_algorithm_algorithms_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlgorithmsApi* | [**create_algorithm_algorithms_post**](compute_api_client/docs/AlgorithmsApi.md#create_algorithm_algorithms_post) | **POST** /algorithms | Create algorithm
*AlgorithmsApi* | [**delete_algorithm_algorithms_id_delete**](compute_api_client/docs/AlgorithmsApi.md#delete_algorithm_algorithms_id_delete) | **DELETE** /algorithms/{id} | Destroy algorithm
*AlgorithmsApi* | [**read_algorithm_algorithms_id_get**](compute_api_client/docs/AlgorithmsApi.md#read_algorithm_algorithms_id_get) | **GET** /algorithms/{id} | Retrieve algorithm
*AlgorithmsApi* | [**read_algorithms_algorithms_get**](compute_api_client/docs/AlgorithmsApi.md#read_algorithms_algorithms_get) | **GET** /algorithms | List algorithms
*AlgorithmsApi* | [**update_algorithm_algorithms_id_put**](compute_api_client/docs/AlgorithmsApi.md#update_algorithm_algorithms_id_put) | **PUT** /algorithms/{id} | Update algorithm
*AuthConfigApi* | [**auth_config_auth_config_get**](compute_api_client/docs/AuthConfigApi.md#auth_config_auth_config_get) | **GET** /auth_config | Get suggested authentication configuration
*BackendApi* | [**create_backend_backends_post**](compute_api_client/docs/BackendApi.md#create_backend_backends_post) | **POST** /backends | Create backend
*BackendApi* | [**read_backend_backends_id_get**](compute_api_client/docs/BackendApi.md#read_backend_backends_id_get) | **GET** /backends/{id} | Retrieve backend
*BackendApi* | [**read_backend_self_backends_me_get**](compute_api_client/docs/BackendApi.md#read_backend_self_backends_me_get) | **GET** /backends/me | Retrieve backend
*BackendApi* | [**read_backends_backends_get**](compute_api_client/docs/BackendApi.md#read_backends_backends_get) | **GET** /backends | List backends
*BackendApi* | [**update_backend_self_backends_me_patch**](compute_api_client/docs/BackendApi.md#update_backend_self_backends_me_patch) | **PATCH** /backends/me | Update backend
*BackendTypesApi* | [**read_backend_type_backend_types_id_get**](compute_api_client/docs/BackendTypesApi.md#read_backend_type_backend_types_id_get) | **GET** /backend_types/{id} | Retrieve backend type
*BackendTypesApi* | [**read_backend_types_backend_types_get**](compute_api_client/docs/BackendTypesApi.md#read_backend_types_backend_types_get) | **GET** /backend_types/ | List backend types
*BatchJobsApi* | [**create_batch_job_batch_jobs_post**](compute_api_client/docs/BatchJobsApi.md#create_batch_job_batch_jobs_post) | **POST** /batch_jobs | Create batch job
*BatchJobsApi* | [**enqueue_batch_job_batch_jobs_id_enqueue_patch**](compute_api_client/docs/BatchJobsApi.md#enqueue_batch_job_batch_jobs_id_enqueue_patch) | **PATCH** /batch_jobs/{id}/enqueue | Enqueue batch job for execution
*BatchJobsApi* | [**finish_batch_job_batch_jobs_id_finish_patch**](compute_api_client/docs/BatchJobsApi.md#finish_batch_job_batch_jobs_id_finish_patch) | **PATCH** /batch_jobs/{id}/finish | Finish batch job
*BatchJobsApi* | [**peek_batch_job_batch_jobs_peek_patch**](compute_api_client/docs/BatchJobsApi.md#peek_batch_job_batch_jobs_peek_patch) | **PATCH** /batch_jobs/peek | Peek batch job
*BatchJobsApi* | [**pop_batch_job_batch_jobs_pop_patch**](compute_api_client/docs/BatchJobsApi.md#pop_batch_job_batch_jobs_pop_patch) | **PATCH** /batch_jobs/pop | Take batch job
*BatchJobsApi* | [**read_batch_jobs_batch_jobs_get**](compute_api_client/docs/BatchJobsApi.md#read_batch_jobs_batch_jobs_get) | **GET** /batch_jobs | List batch jobs
*BatchJobsApi* | [**unpop_batch_job_batch_jobs_unpop_patch**](compute_api_client/docs/BatchJobsApi.md#unpop_batch_job_batch_jobs_unpop_patch) | **PATCH** /batch_jobs/unpop | Take batch job
*CommitsApi* | [**compile_commit_commits_id_compile_post**](compute_api_client/docs/CommitsApi.md#compile_commit_commits_id_compile_post) | **POST** /commits/{id}/compile | Compile file in a commit
*CommitsApi* | [**create_commit_commits_post**](compute_api_client/docs/CommitsApi.md#create_commit_commits_post) | **POST** /commits | Create commit
*CommitsApi* | [**delete_commit_commits_id_delete**](compute_api_client/docs/CommitsApi.md#delete_commit_commits_id_delete) | **DELETE** /commits/{id} | Destroy commit
*CommitsApi* | [**read_commit_commits_id_get**](compute_api_client/docs/CommitsApi.md#read_commit_commits_id_get) | **GET** /commits/{id} | Get commit by ID
*CommitsApi* | [**read_commits_commits_get**](compute_api_client/docs/CommitsApi.md#read_commits_commits_get) | **GET** /commits | List commits
*FilesApi* | [**create_file_files_post**](compute_api_client/docs/FilesApi.md#create_file_files_post) | **POST** /files | Create file
*FilesApi* | [**delete_file_files_id_delete**](compute_api_client/docs/FilesApi.md#delete_file_files_id_delete) | **DELETE** /files/{id} | Destroy file
*FilesApi* | [**read_file_files_id_get**](compute_api_client/docs/FilesApi.md#read_file_files_id_get) | **GET** /files/{id} | Retrieve file
*FilesApi* | [**read_files_files_get**](compute_api_client/docs/FilesApi.md#read_files_files_get) | **GET** /files | List files
*FinalResultsApi* | [**create_final_result_final_results_post**](compute_api_client/docs/FinalResultsApi.md#create_final_result_final_results_post) | **POST** /final_results | Create final result
*FinalResultsApi* | [**read_final_result_by_job_id_final_results_job_job_id_get**](compute_api_client/docs/FinalResultsApi.md#read_final_result_by_job_id_final_results_job_job_id_get) | **GET** /final_results/job/{job_id} | Retrieve final result by job ID
*FinalResultsApi* | [**read_final_result_final_results_id_get**](compute_api_client/docs/FinalResultsApi.md#read_final_result_final_results_id_get) | **GET** /final_results/{id} | Retrieve final result
*HealthApi* | [**healthz_healthz_get**](compute_api_client/docs/HealthApi.md#healthz_healthz_get) | **GET** /healthz | Report health
*JobsApi* | [**create_job_jobs_post**](compute_api_client/docs/JobsApi.md#create_job_jobs_post) | **POST** /jobs | Create job
*JobsApi* | [**delete_job_jobs_id_delete**](compute_api_client/docs/JobsApi.md#delete_job_jobs_id_delete) | **DELETE** /jobs/{id} | Destroy job
*JobsApi* | [**read_job_jobs_id_get**](compute_api_client/docs/JobsApi.md#read_job_jobs_id_get) | **GET** /jobs/{id} | Retrieve job
*JobsApi* | [**read_jobs_jobs_get**](compute_api_client/docs/JobsApi.md#read_jobs_jobs_get) | **GET** /jobs | List jobs
*JobsApi* | [**update_job_status_jobs_id_patch**](compute_api_client/docs/JobsApi.md#update_job_status_jobs_id_patch) | **PATCH** /jobs/{id} | Update Job Status
*LanguagesApi* | [**read_language_languages_id_get**](compute_api_client/docs/LanguagesApi.md#read_language_languages_id_get) | **GET** /languages/{id} | Retrieve language
*LanguagesApi* | [**read_languages_languages_get**](compute_api_client/docs/LanguagesApi.md#read_languages_languages_get) | **GET** /languages | List languages
*MembersApi* | [**create_member_members_post**](compute_api_client/docs/MembersApi.md#create_member_members_post) | **POST** /members | Create member
*MembersApi* | [**delete_member_members_id_delete**](compute_api_client/docs/MembersApi.md#delete_member_members_id_delete) | **DELETE** /members/{id} | Destroy member
*MembersApi* | [**read_member_members_id_get**](compute_api_client/docs/MembersApi.md#read_member_members_id_get) | **GET** /members/{id} | Retrieve member
*MembersApi* | [**read_members_members_get**](compute_api_client/docs/MembersApi.md#read_members_members_get) | **GET** /members | List members
*MetadataApi* | [**create_metadata_self_metadata_post**](compute_api_client/docs/MetadataApi.md#create_metadata_self_metadata_post) | **POST** /metadata | Create metadata
*MetadataApi* | [**read_metadata_by_backend_id_metadata_backend_backend_id_get**](compute_api_client/docs/MetadataApi.md#read_metadata_by_backend_id_metadata_backend_backend_id_get) | **GET** /metadata/backend/{backend_id} | Retrieve metadata by backend ID
*MetadataApi* | [**read_metadata_metadata_id_get**](compute_api_client/docs/MetadataApi.md#read_metadata_metadata_id_get) | **GET** /metadata/{id} | Get metadata by ID
*PermissionsApi* | [**read_permission_group_permission_groups_id_get**](compute_api_client/docs/PermissionsApi.md#read_permission_group_permission_groups_id_get) | **GET** /permission_groups/{id} | Retrieve permission groups
*PermissionsApi* | [**read_permission_groups_permission_groups_get**](compute_api_client/docs/PermissionsApi.md#read_permission_groups_permission_groups_get) | **GET** /permission_groups/ | List permission groups
*PermissionsApi* | [**read_permission_permissions_id_get**](compute_api_client/docs/PermissionsApi.md#read_permission_permissions_id_get) | **GET** /permissions/{id} | Retrieve permissions
*PermissionsApi* | [**read_permissions_permissions_get**](compute_api_client/docs/PermissionsApi.md#read_permissions_permissions_get) | **GET** /permissions/ | List permissions
*ProjectsApi* | [**create_project_projects_post**](compute_api_client/docs/ProjectsApi.md#create_project_projects_post) | **POST** /projects | Create project
*ProjectsApi* | [**delete_project_projects_id_delete**](compute_api_client/docs/ProjectsApi.md#delete_project_projects_id_delete) | **DELETE** /projects/{id} | Destroy project
*ProjectsApi* | [**partial_update_project_projects_id_patch**](compute_api_client/docs/ProjectsApi.md#partial_update_project_projects_id_patch) | **PATCH** /projects/{id} | Partially update project
*ProjectsApi* | [**read_project_projects_id_get**](compute_api_client/docs/ProjectsApi.md#read_project_projects_id_get) | **GET** /projects/{id} | Retrieve project
*ProjectsApi* | [**read_projects_projects_get**](compute_api_client/docs/ProjectsApi.md#read_projects_projects_get) | **GET** /projects | List projects
*ProjectsApi* | [**update_project_projects_id_put**](compute_api_client/docs/ProjectsApi.md#update_project_projects_id_put) | **PUT** /projects/{id} | Update project
*ReservationsApi* | [**create_reservation_reservations_post**](compute_api_client/docs/ReservationsApi.md#create_reservation_reservations_post) | **POST** /reservations | Create reservation
*ReservationsApi* | [**read_reservation_reservations_id_get**](compute_api_client/docs/ReservationsApi.md#read_reservation_reservations_id_get) | **GET** /reservations/{id} | Retrieve reservation
*ReservationsApi* | [**read_reservations_reservations_get**](compute_api_client/docs/ReservationsApi.md#read_reservations_reservations_get) | **GET** /reservations | List reservations
*ReservationsApi* | [**terminate_reservation_reservations_id_terminate_patch**](compute_api_client/docs/ReservationsApi.md#terminate_reservation_reservations_id_terminate_patch) | **PATCH** /reservations/{id}/terminate | Terminate reservation
*ResultsApi* | [**create_result_results_post**](compute_api_client/docs/ResultsApi.md#create_result_results_post) | **POST** /results | Create result
*ResultsApi* | [**delete_results_by_job_id_results_job_job_id_delete**](compute_api_client/docs/ResultsApi.md#delete_results_by_job_id_results_job_job_id_delete) | **DELETE** /results/job/{job_id} | Delete results by job ID
*ResultsApi* | [**read_result_results_id_get**](compute_api_client/docs/ResultsApi.md#read_result_results_id_get) | **GET** /results/{id} | Retrieve result
*ResultsApi* | [**read_results_by_algorithm_id_results_algorithm_algorithm_id_get**](compute_api_client/docs/ResultsApi.md#read_results_by_algorithm_id_results_algorithm_algorithm_id_get) | **GET** /results/algorithm/{algorithm_id} | Retrieve results by algorithm ID
*ResultsApi* | [**read_results_by_job_id_results_job_job_id_get**](compute_api_client/docs/ResultsApi.md#read_results_by_job_id_results_job_job_id_get) | **GET** /results/job/{job_id} | Retrieve results by job ID
*TeamsApi* | [**read_team_teams_id_get**](compute_api_client/docs/TeamsApi.md#read_team_teams_id_get) | **GET** /teams/{id} | Retrieve teams
*TeamsApi* | [**read_teams_teams_get**](compute_api_client/docs/TeamsApi.md#read_teams_teams_get) | **GET** /teams/ | List teams
*TransactionsApi* | [**read_transaction_transactions_id_get**](compute_api_client/docs/TransactionsApi.md#read_transaction_transactions_id_get) | **GET** /transactions/{id} | Retrieve transactions
*TransactionsApi* | [**read_transactions_transactions_get**](compute_api_client/docs/TransactionsApi.md#read_transactions_transactions_get) | **GET** /transactions/ | List transactions
*UsersApi* | [**create_user_users_post**](compute_api_client/docs/UsersApi.md#create_user_users_post) | **POST** /users | Create user
*UsersApi* | [**delete_user_users_id_delete**](compute_api_client/docs/UsersApi.md#delete_user_users_id_delete) | **DELETE** /users/{id} | Destroy user
*UsersApi* | [**read_user_users_id_get**](compute_api_client/docs/UsersApi.md#read_user_users_id_get) | **GET** /users/{id} | Retrieve user
*UsersApi* | [**read_users_users_get**](compute_api_client/docs/UsersApi.md#read_users_users_get) | **GET** /users | List users


## Documentation For Models

 - [Algorithm](compute_api_client/docs/Algorithm.md)
 - [AlgorithmIn](compute_api_client/docs/AlgorithmIn.md)
 - [AlgorithmType](compute_api_client/docs/AlgorithmType.md)
 - [AuthConfig](compute_api_client/docs/AuthConfig.md)
 - [Backend](compute_api_client/docs/Backend.md)
 - [BackendIn](compute_api_client/docs/BackendIn.md)
 - [BackendPatch](compute_api_client/docs/BackendPatch.md)
 - [BackendStatus](compute_api_client/docs/BackendStatus.md)
 - [BackendType](compute_api_client/docs/BackendType.md)
 - [BackendWithAuthentication](compute_api_client/docs/BackendWithAuthentication.md)
 - [BatchJob](compute_api_client/docs/BatchJob.md)
 - [BatchJobIn](compute_api_client/docs/BatchJobIn.md)
 - [BatchJobStatus](compute_api_client/docs/BatchJobStatus.md)
 - [Commit](compute_api_client/docs/Commit.md)
 - [CommitIn](compute_api_client/docs/CommitIn.md)
 - [CompilePayload](compute_api_client/docs/CompilePayload.md)
 - [CompileStage](compute_api_client/docs/CompileStage.md)
 - [Domain](compute_api_client/docs/Domain.md)
 - [File](compute_api_client/docs/File.md)
 - [FileIn](compute_api_client/docs/FileIn.md)
 - [FinalResult](compute_api_client/docs/FinalResult.md)
 - [FinalResultIn](compute_api_client/docs/FinalResultIn.md)
 - [HTTPBadRequestError](compute_api_client/docs/HTTPBadRequestError.md)
 - [HTTPNotFoundError](compute_api_client/docs/HTTPNotFoundError.md)
 - [HTTPValidationError](compute_api_client/docs/HTTPValidationError.md)
 - [Job](compute_api_client/docs/Job.md)
 - [JobIn](compute_api_client/docs/JobIn.md)
 - [JobPatch](compute_api_client/docs/JobPatch.md)
 - [JobStatus](compute_api_client/docs/JobStatus.md)
 - [Language](compute_api_client/docs/Language.md)
 - [LocationInner](compute_api_client/docs/LocationInner.md)
 - [Member](compute_api_client/docs/Member.md)
 - [MemberIn](compute_api_client/docs/MemberIn.md)
 - [Metadata](compute_api_client/docs/Metadata.md)
 - [MetadataIn](compute_api_client/docs/MetadataIn.md)
 - [PageAlgorithm](compute_api_client/docs/PageAlgorithm.md)
 - [PageBackend](compute_api_client/docs/PageBackend.md)
 - [PageBackendType](compute_api_client/docs/PageBackendType.md)
 - [PageBatchJob](compute_api_client/docs/PageBatchJob.md)
 - [PageCommit](compute_api_client/docs/PageCommit.md)
 - [PageFile](compute_api_client/docs/PageFile.md)
 - [PageJob](compute_api_client/docs/PageJob.md)
 - [PageLanguage](compute_api_client/docs/PageLanguage.md)
 - [PageMember](compute_api_client/docs/PageMember.md)
 - [PageMetadata](compute_api_client/docs/PageMetadata.md)
 - [PagePermission](compute_api_client/docs/PagePermission.md)
 - [PagePermissionGroup](compute_api_client/docs/PagePermissionGroup.md)
 - [PageProject](compute_api_client/docs/PageProject.md)
 - [PageReservation](compute_api_client/docs/PageReservation.md)
 - [PageResult](compute_api_client/docs/PageResult.md)
 - [PageTeam](compute_api_client/docs/PageTeam.md)
 - [PageTransaction](compute_api_client/docs/PageTransaction.md)
 - [PageUser](compute_api_client/docs/PageUser.md)
 - [Permission](compute_api_client/docs/Permission.md)
 - [PermissionGroup](compute_api_client/docs/PermissionGroup.md)
 - [Project](compute_api_client/docs/Project.md)
 - [ProjectIn](compute_api_client/docs/ProjectIn.md)
 - [ProjectPatch](compute_api_client/docs/ProjectPatch.md)
 - [Reservation](compute_api_client/docs/Reservation.md)
 - [ReservationIn](compute_api_client/docs/ReservationIn.md)
 - [Result](compute_api_client/docs/Result.md)
 - [ResultIn](compute_api_client/docs/ResultIn.md)
 - [Role](compute_api_client/docs/Role.md)
 - [ShareType](compute_api_client/docs/ShareType.md)
 - [Team](compute_api_client/docs/Team.md)
 - [Transaction](compute_api_client/docs/Transaction.md)
 - [User](compute_api_client/docs/User.md)
 - [UserIn](compute_api_client/docs/UserIn.md)
 - [ValidationError](compute_api_client/docs/ValidationError.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="user_bearer"></a>
### user_bearer

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://auth.qi2.quantum-inspire.com/realms/oidc_development/protocol/openid-connect/auth
- **Scopes**: N/A

<a id="backend"></a>
### backend

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




